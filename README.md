# DUO CUB bias analysis

This bias analysis is part of a quantitative and qualitative audit of DUO's control process to (un)duly allocated college grants.

📄 Audit report: [*Addendum Bias prevented*](https://algorithmaudit.eu/algoprudence/cases/aa202402_bias-prevented_addendum/)

ℹ️ Data: [Statistics Netherlands](https://www.cbs.nl/nl-nl/maatwerk/2024/21/ontvangers-uitwonendenbeurs-herkomst-2014-2017-2019-2021-en-2022)

## Key findings
-   Finding 1: The CUB process as a whole has been biased against students with a non-European migration background.
-   Finding 2: The risk profile used in the CUB process was biased against students with a non-European migration background. This bias was caused by assigning higher risk scores to students with a certain type of education (mbo-students) and to students living closer to their parent(s).
-   Finding 3: Manual selection of students for control reinforced bias in the CUB process.
-   Finding 4: Due to bias in the CUB process against students with a non-European migration background, more unduly granted loans have been observed for this group. This is primarily caused by the overinspection of this demography.
-   Finding 5: A significant part of the students appealing a decision of unduly allocated grants have a non-European migration background. No bias has been identified in the appeal procedure itself.

<sub>CUB process stands for students subjected to control procedure whether college grants are (un)duly allocated</sub>

![image](./images/Overview_CUB-2014.png)

## Project description
Education Executive Agency of The Netherlands (DUO) performs checks to ensure that disbursed college grants are duly granted. This process is known as the College Grant Check (in Dutch: CUB). Suspicion has emerged that the CUB process may be biased against students with a migration background. This suspicion is based on the appeal procedures initiated by students who were found to have received grants unduly. Due to the General Data Protection Regulation (GDPR), DUO does not collect information on the origin of students during the CUB-process. The Dutch national office of statistics (Netherlands Statistics) has therefore been asked to provide aggregated statistics on the country of birth and country of origin of 300.000+ students in the period 2014-2022. A supervised bias analysis of these data are shared in this repository. DUO has provided CBS with data on eight different populations, including background information (citzen service number, education, age, distance to parent(s)) and process characteristics (risk category, selected for control, outcome control, appeal procedure, outcome appeal).

## Definition bias
Bias is defined as significant deviations in the demographic distribution compared to the start population (the population of all recipients of college grants), resulting from disproportionate selection of certain students during the CUB process. If there is a substantial overrepresentation of students with a migration background in various steps of the CUB process, it indicates that the CUB process (and/or its various steps) is biased against this demographic. Here, bias does not imply conscious bias, i.e., premeditated and deliberate selection of a particular demographic by DUO or individual civil servants. In this study, bias refers to measured disparities in the data as an (unintentional) effect of the CUB process steps. There is no bias if the demographic proportions remain almost unchanged throughout the CUB process.

## Definition migration background
Date provided by the Dutch national office of statistics (Statistics Netherlands):
-   country of birth (exact defintion can be found in [DUO_CUB_Netherlands_Statistics.xlsx](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/DUO_CUB_Netherlands_Statistics.xlsx))
-   country of origin (exact defintion can be found in [DUO_CUB_Netherlands_Statistics.xlsx](https://github.com/NGO-Algorithm-Audit/DUO-CUB/blob/main/DUO_CUB_Netherlands_Statistics.xlsx))

Overview of used terminology:

![image](./images/Migration_overview_EN.png)

![image](./images/Migration_tree_EN.png)

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