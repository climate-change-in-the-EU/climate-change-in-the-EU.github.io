# Climate change in the EU

Authors: Lukas Henne, Elisabeth Reuhl

## List of contents
[1. Introduction](#1-introduction)  
[2. Scenario](#2-scenario)  
[3. Original dataset and mashup datasets](#3-original-datasets-and-mashup-datasets)  
[3.1. Original datasets](#31-original-datasets)  
[3.2. Mashup dataset](#32-mashup-dataset)  
[4. Quality analysis of the datasets](#4-quality-analysis-of-the-datasets)  
[5. Legal analysis](#5-legal-analysis)  
[6. Ethics analysis](#6-ethics-analysis)  
[7. Technical analysis](#7-technical-analysis)  
[7.1. Processing of the datasets](#71-processing-of-the-datasets)  
[7.2. Creating the mashup dataset](#72-creating-the-mashup-dataset)  
[8. Sustainability of the update the datasets over the time](#8-sustainability-of-the-update-the-datasets-over-the-time)  
[9. Visualization](#9-visualization)  
[10. RDF assertion of the metadata](#10-rdf-assertion-of-the-metadata)  


## 1. Introduction
This project investigates the European public's opinion on the problem of climate change and attempts to correlate it with various data on actual national greenhouse gas emissions and energy usage from renewable sources.
It uses openly accessible datasets which have been processed for comparability and visualized in the form of graphs.
The leading questions these reports address are as follows:

* Do Europeans have comparable views on the problem of climate change across countries? If so, has this been always been the case in past years?
* Generally, how serious do Europeans deem the problem of climate change to be?
* Does the concern for climate change reflect in national consumption statistics, e.g. greenhouse gas emissions or the share of energy generated from renewable sources?

The project website aims to present the user with a possibility to explore datasets sourced from the [EU Open Data Portal](https://data.europa.eu/euodp/en/home).
Beside basic access to the mashup dataset in file form, it can also be explored visually in correspondence to the countries of the EU as they are located on an interactive map.

## 2. Scenario
From an outside view, multiple tendencies are often supposed when considering the EU's response to the problem of climate change:

* The countries of the EU seem to experience wide and growing disparities with respect to the seriousness they attribute to the issue.
* There seem to be fundamental differences in what structural actions the national governments of the EU consider appropriate in this situation, with some governments making great efforts to invest in progressive technologies ensuring energy sustainability and less pollutive energy generation, while others do not push for changes away from fossil fuels.
* The government's view and structural action doesn't always represent its own people's position on the issue, meaning that e.g. the population of a country may be very aware of the severity of the problem while the government does not take decisive action.

Some of the open data offered on [EU Open Data Portal](https://data.europa.eu/euodp/en/home) show numerous kinds of potential for insights into the reality of the European people's attitude towards climate change.
Using parts of this data, we have attempted 

## 3. Original datasets and mashup datasets
### 3.1. Original datasets 
Firstly, the project makes use of data gathered from eight Special Eurobarometer surveys that were all conducted with a dedicated focus on climate change between the years of 2008 and 2019. This data is stored [here](https://github.com/climate-change-in-the-EU/climate-change-in-the-EU.github.io/tree/master/data/original_data/special_eb).
Data from the following datasets was used:

#### D1
| Dataset ID in the EU Open Data Portal | Year | Reference Number | Title                                         | Fieldwork Conducted |
|------------------------------------|------|-----------|-----------------------------------------------|---------------|
| [S2212_91_3_490_ENG](https://data.europa.eu/euodp/en/data/dataset/S2212_91_3_490_ENG) | 2019 | 490       | Climate Change                                | April 2019    |
| [S2140_87_1_459_ENG](https://data.europa.eu/euodp/en/data/dataset/S2140_87_1_459_ENG) | 2017 | 459       | Climate change                                | March 2017    |
| [S2060_83_4_435_ENG](https://data.europa.eu/euodp/en/data/dataset/S2060_83_4_435_ENG) | 2015 | 435       | Climate change                                | May 2015      |
| [S1084_80_2_409](https://data.europa.eu/euodp/en/data/dataset/S1084_80_2_409) | 2014 | 409       | Climate change                                | November 2013 |
| [S1007_75_4_EBS372](https://data.europa.eu/euodp/en/data/dataset/S1007_75_4_EBS372) | 2011 | 372       | Climate change                                | June 2011     |
| [S703_72_1_EBS322](https://data.europa.eu/euodp/en/data/dataset/S703_72_1_EBS322) | 2009 | 322       | Europeans'attitudes towards climate change    | August 2009   |
| [S942_71_1_EBS313](https://data.europa.eu/euodp/en/data/dataset/S942_71_1_EBS313) | 2009 | 313       | Europeans’ attitudes towards climate change   | January 2009  |
| [S1461_69_2_300](https://data.europa.eu/euodp/en/data/dataset/S1461_69_2_300) | 2008 | 300       | Europeans' attitudes towards climate change   | March 2008    |

From each dataset, only the section "Volume A: Countries" is used in this project.

All of these surveys contain mostly the same questions. We have picked out four questions which were present in many surveys and which we found suitable for further analysis:
* "Which of the following do you consider to be the single most serious problem facing the world as a whole?" (**'most_serious_problem'**)
* "And how serious a problem do you think climate change is at this moment?" (**'severity_of_problem'**)
* "In your opinion, who within the EU is responsible for tackling climate change?" (**'who_is_responsible'**)
* "Have you personally taken any action to fight climate change over the past six months?" (**'personally_taken_action'**)
For easier handling during the data processing, we gave each of them a shorter name, denoted above in parentheses.

By comparing the responses of EU citizens to these questions, both between countries and along the course of time, we can track the development of possiby diverging (or converging?) attitudes towards the issue of climate change.


Additionally, we chose some statistical resources pertaining to greenhouse gas emissions and the use of renewable energy, which we deem to be connected to the issue of climate change. This data is stored [here](https://github.com/climate-change-in-the-EU/climate-change-in-the-EU.github.io/tree/master/data/original_data/statistical_data).
These are:

#### D2
1. [Greenhouse gas emissions per capita (2000-2017)](https://data.europa.eu/euodp/en/data/dataset/rc2ELCDeTGfxdpE27gyzow)
2. [Share of renewable energy in gross final energy consumption (2004-2017)](https://data.europa.eu/euodp/en/data/dataset/kLwnawdAsL0qfRS0PzvDfw)

### 3.2. Mashup dataset
The mashup dataset is stored [here](https://github.com/climate-change-in-the-EU/climate-change-in-the-EU.github.io/tree/master/data/processed_data/mashup).

## 4. Quality analysis of the datasets
Firstly, we deem the data from the datasets to be generally trustworthy due to their provenance from one of the central EU portals for open data, and due to being conducted on behalf of the European Commission and published by the Directorate-General for Communication of the European Commission.

The _Eurobarometer_ surveys are planned by the [GESIS Leibniz Institute for the Social Sciences](https://www.gesis.org), and carried out in the member states by the institute's national partners.
Our attempts at thoroughly checking the methodology behind the data have been hindered signicantly by the fact that the GESIS catalogue database [was hacked](https://www.gesis.org/en/institute/press-and-media/press-releases-details/article/zugangsdaten-des-datenbestandskatalogs-von-gesis-gehackt), and accordingly the primary survey data on which the datasets are based was not available to us.
We thus had to accept other electronic versions of the same surveys, which were less convenient to deal with (see section [7. Technical analysis (formats, metadata, URI, provenance)](#7.-Technical-analysis)).

In addition, it has to be mentioned that the irregularity in publication dates of the Special Eurobarometers may threaten the comparability of the data, as compared to the regularly conducted Standard Eurobarometers.
While generally, the Special Eurobarometer data does cover the timespan between 2008 and 2019, there are several years in between which do not have corresponding data.

The data in D2, on the other hand, is strictly annual, which allows for significantly more reliable analyses.

## 5. Legal analysis
The data in D1 is not provided under a concise formal license, instead they are handled as documents of the European Commission and thus subject to the [Commission Decision of 12 December 2011 on the reuse of Commission documents.](https://eur-lex.europa.eu/eli/dec/2011/833/oj). 
Compared to Creative Commons licenses, this license is quite hard to understand for lay people as is only presented in the form of the document published in the Official Journal of the European Union, which requires a good reading comprehension for legal documents.
We deem it to be no more restrictive than the Creative Commons Attribution 4.0 International license (see below), and consider it ethically justifiable to use the data in this non-commercial project.
In fact, the Commission has, in February 2019, [adopted a Decision](https://ec.europa.eu/newsroom/dae/document.cfm?doc_id=58807) that considers CC-BY 4.0 and CC0 the default licenses for its published data.

The data in D2 is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), which allows free sharing, reusing and modifying of the resources, as long as their source is explicitly credited.

## 6. Ethics analysis
As explained in section [4. Quality analysis of the datasets](#4-quality-analysis-of-the-datasets), the datasets can be deemed generally trustworthy.

However, a valid point of criticism is that the commissioner of the Eurobarometers (European Commission) is also the topic of the survey, since respondents are asked about their opinions about the EU. In their article Martin Höpner and Bojan Jurczyk, researchers of the Max Planck Institute for the Study of Societies, criticize this and list multiple instances of manipulative tendencies, suggestive questions, or unequally distributed positive/negative answer possibilities. 
(Höpner, Martin; Jurczyk, Bojan. 2012. Kritik des Eurobarometers. Über die Verwischung der Grenze zwischen seriöser Demoskopie und interessengeleiteter Propaganda. In: Leviathan 40, 3, 326–349. [PDF](https://www.leviathan.nomos.de/fileadmin/leviathan/doc/Aufsatz_Leviathan_12_03.pdf))

In the case of the four questions selected by us (see [D1](#D1)), we did not notice definite instances of this. Similar questions about survey design and the validity or significance of questions and their answers would likely have to be raised for most data collected in surveys. For the scope of our project we believe that the data is ethically justifiable.

We do not have ethical concerns with regard to the protection of respondents' personal information, since answers are never presented for the scope of a single person but only the combined data for all respondents from a country, which is usually around 1000 people.

## 7. Technical analysis
The _Eurobarometer_ datasets (D1) is only available as Microsoft Office Excel spreadsheets (_XLS_ filetype).
Furthermore, all results of an individual survey were summarized in one _XLS_ file, in which they where organized across numerous sheets, each usually representing the distribution of the respondents' answers to an individual question.
This data format posed significant hurdles to the automatic processing we had intended.

The statistical data (D2) is available as _tab-separated value_ (TSV) files providing a text-only representation of the corresponding spreadsheet.
These files were far easier to process and did not need to be modified much in order to be used for the purpose of visualization, as they were not as structurally complex.

### 7.1. Processing of the datasets
The original datasets from the Special Eurobarometer surveys on climate change (D1) required a relatively complex processing. This is handled by the Python file [process_special_eb.py](https://github.com/climate-change-in-the-EU/climate-change-in-the-EU.github.io/blob/master/python_scripts/process_special_eb.py). There are three steps to the processing:
1. Converting the sheets containing interesting questions from _XLS_ to _CSV_
2. Extracting selected data from the _CSV_ files of step 1
3. Combining the data of step 2 into a single _CSV_ file

The steps are more precisely documented by comments inside the code. 
The files created in each step can be found in the folder [data/processed_data/special_eb](https://github.com/climate-change-in-the-EU/climate-change-in-the-EU.github.io/tree/master/data/processed_data/special_eb).

While the processing is generally automated with the script, it was neccessary to define some variables based on our visual inspection of the orginal _XLS_ and preliminary _CSV_ files: 
For example for step 1, it was neccessary to list the names of the sheets for each of the questions we were interested in (the codes of the questions), as they sometimes changed between surveys. Furthermore, the section of the spreadsheets containing the actual data had to be defined. We also hard coded the rows of data that we wanted to extract from each of the questions' data during step 2. 

The Python libraries 'xlrd', 'csv', and 'pandas' have been chosen for reading in data from _XLS_ files, writing to/reading from _CSV_ files, and converging multiple tables, respectively.

### 7.2. Creating the mashup dataset
The creation of a mashup containing all data is done by the Python file [mashup.py](https://github.com/climate-change-in-the-EU/climate-change-in-the-EU.github.io/blob/master/python_scripts/mashup.py). 
The data is concatenated and transformed to a single _XML_ file. 
The _XML_ (_Extensible Markup Language_) format was chosen because it allows the creation of a structured and well human-readable file which at the same time contains data which itself is somewhat differently structured in each case of the original datasets.

``mashup.py`` uses three additional libraries for processing the original data:
1. The ``pandas`` library offers a wide array of tools for data processing and analysis. 
In our case, the ``pandas.read_csv`` function proved to be especially useful, as it allows for importing the comma-seperated text spreadsheets as complex ``dataframe``objects that can be easily manipulated within the Python script.
Merging the datasets while preserving all necessary information about each datum's origin and connections was therefore quite convenient.

2. The ``xml.etree.ElementTree`` library is a built-in Python library that supports the creation of XML documents on the basis of ``ElementTree`` objects.
The script makes use of this function by iteratively creating hierarchically ordered XML nodes from the cells contained in the ``dataframe`` object.

3. The ``lxml`` library is another package supporting the creation and manipulation of XML documents.
Its only use for ``mashup.py`` is to reformat the previously output XML document to give it a more easily readable appearance for the user.

## 8. Sustainability of the update the datasets over the time
More data of the kind we have used is likely to be published somewhat regularly on the EU Open Data portal.
Eurobarometers have been in active publication since the 1970s, and as the issue of climate change becomes more publicly present and significant, we would expect the interest in dedicated surveys on this topic to continue to increase as well.

The mashup dataset will not be updated for the time being, as it already covers a comprehensive timespan and the statistical data of GHG emissions and the share of renewable energy need to 'catch up' to the year 2019, in which the most recent _Eurobarometer_ was published.
We expect that an equivalent can be created for a corresponding timespan in future years, affording at most an equal amount of processing work, or indeed less work as soon as the primary data is once again available from the GESIS portal.

## 9. Visualization
The visualization consists of an interactive map and four charts that will be shown when clicking within the borders of a country on the map.
The interactive parts of the map cover all member states of the European Union.
Out of the four charts, two provide an overview of answers by the public to a Eurobarometer question, and each of the other two shows data from one of the sets we merged into D2.
Thus, only half of the Eurobarometer data we processed is currently being used for visualization. 

The interactive map is built with the help of [``leaflet.js``](https://leafletjs.com), a JavaScript library providing functions for constructing overlays from maps.
Additionally, we rely on the ``leaflet-ajax`` plugin to import the geometrical shapes of EU countries from a geoJSON dataset which is in the public domain.

Plotting the graphs on demand is done by forwarding necessary information about the country area that the user has interacted with to [``plotly.js``](https://plot.ly/javascript/), another JavaScript package that helps in creating interactive maps.
The user can add as many countries as they like to the diagrams by clicking on the corresponding map area.

## 10. RDF assertion of the metadata
For the statistical data used (D2), no changes to the data were made, therefore the orginal metadata holds true. The metadata in the _DCAT_ (Data Catalog Vocabulary) _RDF_ vocabulary is found on the datasets' EU Open Data Portal pages (see links under D2). The _RDF_ files are also saved to the [directory](https://github.com/climate-change-in-the-EU/climate-change-in-the-EU.github.io/tree/master/data/original_data/metadata/) which is holding a copy of the original datasets.

For the survey data (D1), changes have been made to the data (as described in section [7.1. Processing of the datasets](#71-processing-of-the-datasets). This metadata can be found 

The mashup dataset's metadata can be found
