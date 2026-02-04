from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import blue
import re

def create_resume_pdf(resume_text, file_path):
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    styles = getSampleStyleSheet()

    link_style = ParagraphStyle(
        "LinkStyle",
        parent=styles["Normal"],
        textColor=blue
    )

    story = []

    story.append(Paragraph("<b>RESUME</b>", styles["Title"]))
    story.append(Spacer(1, 12))

    lines = resume_text.split("\n")

    for line in lines:
        line = line.strip()
        if not line:
            story.append(Spacer(1, 8))
            continue

        line = re.sub(
            r"(https?://\S+)",
            r'<a href="\1">\1</a>',
            line
        )
        line = re.sub(
            r"([\w\.-]+@[\w\.-]+)",
            r'<a href="mailto:\1">\1</a>',
            line
        )

        story.append(Paragraph(line, link_style))

    doc.build(story)
