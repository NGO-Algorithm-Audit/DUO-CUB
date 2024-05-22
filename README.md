# DUO CUB bias analysis

This bias analysis is part of a quantitative and qualitative audit of DUO's control process to (un)duly allocated college grants.

📄 Audit report: [*Bias prevented*](https://algorithmaudit.eu/algoprudence/cases/aa202402_bias-prevented_addendum/)

⌗ Data: [Statistics Netherlands](https://www.cbs.nl/nl-nl/maatwerk/2024/21/ontvangers-uitwonendenbeurs-herkomst-2014-2017-2019-2021-en-2022)

## Project description
Education Executive Agency of The Netherlands (DUO) performs checks to ensure that disbursed college grants are duly granted. This process is known as the College Grant Check (in Dutch: CUB). Suspicion has emerged that the CUB process may be biased against students with a migration background. This suspicion is based on the appeal procedures initiated by students who were found to have received grants unduly. Due to the General Data Protection Regulation (GDPR), DUO does not collect information on the origin of students during the CUB-process. The Dutch national office of statistics (Netherlands Statistics) has therefore been asked to provide aggregated statistics on the country of birth and country of origin of 300.000+ students in the period 2014-2022. A supervised bias analysis of these data are shared in this repository. DUO has provided CBS with data on eight different populations, including background information (citzen service number, education, age, distance to parent(s)) and process characteristics (risk category, selected for control, outcome control, appeal procedure, outcome appeal).

### Methods used
-   Supervised bias analysis
    - Demographic parity plots for aggregation statistics provided by Netherlands Statistics 

## Repo Overview
    .
    ├── DUO_CUB_Netherlands_Statistics.xlsx                  # Dataset provided by Netherlands Statistics (translated to EN)
    ├── .gitignore                                           # Files to be ignored in this repo
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