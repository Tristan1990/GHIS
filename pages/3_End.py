# pages/3_End.py
# OUTRO PAGE — character-specific evening reflection,
# then progressive reveal of trait paragraphs, finally navigate to 4_Outro.

import streamlit as st
from pathlib import Path
from PIL import Image
from data.characters import CHARACTERS

# ────────────────────────────────────────────────────────────
# State & meta
# ────────────────────────────────────────────────────────────

cid     = st.session_state.get("selected_character")
scores  = st.session_state.get("scores", {})
meta    = CHARACTERS.get(cid, {})
traits  = meta.get("traits", [])  # in the same order as defined for that character

# If for some reason no character is selected, bail out:
if cid is None or meta == {}:
    st.error("No character selected.")
    st.stop()

# Build a lookup key (“sock”, “carol”, “bram”, “fatima”) from the character’s name:
char_key = meta["name"].lower()

# ────────────────────────────────────────────────────────────
# Buckets (LOW / MEDIUM / HIGH) per trait
# ────────────────────────────────────────────────────────────

bucket = {}
for t in traits:
    v = scores.get(t, 0)
    if v < 7:
        bucket[t] = "LOW"
    elif v < 15:
        bucket[t] = "MEDIUM"
    else:
        bucket[t] = "HIGH"

# ────────────────────────────────────────────────────────────
# Character-specific intro paragraph (always visible)
# ────────────────────────────────────────────────────────────

INTRO = {
    "fatima": (
        "Back home, as evening settles, Fatima lays out her prayer mat. "
        "The rhythm of prayer helps her reflect on the day’s choices and emotions."
    ),
    "sock": (
        "Back home, as night folds in, Sock collapses onto the couch. "
        "Moss crawls lazily across their chest, a quiet anchor in the stillness. "
        "They put on a familiar YouTuber – opinionated, funny, just sharp enough to feel safe. "
        "The video ends, but the buzzing doesn’t. The day lingers…"
    ),
    "carol": (
        "Back in her room, Carol collapses onto the bed, jacket still on, head pounding from the whirlwind of the day."
    ),
    "bram": (
        "Back home, Bram drops his bag by the door and heads straight to the kitchen. "
        "Protein-heavy meal, shower, planner, twenty minutes of focused listening to an audiobook. Routine. "
        "He likes ending the day with order – something predictable, something his. "
        "But even as the evening settles, his mind drifts back to the day."
    ),
}

# ────────────────────────────────────────────────────────────
# Trait-bucket text, customised per character pronouns
# ────────────────────────────────────────────────────────────

