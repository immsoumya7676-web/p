from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime

styles = getSampleStyleSheet()

def generate_report(data, filename="Inspection_Report.pdf"):

    doc = SimpleDocTemplate(filename)

    story = []

    story.append(
        Paragraph("<b>PackSecure AI Inspection Report</b>", styles['Title'])
    )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(f"Date : {datetime.now()}", styles['BodyText'])
    )

    story.append(Spacer(1,20))

    for key,value in data.items():

        story.append(
            Paragraph(f"<b>{key}</b> : {value}", styles['BodyText'])
        )

    story.append(Spacer(1,20))

    story.append(
        Paragraph(
        "<b>Conclusion :</b> AI detected possible packaging anomalies. Manual inspection recommended.",
        styles['BodyText']
        )
    )

    doc.build(story)

    return filename
