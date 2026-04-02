import streamlit as st
import os

# 1. PAGE CONFIG (Must be the first Streamlit command)
st.set_page_config(page_title="Krishna Kumar Karki", layout="wide")

# --- 2. CUSTOM CSS FOR BRANDING & FOOTER ---
st.markdown("""
    <style>
        /* Top Navigation Style */
        .top-bar {
            display: flex;
            align-items: center;
            padding: 10px 0;
            border-bottom: 2px solid #008080;
            margin-bottom: 20px;
        }
        .top-bar img {
            border-radius: 50%;
            margin-right: 15px;
            border: 2px solid #1e3a8a;
            object-fit: cover;
        }
        .top-bar h1 {
            font-size: 1.8rem !important;
            margin: 0;
            color: #1e3a8a;
            font-weight: bold;
            text-transform: uppercase;
        }

        /* Footer Style */
        .footer {
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #008080;
            color: white;
            text-align: center;
            padding: 12px 0;
            z-index: 100;
        }
        .footer a {
            color: white;
            margin: 0 15px;
            text-decoration: none;
            font-size: 1.1rem;
            font-weight: 500;
        }
        
        /* Spacing for main content so footer doesn't overlap */
        .main-block {
            margin-bottom: 120px;
        }

        /* Button Styling */
        .stButton>button {
            width: 100%;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)

# --- 3. TOP NAVIGATION BAR ---
# Using the first profile image as your icon
icon_path = "profile_1 (1).jpg"
st.markdown(f"""
    <div class="top-bar">
        <img src="app/static/{icon_path}" onerror="this.src='https://cdn-icons-png.flaticon.com/512/3135/3135715.png'" width="50" height="50">
        <h1>KRISHNA KUMAR KARKI</h1>
    </div>
    """, unsafe_allow_html=True)

# --- 4. HERO SECTION (6 PHOTOS SLIDER) ---
# Updated list to match your exact filenames in the latest screenshot
hero_images = [
    "profile_1 (1).jpg", "profile_1 (1).png", "profile_1 (2).jpg", 
    "profile_1 (2).png", "profile_1 (3).jpg", "your-picture.png"
]

if 'hero_index' not in st.session_state:
    st.session_state.hero_index = 0

current_img = hero_images[st.session_state.hero_index]

# Display the main hero image
if os.path.exists(current_img):
    st.image(current_img, use_container_width=True)
else:
    st.warning(f"File '{current_img}' not found. Check names in your folder.")

# Navigation Arrows for Slider
c1, c2, c3 = st.columns([1, 10, 1])
with c1:
    if st.button("❮"):
        st.session_state.hero_index = (st.session_state.hero_index - 1) % len(hero_images)
        st.rerun()
with c3:
    if st.button("❯"):
        st.session_state.hero_index = (st.session_state.hero_index + 1) % len(hero_images)
        st.rerun()

# --- 5. ABOUT & CONTACT SECTION ---
st.markdown('<div class="main-block">', unsafe_allow_html=True)

st.title("About Me")
st.write("""
I am a **Chemical Engineer** and **Erasmus Mundus Scholar** currently based in **Turin, Italy**. 
My expertise includes process design, techno economic anaysis of industrial process, modeling of physical and chemical process.
""")

# Action Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("📖 Read More (Full CV)"):
        st.switch_page("pages/1_CURRICULUM_VITAE.py")
with col2:
    if os.path.exists("CV.pdf"):
        with open("CV.pdf", "rb") as f:
            st.download_button("📥 Download CV (PDF)", f, file_name="Krishna_Karki_CV.pdf")
with col3:
    # This button opens your separate contact page
    if st.button("📩 Contact Me"):
        st.switch_page("pages/4_CONTACT.py")

st.markdown('</div>', unsafe_allow_html=True)

# --- 6. SOCIAL FOOTER ---
st.markdown(f"""
    <div class="footer">
        <span>© 2026 Krishna Kumar Karki</span>
        <a href="https://www.linkedin.com/in/krishna-kumar-karki/" target="_blank">
            <span style="background:#0077b5; padding:2px 5px; border-radius:3px;">in</span> LinkedIn
        </a>
        <a href="https://www.quora.com/profile/Krishna-Kumar-Karki-1/answers" target="_blank">
            <span style="background:#b92b27; padding:2px 5px; border-radius:3px;">Q</span> Quora
        </a>
    </div>
    """, unsafe_allow_html=True)