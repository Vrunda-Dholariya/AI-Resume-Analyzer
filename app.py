import streamlit as st
from groq import Groq
from pypdf import PdfReader

# ---------- PAGE CONFIG (must be the FIRST Streamlit command) ----------
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide",
)

# Connect to Groq
client = Groq(api_key=st.secrets["GROQ_API_KEY"])

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
    .stButton button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        font-size: 18px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# ---------- SIDEBAR ----------
with st.sidebar:
    st.header("ℹ️ How to use")
    st.write("1. Upload your resume as a PDF")
    st.write("2. Paste a job description")
    st.write("3. Click **Analyze Match**")
    st.divider()
    st.write("Built with 🐍 Python, Groq AI & Streamlit")
    st.write("Made by **Vrunda Dholariya**")

# ---------- HEADER ----------
st.markdown(
    "<h1 style='text-align: center; color: #2E86C1;'>📄 AI Resume Analyzer</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; color: gray;'>Check how well your resume matches any job — powered by AI</p>",
    unsafe_allow_html=True,
)
st.divider()

# ---------- HELPER: read all text out of an uploaded PDF ----------
def extract_text_from_pdf(uploaded_file):
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text

# ---------- INPUTS ----------
col1, col2 = st.columns(2)

with col1:
    uploaded_resume = st.file_uploader("📄 Upload your Resume (PDF)", type="pdf")

with col2:
    job_text = st.text_area("💼 Paste the Job Description here", height=300)

# ---------- ANALYZE ----------
if st.button("Analyze Match", type="primary"):
    if uploaded_resume is None or job_text == "":
        st.warning("⚠️ Please upload your resume AND paste the job description.")
    else:
        resume_text = extract_text_from_pdf(uploaded_resume)

        # The system prompt: instructions that shape how the AI behaves
        system_prompt = """You are an expert technical recruiter and ATS (Applicant Tracking System) analyzer.
You will be given a candidate's RESUME and a JOB DESCRIPTION.
Analyze how well the resume matches the job and respond in this exact format using markdown:

## 🎯 Match Score
Give a score out of 100% with one sentence explaining it.

## ✅ Matching Strengths
Bullet points of skills/experience in the resume that match the job.

## ❌ Missing Keywords & Skills
Bullet points of important skills/keywords from the job description that are missing in the resume.

## 💡 Suggestions to Improve
3 to 5 specific, actionable tips to improve the resume for this job.

Be honest, specific, and encouraging."""

        # Call the AI, showing a spinner while it thinks
        with st.spinner("🤖 Analyzing your resume..."):
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": f"RESUME:\n{resume_text}\n\nJOB DESCRIPTION:\n{job_text}"}
                ],
            )
            analysis = response.choices[0].message.content

        st.divider()
        st.markdown(analysis)
