import os
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT


def create_pdf():
    file_name = "India_Rape_Cases_Data_2000_2026.pdf"
    doc = SimpleDocTemplate(
        file_name,
        pagesize=letter,
        topMargin=0.75 * inch,
        bottomMargin=0.75 * inch,
        leftMargin=0.75 * inch,
        rightMargin=0.75 * inch,
    )

    styles = getSampleStyleSheet()

    # Custom styles
    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Title"],
        fontSize=22,
        leading=26,
        textColor=HexColor("#1a237e"),
        spaceAfter=6,
        alignment=TA_CENTER,
    )
    subtitle_style = ParagraphStyle(
        "CustomSubtitle",
        parent=styles["Normal"],
        fontSize=11,
        leading=14,
        textColor=HexColor("#555555"),
        spaceAfter=20,
        alignment=TA_CENTER,
    )
    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=16,
        leading=20,
        textColor=HexColor("#283593"),
        spaceBefore=16,
        spaceAfter=10,
    )
    body_style = ParagraphStyle(
        "CustomBody",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        spaceAfter=6,
    )
    bullet_style = ParagraphStyle(
        "CustomBullet",
        parent=styles["Normal"],
        fontSize=10,
        leading=14,
        leftIndent=20,
        spaceAfter=4,
        bulletIndent=8,
    )
    sub_bullet_style = ParagraphStyle(
        "SubBullet",
        parent=styles["Normal"],
        fontSize=9,
        leading=13,
        leftIndent=40,
        spaceAfter=4,
        bulletIndent=28,
        textColor=HexColor("#333333"),
    )

    elements = []

    # ── Title Page ──
    elements.append(Spacer(1, 2 * inch))
    elements.append(Paragraph("Rape Cases in India: 2000–2026<br/>Context and Data", title_style))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(
        "Year-Wise Statistics, Political Context, and Judicial Release Information<br/>"
        "Source: NCRB Reports",
        subtitle_style,
    ))
    elements.append(PageBreak())

    # ── Context & Data Availability ──
    elements.append(Paragraph("Context & Data Availability", heading_style))
    context_bullets = [
        "Data Source: National Crime Records Bureau (NCRB) – 'Crime in India' reports.",
        "The numbers reflect <i>registered cases</i> under Section 376 IPC (and later POCSO).",
        "An increase in numbers post-2012 points to better reporting and broader legal definitions "
        "(following the Nirbhaya case), rather than purely an increase in crime rate.",
        "Data for 2024–2026: Official consolidated NCRB reports trail by 1–2 years, so exact figures "
        "for these years are pending compilation.",
    ]
    for b in context_bullets:
        elements.append(Paragraph(f"•  {b}", bullet_style))
    elements.append(Spacer(1, 12))

    # ── Year-wise Data Table ──
    data = [
        ("2000", "16,496", "NDA (BJP-led)", "Atal Bihari Vajpayee"),
        ("2001", "16,075", "NDA (BJP-led)", "Atal Bihari Vajpayee"),
        ("2002", "16,373", "NDA (BJP-led)", "Atal Bihari Vajpayee"),
        ("2003", "15,847", "NDA (BJP-led)", "Atal Bihari Vajpayee"),
        ("2004", "18,233", "NDA / UPA (INC-led)", "A.B. Vajpayee / Manmohan Singh"),
        ("2005", "18,359", "UPA (INC-led)", "Manmohan Singh"),
        ("2006", "19,348", "UPA (INC-led)", "Manmohan Singh"),
        ("2007", "20,737", "UPA (INC-led)", "Manmohan Singh"),
        ("2008", "21,467", "UPA (INC-led)", "Manmohan Singh"),
        ("2009", "21,397", "UPA (INC-led)", "Manmohan Singh"),
        ("2010", "22,172", "UPA (INC-led)", "Manmohan Singh"),
        ("2011", "24,206", "UPA (INC-led)", "Manmohan Singh"),
        ("2012", "24,923", "UPA (INC-led)", "Manmohan Singh"),
        ("2013", "33,707*", "UPA (INC-led)", "Manmohan Singh"),
        ("2014", "36,735", "UPA / NDA (BJP-led)", "Manmohan / Narendra Modi"),
        ("2015", "34,651", "NDA (BJP-led)", "Narendra Modi"),
        ("2016", "38,947", "NDA (BJP-led)", "Narendra Modi"),
        ("2017", "32,559", "NDA (BJP-led)", "Narendra Modi"),
        ("2018", "33,356", "NDA (BJP-led)", "Narendra Modi"),
        ("2019", "32,033", "NDA (BJP-led)", "Narendra Modi"),
        ("2020", "28,046", "NDA (BJP-led)", "Narendra Modi"),
        ("2021", "31,677", "NDA (BJP-led)", "Narendra Modi"),
        ("2022", "31,516", "NDA (BJP-led)", "Narendra Modi"),
        ("2023", "29,670", "NDA (BJP-led)", "Narendra Modi"),
        ("2024", "Pending", "NDA (BJP-led)", "Narendra Modi"),
        ("2025", "Pending", "NDA (BJP-led)", "Narendra Modi"),
        ("2026", "Pending", "NDA (BJP-led)", "Narendra Modi"),
    ]

    elements.append(Paragraph("NCRB Data: Year-Wise Registered Cases (2000–2026)", heading_style))
    elements.append(Paragraph(
        "<i>* 2013 spike attributed to the Criminal Law (Amendment) Act, 2013</i>",
        ParagraphStyle("footnote", parent=styles["Normal"], fontSize=8, textColor=HexColor("#888888"), spaceAfter=8),
    ))

    header = ["Year", "Cases Registered", "Ruling Party", "Prime Minister"]
    table_data = [header] + [list(row) for row in data]

    col_widths = [0.7 * inch, 1.3 * inch, 2.2 * inch, 2.8 * inch]
    table = Table(table_data, colWidths=col_widths, repeatRows=1)

    dark_blue = HexColor("#1a237e")
    light_blue = HexColor("#e8eaf6")
    table.setStyle(TableStyle([
        # Header
        ("BACKGROUND", (0, 0), (-1, 0), dark_blue),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 10),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 6),
        ("TOPPADDING", (0, 0), (-1, 0), 6),
        # Body
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("TOPPADDING", (0, 1), (-1, -1), 3),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 3),
        # Alternating rows
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), light_blue]),
        # Grid
        ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#cccccc")),
        ("ALIGN", (0, 0), (1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ]))

    elements.append(table)
    elements.append(PageBreak())

    # ── Release of Convicted Accused ──
    elements.append(Paragraph("Release of Convicted Accused: Overview", heading_style))
    overview_bullets = [
        "NCRB does not publish national aggregated statistics specifically on convicted rapists released.",
        "Overall Conviction Rate: Remains low (22%–28%). Acquittals form the majority "
        "due to hostile witnesses, lack of evidence, and delays.",
        "Prison administration is a 'State Subject'. Premature release decisions are made "
        "by State Sentence Review Boards (SSRBs).",
    ]
    for b in overview_bullets:
        elements.append(Paragraph(f"•  {b}", bullet_style))
    elements.append(Spacer(1, 16))

    # ── Reasons for Release ──
    elements.append(Paragraph("Reasons for Release", heading_style))

    reasons = [
        (
            "1. Remission of Sentence (Premature Release)",
            "Provided for 'good behavior', finishing 14 years jail term. "
            "Example: 11 Bilkis Bano convicts were originally released by Gujarat govt via its "
            "1992 policy (later struck down by the Supreme Court as illegal in 2024).",
        ),
        (
            "2. Parole / Furlough",
            "Temporary release for medical/family emergencies or societal ties. "
            "Example: High-profile cases like Gurmeet Ram Rahim receiving recurrent parole, "
            "which sometimes sparks political debate.",
        ),
        (
            "3. Completion of Standard Term",
            "For cases without life imprisonment, standard terms are finished routinely.",
        ),
    ]
    for heading, detail in reasons:
        elements.append(Paragraph(f"<b>{heading}</b>", bullet_style))
        elements.append(Paragraph(f"→  {detail}", sub_bullet_style))

    # Build the PDF
    doc.build(elements)
    print(f"PDF saved successfully as {file_name}")


if __name__ == "__main__":
    create_pdf()
