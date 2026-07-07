# 📄 AI Resume Analyzer

A live Generative AI web app that analyzes how well a resume matches a job
description — giving a match score, matching strengths, missing keywords, and
actionable suggestions. Built with the Groq LLM API and Streamlit.

**🔗 Live Demo:** _(paste your Streamlit link here after deploying)_

---

## 📌 The problem it solves
Job seekers often get rejected without knowing *why* their resume didn't fit.
This tool gives instant, honest feedback so they can tailor their resume to
each job before applying.

## 🛠️ Tech Stack
- **Python**
- **Groq API** — large language model (Llama 3.3) for the analysis
- **pypdf** — extracts text from uploaded PDF resumes
- **Streamlit** — web interface and deployment

## ⚙️ How it works
1. User uploads their resume as a PDF and pastes a job description.
2. `pypdf` extracts the text from the PDF.
3. A carefully designed **system prompt** instructs the LLM to act as an ATS /
   technical recruiter and return a structured analysis.
4. The resume text + job description are sent to the Groq API, and the
   formatted result is displayed live.

## 🔒 Security
The Groq API key is stored securely using **Streamlit secrets** — it is never
hard-coded or committed to GitHub (`.streamlit/secrets.toml` is git-ignored).

## ✨ Features
- PDF resume upload with automatic text extraction
- Match score out of 100%
- Matching strengths and missing keywords
- Actionable suggestions to improve the resume
- Input validation before calling the AI

## ▶️ Run it locally
```bash
pip install -r requirements.txt
# add your key to .streamlit/secrets.toml as: GROQ_API_KEY = "your_key"
streamlit run app.py
```

---
Built by **Vrunda Dholariya** as part of my AI/ML learning journey. 🚀
