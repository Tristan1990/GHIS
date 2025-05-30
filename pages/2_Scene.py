import streamlit as st
import game_router as gr

gr.init_state()

if not st.session_state.selected_character:
    st.switch_page("pages/1_Character_Select.py")
else:
    gr.render_current_scene()
