# game_router.py
import random
from pathlib import Path
from PIL import Image, ImageOps
import streamlit as st

from data.characters import CHARACTERS
from data.scenes     import SCENES

BANNER_HEIGHT = 350  # px — change once, everywhere
if not hasattr(st, "rerun"):             # back-compat
    st.rerun = st.experimental_rerun


# ─────────────────────────── helpers ────────────────────────────
def load_banner(path: Path, height: int = BANNER_HEIGHT) -> Image.Image:
    img = Image.open(path)
    if img.height > height:
        ratio = height / img.height
        img   = img.resize((int(img.width * ratio), height),
                           Image.Resampling.LANCZOS)
    return img


def apply_delta(delta_list: list[tuple[int, int]]):
    traits = CHARACTERS[st.session_state.selected_character]["traits"]
    for idx, change in delta_list:
        tr = traits[idx]
        st.session_state.scores[tr] = max(0, st.session_state.scores[tr] + change)


def init_state():
    for k, default in [
        ("selected_character", None),
        ("current_scene",      None),
        ("scores",             None),
    ]:
        st.session_state.setdefault(k, default)


def pick_character(char_id: str):
    st.session_state.selected_character = char_id
    st.session_state.current_scene      = CHARACTERS[char_id]["intro"]
    st.session_state.scores             = CHARACTERS[char_id]["scores"].copy()


def go_to(scene_id: str):
    if scene_id == "FINALE":
        cid = st.session_state.selected_character
        scene_id = CHARACTERS[cid]["finale"]
    st.session_state.current_scene = scene_id


def render_trait_bars():
    traits = CHARACTERS[st.session_state.selected_character]["traits"]
    scores = st.session_state.scores
    cols   = st.columns(len(traits))
    for col, tr in zip(cols, traits):
        with col:
            st.markdown(f"**{tr}**")
            st.progress(scores[tr] / 20, text=str(scores[tr]))


# ──────────────────────── main renderer ─────────────────────────
def render_current_scene():
    init_state()
    cid      = st.session_state.selected_character
    scene_id = st.session_state.current_scene
    scene    = SCENES[scene_id]

    # 1) Top-row: bars + recent diff
    bars_col, diff_col = st.columns([3, 1], gap="large")
    with bars_col:
        render_trait_bars()
    with diff_col:
        if (
            st.session_state.get("last_diff_scene") == scene_id
            and "last_snapshot" in st.session_state
        ):
            before = st.session_state.last_snapshot
            after  = st.session_state.scores
            st.markdown("#### Recent Changes")
            for tr, old_val in before.items():
                delta = after[tr] - old_val
                if delta:
                    sign = "+" if delta > 0 else ""
                    st.markdown(f"- **{tr}**: {old_val} → {after[tr]} ({sign}{delta})")
            del st.session_state.last_snapshot
            del st.session_state.last_diff_scene
    st.markdown("---")

    # 2) ── INTRO SEQUENCES ──────────────────────────────────────
    if "narrative_steps" in scene:
        # set / reset step counter
        if (st.session_state.get("active_intro") != scene_id
            or "intro_step" not in st.session_state):
            st.session_state.active_intro = scene_id
            st.session_state.intro_step   = 0

        idx   = st.session_state.intro_step
        steps = scene["narrative_steps"]

        img_col, text_col = st.columns([4, 8], gap="large")
        with img_col:
            st.image(load_banner(Path("assets") / scene["banner"]),
                     use_container_width=True)

        with text_col:
            st.markdown(f"### {scene['prompt']}")
            st.markdown(steps[idx]["text"])

            if st.button("Continue…", use_container_width=False):
                # snapshot **before** applying change
                st.session_state.last_snapshot = st.session_state.scores.copy()

                is_last = (idx == len(steps) - 1)
                target  = scene["next_scene"] if is_last else scene_id
                st.session_state.last_diff_scene = target

                apply_delta(steps[idx]["delta"])

                if is_last:
                    go_to(scene["next_scene"])
                else:
                    st.session_state.intro_step += 1
                st.rerun()
        return

    # 3) ── SPECIAL SCENE-5 (one random option) ──────────────────
    if scene_id.endswith("_scene5"):
        key = f"{scene_id}_choice_idx"
        if key not in st.session_state:
            st.session_state[key] = random.randrange(len(scene["options"]))
        opt_idx               = st.session_state[key]
        label, next_id, dlt   = scene["options"][opt_idx]

        left, right = st.columns([4, 6], gap="large")
        with left:
            st.image(load_banner(Path("assets") / scene["banner"]),
                     use_container_width=True)
        with right:
            st.markdown(f"### {scene['prompt']}")
            st.markdown("> You have been assigned to this group:")
            st.markdown(f"**{label}**")
            if st.button("Proceed", use_container_width=True):
                st.session_state.last_snapshot   = st.session_state.scores.copy()
                st.session_state.last_diff_scene = next_id
                apply_delta(dlt)

                if next_id is None:
                    st.switch_page("pages/3_End.py"); return
                if next_id == "FINALE":
                    next_id = CHARACTERS[cid]["finale"]

                st.session_state.current_scene = next_id
                st.rerun()
        return

    # 4) ── REGULAR CHOICE SCENES ────────────────────────────────
    left, right = st.columns([4, 6], gap="large")
    with left:
        st.image(load_banner(Path("assets") / scene["banner"]),
                 use_container_width=True)
    with right:
        st.markdown(f"### {scene['prompt']}")
        st.markdown("#### Choose an action:")
        for i, (label, next_id, dlt) in enumerate(scene["options"]):
            if st.button(label, key=f"{scene_id}_{i}", use_container_width=True):
                st.session_state.last_snapshot   = st.session_state.scores.copy()
                st.session_state.last_diff_scene = next_id
                apply_delta(dlt)

                if next_id is None:
                    st.switch_page("pages/3_End.py"); return
                if next_id == "FINALE":
                    next_id = CHARACTERS[cid]["finale"]

                st.session_state.current_scene = next_id
                st.rerun()
