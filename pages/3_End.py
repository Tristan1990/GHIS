import streamlit as st
from pathlib import Path
from data.characters import CHARACTERS

# ── helper: reset & restart ─────────────────────────────────────
# 3_end.py
def reset_and_restart():
    st.session_state.clear()
    st.switch_page("app.py")    



# ── pull data from session ──────────────────────────────────────
cid     = st.session_state.get("selected_character")
scores  = st.session_state.get("scores", {})
meta    = CHARACTERS.get(cid, {})
traits  = meta.get("traits", [])

# ── two-column layout ───────────────────────────────────────────
left, right = st.columns([3, 5], gap="large")

# LEFT  – single outro banner + replay button
with left:
    outro_img = Path("assets/banners/final_outro.png")
    if outro_img.exists():
        st.image(str(outro_img), use_container_width=True)
    else:
        st.warning("Add **assets/banners/final_outro.png** to your assets folder.")

    # ONE replay button – clears state and returns to select screen
    if st.button("🔄 Play again", use_container_width=True):
        reset_and_restart()

# RIGHT – scores box + thank-you box
with right:
    # Final scores
    st.markdown(
        "<div style='border:1px solid #777;border-radius:6px;padding:8px;'>"
        "<strong>Final Scores</strong><br>",
        unsafe_allow_html=True,
    )
    for tr in traits:
        st.markdown(f"- **{tr}**: {scores.get(tr,0)}")
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("&nbsp;")

    # Thank-you
    st.markdown(
        "<div style='border:1px solid #777;border-radius:6px;padding:8px;'>"
        "<h3 style='margin-top:0'>🎉 Thanks for playing!</h3>"
        "<p>Your journey with these characters has just begun.<br>"
        "Feel free to start another run and explore different choices.</p>"
        "</div>",
        unsafe_allow_html=True,
    )
