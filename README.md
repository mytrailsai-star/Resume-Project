Transformer-Based Resume–JD Matching System
This project is an AI-powered system that matches resumes with a given Job Description (JD) using NLP and transformer-based embeddings.
It ranks resumes based on relevance and highlights matched and missing skills.

🚀 Features
Upload multiple resumes (PDF)
Paste a Job Description
Resume ranking based on semantic similarity
Display matched skills
Identify missing skills
Web-based interface (browser supported)
🛠️ Tech Stack
Python
Streamlit
Sentence Transformers
PyMuPDF (fitz)
NLP / Embeddings
📅 Development Progress
Day 1
Project setup and environment configuration
Installed required libraries
Basic Streamlit app structure created
Initial resume and JD input handling
Day 2
Implemented PDF resume text extraction using PyMuPDF
Added support for multiple resume uploads
Integrated transformer-based embedding model
Calculated similarity between resume and JD
Day 3
Implemented resume ranking logic
Faced browser and rendering issues
Debugged upload and re-run problems in Streamlit
Improved data flow between resumes and JD
Day 4
Resume ranking displayed correctly
Matched skills and missing skills shown clearly
Browser issues resolved
Application running smoothly end-to-end
📌 How It Works
Upload one or more resumes (PDF format)
Paste the Job Description
The system:
Extracts text from resumes
Converts text to embeddings
Computes similarity scores
Ranks resumes
Displays matched and missing skills
📈 Future Improvements
Skill weighting
Resume score visualization (charts)
Support for DOCX resumes
Deployment on cloud (Streamlit Cloud / Hugging Face)
🤝 Contributing
Pull requests are welcome. For major changes, please open an issue first.

📄 License
This project is for educational and research purposes.
---
## 🚀 Live Demo

You can try the application here:

🔗 https://resume-project-mtet6vwn8uxvsvxjkampsm.streamlit.app/

### How it works
1. Upload one or more resume PDFs
2. Paste a Job Description
3. The app ranks resumes by match percentage
4. Shows matched and missing skills for each resume
