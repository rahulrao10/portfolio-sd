# Gauri Dilip Randive — Software Developer Portfolio

A simple and professional portfolio website built with Python and Streamlit.

## Features

- Gauri Dilip Randive — Software Developer
- Simple professional introduction
- Java, Python, SQL, DBMS and web development skills
- Projects section
- Automatically displays public GitHub repositories
- GitHub profile button
- LinkedIn placeholder
- Contact information
- Profile photo support
- Responsive Streamlit layout

## Setup

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Add the profile photo

Place the profile photo in:

```text
assets/profile.jpg
```

### 3. Add GitHub username

Open `app.py` and replace:

```python
GITHUB_USERNAME = "YOUR_GITHUB_USERNAME"
```

with the actual GitHub username.

The Projects section will automatically retrieve public repositories using the GitHub API.

### 4. Add LinkedIn later

Replace:

```python
LINKEDIN_URL = "#"
```

with the LinkedIn profile URL.

### 5. Run the portfolio

```bash
streamlit run app.py
```


Portfolio updates: refreshed styling, updated full name and contact email, and added Big Data Analytics to the skills list. Add your GitHub username and LinkedIn URL near the top of `app.py` to enable those profile links.
