import streamlit as st

# Define your custom CSS
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400&display=swap');

body {
    font-family: 'Inter'
}
</style>
"""

# Inject custom CSS with markdown
st.markdown(custom_css, unsafe_allow_html=True)

st.title("🎈 My new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)
