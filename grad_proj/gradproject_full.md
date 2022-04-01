---
layout: page
title: Graduate Project
nav_exclude: true
description: Specifications for the grad project for Data 200.
markdown: kramdown
---
# Graduate Project
{:.no_toc}

* TOC
{:toc}

## Introduction

The graduate project is offered only to students enrolled in Data C200 or CS C200A. Other students are welcome to explore the questions and datasets in the project for personal learning, but their work will not be graded or counted towards their final grades.

The purpose of the project is to give students experience in both open-ended data science analysis and research in general. In this project, you will work with **one or any combination** of the following datasets provided to you to explore research questions that you define.

**Project criteria**: In addition to the general guidelines, each dataset option below has its own set of additional requirements for Report Format and Submission. Be sure to consult the correct section for your project option.

**Grading**: You will receive peer review feedback before the final deadline, and you are expected to incorporate the peer feedback into the final report and presentation. You will be graded on both the final report and presentation, as well as [deliverables](#deliverables) before the submission of the final reports, including your peer reviews.

**Teamwork**: You can work alone or in a group with **at most two other students**. If you are interested in working with others, we have an [Ed post](https://edstem.org/us/courses/15436/discussion/1058477) for teammate search. Everyone in the same group will receive the same grade. The group size will be taken into consideration when grading.

## Timeline


| Date (by EOD at 11:59pm Pacific) 	| Event / Deliverable           |
|--------------------------	|---------------------------------------------	|
| 4/9                       | Research proposal and project groups due    	|
| 4/22                      | Project checkpoint                          	|
| 4/27                    	| First draft of final report due             	|
| 4/28                   	  | Peer review open                            	|
| 5/2                       | Peer review due                             	|
| 5/9                       | Revised final report due                    	|
| 5/11                      | Presentation video due                      	|
| 5/13                      | Presentation video released (at discretion) 	|

## Deliverables and Grade Breakdown

| Deliverable                          	| Weight 	|
|--------------------------------------	|--------	|
| Research proposal and project groups 	| 10%    	|
| Checkpoint                            |  0%     |
| Submission of first draft            	| 10%    	|
| Peer review                         	| 15%    	|
| Final report: Analysis notebook      	| 20%    	|
| Final report: Project writeup        	| 30%    	|
| Final presentation video             	| 15%    	|

The project checkpoint is a quick Google Form to assess if you are making progress towards your goals.

## Datasets

This section contains the datasets we will provide to you to explore your research questions.

- You must incorporate **at least one** of the provided datasets.
- You are welcome to **bring in additional datasets** to complement the datasets provided here, but you must cite the sources and clearly describe the content of any additional data you use in the final report.

Should you need to connect together multiple datasets, please be sure to consult the [extra resource on causal inference](#extra-resources-causal-inference).

### Accessing Datasets

All the datasets provided by us can be found inside the following link on Google Drive:

<p align="center">
<a href="https://drive.google.com/drive/u/0/folders/1WGxxvFMqXutk3WKGqbHYJx0urmQp9Lbw">Graduate Project Datasets Google Drive</a>
</p>

If you wish to work on Datahub, use the following instructions on how to easily move the data from Google Drive onto Datahub (keep in mind that your Datahub kernel can only manage 2GB of memory at maximum).

If you wish to work on the project locally, you can also download the zip files containing the datasets for each topic.

#### **How to Pull Data from Google Drive directly onto Datahub**
{:.no_toc}

1. _Get the Google Drive ID of the file_. You can do this by first getting the URL of the file. You do this by right-clicking on the file in Google Drive and pressing 'Get Link'. Once you have the URL, you can find the ID by looking for the set of characters after the /d/ in the url. For example, in the following url: `https://drive.google.com/file/d/16-4O_lJGioPC5G9il4vR_XrCgJ3J9_zK/view?usp=sharing` , the Google Drive ID would be `16-4O_lJGioPC5G9il4vR_XrCgJ3J9_zK`.
2. _Download the data_. Once you have the Google Drive ID of the file, you can use the `utils.py` file inside the `grad_proj` directory on your Datahub. This file has a number of useful functions for downloading data. You'll want to use `fetch_and_cache_gdrive`. You will call the function in a notebook. The function takes in two arguments: **(1) Google Drive ID** that you got in the previous step, and **(2) name of the file**. Calling the function will generate a `data` folder and place the file into that folder, using the name you came up with as the second argument of the function.

Hopefully the above steps help you to access the data on Google Drive. There are other ways to move the data onto Datahub. Consider looking into [`gdown`](https://github.com/wkentaro/gdown) or just downloading the data from Google Drive and uploading it to Datahub manually.

Take a look at the other functions in `utils.py` if you'd like to use other data sources to supplement your project. 


### Topic 1: COVID-19

#### Dataset A: Testing and Mortality Statistics
{:.no_toc}

This dataset contains US reports on COVID-19 testing and cases from the [COVID-19 Data Repository by the Center for Systems Science and Engineering (CSSE) at Johns Hopkins University](https://github.com/CSSEGISandData/COVID-19) and CDC (Centers for Disease Control and Prevention). You can access all the data within the `Topic 1/Dataset A` directory on Google Drive:

* `csse_covid_19_daily_reports_us.csv` contains US daily reports ([documentation](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data#usa-daily-state-reports-csse_covid_19_daily_reports_us))
* `cdc_death_counts_by_sex_age_state.csv` contains US weekly reports on deaths involving COVID-19, pneumonia, and influenza reported to NCHS by sex, age, group, and state. ([documentation](https://data.cdc.gov/NCHS/Provisional-COVID-19-Death-Counts-by-Sex-Age-and-S/9bhg-hcku))
* `cdc_death_counts_by_conditons.csv` contains US weekly reports on health conditions and contributing causes mentioned in conjunction with deaths involving COVID-19. ([documentation](https://data.cdc.gov/NCHS/Conditions-contributing-to-deaths-involving-corona/hk9y-quqm))

You must choose to work with **at least 2 of the reports** above in your analysis.

#### Dataset B: Impact on Health Care
{:.no_toc}

This dataset contains reports from the Household Pulse Survey launched by NCHS in partnership with the U.S. Census Bureau; it focuses on how COVID-19 has affected survey correspondents' mental health and their access to health care. In addition, it provides statistics on usage of telemedicine by healthcare providers. You can access all the data within the `Topic 1/Dataset B` directory on Google Drive:

* `nchs_covid_indicators_of_anxiety_depression.csv` contains survey estimates of responses to questions that are indicators of anxiety or depression based on reported frequency of symptoms within the past week. ([documentation](https://data.cdc.gov/NCHS/Indicators-of-Anxiety-or-Depression-Based-on-Repor/8pt5-q6wp))
* `nchs_covid_mental_health_care.csv` contains survey estimates of responses to questions that ask if participants have accessed mental health care in the past 4 weeks. ([documentation](https://data.cdc.gov/NCHS/Mental-Health-Care-in-the-Last-4-Weeks/yni7-er2q))
* `nchs_covid_health_insurance_coverage.csv` contains survey estimates of responses to questions that ask about participants' health insurance coverage. ([documentation](https://data.cdc.gov/NCHS/Indicators-of-Health-Insurance-Coverage-at-the-Tim/jb9g-gnvr))
* `nchs_covid_reduced_access_to_health_care.csv` contains survey estimates of responses to questions that ask if participants have experienced delay or been refused health care due to COVID-19. ([documentation](https://data.cdc.gov/NCHS/Indicators-of-Reduced-Access-to-Care-Due-to-the-Co/xb3p-q62w))
* `nchs_covid_telemedicine_usage.csv` contains survey estimates of responses to questions that ask if healthcare providers offered telemedicine (including video and telephone appointments) -- both during and before the pandemic -- and about the use of telemedicine during the pandemic. ([documentation](https://data.cdc.gov/NCHS/Use-of-Telemedicine-During-COVID-19/8xy9-ubqz))

You must choose to work with **at least 3 of the reports** above in your analysis.

#### Dataset C: Ongoing Researches
{:.no_toc}

This dataset contains (in full-text and metadata form) scholarly articles related to COVID-19. The data are optimized for machine readability and made available for use by the global research community. The dataset is intended to mobilize researchers to generate new insights from the articles in support of the fight against this infectious disease. You can access all the data within the `Topic 1/Dataset C` directory on Google Drive:

* `covid_open_research_dataset.txt` contains the link that will guide you to obtain the full-text and metadata dataset of COVID-related research articles. ([documentation](https://azure.microsoft.com/en-us/services/open-datasets/catalog/covid-19-open-research/))

### Topic 2: Climate and the Environment

#### Dataset A: General Measurements and Statistics <a name="2-a"></a>
{:.no_toc}

This dataset contains some general statistics and measurements of various aspects of the climate and the environment. You can access all the data within the `Topic 2/Dataset A` directory on Google Drive. It includes the following reports:

- `daily_global_weather_2020.csv` contains data on daily temperature and precipitation measurements. To learn how to use the data from this file, please read the following section on the first report.
- `us_greenhouse_gas_emissions_direct_emitter_facilities.csv` and `us_greenhouse_gas_emission_direct_emitter_gas_type.csv` contain data reported by EPA (Environment Protection Agency) on greenhouse gas emissions, detailing the specific types of gas reported by facilities and general information about the facilities themselves. The dataset is made available through EPA's [GHGRP (Greenhouse Gas Reporting Program)](https://www.epa.gov/ghgreporting).
- `us_air_quality_measures.csv` contains data from the EPA's AQS (Air Quality System) that measures air quality on a county level from approximately 4000 monitoring stations around the country. ([source](https://data.cdc.gov/Environmental-Health-Toxicology/Air-Quality-Measures-on-the-National-Environmental/cjae-szjv))
- `aqi_data` contains more data from the EPA from a number of sites across a multitude of different metrics. ([source](https://aqs.epa.gov/aqsweb/airdata/download_files.html))

The following subsection contains more details on how to work with the first report on global daily temperature and precipitation:

The first report on daily temperature and precipitation is measured by weather stations in the [Global Historical Climatology Network](https://www.ncdc.noaa.gov/data-access/land-based-station-data/land-based-datasets/global-historical-climatology-network-ghcn) for January to December 2021.

The data in `daily_global_weather_2021.csv` is derived from the source file at https://www1.ncdc.noaa.gov/pub/data/ghcn/daily/by_year/2021.csv.gz.

To help you get started with a dataset of manageable size, we have preprocessed the GHCN dataset to include only the average temperature and precipitation measurements from stations that have both measurements. Each row in the preprocessed dataset contains both the average temperature and precipitation measurements for a given station on a given date.

If you wish to explore the climate data for a different year, you can use the `GHCN_data_preprocessing.ipynb` notebook to download and perform the preprocessing described above. Please be advised that depending on the dataset size for a given year, `GHCN_data_preprocessing.ipynb` may not run on DataHub. We will not be providing infrastructural support for running the notebook, but you are welcome to run it on a different machine you have access to or ask a GSI to dump the data for you.

The data contains only the (latitude, longitude) coordinates for the weather stations. To map the coordinates to geographical locations, the [reverse-geocoder](https://github.com/thampiman/reverse-geocoder) package mentioned in the [References](#coordinates) section might be helpful.

#### Dataset B: Biodiversity in the Ecosystem
{:.no_toc}

This dataset contains studies focused specifically on the impact of environmental and climate changes on biodiversity and the local ecosystems. You can access all the data within the `Topic 2/Dataset B` directory on Google Drive. It includes the following reports:

- `bioCON_plant_diversity.csv` contains data collected as part of an ecological experiment, BioCON (Biodiversity, CO2, and Nitrogen), that started in 1997 and focused on studying biodiversity within the plant species at Cedar Creek Ecosystem Science Preserve. ([documentation](https://search.dataone.org/view/https%3A%2F%2Fpasta.lternet.edu%2Fpackage%2Fmetadata%2Feml%2Fknb-lter-cdr%2F339%2F9))
- `plant_pollinator_diversity_set1.csv` and `plant_pollinator_diversity_set2.csv` contain ecological data collected from a long-term observation study from 2011 to 2018 that focuses on plant-pollinator interaction and its impact on local biodiversity. ([documentation](https://search.dataone.org/view/https%3A%2F%2Fpasta.lternet.edu%2Fpackage%2Fmetadata%2Feml%2Fknb-lter-and%2F5216%2F6))
- `national_parks_biodiversity_parks.csv` and `national_parks_biodiversity_species.csv` contain data published by the National Park Service on animal and plant species identified in individual national parks.

### Topic 3: Emerging Researches and Technologies <a name="tech"></a>

#### Dataset A: Space Exploration
{:.no_toc}

This dataset contains a set of reports from pioneering researches that explore the outer space. Much of the data from these studies have provided a rich foundation for a variety of large-scale research projects that explore widely discussed topics such as habitable exoplanets or search for extraterrestrial life.

You can access all the data within the `Topic 3/Dataset A` directory on Google Drive. It includes the following reports:

- `kepler_exoplanet_search.csv` contains data collected by NASA from the Kepler Space Observatory as part of a long-term study on finding habitable exoplanets from over 10,000 candidates. ([source](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=koi))
- `kelper_planetary_system_composite.csv` contains data collected by NASA from the Kelper Space Observatory as part of an ongoing study that tabulates all confirmed planetary systems outside the solar system. You are encouraged to use the composite data in conjunction with the exoplanet search results above. ([source](https://exoplanetarchive.ipac.caltech.edu/cgi-bin/TblView/nph-tblView?app=ExoTbls&config=PSCompPars))
- `nasa_neows.csv` contains data collected from NASA's [NeoWs (Near Earth Object Web Service)](https://neowise.ipac.caltech.edu/) that collects information on near earth asteroids.

#### Dataset B: Recommender Systems
{:.no_toc}

A recommender system is an information filtering system that focuses on predicting the preference a user would give to an item by predicting its rank; it is used in a variety of areas, such as search engines, online shopping platforms, etc. This dataset contains a set of reports on various tools using a recommender system.

You can access all the data within the `Topic 3/Dataset B` directory on Google Drive. It includes the following reports:
- `fitness_recommendation.txt` contains a link to access the fitness data from sequential sensors for various workouts. ([documentation](https://sites.google.com/eng.ucsd.edu/fitrec-project/home))
- `amazon_reviews.txt` contains a link to access the data on a subset of Amazon product reviews. The report includes metadata such as ratings and text on the reviews and general information about the product. ([documentation](https://nijianmo.github.io/amazon/index.html))

## Report Format and Submission
The project submission should include the following two components.

### [Component 1] Analysis Notebooks

The Jupyter Notebook(s) containing all the analyses that you performed on the datasets to support your claims in the narrative notebook. Make sure that all references to datasets are done as `data/[path to data files]`. You can copy the datasets from `~/shared/grad_proj/multiple_datasets` into `data/` at the top-level directory for your project on DataHub to do this.

Your analysis notebook(s) should address all of the following components in the data science lifecycle. Please note that a thorough explanation of your thought process and approach is **as important as** your work. We have provided a few preliminary questions/tips you can think about for each part:
- **Data Sampling and Collection**
  - How were the data collected?
  - Was there any potential bias introduced in the sampling process?
- **Data Cleaning**
  - What type of data are you currently exploring?
  - What is the granularity of the data?
  - What does the distribution of the data look like? Are there any outliers? Are there any missing or invalid entries?
- **Exploratory Data Analysis**
  - Is there any correlation between the variables you are interested in exploring?
  - How would you cleanly and accurately visualize the relationship among variables?
- **Data Modeling and Inferences**
  - Please note that the following datasets have a data modeling requirement, i.e. you need to utilize at least 1 machine learning model we teach in this class in your project: Topic 1 - Dataset A, Topic 1 - Dataset C, Topic 2 - Dataset A, Topic 3 - Dataset A, Topic 3 - Dataset B. For datasets not mentioned above, you are welcome to continue building machine learning model(s). Otherwise, we will be placing more
  emphasis on the inference part instead.
  - Here are a few components your notebook must address if your focus is on modeling:
    - What type of machine learning problem are you investigating?
    - What model do you plan on using and why?
    - Does your model require hyperparameter tuning? If so, how do you approach it?
    - How do you engineer the features for your model? What are the rationales behind selecting these features?
    - How do you perform cross validation on your model?
    - What loss metrics are you using to evaluate your model?
    - From a bias-variance tradeoff standpoint, how do you assess the performance of your model? How do you check if it is overfitting?
    - How would you improve your model based on the outcome?
  - If you are choosing to pursue your research question from an inference angle
    - Your notebook must demonstrate sufficient analysis and visualization to support your conclusion. 
    - You must have a clearly constructed hypothesis test (including a clearly defined test statistic, significance level, and justification of chosen procedure)
    - We will not restrict you to the type of statistical test you conduct as there are many different statistical techniques that may apply to your case. However, we also ask that you provide detailed justification for the techniques you choose and how it allows you make those inferences.

### [Component 2] Project Writeup

This is a single PDF that summarizes your workflow and what you have learned. It should be structured as a research paper and include a title, list of authors, abstract, introduction, description of data, description of methods, summary of results, and discussion. Make sure to number figures and tables and include informative captions.

If you wish, you can render the PDF using LaTeX, provided that the provenance of the figures is clearly labeled in the main narrative, and the figures can be reproduced by running the analysis notebooks.

Specifically, you should address the following in the narrative:

* Clearly stated research questions and why they are interesting and important. You must include **at least one research question involving at least one or more datasets from one of the topics we provided**, but you may include additional research questions about each individual dataset. At least one of your research questions has to include a modeling component, e.g., can we build a model using climate data to predict growth in COVID-19 cases accurately?
* A brief survey of related work on the topic(s) of your analysis and how your project differs from or complements existing research.
* If applicable, descriptions of additional datasets that you gathered to support your analysis.
* Methodology: carefully describe the methods you use and why they are appropriate for answering your search questions. It must include
    * a brief overview of causal inference, which should be written in a way such that another student in Data 100 who has never been exposed to the concept can carry out the analyses involving the datasets in your project.
    * a detailed description of how modeling is done in your project, including inference or prediction methods used, feature engineering and regularization if applicable, and cross-validation or test data as appropriate for model selection and evaluation.  
* _Interesting findings_* about each dataset when analyzed individually. Include visualizations and descriptions of data cleaning and data transformation necessary to perform the analysis that led to your findings.
* _Interesting findings_* involving your datasets. Include visualizations and descriptions of data cleaning and data transformation necessary to perform the analysis that led to your findings.
* Analysis of your findings to answer your research question(s). Include visualizations and specific results. If your research questions contain a modeling component, you must compare the results using different inference or prediction methods (e.g., linear regression, logistic regression, or classification and regression trees). Can you explain why some methods performed better than others?
* An evaluation of your approach and discuss any limitations of the methods you used.
* Describe any surprising discoveries that you made and future work.

\* Examples of **interesting findings**: interesting data distributions and trends, correlations between different features, the relationship between the data distribution for the general population and specific datasets (e.g., the gender distribution in the census dataset vs. in the mental health dataset), specific features that are notably effective/ineffective for prediction.

The narrative notebook should include figures sparingly to support specific claims. It can include runnable components, but it should not have large amounts of code. The length of the report should be 8 ± 2 pages when it is printed as a PDF, excluding figures and code.

Tip: if you need to write a large amount of $\LaTeX$, you may want to use the `%%latex` cell magic.

Please submit everything as a zip file to the final report submission portal on Gradescope. Please make sure the folder in the zip file has the following structure:

```
studentIDs/
    data/[all datasets used]
    analysis/[analysis notebooks]
    narrative/[narrative notebook]
    figures/[figures included in the narrative notebook]
```

For groups with multiple members, please use student IDs joined by `_` as the name for the top-level directory. The analysis notebooks must be runnable within this directory structure. If the narrative notebook includes any figures that are created in the analysis notebooks, the figures should be saved to `figures/` by the analysis notebooks and imported from `figures/` by the narrative notebook.

## Rubrics
### Peer Review

Each group will peer review the projects from another group. The review will be graded by staff out of a total of 15 points. Each review should include the following components:

1. (5 points) A summary of the report. The summary should address at least the following:
  - What research question does the group propose? Why is it important?
  - How does the dataset relate to the research question?
  - What data modeling/inference techniques do the group primarily use to gain insights into their research question? Why are these techniques suitable for the task?
  - What are the next steps a researcher can take if they want to investigate the question further based off the work in the project?

2. (10 points, 2 per component) An evaluation of the report based on the Data Science Lifecycle. The review should include at least **one strong point and one suggestion for improvement** for each of the following components in the project:
  - Data collection and sampling
  - Data cleaning
  - Exploratory data analysis (data wrangling, visualization, etc.)
  - Data modeling (feature engineering, selection of the model, and evaluation of the model's performance, etc.)
  - Inference (do the results from the model sufficiently support the conclusion within the report?)

### Final Report: Analysis Notebook

| Criterion                                             | Points|
|-------------------------------------------------------|-------|
| Code readability and documentation                    | 5     |
| Proper and sufficient utilization of Python libraries | 5     |
| Overall code quality                                  | 3     |
| Replicability of the results                          | 7     |
| **Total**                                             | **20**|

### Final Report: Project Writeup

| Criterion                                                              | Points|
|------------------------------------------------------------------------|-------|
| Introduction, motivation, and presentation of the research question(s) | 3     |
| Exploratory data analysis                                              | 5     |
| Modeling and inference techniques                                      | 7     |
| Analysis of results                                                    | 7     |
| Implementation of peer review feedback                                 | 3     |
| Discussion of potential societal impacts and/or ethical concerns       | 2     |
| Overall clarity and structure of the report                            | 3     |
| **Total**                                                              | **30**|


## Extra Resources: Causal Inference

When studying the relationship between datasets, you might want to consult the following references on causality vs. correlation. Oftentimes, it is tempting to make claims about causal relationships when there is not enough evidence from the data to support such claims. Please review the following references, or other reputable references that you find on the topic to familiarize yourself with relevant concepts and methods.

* [Data 102  Data, Inference, and Decisions Spring 2020: Lecture 13: Causal Inference I. Moritz Hardt.](https://data102.org/sp20/assets/notes/notes13.pdf)
* [Hernán MA, Robins JM (2020). Causal Inference: What If. Boca Raton: Chapman & Hall/CRC.](https://www.hsph.harvard.edu/miguel-hernan/causal-inference-book/)
* [Advanced Data Analysis from an Elementary Point of View by Cosma Rohilla Shalizi](https://www.stat.cmu.edu/~cshalizi/ADAfaEPoV/)
