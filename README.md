# Climate change in the EU

[1. Introduction](#1.-Introduction)  
[2. Scenario](#2.-Scenario)  
[3. Original dataset and mashup datasets](#3.-Original-dataset-and-mashup-datasets)  
[4. Quality analysis of the datasets](#4.-Quality-analysis-of-the-datasets)  
[5. Legal analysis (privacy, license, purpose, etc.)](#5.-Legal-analysis-(privacy,-license,-purpose,-etc.))  
[6. Ethics analysis](#6.-Ethics-analysis)  
[7. Technical analysis (formats, metadata, URI, provenance)](#7.-Technical-analysis)  
[8. Sustainability of the update the datasets over the time](#8.-Sustainability-of-the-update-the-datasets-over-the-time)  
[9. Visualization](#9.-Visualization)  
[10. RDF assertion of the metadata](#10.-RDF-assertion-of-the-metadata)  


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

## 3. Original dataset and mashup datasets
Firstly, the project makes use of data gathered from eight Special Eurobarometer surveys that were all conducted with a dedicated focus on climate change.
All of these surveys lead with the same fundamental question, in almost identical wording:

> Which of the following do you consider to be the single most serious problem facing the world as a whole? (_Special Eurobarometer 409_)

By comparing the responses of EU citizens to this question, both between countries and along the course of time, we can track the development of possiby diverging (or converging?) attitudes towards the issue.

The following datasets were used for this purpose:

#### D1
1. [Special Eurobarometer 300 (September 2008)](https://data.europa.eu/euodp/en/data/dataset/S1461_69_2_300)
2. [Special Eurobarometer 313 (July 2009)](https://data.europa.eu/euodp/en/data/dataset/S942_71_1_EBS313)
3. [Special Eurobarometer 322 (November 2009)](https://data.europa.eu/euodp/en/data/dataset/S703_72_1_EBS322)
4. [Special Eurobarometer 372 (October 2011)](https://data.europa.eu/euodp/en/data/dataset/S1007_75_4_EBS372)
5. [Special Eurobarometer 409 (March 2014)](https://data.europa.eu/euodp/en/data/dataset/S1084_80_2_409)
6. [Special Eurobarometer 435 (November 2015)](https://data.europa.eu/euodp/en/data/dataset/S2060_83_4_435_ENG)
7. [Special Eurobarometer 459 (September 2017)](https://data.europa.eu/euodp/en/data/dataset/S2140_87_1_459_ENG)
8. [Special Eurobarometer 490 (September 2019)](https://data.europa.eu/euodp/en/data/dataset/S2212_91_3_490_ENG)

Additionally, we gathered some statistical resources on various issues pertaining to structural energy questions which we deem to be somewhat connected to the issue of climate change.
These are:

#### D2
1. [Greenhouse gas emissions per capita (2000-2017)](https://data.europa.eu/euodp/en/data/dataset/rc2ELCDeTGfxdpE27gyzow)
2. [Share of renewable energy in gross final energy consumption (2004-2017)](https://data.europa.eu/euodp/en/data/dataset/kLwnawdAsL0qfRS0PzvDfw)

## 4. Quality analysis of the datasets
Firstly, we deem the data from the datasets to be generally trustworthy due to their provenance from one of the central EU portals for open data.
The _Eurobarometer_ surveys are planned by the [GESIS Leibniz Institute for the Social Sciences](https://www.gesis.org), and carried out in the member states by the institute's national partners.
Our attempts at thoroughly checking the methodology behind the data have been hindered signicantly by the fact that the GESIS catalogue database [was hacked](https://www.gesis.org/en/institute/press-and-media/press-releases-details/article/zugangsdaten-des-datenbestandskatalogs-von-gesis-gehackt), and accordingly the primary survey data on which the datasets are based was not available to us.
We thus had to accept other electronic versions of the same surveys, which were less convenient to deal with (see section _Technical analysis_).

In addition, it has to be mentioned that the irregularity in publication dates of the Eurobarometers may threaten the comparability of the data.
While generally, the Eurobarometer data does cover the timespan between 2008 and 2019, there are several years in between which do not have corresponding data.
The data in D2, on the other hand, is strictly annual, which allows for significantly more reliable analyses.

## 5. Legal analysis (privacy, license, purpose, etc.)
The data in D1 is not provided under a concise formal license, instead they are handled as documents of the European Commission and thus subject to the [Commission Decision of 12 December 2011 on the reuse of Commission documents.](https://eur-lex.europa.eu/eli/dec/2011/833/oj)

The data in D2 is licensed under [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/), which allows free sharing, reusing and modifying of the resources, as long as their source is explicitly credited.

## 6. Ethics analysis

## 7. Technical analysis
The _Eurobarometer_ datasets were only available as Microsoft Office Excel spreadsheets (_.xls_ filetype).
Furthermore, all results of an individual survey were summarized in one _.xls_ file, in which they where organized across numerous sheets, each usually representing the distribution of the respondents' answers to an individual question.
This data format posed significant hurdles to the automatic processing we had intended.

The statistical data D2 is comprised of were available as _tab-separated value_ (TSV) files providing a text-only representation of the corresponding spreadsheet.
These files were far easier to process, as they were not as structurally complex, and simpler to manipulate for the purpose of visualization.

## 8. Sustainability of the update the datasets over the time
More data of the kind we have used is likely to be published somewhat regularly on the EU Open Data portal.
Eurobarometers have been in active publication since the 1970s, and as the issue of climate change becomes more publicly present and significant, we would expect the interest in dedicated surveys on this topic to continue to increase as well.

The mashup dataset will not be updated for the time being, as it already covers a comprehensive timespan and the statistical data of GHG emissions and the share of renewable energy need to 'catch up' to the year 2019, in which the most recent _Eurobarometer_ was published.
We expect that an equivalent can be created for a corresponding timespan in future years, affording at most an equal amount of processing work, or indeed less work as soon as the primary data is once again available from the GESIS portal.

## 9. Visualization

## 10. RDF assertion of the metadata