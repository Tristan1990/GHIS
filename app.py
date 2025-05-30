# app.py

import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
from PIL import Image, ImageOps
import io

from game_router import pick_character
from data.characters import CHARACTERS

# -----------------------------------------------------------
# 1  Page config – collapsed sidebar
# -----------------------------------------------------------
try:
    st.set_page_config(
        page_title="Interactive Narrative",
        page_icon="🎮",
        layout="wide",
        initial_sidebar_state="collapsed",
    )
except st.errors.StreamlitSetPageConfigMustBeFirstCommandError:
    pass

# -----------------------------------------------------------
# 2  Hide the sidebar + inject CSS for layout & badges
# -----------------------------------------------------------
st.markdown(
    """
    <style>
      /* Hide the built-in Streamlit sidebar */
      section[data-testid="stSidebar"] {
        display: none !important;
      }
      div[data-testid="stSidebarCollapsed"] + div[role="main"] {
        margin-left: 0 !important;
      }

      /* Our flex wrapper for each character column */
      .col-flex {
        display: flex;
        flex-direction: column;
        height: 100%;
      }
      .col-flex .stButton {
        margin-top: auto;  /* push the button to the bottom */
      }

      /* Pronoun badge styling */
      .pronoun-badge {
        display: inline-block;
        background: #f0f0f0;
        color: #333;
        border-radius: 4px;
        padding: 0 6px;
        font-size: 0.8rem;
        margin-left: 8px;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------------------------------------
# 3  Paths & constants
# -----------------------------------------------------------
BASE_DIR  = Path(__file__).parent
ASSETS    = BASE_DIR / "assets"
PORTRAITS = ASSETS / "portraits"
SUPPORTED = {".png", ".jpg", ".jpeg", ".webp", ".avif"}
CHAR_SIZE = 180  # square portrait size in px

# -----------------------------------------------------------
# 4  Helper functions
# -----------------------------------------------------------
def find_portrait(stem: str) -> Path | None:
    if not PORTRAITS.exists():
        return None
    for p in PORTRAITS.iterdir():
        if p.stem.lower() == stem.lower() and p.suffix.lower() in SUPPORTED:
            return p
    return None

def load_image(path: Path) -> Image.Image | None:
    try:
        return Image.open(path)
    except Exception:
        try:
            return Image.open(io.BytesIO(path.read_bytes()))
        except Exception:
            return None

def make_square(img: Image.Image, size: int) -> Image.Image:
    img = ImageOps.contain(img, (size, size), Image.Resampling.LANCZOS)
    canvas = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    canvas.paste(img, ((size - img.width) // 2, (size - img.height) // 2))
    return canvas

# -----------------------------------------------------------
# 5  Banner (external HTML)
# -----------------------------------------------------------
components.html(
    """
    <div class='banner'>
      <img src='https://www.firstunitarianottawa.ca/uploads/2/1/0/6/21068182/uu-pride-banner_orig.png' alt='UU Pride Banner'>
    </div>
    <style>
      .banner {
        width:100%;
        height:200px;
        overflow:hidden;
        display:flex;
        align-items:center;
        justify-content:center;
        background:#000;
      }
      .banner img {
        width:100%;
        height:100%;
        object-fit:cover;
      }
    </style>
    """,
    height=210,
)

st.subheader("Choose your character")

# -----------------------------------------------------------
# 6  Session state init
# -----------------------------------------------------------
if "selected_character" not in st.session_state:
    st.session_state.selected_character = None

# -----------------------------------------------------------
# 7  Render characters + Experience Points sidebar
# -----------------------------------------------------------
cols = st.columns([1, 1, 1, 1, 0.8], gap="large")

# 7a) Four character columns
for col, (char_id, meta) in zip(cols[:-1], CHARACTERS.items()):
    with col:
        # flex container start
        st.markdown('<div class="col-flex">', unsafe_allow_html=True)

        # Portrait
        pic = find_portrait(meta["stem"])
        if pic:
            img = load_image(pic)
            st.image(make_square(img.convert("RGBA"), CHAR_SIZE), width=CHAR_SIZE)
        else:
            st.warning(f"Add {meta['stem']}.[png|jpg|webp|avif] to assets/portraits/")

        # Name + pronouns
        pronouns = meta.get("pronouns", "")
        st.markdown(
            f"### {meta['name']}<span class='pronoun-badge'>{pronouns}</span>",
            unsafe_allow_html=True,
        )

        # Description
        st.markdown(meta["desc"])

        # Play button (auto-pushed to bottom)
        if st.button(f"Play as {meta['name']}", key=char_id, use_container_width=True):
            pick_character(char_id)
            st.switch_page("pages/2_Scene.py")

        # flex container end
        st.markdown('</div>', unsafe_allow_html=True)

# 7b) XP sidebar on the right
with cols[-1]:
    st.markdown(
        """
        <div style='border:1px solid #666;border-radius:6px;padding:1rem;
                    font-size:0.95rem;line-height:1.4;'>
          <strong>Experience Points</strong>
          <ul style='margin-top:0.5rem;padding-left:1.2rem;'>
            <li><strong>Energy ⚡️</strong>: Physical & mental stamina; depleted by stress or exertion.</li>
            <li><strong>Comfort 🌿</strong>: Emotional safety & physical ease; shaped by environment & accessibility.</li>
            <li><strong>Social 💬</strong>: Confidence & ease in interactions; feeling accepted and connected.</li>
            <li><strong>Fulfillment 🌈</strong>: Sense of satisfaction, enjoyment, and purpose.</li>
          </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

# -----------------------------------------------------------
# 8  Fallback info if no pick
# -----------------------------------------------------------
if not st.session_state.selected_character:
    st.info("Select a character to continue.")
