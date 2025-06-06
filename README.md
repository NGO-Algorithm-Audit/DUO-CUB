# Bias analysis indirect discrimination in control process Dutch Executive Agency for Education

This bias analysis is part of a quantitative and qualitative audit of the Dutch's Executive Agency for Education (DUO) control process to check whether students were (un)duly allocated college grants, known as the CUB process. This data study provides quantitative support for indirect discrimination in this process.

#### Timeline
🗞️ News article [21-06-2023]: Journalists claim that more than 95% of the students appealing against a decision of DUO have a migration background.

🕵🏻‍♀️ Independent research [07-07-2023]: The Dutch Minister of Education has announced two independent external investigations: one conducted by PwC on behalf of the Minister and another by Algorithm Audit on behalf of DUO.

📄 1st audit report [01-03-2024]: Algorithm Audit's audit report [*Preventing prejudice*](https://algorithmaudit.eu/nl/algoprudence/cases/aa202401_preventing-prejudice/) and PwC's audit report [*Misusage college grant*](https://www.tweedekamer.nl/kamerstukken/detail?id=2024D07564&did=2024D07564) are sent to the Dutch Parliament.

ℹ️ Data [06-05-2024]: Aggregation statistics of the migration background of 300.000+ students in the period 2014-2022 are shared by [Statistics Netherlands](https://www.cbs.nl/nl-nl/maatwerk/2024/21/ontvangers-uitwonendenbeurs-herkomst-2014-2017-2019-2021-en-2022) with DUO and Algorithm Audit.

📄 2nd audit report [22-05-2024]: Algorithm Audit's audit report [*Addendum Preventing prejudice*](https://algorithmaudit.eu/algoprudence/cases/aa202402_preventing-prejudice_addendum/) is sent to the Dutch Parliament.

📣 Political reaction [22-05-2024]: [Apologies](https://www.rijksoverheid.nl/actueel/nieuws/2024/03/01/kabinet-maakt-excuses-voor-indirecte-discriminatie-bij-controles-op-de-uitwonendenbeurs) of Dutch Minister for Education for indirect discrimination in the CUB process to disadvantaged students.

⚖️ Court ruling [29-10-2024]: Dutch court [ruled](https://uitspraken.rechtspraak.nl/details?id=ECLI:NL:RBOVE:2024:5627) that evidence obtained through a control process that indirectly discriminates is invalid (ECLI:NL:RBOVE:2024:5627).

€ Compensation [11-11-2024]: Dutch Minister for Education [announces](https://www.rijksoverheid.nl/actueel/nieuws/2024/11/11/gecontroleerde-oud-studenten-met-uitwonendenbeurs-krijgen-geld-terug) €61M compensation for 10,000+ disadvantaged students.

🧪 Scientific article [05-05-2025]: Pre-print [scientific article](https://arxiv.org/pdf/2502.01713) 'Auditing a Dutch public sector risk profiling algorithm using an unsupervised bias detection tool'.

![image](./Images/Overview_CUB_process.png)

## Key findings
-   **Finding 1:** The CUB process as a whole (Step 1-5) has been biased against students with a non-European migration background.
-   **Finding 2:** The risk profile used in Step 1 of the CUB process was biased against students with a non-European migration background. This bias was caused by assigning higher risk scores to students with following vocational training (mbo-students) and to students living closer to their parent(s), indirectly assigning a higher risk score to students with a non-European migration background due to overrepresentation in these groups.
-   **Finding 3:** Manual selection of students for control (Step 3) reinforced bias in the CUB process.
-   **Finding 4:** Due to bias in the CUB process against students with a non-European migration background, more unduly granted loans have been observed for this group. This is primarily caused by the overinspection of this demography.
-   **Finding 5:** A significant part of the students appealing a decision of unduly allocated grants have a non-European migration background. No bias has been identified in the appeal procedure itself (Step 6).

![image](./Images/Bias_CUB-2014_new.png)

## Project description
Education Executive Agency of The Netherlands (DUO) performs checks to ensure that disbursed college grants are duly granted. This process is known as the College Grant Check (in Dutch: CUB). Suspicion has emerged that the CUB process may be biased against students with a migration background. This suspicion is based on the appeal procedures initiated by students who were found to have received grants unduly. Due to the General Data Protection Regulation (GDPR), DUO does not collect information on the origin of students during the CUB-process. The Dutch national office of statistics (Netherlands Statistics) has therefore been asked to provide aggregated statistics on the country of birth and country of origin of 300.000+ students in the period 2014-2022. A supervised bias analysis of these data are shared in this repository. DUO has provided CBS with data on eight different populations, including background information (citzen service number, education, age, distance to parent(s)) and process characteristics (risk category, selected for control, outcome control, appeal procedure, outcome appeal).

## Definition bias
Bias is defined as significant deviations in the demographic distribution compared to the start population (the population of all recipients of college grants), resulting from disproportionate selection of certain students during the CUB process. If there is a substantial overrepresentation of students with a migration background in various steps of the CUB process, it indicates that the CUB process (and/or its various steps) is biased against this demographic. Here, bias does not imply conscious bias, i.e., premeditated and deliberate selection of a particular demographic by DUO or individual civil servants. In this study, bias refers to measured disparities in the data as an (unintentional) effect of the CUB process steps. There is no bias if the demographic proportions remain almost unchanged throughout the CUB process.

## Definition migration background
Date provided by the Dutch national office of statistics (Statistics Netherlands):
-   country of birth (exact defintion can be found in [DUO_CUB_Netherlands_Statistics.xlsx](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/DUO_CUB_Netherlands_Statistics.xlsx))
-   country of origin (exact defintion can be found in [DUO_CUB_Netherlands_Statistics.xlsx](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/DUO_CUB_Netherlands_Statistics.xlsx))

Overview of used terminology:

![image](./Images/Migration_tree_EN.png)

![image](./Images/Migration_overview_EN.png)

### Methods used
-   Supervised bias analysis
    - Demographic parity plots for aggregation statistics provided by Netherlands Statistics 

## Repo Overview
    .
    ├── DUO_CUB_Netherlands_Statistics.xlsx                  # Dataset provided by Netherlands Statistics (translated to EN)
    ├── .gitignore                                           # Files to be ignored in this repo
    ├── Images                                               # Images
    ├── LICENSE                                              # MIT license for sharing
    ├── README.md                                            # Readme file 
    └── Supervised bias analysis                             # Bias analysis based on Excel doc

## Notebooks
-	[CUB-2014](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/Supervised%20bias%20analysis/Table1.ipynb)
-	[CUB-2019](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/Supervised%20bias%20analysis/Table2.ipynb)
-	[Appeal-2014](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/Supervised%20bias%20analysis/Table5.ipynb)
-	[Appeal-2019](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/Supervised%20bias%20analysis/Table6.ipynb)
-	[Appeal-2021](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/Supervised%20bias%20analysis/Table7.ipynb)
-	[Appeal-2022](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/Supervised%20bias%20analysis/Table8.ipynb)

## Contributing members
- Floris Holstege | https://github.com/fholstege
- Jurriaan Parie | https://github.com/jfparie