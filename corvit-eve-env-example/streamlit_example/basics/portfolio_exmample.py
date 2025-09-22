import streamlit as st
from PIL import Image
import base64

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="My Portfolio", layout="wide")

# ----------------------------
# Custom CSS
# ----------------------------
st.markdown("""
    <style>
    /* Overall Page Styling */
    body {
        background-color: #f9f9f9;
        font-family: 'Helvetica Neue', sans-serif;
    }

    /* Hero Section */
    .hero {
        text-align: center;
        padding: 60px 20px;
        background: linear-gradient(135deg, #4A90E2, #50E3C2);
        border-radius: 12px;
        color: white;
        margin-bottom: 40px;
    }

    .hero h1 {
        font-size: 3rem;
        font-weight: bold;
    }

    .hero p {
        font-size: 1.2rem;
        margin-top: 10px;
    }

    /* Section Headings */
    .section-title {
        font-size: 2rem;
        font-weight: bold;
        color: #333;
        margin-bottom: 20px;
        text-align: center;
    }

    /* Cards */
    .card {
        background: white;
        border: 1px solid #e0e0e0;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        transition: 0.3s;
        height: 100%;
    }
    .card:hover {
        box-shadow: 0px 4px 20px rgba(0,0,0,0.1);
        transform: translateY(-5px);
    }

    /* Footer */
    .footer {
        text-align: center;
        margin-top: 50px;
        padding: 20px;
        font-size: 0.9rem;
        color: #777;
    }
    </style>
""", unsafe_allow_html=True)

# ----------------------------
# Hero Section
# ----------------------------
st.markdown("""
<div class="hero">
    <h1>👋 Hi, I'm Muhammad Fahad</h1>
    <p>Flutter Developer | AI Enthusiast | Remote Software Engineer</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------
# About Me Section
# ----------------------------
st.markdown("<div class='section-title'>About Me</div>", unsafe_allow_html=True)
st.write("""
I'm a **Flutter Developer** with 2+ years of experience building mobile applications 
for Android and iOS. I specialize in creating **offline-first apps**, integrating **RESTful APIs**, 
and implementing clean architectures like **MVVM** with **Riverpod** and **Bloc**.  

I love working with modern technologies, building scalable solutions, and collaborating with 
remote teams to create impactful products.
""")

# ----------------------------
# Skills Section
# ----------------------------
st.markdown("<div class='section-title'>My Skills</div>", unsafe_allow_html=True)

skills = [
    {"name": "Flutter", "icon": "💙"},
    {"name": "Dart", "icon": "🎯"},
    {"name": "Firebase", "icon": "🔥"},
    {"name": "Python", "icon": "🐍"},
    {"name": "REST APIs", "icon": "🔗"},
    {"name": "Riverpod / Bloc", "icon": "⚙️"},
]

cols = st.columns(3)
for index, skill in enumerate(skills):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="card">
            <h2 style="font-size:40px;">{skill['icon']}</h2>
            <p style="font-size:18px;">{skill['name']}</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------
# Projects Section
# ----------------------------
st.markdown("<div class='section-title'>Projects</div>", unsafe_allow_html=True)

projects = [
    {
        "title": "NutraStat IPM",
        "description": "A shipboard management app for cleaning, food delivery, and employee tracking with offline-first sync.",
        "image": "assets/img.png"
    },
    {
        "title": "Cyber Security App",
        "description": "A Flutter-based cyber security mobile application with real-time notifications and Firebase integration.",
        "image": "assets/img.png"
    },
    {
        "title": "Fashion AI Recommendation App",
        "description": "An AI-powered app suggesting personalized fashion, jewelry, and makeup using advanced ML models.",
        "image": "assets/img.png"
    }
]

proj_cols = st.columns(3)
for index, proj in enumerate(projects):
    with proj_cols[index % 3]:
        st.markdown(f"""
        <div class="card">
            <img src="{proj['image']}" style="width:100%; height:150px; object-fit:cover; border-radius:8px; margin-bottom:10px;">
            <h3>{proj['title']}</h3>
            <p style="font-size:14px; color:#555;">{proj['description']}</p>
        </div>
        """, unsafe_allow_html=True)

# ----------------------------
# Contact Section
# ----------------------------
st.markdown("<div class='section-title'>Contact Me</div>", unsafe_allow_html=True)
contact_form = st.form(key='contact_form')
with contact_form:
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message")
    submit = st.form_submit_button("Send Message")

    if submit:
        if name and email and message:
            st.success("Thank you for reaching out! I'll get back to you soon.")
        else:
            st.error("Please fill out all fields before submitting.")

# ----------------------------
# Footer
# ----------------------------
st.markdown("""
<div class="footer">
    © 2025 Muhammad Fahad | Built with ❤️ using Streamlit
</div>
""", unsafe_allow_html=True)
