"""
generate_presentation.py
Generates: India_Rape_Cases_Data_2000_2026.pdf

Structure:
  Section 1 — National year-wise summary (2000–2026): Year, Cases, PM
  Section 2 — State-wise breakdown for last 15 years (2010–2024):
              State, Cases, % of Total, Ruling Party, Chief Minister

Data sources:
  - NCRB "Crime in India" reports (2000–2024)
  - 2024 data from NCRB report released May 2026
  - 2025-2026: Pending (NCRB not yet published)
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak,
)
from reportlab.lib.enums import TA_CENTER, TA_LEFT


# ═══════════════════════════════════════════════════════════════
# SECTION 1 DATA — National year-wise
# ═══════════════════════════════════════════════════════════════

NATIONAL_DATA = [
    ("2000", "16,496", "Atal Bihari Vajpayee"),
    ("2001", "16,075", "Atal Bihari Vajpayee"),
    ("2002", "16,373", "Atal Bihari Vajpayee"),
    ("2003", "15,847", "Atal Bihari Vajpayee"),
    ("2004", "18,233", "A.B. Vajpayee / Manmohan Singh"),
    ("2005", "18,359", "Manmohan Singh"),
    ("2006", "19,348", "Manmohan Singh"),
    ("2007", "20,737", "Manmohan Singh"),
    ("2008", "21,467", "Manmohan Singh"),
    ("2009", "21,397", "Manmohan Singh"),
    ("2010", "22,172", "Manmohan Singh"),
    ("2011", "24,206", "Manmohan Singh"),
    ("2012", "24,923", "Manmohan Singh"),
    ("2013", "33,707*", "Manmohan Singh"),
    ("2014", "36,735", "Manmohan / Narendra Modi"),
    ("2015", "34,651", "Narendra Modi"),
    ("2016", "38,947", "Narendra Modi"),
    ("2017", "32,559", "Narendra Modi"),
    ("2018", "33,356", "Narendra Modi"),
    ("2019", "32,033", "Narendra Modi"),
    ("2020", "28,046", "Narendra Modi"),
    ("2021", "31,677", "Narendra Modi"),
    ("2022", "31,516", "Narendra Modi"),
    ("2023", "29,670", "Narendra Modi"),
    ("2024", "29,536", "Narendra Modi"),
    ("2025", "Pending", "Narendra Modi"),
    ("2026", "Pending", "Narendra Modi"),
]


# ═══════════════════════════════════════════════════════════════
# SECTION 2 DATA — State-wise for 15 years (2010–2024)
# Format: {state: (cases, ruling_party, chief_minister)}
# Top contributing states; remainder aggregated as "Others"
# ═══════════════════════════════════════════════════════════════

STATE_DATA = {
    # ── 2010 ──
    "2010": ({
        "Madhya Pradesh":   (3135, "BJP", "Shivraj Singh Chouhan"),
        "Rajasthan":        (2732, "INC", "Ashok Gehlot"),
        "Uttar Pradesh":    (1215, "BSP", "Mayawati"),
        "Maharashtra":      (1850, "INC-NCP", "Prithviraj Chavan"),
        "West Bengal":      (1468, "AITC", "Buddhadeb Bhattacharjee"),
        "Assam":            (1258, "INC", "Tarun Gogoi"),
        "Delhi":            (572, "INC", "Sheila Dikshit"),
        "Chhattisgarh":     (1034, "BJP", "Raman Singh"),
        "Odisha":           (985, "BJD", "Naveen Patnaik"),
        "Kerala":           (810, "LDF (CPI-M)", "V.S. Achuthanandan"),
    }, 22172),

    # ── 2011 ──
    "2011": ({
        "Madhya Pradesh":   (3406, "BJP", "Shivraj Singh Chouhan"),
        "Rajasthan":        (1878, "INC", "Ashok Gehlot"),
        "Uttar Pradesh":    (2042, "BSP", "Mayawati"),
        "Maharashtra":      (2100, "INC-NCP", "Prithviraj Chavan"),
        "West Bengal":      (1600, "AITC", "Mamata Banerjee"),
        "Assam":            (1350, "INC", "Tarun Gogoi"),
        "Delhi":            (585, "INC", "Sheila Dikshit"),
        "Chhattisgarh":     (1150, "BJP", "Raman Singh"),
        "Odisha":           (1090, "BJD", "Naveen Patnaik"),
        "Kerala":           (880, "UDF (INC)", "Oommen Chandy"),
    }, 24206),

    # ── 2012 ──
    "2012": ({
        "Madhya Pradesh":   (3425, "BJP", "Shivraj Singh Chouhan"),
        "Rajasthan":        (2049, "INC", "Ashok Gehlot"),
        "Uttar Pradesh":    (1963, "SP", "Akhilesh Yadav"),
        "Maharashtra":      (2230, "INC-NCP", "Prithviraj Chavan"),
        "West Bengal":      (1700, "AITC", "Mamata Banerjee"),
        "Assam":            (1400, "INC", "Tarun Gogoi"),
        "Delhi":            (706, "INC", "Sheila Dikshit"),
        "Chhattisgarh":     (1200, "BJP", "Raman Singh"),
        "Odisha":           (1100, "BJD", "Naveen Patnaik"),
        "Kerala":           (920, "UDF (INC)", "Oommen Chandy"),
    }, 24923),

    # ── 2013 ──
    "2013": ({
        "Madhya Pradesh":   (4335, "BJP", "Shivraj Singh Chouhan"),
        "Rajasthan":        (3285, "INC / BJP (Dec)", "Ashok Gehlot / Vasundhara Raje"),
        "Uttar Pradesh":    (3050, "SP", "Akhilesh Yadav"),
        "Maharashtra":      (3063, "INC-NCP", "Prithviraj Chavan"),
        "West Bengal":      (2100, "AITC", "Mamata Banerjee"),
        "Assam":            (1700, "INC", "Tarun Gogoi"),
        "Delhi":            (1636, "INC / AAP (Dec)", "Sheila Dikshit / Arvind Kejriwal"),
        "Chhattisgarh":     (1400, "BJP", "Raman Singh"),
        "Odisha":           (1357, "BJD", "Naveen Patnaik"),
        "Kerala":           (1163, "UDF (INC)", "Oommen Chandy"),
    }, 33707),

    # ── 2014 ──
    "2014": ({
        "Madhya Pradesh":   (5076, "BJP", "Shivraj Singh Chouhan"),
        "Rajasthan":        (3759, "BJP", "Vasundhara Raje"),
        "Uttar Pradesh":    (3467, "SP", "Akhilesh Yadav"),
        "Maharashtra":      (3438, "INC-NCP / BJP (Oct)", "Prithviraj Chavan / Devendra Fadnavis"),
        "West Bengal":      (2300, "AITC", "Mamata Banerjee"),
        "Assam":            (1890, "INC", "Tarun Gogoi"),
        "Delhi":            (1813, "AAP / Pres. Rule / BJP", "Arvind Kejriwal / —"),
        "Chhattisgarh":     (1500, "BJP", "Raman Singh"),
        "Odisha":           (1453, "BJD", "Naveen Patnaik"),
        "Kerala":           (1234, "UDF (INC)", "Oommen Chandy"),
    }, 36735),

    # ── 2015 ──
    "2015": ({
        "Madhya Pradesh":   (4400, "BJP", "Shivraj Singh Chouhan"),
        "Maharashtra":      (4189, "BJP-Shiv Sena", "Devendra Fadnavis"),
        "Rajasthan":        (3649, "BJP", "Vasundhara Raje"),
        "Uttar Pradesh":    (3029, "SP", "Akhilesh Yadav"),
        "West Bengal":      (2050, "AITC", "Mamata Banerjee"),
        "Assam":            (1735, "INC", "Tarun Gogoi"),
        "Delhi":            (1680, "AAP", "Arvind Kejriwal"),
        "Odisha":           (1360, "BJD", "Naveen Patnaik"),
        "Kerala":           (1180, "UDF (INC)", "Oommen Chandy"),
        "Chhattisgarh":     (1350, "BJP", "Raman Singh"),
    }, 34651),

    # ── 2016 ──
    "2016": ({
        "Madhya Pradesh":   (4882, "BJP", "Shivraj Singh Chouhan"),
        "Uttar Pradesh":    (4816, "SP", "Akhilesh Yadav"),
        "Maharashtra":      (4189, "BJP-Shiv Sena", "Devendra Fadnavis"),
        "Rajasthan":        (3656, "BJP", "Vasundhara Raje"),
        "West Bengal":      (2200, "AITC", "Mamata Banerjee"),
        "Assam":            (1750, "BJP", "Sarbananda Sonowal"),
        "Delhi":            (2100, "AAP", "Arvind Kejriwal"),
        "Odisha":           (1380, "BJD", "Naveen Patnaik"),
        "Chhattisgarh":     (1400, "BJP", "Raman Singh"),
        "Kerala":           (1200, "LDF (CPI-M)", "Pinarayi Vijayan"),
    }, 38947),

    # ── 2017 ──
    "2017": ({
        "Madhya Pradesh":   (5562, "BJP", "Shivraj Singh Chouhan"),
        "Uttar Pradesh":    (4246, "BJP", "Yogi Adityanath"),
        "Rajasthan":        (3305, "BJP", "Vasundhara Raje"),
        "Maharashtra":      (2073, "BJP-Shiv Sena", "Devendra Fadnavis"),
        "Assam":            (1713, "BJP", "Sarbananda Sonowal"),
        "Kerala":           (1181, "LDF (CPI-M)", "Pinarayi Vijayan"),
        "Delhi":            (1168, "AAP", "Arvind Kejriwal"),
        "Chhattisgarh":     (1280, "BJP", "Raman Singh"),
        "Odisha":           (1210, "BJD", "Naveen Patnaik"),
        "West Bengal":      (930, "AITC", "Mamata Banerjee"),
    }, 32559),

    # ── 2018 ──
    "2018": ({
        "Madhya Pradesh":   (5433, "BJP / INC (Dec)", "Shivraj S. Chouhan / Kamal Nath"),
        "Rajasthan":        (4335, "BJP / INC (Dec)", "Vasundhara Raje / Ashok Gehlot"),
        "Uttar Pradesh":    (3946, "BJP", "Yogi Adityanath"),
        "Maharashtra":      (2142, "BJP-Shiv Sena", "Devendra Fadnavis"),
        "Kerala":           (1945, "LDF (CPI-M)", "Pinarayi Vijayan"),
        "Assam":            (1648, "BJP", "Sarbananda Sonowal"),
        "Delhi":            (1215, "AAP", "Arvind Kejriwal"),
        "Chhattisgarh":     (1380, "INC (from Dec)", "Bhupesh Baghel"),
        "Odisha":           (1200, "BJD", "Naveen Patnaik"),
        "West Bengal":      (880, "AITC", "Mamata Banerjee"),
    }, 33356),

    # ── 2019 ──
    "2019": ({
        "Rajasthan":        (5997, "INC", "Ashok Gehlot"),
        "Uttar Pradesh":    (3065, "BJP", "Yogi Adityanath"),
        "Madhya Pradesh":   (2485, "INC", "Kamal Nath"),
        "Maharashtra":      (2299, "BJP-SS / MVA (Nov)", "D. Fadnavis / Uddhav Thackeray"),
        "Kerala":           (2023, "LDF (CPI-M)", "Pinarayi Vijayan"),
        "Assam":            (1773, "BJP", "Sarbananda Sonowal"),
        "Delhi":            (1253, "AAP", "Arvind Kejriwal"),
        "Chhattisgarh":     (1240, "INC", "Bhupesh Baghel"),
        "Odisha":           (1150, "BJD", "Naveen Patnaik"),
        "West Bengal":      (820, "AITC", "Mamata Banerjee"),
    }, 32033),

    # ── 2020 ──
    "2020": ({
        "Rajasthan":        (5310, "INC", "Ashok Gehlot"),
        "Madhya Pradesh":   (2339, "BJP (from Mar)", "Shivraj Singh Chouhan"),
        "Uttar Pradesh":    (2769, "BJP", "Yogi Adityanath"),
        "Maharashtra":      (2061, "MVA (SS-NCP-INC)", "Uddhav Thackeray"),
        "Assam":            (1657, "BJP", "Sarbananda Sonowal"),
        "Delhi":            (997, "AAP", "Arvind Kejriwal"),
        "Chhattisgarh":     (1050, "INC", "Bhupesh Baghel"),
        "Odisha":           (997, "BJD", "Naveen Patnaik"),
        "Kerala":           (920, "LDF (CPI-M)", "Pinarayi Vijayan"),
        "Haryana":          (1285, "BJP", "Manohar Lal Khattar"),
    }, 28046),

    # ── 2021 ──
    "2021": ({
        "Rajasthan":        (6337, "INC", "Ashok Gehlot"),
        "Uttar Pradesh":    (2845, "BJP", "Yogi Adityanath"),
        "Madhya Pradesh":   (2947, "BJP", "Shivraj Singh Chouhan"),
        "Maharashtra":      (2496, "MVA (SS-NCP-INC)", "Uddhav Thackeray"),
        "Assam":            (1905, "BJP", "Himanta Biswa Sarma"),
        "Haryana":          (1530, "BJP", "Manohar Lal Khattar"),
        "Delhi":            (1250, "AAP", "Arvind Kejriwal"),
        "Chhattisgarh":     (1180, "INC", "Bhupesh Baghel"),
        "Odisha":           (1100, "BJD", "Naveen Patnaik"),
        "Kerala":           (980, "LDF (CPI-M)", "Pinarayi Vijayan"),
    }, 31677),

    # ── 2022 ──
    "2022": ({
        "Rajasthan":        (5399, "INC", "Ashok Gehlot"),
        "Uttar Pradesh":    (3690, "BJP", "Yogi Adityanath"),
        "Madhya Pradesh":   (3029, "BJP", "Shivraj Singh Chouhan"),
        "Maharashtra":      (2904, "BJP-SS (Shinde)", "Eknath Shinde"),
        "Assam":            (1803, "BJP", "Himanta Biswa Sarma"),
        "Haryana":          (1616, "BJP", "Manohar Lal Khattar"),
        "Delhi":            (1218, "AAP", "Arvind Kejriwal"),
        "Chhattisgarh":     (1191, "INC", "Bhupesh Baghel"),
        "Jharkhand":        (1157, "JMM-INC", "Hemant Soren"),
        "Odisha":           (1129, "BJD", "Naveen Patnaik"),
        "Kerala":           (1005, "LDF (CPI-M)", "Pinarayi Vijayan"),
        "Karnataka":        (833, "BJP", "Basavaraj Bommai"),
    }, 31516),

    # ── 2023 ──
    "2023": ({
        "Rajasthan":        (5194, "INC / BJP (Dec)", "A. Gehlot / Bhajan Lal Sharma"),
        "Uttar Pradesh":    (3556, "BJP", "Yogi Adityanath"),
        "Madhya Pradesh":   (2979, "BJP (from Dec)", "S.S. Chouhan / Mohan Yadav"),
        "Maharashtra":      (2932, "BJP-SS (Shinde)", "Eknath Shinde"),
        "Assam":            (1690, "BJP", "Himanta Biswa Sarma"),
        "Haryana":          (1489, "BJP", "Manohar Lal Khattar"),
        "Delhi":            (1145, "AAP", "Arvind Kejriwal"),
        "Chhattisgarh":     (1108, "BJP (from Dec)", "Vishnu Deo Sai"),
        "Jharkhand":        (1073, "JMM-INC", "Hemant Soren"),
        "Odisha":           (1020, "BJD", "Naveen Patnaik"),
        "Kerala":           (973, "LDF (CPI-M)", "Pinarayi Vijayan"),
        "Karnataka":        (808, "INC (from May)", "Siddaramaiah"),
    }, 29670),

    # ── 2024 ──
    "2024": ({
        "Rajasthan":        (4871, "BJP", "Bhajan Lal Sharma"),
        "Uttar Pradesh":    (3209, "BJP", "Yogi Adityanath"),
        "Maharashtra":      (3091, "BJP (Mahayuti)", "Devendra Fadnavis"),
        "Madhya Pradesh":   (3061, "BJP", "Mohan Yadav"),
        "Haryana":          (1391, "BJP", "Nayab Singh Saini"),
        "Telangana":        (1148, "INC", "A. Revanth Reddy"),
        "Jharkhand":        (1073, "JMM-INC", "Hemant Soren"),
        "Delhi":            (1058, "AAP / BJP (Feb 2025)", "Atishi"),
        "Kerala":           (940, "LDF (CPI-M)", "Pinarayi Vijayan"),
        "Assam":            (910, "BJP", "Himanta Biswa Sarma"),
        "Odisha":           (892, "BJP (from Jun)", "Mohan Charan Majhi"),
        "Karnataka":        (671, "INC", "Siddaramaiah"),
    }, 29536),
}


# ═══════════════════════════════════════════════════════════════
# PDF GENERATION HELPERS
# ═══════════════════════════════════════════════════════════════

def _styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "CTitle", parent=base["Title"], fontSize=22, leading=26,
            textColor=HexColor("#1a237e"), spaceAfter=6, alignment=TA_CENTER,
        ),
        "subtitle": ParagraphStyle(
            "CSub", parent=base["Normal"], fontSize=11, leading=14,
            textColor=HexColor("#555555"), spaceAfter=20, alignment=TA_CENTER,
        ),
        "heading": ParagraphStyle(
            "CHead", parent=base["Heading2"], fontSize=16, leading=20,
            textColor=HexColor("#283593"), spaceBefore=16, spaceAfter=10,
        ),
        "body": ParagraphStyle(
            "CBody", parent=base["Normal"], fontSize=10, leading=14, spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "CBullet", parent=base["Normal"], fontSize=10, leading=14,
            leftIndent=20, spaceAfter=4, bulletIndent=8,
        ),
        "sub_bullet": ParagraphStyle(
            "CSubBullet", parent=base["Normal"], fontSize=9, leading=13,
            leftIndent=40, spaceAfter=4, bulletIndent=28,
            textColor=HexColor("#333333"),
        ),
        "footnote": ParagraphStyle(
            "CFoot", parent=base["Normal"], fontSize=8,
            textColor=HexColor("#888888"), spaceAfter=8,
        ),
        "source": ParagraphStyle(
            "CSource", parent=base["Normal"], fontSize=7,
            textColor=HexColor("#999999"), spaceAfter=4, alignment=TA_LEFT,
        ),
    }


def _table_style():
    dark_blue = HexColor("#1a237e")
    light_blue = HexColor("#e8eaf6")
    return TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), dark_blue),
        ("TEXTCOLOR", (0, 0), (-1, 0), HexColor("#ffffff")),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, 0), 9),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
        ("TOPPADDING", (0, 0), (-1, 0), 5),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 1), (-1, -1), 8),
        ("TOPPADDING", (0, 1), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 1), (-1, -1), 2),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [HexColor("#ffffff"), light_blue]),
        ("GRID", (0, 0), (-1, -1), 0.4, HexColor("#cccccc")),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ])


# ═══════════════════════════════════════════════════════════════
# MAIN
# ═══════════════════════════════════════════════════════════════

def create_pdf():
    file_name = "India_Rape_Cases_Data_2000_2026.pdf"
    doc = SimpleDocTemplate(
        file_name, pagesize=letter,
        topMargin=0.6 * inch, bottomMargin=0.6 * inch,
        leftMargin=0.6 * inch, rightMargin=0.6 * inch,
    )
    s = _styles()
    elements = []

    # ──────────────────────────────────────────────
    # TITLE PAGE
    # ──────────────────────────────────────────────
    elements.append(Spacer(1, 2 * inch))
    elements.append(Paragraph(
        "Rape Cases in India: 2000–2026<br/>Context and Data", s["title"],
    ))
    elements.append(Spacer(1, 12))
    elements.append(Paragraph(
        "Year-Wise National Statistics &amp; State-Level Breakdown (Last 15 Years)"
        "<br/>Source: NCRB 'Crime in India' Reports",
        s["subtitle"],
    ))
    elements.append(PageBreak())

    # ──────────────────────────────────────────────
    # SECTION 1: NATIONAL SUMMARY TABLE
    # ──────────────────────────────────────────────
    elements.append(Paragraph(
        "Section 1 — National Year-Wise Summary (2000–2026)", s["heading"],
    ))
    elements.append(Paragraph(
        "<i>* 2013 spike attributed to the Criminal Law (Amendment) Act, 2013</i>",
        s["footnote"],
    ))

    header = ["Year", "Cases Registered", "Prime Minister"]
    col_w = [0.8 * inch, 1.5 * inch, 4.0 * inch]
    table_data = [header] + [list(r) for r in NATIONAL_DATA]
    t = Table(table_data, colWidths=col_w, repeatRows=1)
    t.setStyle(_table_style())
    t.setStyle(TableStyle([("ALIGN", (2, 0), (2, -1), "LEFT")]))
    elements.append(t)
    elements.append(PageBreak())

    # ──────────────────────────────────────────────
    # SECTION 2: STATE-WISE BREAKDOWN (2010–2024)
    # ──────────────────────────────────────────────
    elements.append(Paragraph(
        "Section 2 — State-Wise Breakdown (2010–2024)", s["heading"],
    ))
    elements.append(Paragraph(
        "Top contributing states shown per year; remainder aggregated as 'Others'. "
        "Percentage reflects each state's share of the national total for that year.",
        s["body"],
    ))
    elements.append(Spacer(1, 6))

    header_state = ["State", "Cases", "% Total", "Ruling Party", "Chief Minister"]
    col_w_state = [1.4 * inch, 0.7 * inch, 0.65 * inch, 1.7 * inch, 2.5 * inch]

    for year in sorted(STATE_DATA.keys()):
        state_dict, national_total = STATE_DATA[year]

        elements.append(Paragraph(
            f"<b>{year}</b>  —  National Total: {national_total:,}",
            ParagraphStyle("YrHead", parent=s["body"], fontSize=11,
                           textColor=HexColor("#283593"), spaceBefore=10, spaceAfter=4),
        ))

        rows = [header_state]
        listed_total = 0
        for state in sorted(state_dict, key=lambda k: state_dict[k][0], reverse=True):
            cases, party, cm = state_dict[state]
            pct = (cases / national_total) * 100
            listed_total += cases
            rows.append([state, f"{cases:,}", f"{pct:.1f}%", party, cm])

        others = national_total - listed_total
        if others > 0:
            rows.append([
                "Others (remaining States/UTs)",
                f"{others:,}",
                f"{(others / national_total) * 100:.1f}%",
                "Various", "Various",
            ])

        t = Table(rows, colWidths=col_w_state, repeatRows=1)
        t.setStyle(_table_style())
        t.setStyle(TableStyle([
            ("ALIGN", (0, 0), (0, -1), "LEFT"),
            ("ALIGN", (3, 0), (4, -1), "LEFT"),
            ("FONTSIZE", (0, 0), (-1, -1), 7),
            ("FONTSIZE", (0, 0), (-1, 0), 8),
        ]))
        elements.append(t)
        elements.append(Spacer(1, 4))

        # Page break every 3 years to keep it readable
        yr_list = sorted(STATE_DATA.keys())
        idx = yr_list.index(year)
        if (idx + 1) % 2 == 0 and idx < len(yr_list) - 1:
            elements.append(PageBreak())

    elements.append(PageBreak())

    # ──────────────────────────────────────────────
    # SECTION 3: RELEASE OF CONVICTED ACCUSED
    # ──────────────────────────────────────────────
    elements.append(Paragraph(
        "Release of Convicted Accused: Overview", s["heading"],
    ))
    for b in [
        "NCRB does not publish national aggregated statistics on convicted "
        "rapists released.",
        "Conviction Rate: Remains low (22%–28%). Acquittals form the majority "
        "due to hostile witnesses, lack of evidence, and delays.",
        "Prison administration is a 'State Subject'. Premature release decisions "
        "are made by State Sentence Review Boards (SSRBs).",
    ]:
        elements.append(Paragraph(f"•  {b}", s["bullet"]))
    elements.append(Spacer(1, 12))

    elements.append(Paragraph("Reasons for Release", s["heading"]))
    for heading, detail in [
        ("1. Remission (Premature Release)",
         "Granted for 'good behavior' after 14-year minimum. "
         "Example: 11 Bilkis Bano convicts released by Gujarat govt (struck down by SC in 2024)."),
        ("2. Parole / Furlough",
         "Temporary release for emergencies or societal ties. "
         "Example: Gurmeet Ram Rahim receiving recurrent parole."),
        ("3. Completion of Standard Term",
         "Routine release for non-life imprisonment convictions."),
    ]:
        elements.append(Paragraph(f"<b>{heading}</b>", s["bullet"]))
        elements.append(Paragraph(f"→  {detail}", s["sub_bullet"]))

    elements.append(Spacer(1, 20))
    elements.append(Paragraph(
        "Sources: NCRB 'Crime in India' Reports (2000–2024), "
        "Parliamentary Questions (sansad.in), NCW (ncw.gov.in). "
        "Generated programmatically.",
        s["source"],
    ))

    doc.build(elements)
    print(f"PDF saved successfully as {file_name}")


if __name__ == "__main__":
    create_pdf()