TEXT = {
    "fatima": {
        "Energy ⚡️": {
            "LOW":    "She feels the weight of the day in her bones. Every step, every moment took something out of her.",
            "MEDIUM": "She’s tired, but not depleted – just enough energy left to breathe deeply and be present.",
            "HIGH":   "Despite everything, she feels energized – as if the day, for all its challenges, fueled her more than it drained her.",
        },
        "Social 💬": {
            "LOW":    "Though surrounded by people, Fatima often felt distant – like the conversations happened just outside her reach.",
            "MEDIUM": "Some interactions stayed surface-level, others left warmth; the day offered just enough connection to carry forward.",
            "HIGH":   "Her day was shaped by meaningful exchanges: moments of laughter, recognition, and shared understanding.",
        },
        "Comfort 🌿": {
            "LOW":    "She felt out of place more than once today, her body tense in spaces that didn’t feel made for her.",
            "MEDIUM": "There were moments of calm and moments of discomfort – a day of navigating, not settling.",
            "HIGH":   "She found quiet pockets of peace throughout the day, spaces where she could simply be.",
        },
        "Fulfillment 🌈": {
            "LOW":    "The day left her questioning her place, unsure if she had been true to herself or simply endured.",
            "MEDIUM": "Not every moment felt right, but she still found small reminders of what matters to her.",
            "HIGH":   "She ends the day proud – grounded in her values, and grateful for the ways she stayed close to herself.",
        },
        "__closing__": "Most importantly: she showed up. And tomorrow, she’ll do it all again.",
    },

    "sock": {
        "Energy ⚡️": {
            "LOW":    "Their limbs feel leaden, their thoughts tangled – today wrung them out.",
            "MEDIUM": "The day left them tired but intact, like a match burned halfway.",
            "HIGH":   "Somehow, despite everything, they feel charged – like showing up gave them power.",
        },
        "Social 💬": {
            "LOW":    "Most of the day, they felt like they were watching through glass: present, but not quite in it.",
            "MEDIUM": "A few small conversations stuck: enough to remind them that connection is possible, even if it’s rare.",
            "HIGH":   "They found their rhythm with people today: honest exchanges, unforced laughter, no masks.",
        },
        "Comfort 🌿": {
            "LOW":    "Their edges never softened; the world felt loud, and they never fully landed in it.",
            "MEDIUM": "Some moments gave them room to breathe, others pressed in, but they made it through.",
            "HIGH":   "They found pockets of stillness, places where they didn’t have to flinch or explain.",
        },
        "Fulfillment 🌈": {
            "LOW":    "They’re left wondering if today mattered, if they were honest, or just coping.",
            "MEDIUM": "It wasn’t perfect, but there were moments that felt like them – tiny sparks of truth.",
            "HIGH":   "They end the day proud. Not loud-proud, but the quiet kind: the kind that says, I didn’t disappear.",
        },
        "__closing__": "They showed up. They stayed true. And tomorrow, they’ll do it all again.",
    },

    "carol": {
        "Energy ⚡️": {
            "LOW":    "Her back aches with the weight of everything she poured into the day. Her brain feels like it has sprinted a marathon with no water break.",
            "MEDIUM": "She’s tired in that buzzing, satisfying way, like she’s lived a whole week in a single afternoon.",
            "HIGH":   "Somehow, she’s still riding the high. The day’s chaos fed her just enough adrenaline to keep dancing through it all.",
        },
        "Social 💬": {
            "LOW":    "She was around people all day, but the connection never really clicked. Everything felt just out of sync – like laughing half a second too late.",
            "MEDIUM": "She had her moments – quick chats, a compliment here or there. Nothing deep, but enough to remind her she’s not alone.",
            "HIGH":   "The day was a whirlwind of faces, laughter, and sparks. She felt seen, heard, even celebrated. The kind of day that makes her feel magnetic.",
        },
        "Comfort 🌿": {
            "LOW":    "Her nerves are frayed. Too much stimulation, not enough grounding. Her room is finally quiet, but now her thoughts are loud.",
            "MEDIUM": "Some moments felt safe, others too much. She rolled with it, but she’s craving a soft place to land.",
            "HIGH":   "She managed to find little sanctuaries throughout the day – between music, sunlight, and people who just got her.",
        },
        "Fulfillment 🌈": {
            "LOW":    "She ends the day wondering if she showed up as herself, or just played a character everyone liked better.",
            "MEDIUM": "She didn't hit every note, but there were still sparks: tiny wins, a good laugh, a line of poetry worth keeping.",
            "HIGH":   "She feels it in her chest: that quiet hum of alignment. Like today was one step closer to who she’s becoming.",
        },
        "__closing__": "The day was a lot, but it was hers. She showed up – messy, late, impulsive, but fully herself. And she’ll do it all again tomorrow.",
    },

    "bram": {
        "Energy ⚡️": {
            "LOW":    "He can feel the fatigue in his shoulders – too many moments demanded his focus, and it shows.",
            "MEDIUM": "He’s a little worn down, but still steady – a manageable kind of tired he knows well.",
            "HIGH":   "The day sharpened him more than it drained him – he finishes with clarity and momentum.",
        },
        "Social 💬": {
            "LOW":    "He kept his distance today, and while it made things easier, part of him wonders what he missed.",
            "MEDIUM": "Some conversations felt useful, others felt like effort, but overall, he held his own.",
            "HIGH":   "He surprised himself with how much he connected – intentional moments, not just small talk.",
        },
        "Comfort 🌿": {
            "LOW":    "He spent more time on edge than he’d like to admit – out of sync with the spaces around him.",
            "MEDIUM": "The day had its awkward moments, but nothing he couldn’t navigate with a steady hand.",
            "HIGH":   "Most of today fit his pace: familiar enough to focus, calm enough to breathe.",
        },
        "Fulfillment 🌈": {
            "LOW":    "He did what was expected, but it didn’t feel like it meant much – not yet.",
            "MEDIUM": "There were glimpses of purpose, even if some of it still felt routine.",
            "HIGH":   "He ends the day with a quiet pride – not just for what he did, but for how he showed up.",
        },
        "__closing__": "He leans back in his chair, sets his glasses aside, and rubs his eyes. He met the day head-on and that’s enough, for now. Tomorrow he’ll do it all again.",
    },
}

# ────────────────────────────────────────────────────────────
# Build paragraph list: always show intro, then trait‐bucket paragraphs in order, then closing
# ────────────────────────────────────────────────────────────

intro_text   = INTRO.get(char_key, "")
trait_texts  = [TEXT[char_key][t][bucket[t]] for t in traits]
closing_text = TEXT[char_key]["__closing__"]

# Compose the full list of paragraphs.  Paragraph 0 is intro, then four trait paragraphs, then closing.
paragraphs = [intro_text] + trait_texts + [closing_text]

# ────────────────────────────────────────────────────────────
# Step counter for progressive reveal
# ────────────────────────────────────────────────────────────

if "final_step" not in st.session_state:
    st.session_state.final_step = 0  # how many of the trait/closing paragraphs are visible
step = st.session_state.final_step

# ────────────────────────────────────────────────────────────
# Layout: final_‹key› banner on left / reflection text on right
# ────────────────────────────────────────────────────────────

left_col, right_col = st.columns([3, 5], gap="large")

# ▸ Left – show that character’s “final_‹key›.png” banner
with left_col:
    banner_path = Path("assets") / "banners" / f"final_{char_key}.png"
    if banner_path.exists():
        st.image(Image.open(banner_path), use_container_width=True)
    else:
        st.warning(f"Add “assets/banners/final_{char_key}.png” to your assets folder.")

# ▸ Right – intro (always visible) + progressive paragraphs + navigation button
with right_col:
    st.markdown("### Evening Reflection")

    # Show the intro paragraph (index 0)
    st.markdown(paragraphs[0])
    st.markdown("")  # spacer

    # Reveal the next `step` paragraphs from index 1 onward
    for i in range(step):
        st.markdown(paragraphs[1 + i])
        st.markdown("")

    # If not everything is revealed yet, show “Show next…” button
    total_revealable = len(paragraphs) - 1  # excludes the intro
    if step < total_revealable:
        if st.button("Show next…", use_container_width=True):
            st.session_state.final_step += 1
            st.rerun()
    else:
        # All paragraphs are visible; final button to go to the overall outro
        if st.button("View day summary →", use_container_width=True):
            st.switch_page("pages/4_Outro.py")
