import streamlit as st
import os

# --- PAGE CONFIG ---
st.set_page_config(page_title="Krishna Kumar Karki | CV", layout="wide")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .stHeader { color: #1e3a8a; }
    .section-header { color: #008080; font-weight: bold; border-bottom: 2px solid #008080; padding-bottom: 5px; }
    </style>
    """, unsafe_allow_html=True)

st.title("📄 Full Curriculum Vitae")
st.caption("Last Updated: April 2, 2026") # [cite: 127]

# --- PERSONAL INFORMATION ---
st.markdown('<p class="section-header">👤 Personal Information</p>', unsafe_allow_html=True)
st.write("**Name:** Krishna Kumar Karki") # [cite: 91]
st.write("**Date of Birth:** 20/12/1998") # [cite: 92]
st.write("**Address:** Via Bernardino Galliari 30, 10125 Turin, Italy") # [cite: 93]
st.write("**Phone:** +4915755659606 | **Email:** karki.kris1998@gmail.com") # [cite: 94, 95]
st.write("**LinkedIn:** [linkedin.com/in/krishna-kumar-karki/](https://www.linkedin.com/in/krishna-kumar-karki/)") # [cite: 96]

# --- EDUCATION ---
st.markdown('<p class="section-header">🎓 Education</p>', unsafe_allow_html=True)

with st.expander("Masters in Multiphase Science | Politecnico di Torino, Ecole des Mines"):
    st.write("**09/2025 - Current | Turin, Italy**") # [cite: 99, 100, 102]

with st.expander("Master's in Chemical Engineering | FH Münster & Ecole des Mines"):
    st.write("**11/2023 - 09/2025 | Germany & France**") # [cite: 101]
    st.write("Completed all core graduate-level coursework.") # [cite: 101]

with st.expander("BE Chemical Engineering | Kathmandu University"):
    st.write("**07/2018 - 05/2023 | Dhulikhel, Nepal**") # [cite: 101]
    st.write("**Thesis:** Plant Design for Production of Acetaminophen from Nitrobenzene (PFD, P&ID, Equipment Design, Economic analysis, Safety and Hazards).") # [cite: 101]

with st.expander("Foundational Course for BSc | Tribhuwan University"):
    st.write("**07/2018 - 05/2023 | Kathmandu, Nepal**") # [cite: 103, 109]
    st.write("Majors in Geology, Mathematics, and Physics.") # [cite: 110]

# --- WORK EXPERIENCE ---
st.markdown('<p class="section-header">💼 Work Experience</p>', unsafe_allow_html=True)

with st.expander("Student Research Assistant | Münster University of Applied Sciences"):
    st.write("**12/2024 - 02/2025 | Germany**") # [cite: 88, 89]
    st.write("Microalgae and fluid mechanics experimental setup.") # 

with st.expander("Restaurant Assistant | Steinfurt, Germany"):
    st.write("**06/2024 - 08/2025**") # 
    st.write("Food preparation, baking Flammkuchen, and hygiene management.") # 

with st.expander("Working Student | Succedo Unternehmensberatung GmbH"):
    st.write("**04/2024 - 06/2024 | Germany**") # 
    st.write("Calculated yearly energy consumption for German companies and organized logs.") # 

with st.expander("Research Assistant | National Innovation Centre"):
    st.write("**12/2022 - 09/2023 | Kathmandu, Nepal**") # 
    st.write("Lab experiment and design for biogas plant reoperation; studied microalgae feasibility.") # 

with st.expander("Research Intern | Natural Product and Bacterial Lab"):
    st.write("**02/2021 - 02/2022 | Dhulikhel, Nepal**") # 
    st.write("Measured antioxidant and enzyme inhibitory potential of metabolites.") # 

with st.expander("Science Teacher | Sunghava English Boarding School"):
    st.write("**04/2017 - 05/2018 | Urlabari, Nepal**") # 
    st.write("Instructor for grades 4, 6, and 7.") # 

# --- PROJECT WORK ---
st.markdown('<p class="section-header">🚀 Project Work</p>', unsafe_allow_html=True)

with st.expander("Industrial Master's Project | Supervised by Framatome"):
    st.write("**10/2025 - Present | France**") # [cite: 105, 111]
    st.write("Studying flow properties of metal powders and simulation for nuclear reactor fuel.") # [cite: 112]

with st.expander("🌱 Startup Spirulina | KOICA Funded"):
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.write("### Project Overview")
        st.write("""
        * **Optimization:** Localized spirulina media for the Nepal climate.
        * **Innovation:** Developed Spirulina-infused cookies and pasta.
        * **Research:** Focused on extracting **Phycocyanin** (natural blue antioxidant).
        * **Funding:** Successfully secured seed funding from **KOICA**.
        """)
        
    with col2:
        # Video placed on the right side for a modern CV look
        st.video("https://www.youtube.com/watch?v=tAqX5RSIWTk")

# --- PUBLICATION & WORKSHOPS ---
with st.expander("📄 Publication: Streptomyces sp. G-18 Research"):
    st.markdown("### Antioxidant & Enzyme Inhibitory Potential")
    st.write("**DOI:** [10.1155/2023/6439466](https://doi.org/10.1155/2023/6439466)")
    
    st.write("""
    - **Focus:** Growth media optimization for *Streptomyces sp. G-18*.
    - **Impact:** Demonstrated high antioxidant and enzyme inhibitory potential.
    """)

    # Simple download button (ensure 'publication.pdf' is in your GitHub folder)
    with open("publication.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Full Paper",
            data=pdf_file,
            file_name="Streptomyces_G18_Research.pdf",
            mime="application/pdf"
        )
st.write("**Workshop (04/2025):** Algae Biotechnology, Fraunhofer Institute IGB, Germany.") # [cite: 117, 122]
st.write("**Workshop (06/2025):** Training in Algae Related Industrial Processes, University of Almeria.") # [cite: 118, 123]

# --- SKILLS & COURSES ---
st.markdown('<p class="section-header">🛠️ Skills & Online Courses</p>', unsafe_allow_html=True)
st.write(f"**Software:** C, C++, Python, MS Office, SolidWorks, AutoCAD, Aspen, ImageJ, Polymath, and Ansys.") # 
st.write(f"**Languages:** Nepali (Native), English (C1), Hindi (C1), German (A2.1), Punjabi (A1).") # 
st.write(f"**Online Courses:** Becoming an Entrepreneur (MIT), Algae Biotechnology (UC San Diego), Solid Waste Management (World Bank), etc.") # [cite: 125]

# --- PDF DOWNLOAD & CERTIFICATES ---
st.divider()
cv_filename = "CV_Krishna_Kumar_Karki april 2 2026.pdf"
if os.path.exists(cv_filename):
    with open(cv_filename, "rb") as f:
        st.download_button("📥 Download Full Professional CV (PDF)", f, file_name=cv_filename, use_container_width=True)

st.info("Additional certificates and project photos are available in the expanded sections above.")
