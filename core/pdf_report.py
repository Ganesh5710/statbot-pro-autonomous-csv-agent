from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle
from reportlab.platypus import HRFlowable
import os


def generate_pdf_report(filename, kpis, insights, outlier_summary):

    doc = SimpleDocTemplate(filename)
    elements = []

    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    normal_style = styles["Normal"]

    # Title
    elements.append(Paragraph("StatBot Pro - Data Analytics Report", title_style))
    elements.append(Spacer(1, 0.3 * inch))

    # KPI Section
    elements.append(Paragraph("Key Performance Indicators", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    kpi_data = [[key, str(value)] for key, value in kpis.items()]
    table = Table(kpi_data, colWidths=[3 * inch, 2 * inch])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), colors.whitesmoke),
        ('GRID', (0, 0), (-1, -1), 1, colors.grey)
    ]))

    elements.append(table)
    elements.append(Spacer(1, 0.4 * inch))

    # Insights Section
    elements.append(Paragraph("Automatic Insights", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    insight_list = [ListItem(Paragraph(insight, normal_style)) for insight in insights]
    elements.append(ListFlowable(insight_list, bulletType='bullet'))
    elements.append(Spacer(1, 0.4 * inch))

    # Outlier Section
    elements.append(Paragraph("Outlier Summary", styles["Heading2"]))
    elements.append(Spacer(1, 0.2 * inch))

    elements.append(Paragraph(outlier_summary, normal_style))

    # Build PDF
    doc.build(elements)

    return filename