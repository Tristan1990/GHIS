# pages/4_Outro.py
import streamlit as st
from pathlib import Path
from PIL import Image
from data.characters import CHARACTERS


# ── helper: reset & return to character-select ────────────────────────────────
def replay():
    st.session_state.clear()
    st.switch_page("app.py")


# ── pull data we still need ───────────────────────────────────────────────────
cid     = st.session_state.get("selected_character")
scores  = st.session_state.get("scores", {})
meta    = CHARACTERS.get(cid, {})
traits  = meta.get("traits", [])

st.markdown("## First day at the university summary")

# ── two main columns  ❰ banner ❱  |  ❰ stacked right column ❱ ────────────────
left, right = st.columns([2, 2], gap="small")

# LEFT  >>> big banner
with left:
    banner_path = Path("assets/banners/final_outro.png")
    if banner_path.exists():
        st.image(Image.open(banner_path), use_container_width=True)
    else:
        st.warning("Add **assets/banners/final_outro.png** to your assets folder.")

# RIGHT >>> top box = thank-you  | bottom box = scores
with right:
    # Top-right  ─ thank-you
    st.markdown(
        """
        <div style='border:1px solid #777;border-radius:8px;
                    padding:1rem 1.2rem; margin-bottom:1rem;'>
          <h3 style='margin-top:0'>✨ Thanks for playing!</h3>
          We hope you enjoyed playing and got to know the characters a bit!<br>
          Feel free to start another run and explore different choices.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Bottom-right  ─ score summary
    st.markdown(
        "<div style='border:1px solid #777;border-radius:8px;padding:0.8rem;'>"
        "<strong>Final Scores</strong><br>",
        unsafe_allow_html=True,
    )
    for tr in traits:
        st.markdown(f"- **{tr}**: {scores.get(tr, 0)}")
    st.markdown("</div>", unsafe_allow_html=True)

# Full-width replay button below the two-column block
st.markdown("")
if st.button("🔄 Play again", use_container_width=True):
    replay()
