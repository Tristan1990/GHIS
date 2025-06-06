# pages/3_End.py
import streamlit as st
from pathlib import Path
from PIL import Image
from data.characters import CHARACTERS

cid     = st.session_state.get("selected_character")
scores  = st.session_state.get("scores", {})
meta    = CHARACTERS.get(cid, {})
traits  = meta.get("traits", [])

# ── buckets (low / medium / high) ──────────────────────────────
bucket = {}
for t in traits:
    v = scores.get(t, 0)
    bucket[t] = "LOW" if v < 7 else ("MEDIUM" if v < 15 else "HIGH")

# canned text per trait
TEXT = {
    "Energy ⚡️": {
        "LOW":    "You feel the weight of the day in your bones. Every step, every moment took something out of you.",
        "MEDIUM": "You’re tired, but not depleted—just enough energy left to breathe deeply and be present.",
        "HIGH":   "Despite everything, you feel energized—as if the day, for all its challenges, fueled you more than it drained you."
    },
    "Social 💬": {
        "LOW":    "Though surrounded by people, you often felt distant—like conversations happened just outside your reach.",
        "MEDIUM": "Some interactions stayed surface-level, others brought warmth. The day offered just enough connection to carry you forward.",
        "HIGH":   "Your day was shaped by meaningful exchanges: moments of laughter, recognition, and shared understanding."
    },
    "Comfort 🌿": {
        "LOW":    "You felt out of place more than once today, your body tense in spaces that didn’t feel made for you.",
        "MEDIUM": "There were moments of calm and moments of discomfort—a day of navigating, not settling.",
        "HIGH":   "You found quiet pockets of peace throughout the day, spaces where you could simply be."
    },
    "Fulfillment 🌈": {
        "LOW":    "The day left you questioning your place, unsure if you had been true to yourself or simply endured.",
        "MEDIUM": "Not every moment felt right, but you still found small reminders of what matters to you.",
        "HIGH":   "You end the day proud—grounded in your values, and grateful for the ways you stayed close to yourself."
    },
}

paragraphs = [(t, TEXT[t][bucket[t]]) for t in traits]   # fixed order

# step counter (0-4)
if "final_step" not in st.session_state:
    st.session_state.final_step = 0
step = st.session_state.final_step

# ── layout: portrait left, text right ─────────────────────────
left, right = st.columns([3, 5], gap="large")

# left: character portrait
with left:
    portrait = None
    for ext in [".png", ".jpg", ".jpeg", ".webp", ".avif"]:
        p = Path("assets/portraits") / f"{meta['stem']}{ext}"
        if p.exists():
            portrait = p
            break
    if portrait:
        st.image(Image.open(portrait), use_container_width=True)
    else:
        st.warning(f"Add portrait for {meta['name']} in assets/portraits/")

# right: progressive paragraphs
with right:
    st.markdown("### Evening reflection")
    for i in range(step):
        tr, txt = paragraphs[i]
        st.markdown(f"**{tr}**")
        st.markdown(txt)
        st.markdown("")

    if step < len(paragraphs):
        if st.button("Show next…", use_container_width=True):
            st.session_state.final_step += 1
            st.rerun()
    else:
        if st.button("View day summary →", use_container_width=True):
            st.switch_page("pages/4_Outro.py")
