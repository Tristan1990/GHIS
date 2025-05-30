# game_router.py

import streamlit as st
from pathlib import Path
from PIL import Image, ImageOps

from data.characters import CHARACTERS
from data.scenes     import SCENES

BANNER_HEIGHT = 350  # px ─ change once, everywhere

# Backward-compat shim for older Streamlit
if not hasattr(st, "rerun"):
    st.rerun = st.experimental_rerun

def load_banner(path: Path, height: int = BANNER_HEIGHT) -> Image.Image:
    img = Image.open(path)
    if img.height > height:
        ratio = height / img.height
        img = img.resize((int(img.width * ratio), height),
                         Image.Resampling.LANCZOS)
    return img

def apply_delta(delta_list: list[tuple[int, int]]):
    """
    Apply each (trait_index, change) to the current character's scores.
    """
    traits = CHARACTERS[st.session_state.selected_character]["traits"]
    for idx, change in delta_list:
        tr = traits[idx]
        st.session_state.scores[tr] = max(
            0,
            st.session_state.scores[tr] + change,
        )

def init_state():
    """Ensure the session_state keys exist."""
    if "selected_character" not in st.session_state:
        st.session_state.selected_character = None
    if "current_scene" not in st.session_state:
        st.session_state.current_scene = None
    if "scores" not in st.session_state:
        st.session_state.scores = None

def pick_character(char_id: str):
    """
    Called once user picks a character.
    Initializes intro scene and deep-copies that character’s starting scores.
    """
    st.session_state.selected_character = char_id
    st.session_state.current_scene     = CHARACTERS[char_id]["intro"]
    st.session_state.scores            = CHARACTERS[char_id]["scores"].copy()

def go_to(scene_id: str):
    """
    Helper to go to the next scene (handles "FINALE" placeholder).
    """
    if scene_id == "FINALE":
        cid      = st.session_state.selected_character
        scene_id = CHARACTERS[cid]["finale"]
    st.session_state.current_scene = scene_id

def render_trait_bars():
    """Draw one progress bar per trait."""
    traits = CHARACTERS[st.session_state.selected_character]["traits"]
    scores = st.session_state.scores
    cols   = st.columns(len(traits))
    for col, tr in zip(cols, traits):
        with col:
            st.markdown(f"**{tr}**")
            st.progress(scores[tr] / 20, text=str(scores[tr]))

def render_current_scene():
    """
    Master function to render the current scene:
     - Shows trait bars and recent-changes diff in a single row
     - Renders narrative intros or 3-col choice scenes
    """
    init_state()
    cid      = st.session_state.selected_character
    scene_id = st.session_state.current_scene
    scene    = SCENES[scene_id]

    # 1) Trait bars + diff in one row
    bars_col, diff_col = st.columns([3, 1], gap="large")

    # 1a) Left 75%: trait bars
    with bars_col:
        render_trait_bars()

    # 1b) Right 25%: recent changes (if any)
    with diff_col:
        if (
            st.session_state.get("last_diff_scene") == scene_id
            and "last_snapshot" in st.session_state
        ):
            before = st.session_state.last_snapshot
            after  = st.session_state.scores
            st.markdown("#### Recent Changes")
            for tr, old_val in before.items():
                new_val = after[tr]
                delta   = new_val - old_val
                if delta != 0:
                    sign = "+" if delta > 0 else ""
                    st.markdown(f"- **{tr}**: {old_val} → {new_val} ({sign}{delta})")
            # clear out so we only show once
            del st.session_state.last_snapshot
            del st.session_state.last_diff_scene

    st.markdown("---") 

    # 2) Narrative intros (no choices)
    if "narrative_steps" in scene:
        # initialize step counter on first visit
        if (
            st.session_state.get("active_intro") != scene_id
            or "intro_step" not in st.session_state
        ):
            st.session_state.active_intro = scene_id
            st.session_state.intro_step   = 0

        idx   = st.session_state.intro_step
        steps = scene["narrative_steps"]

        # Banner & title
        banner = Path("assets") / scene["banner"]
        st.image(load_banner(banner), use_container_width=False)
        st.markdown(f"### {scene['prompt']}")

        # Show text
        st.markdown(steps[idx]["text"])

        # Continue through narrative
        if st.button("Continue…", use_container_width=False):
            apply_delta(steps[idx]["delta"])
            st.session_state.intro_step += 1
            if st.session_state.intro_step >= len(steps):
                go_to(scene["next_scene"])
            st.rerun()
        return

    # 3) Choice-based scenes & finales → 3-column layout
    col_img, col_prompt, col_opts = st.columns([3, 6, 3], gap="large")

    # 3a) Left: banner
    with col_img:
        banner = Path("assets") / scene["banner"]
        st.image(load_banner(banner), use_container_width=True)

    # 3b) Middle: prompt
    with col_prompt:
        st.markdown(f"### {scene['prompt']}")

    # 3c) Right: option buttons
    with col_opts:
        st.markdown("#### Choose an action:")
        for i, (label, next_id, delta_list) in enumerate(scene["options"]):
            key = f"{scene_id}_{i}"
            if st.button(label, key=key, use_container_width=True):
                # snapshot scores *before* applying
                st.session_state.last_snapshot = st.session_state.scores.copy()
                # apply the change
                apply_delta(delta_list)

                # determine the scene we’ll land in
                if next_id is None:
                    st.switch_page("pages/3_End.py")
                    return
                if next_id == "FINALE":
                    next_id = CHARACTERS[cid]["finale"]

                # record so diff shows in that next scene
                st.session_state.last_diff_scene = next_id
                st.session_state.current_scene   = next_id
                st.rerun()
