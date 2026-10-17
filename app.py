import streamlit as st
import requests
from pathlib import Path

st.set_page_config(
    page_title="Gauri Randive | Software Developer",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# =========================
# EDIT THESE TWO VALUES
# =========================
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"
LINKEDIN_URL = "#"

GITHUB_PROFILE_URL = (
    f"https://github.com/{GITHUB_USERNAME}"
    if GITHUB_USERNAME != "YOUR_GITHUB_USERNAME"
    else "#"
)

# =========================
# CUSTOM CSS
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@400;500;600;700;800&display=swap');
:root { --ink:#172033; --muted:#667085; --blue:#3457d5; --line:#e5eaf3; }
html, body, [class*="css"] { font-family:'DM Sans',sans-serif; }
.stApp { background:linear-gradient(180deg,#f5f7ff 0%,#fbfcff 42%,#f7f9fc 100%); color:var(--ink); }
.block-container { max-width:1120px; padding-top:1.6rem; padding-bottom:3rem; }
.hero { background:linear-gradient(130deg,#172033 0%,#263d68 58%,#3457d5 100%); border-radius:24px; padding:34px 36px; color:white; margin-bottom:22px; box-shadow:0 18px 45px rgba(31,48,94,.14); }
.hero h1 { font-family:'Manrope',sans-serif; font-size:clamp(30px,4vw,46px); letter-spacing:-1.4px; margin:0 0 8px; font-weight:800; color:#fff; }
.hero h2 { color:#b9ccff; font-size:21px; margin:0 0 15px; font-weight:700; }
.hero p { color:#e0e7f5; font-size:15.5px; line-height:1.8; max-width:700px; }
.section-title { font-family:'Manrope',sans-serif; font-size:27px; letter-spacing:-.6px; font-weight:800; color:#172033; margin:36px 0 17px; }
.card { background:rgba(255,255,255,.92); border:1px solid var(--line); border-radius:18px; padding:23px; height:100%; box-shadow:0 8px 25px rgba(29,43,80,.045); }
.card h3 { margin-top:0; color:#172033; font-family:'Manrope',sans-serif; font-weight:800; }
.card p { color:#667085; line-height:1.75; }
.skill { display:inline-block; background:#edf2ff; color:#2d4ec1; border:1px solid #dce5ff; padding:8px 13px; border-radius:999px; margin:5px 5px 5px 0; font-size:13px; font-weight:700; }
.contact-box { background:linear-gradient(130deg,#172033,#263d68); color:white; border-radius:20px; padding:30px; box-shadow:0 16px 35px rgba(31,48,94,.12); }
.contact-box a { color:#c9d7ff; text-decoration:none; }
.contact-box p { line-height:1.8; }
.footer { text-align:center; color:#7a8498; padding:30px 0 5px; font-size:13px; }
div.stButton > button, div.stLinkButton > a { border-radius:12px; font-weight:700; border:1px solid #dce4f4; min-height:42px; }
div.stButton > button[kind="primary"], div.stLinkButton > a { transition:all .2s ease; }
[data-testid="stImage"] img { border-radius:22px; border:4px solid white; box-shadow:0 15px 35px rgba(31,48,94,.14); }
hr { border-color:#e6eaf2; }
</style>
""", unsafe_allow_html=True)

# =========================
# HEADER
# =========================
st.markdown("""
<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:18px;">
    <div style="font-weight:800;font-size:22px;color:#111827;">GR.</div>
    <div style="color:#4b5563;font-size:14px;">Software Developer · Portfolio</div>
</div>
""", unsafe_allow_html=True)

# =========================
# HERO SECTION
# =========================
photo_path = Path("assets/profile.jpg")

left, right = st.columns([1, 2.2], vertical_alignment="center")

with left:
    if photo_path.exists():
        st.image(str(photo_path), width=210)
    else:
        st.markdown("""
        <div style="
            width:210px;
            height:210px;
            border-radius:50%;
            background:#2563eb;
            display:flex;
            align-items:center;
            justify-content:center;
            color:white;
            font-size:58px;
            font-weight:800;
            border:5px solid white;
            margin:auto;">
            GR
        </div>
        """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div class="hero" style="padding:5">
        <h1>Gauri Dilip Randive</h1>
        <h2>Software Developer</h2>
        <p>
            I am a software developer who enjoys building useful and simple
            applications. I like learning new technologies, solving problems,
            and improving my programming skills. I am interested in creating
            clean, practical and user-friendly software.
        </p>
    </div>
    """, unsafe_allow_html=True)

    b1, b2 = st.columns(2)

    with b1:
        if GITHUB_PROFILE_URL != "#":
            st.link_button(
                "GitHub Profile",
                GITHUB_PROFILE_URL,
                use_container_width=True
            )
        else:
            st.button(
                "GitHub Profile",
                disabled=True,
                use_container_width=True
            )

    with b2:
        if LINKEDIN_URL != "#":
            st.link_button(
                "LinkedIn",
                LINKEDIN_URL,
                use_container_width=True
            )
        else:
            st.button(
                "LinkedIn (add link)",
                disabled=True,
                use_container_width=True
            )

# =========================
# ABOUT
# =========================
st.markdown(
    '<div class="section-title">About Me</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="card">
    <p>
        I am a software developer with an interest in programming and
        application development. I enjoy working with Java, databases and
        web technologies. I am always ready to learn new skills and work
        on projects that help me grow as a developer.
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# SKILLS
# =========================
st.markdown(
    '<div class="section-title">Skills</div>',
    unsafe_allow_html=True
)

skills = [
    "Java",
    "Python",
    "OOP",
    "SQL",
    "DBMS",
    "Big Data Analytics",
    "HTML",
    "CSS",
    "JavaScript",
    "Git & GitHub",
    "Problem Solving",
    "Communication"
]

st.markdown(
    "".join(
        f'<span class="skill">{skill}</span>'
        for skill in skills
    ),
    unsafe_allow_html=True
)

# =========================
# PROJECTS
# =========================
st.markdown(
    '<div class="section-title">Projects</div>',
    unsafe_allow_html=True
)

def get_github_repos(username):
    """Fetch public repositories from GitHub."""
    url = f"https://api.github.com/users/{username}/repos"

    params = {
        "sort": "updated",
        "direction": "desc",
        "per_page": 12
    }

    try:
        response = requests.get(
            url,
            params=params,
            timeout=8,
            headers={
                "Accept": "application/vnd.github+json"
            }
        )

        if response.ok:
            return response.json()

    except requests.RequestException:
        pass

    return []


repos = []

if GITHUB_USERNAME != "YOUR_GITHUB_USERNAME":
    repos = get_github_repos(GITHUB_USERNAME)

if repos:

    cols = st.columns(3)

    for i, repo in enumerate(repos):

        with cols[i % 3]:

            description = (
                repo.get("description")
                or "GitHub software project."
            )

            language = (
                repo.get("language")
                or "Programming"
            )

            st.markdown(
                f"""
                <div class="card">
                    <h3>{repo['name']}</h3>
                    <p>{description}</p>
                    <span class="skill">{language}</span>
                    &nbsp; ⭐ {repo.get('stargazers_count', 0)}
                </div>
                """,
                unsafe_allow_html=True
            )

            st.link_button(
                "View Project",
                repo["html_url"],
                use_container_width=True
            )

else:

    default_projects = [
        (
            "Java Application",
            "A simple application developed using Java and object-oriented programming.",
            "Java"
        ),
        (
            "Database Project",
            "A project using SQL and DBMS concepts to store and manage information.",
            "SQL / DBMS"
        ),
        (
            "Web Application",
            "A simple web application created using HTML, CSS and JavaScript.",
            "Web"
        )
    ]

    cols = st.columns(3)

    for i, (name, description, technology) in enumerate(default_projects):

        with cols[i]:

            st.markdown(
                f"""
                <div class="card">
                    <h3>{name}</h3>
                    <p>{description}</p>
                    <span class="skill">{technology}</span>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.info(
        "Add the GitHub username at the top of app.py to automatically "
        "display the public repositories from the GitHub profile."
    )

# =========================
# CONTACT
# =========================
st.markdown(
    '<div class="section-title">Contact</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="contact-box">
    <h3 style="margin-top:0;">Let's Connect</h3>

    <p>
        📧
        <a href="mailto:gourirandive@gmail.com">
            gourirandive@gmail.com
        </a>
    </p>


    <p>
        💼
        <a href="#" target="_blank">
            LinkedIn — add your profile link
        </a>
    </p>

    <p>
        🐙
        <a href="#" target="_blank">
            GitHub — add your profile link
        </a>
    </p>
</div>
""", unsafe_allow_html=True)

# =========================
# FOOTER
# =========================
st.markdown(
    '<div class="footer">© 2026 Gauri Randive · Software Developer</div>',
    unsafe_allow_html=True
)
