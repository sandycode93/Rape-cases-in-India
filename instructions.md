# Output Generation: Context & Rules

This document outlines the context, rules, and constraints used to programmatically generate (`India_Rape_Cases_Data_2000_2026.pdf`) containing statistics on Indian rape cases (2000–2026) and the context behind the release of convicted individuals.

## 1. Core Rules
1. **Separation of Concerns:** The actual raw data and statistics must **not** be stored in this Markdown file.
2. **Programmatic Generation:** The data must be embedded and run through an isolated Python script (`generate_presentation.py`) leveraging the `reportlab` library.
3. **Format Requirement:** The final output must be delivered neatly as a PDF document.
4. **Data Aggregation:** The script must map out three distinct metrics for each year: Registered Cases, Ruling Political Party, and the acting Prime Minister.
5. **Sub_agent:** Find out the alternative sources for the data for the years 2024-2026. If needed create a sub-agent to find out the data for the years 2024-2026.

## 2. Document Structure
The PDF is structured into two main sections:

### Section 1 — National Year-Wise Summary (2000–2026)
- One table with columns: **Year**, **Cases Registered**, **Prime Minister**
- Covers all 27 years (2000–2026) in a single view
- 2025–2026 marked as "Pending"

### Section 2 — State-Wise Breakdown (Last 15 Years: 2010–2024)
- One table per year showing top contributing states
- Columns: **State**, **Cases**, **% of Total**, **Ruling Party**, **Chief Minister**
- **Tamil Nadu** must be included in every year's state-wise table alongside the existing states
- Remaining states/UTs aggregated as "Others"
- Percentage reflects each state's share of the national total for that year

## 3. Context & Data Collection Nuances
When producing the dataset for the document, the following context and limitations were strictly adhered to:

### A. NCRB Case Statistics
- **Data Source:** The primary source for the quantitative data is the National Crime Records Bureau (NCRB) via its annual "Crime in India" reports.
- **Reporting vs. Incidence:** The numbers reflect *registered cases* under Section 376 IPC (and POCSO where applicable), not the absolute incidence of crime. For instance, the significant statistical surge post-2012 is attributed to the Criminal Law (Amendment) Act, 2013, which broadened definitions and mandated stricter police reporting protocols after the Nirbhaya case.
- **Pending Data (2025–2026):** Because NCRB data consolidation typically trails by 1 to 2 years, final official figures for 2025 onwards do not yet exist. 2024 data sourced from NCRB "Crime in India 2024" released May 2026.
- **Classification method:** The data is classified for each state with the ruling political party and Chief Minister name.

### B. Political Context Mapping
- **Federal:** Criminal statistics and laws (like the IPC/BNSS) are federally tracked, so the national table maps to the Prime Minister at the centre.
- **State:** Criminal cases are broken down for each state along with the count. The percentage for each state from the total cases is produced for each year.

### C. Release of Convicted Accused
- **Lack of National Aggregates:** The NCRB does not publish national-level statistics specifically tracking the number of convicted rape accused released via parole, furlough, or remission. 
- **State Jurisdiction:** Prison administration is a "State Subject". Releases are determined by State Governments and State Sentence Review Boards (SSRBs). 
- **Reasons for Release Highlighted:** Because quantitative data is unavailable, the output explains the structural reasons behind releases:
    1. **Remission (Premature Release):** Granted for "good behavior" (e.g., executing the 14-year minimum). Highlighted by the controversial 2022 release of 11 convicts in the Bilkis Bano case by the Gujarat Government (later dynamically struck down by the Supreme Court in 2024).
    2. **Parole / Furlough:** Temporary releases for emergencies or to maintain societal ties (e.g., cases like Gurmeet Ram Rahim receiving parole).
    3. **Term Completion:** Routine release for non-life convictions.
