# Output Generation: Context & Rules

This document outlines the context, rules, and constraints used to programmatically generate the presentation (`India_Rape_Cases_Data_2000_2026.pptx`) containing statistics on Indian rape cases (2000–2026) and the context behind the release of convicted individuals.

## 1. Core Rules
1. **Separation of Concerns:** The actual raw data and statistics must **not** be stored in this Markdown file.
2. **Programmatic Generation:** The data must be embedded and run through an isolated Python script (`generate_presentation.py`) leveraging the `python-pptx` library.
3. **Format Requirement:** The final output must be delivered neatly as a Presentation (PPTX). 
4. **Data Aggregation:** The script must map out three distinct metrics for each year: Registered Cases, Ruling Political Party, and the acting Prime Minister.

## 2. Context & Data Collection Nuances
When producing the dataset for the presentation, the following context and limitations were strictly adhered to:

### A. NCRB Case Statistics
- **Data Source:** The primary source for the quantitative data is the National Crime Records Bureau (NCRB) via its annual "Crime in India" reports.
- **Reporting vs. Incidence:** The numbers reflect *registered cases* under Section 376 IPC (and POCSO where applicable), not the absolute incidence of crime. For instance, the significant statistical surge post-2012 is attributed to the Criminal Law (Amendment) Act, 2013, which broadened definitions and mandated stricter police reporting protocols after the Nirbhaya case.
- **Pending Data (2024–2026):** Because NCRB data consolidation typically trails by 1 to 2 years, final official figures for 2024 onwards do not yet exist in an aggregated, finalized format. These years must be explicitly marked as "Pending".

### B. Political Context Mapping
- **Federal vs. State:** Criminal statistics and laws (like the IPC/BNSS) are federally tracked, so the mapping ties the year to the ruling national coalition (NDA vs. UPA) and the respective Prime Minister at the center, rather than individual state ministries.

### C. Release of Convicted Accused
- **Lack of National Aggregates:** The NCRB does not publish national-level statistics specifically tracking the number of convicted rape accused released via parole, furlough, or remission. 
- **State Jurisdiction:** Prison administration is a "State Subject". Releases are determined by State Governments and State Sentence Review Boards (SSRBs). 
- **Reasons for Release Highlighted:** Because quantitative data is unavailable, the output explains the structural reasons behind releases:
    1. **Remission (Premature Release):** Granted for "good behavior" (e.g., executing the 14-year minimum). Highlighted by the controversial 2022 release of 11 convicts in the Bilkis Bano case by the Gujarat Government (later dynamically struck down by the Supreme Court in 2024).
    2. **Parole / Furlough:** Temporary releases for emergencies or to maintain societal ties (e.g., cases like Gurmeet Ram Rahim receiving parole).
    3. **Term Completion:** Routine release for non-life convictions.
