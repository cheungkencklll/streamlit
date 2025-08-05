import streamlit as st

# Set page configuration for the app
st.set_page_config(
    page_title="Streamlit Features Demo",
    page_icon="🚀",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Define Home page function
def home_page():
    st.title("🚀 Streamlit Features Demo")
    st.header("Welcome to Streamlit Features Demo")
    st.write("""
    This app demonstrates various features of Streamlit, including:
    - Interactive widgets
    - Layout management
    - Data visualization
    - Media handling
    - File uploads
    - Chat interface
    - Caching
    Navigate using the sidebar to explore each section!
    """)
    st.balloons()

# Define page configurations
pages = {
    "Home": st.Page(
        home_page,
        title="Home",
        icon="🏠"
    ),
    "Widgets": st.Page(
        "pages/Widgets.py",
        title="Interactive Widgets",
        icon="🎮"
    ),
    "Layouts": st.Page(
        "pages/Layouts.py",
        title="Layout Features",
        icon="🗺️"
    ),
    "Data Display": st.Page(
        "pages/Data_Display.py",
        title="Data Visualization",
        icon="📊"
    ),
    "Charts": st.Page(
        "pages/Charts.py",
        title="Charts & Graphs",
        icon="📈"
    ),
    "Media & Files": st.Page(
        "pages/Media_Files.py",
        title="Media & Files",
        icon="📁"
    ),
    "Chat": st.Page(
        "pages/Chat.py",
        title="Chat Interface",
        icon="💬"
    ),
    "Caching": st.Page(
        "pages/Caching.py",
        title="Caching Demo",
        icon="⚡"
    )
}

# Set navigation
page = st.navigation(list(pages.values()))
page.run()