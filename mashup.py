import pandas as pd
import xml.etree.ElementTree as ET
import lxml.etree as etree

most_serious_problem = pd.read_csv("processed_data/special_eb/data/3_final/most_serious_problem/special_eb_most_serious_problem_final.csv")
personally_taken_action = pd.read_csv("processed_data/special_eb/data/3_final/personally_taken_action/special_eb_personally_taken_action_final.csv")
severity_of_problem = pd.read_csv("processed_data/special_eb/data/3_final/severity_of_problem/special_eb_severity_of_problem_final.csv")
who_is_responsible = pd.read_csv("processed_data/special_eb/data/3_final/who_is_responsible/special_eb_who_is_responsible_final.csv")
share_renewable = pd.read_csv("processed_data/statistical_data/share_renewable/share_renewable.tsv", sep="\t")
share_renewable['source'] = 'share_renewable'
ghg_emissions = pd.read_csv("processed_data/statistical_data/ghg_emissions/ghg_emissions.tsv", sep="\t")
ghg_emissions['source'] = 'ghg_emissions'

data = [share_renewable, ghg_emissions]
data_annuals = pd.concat(data)

data = [most_serious_problem, personally_taken_action, severity_of_problem, who_is_responsible]
all_eurobarometer_data = pd.concat(data)
all_eurobarometer_data['source'].replace(regex=True,inplace=True,to_replace=r'\D',value=r'')
all_eurobarometer_data.rename(columns={"UE28-UK\nEU28-UK":"EU28-UK", "UE27\nEU27":"EU27","UE28\nEU28":"EU28"})

root = ET.Element("root")
countries = all_eurobarometer_data.columns[0:36].to_list()
for country in countries:
    subset = all_eurobarometer_data[[country, 'answer/countries', 'question', 'source']]
    cur_country = ET.SubElement(root, "country", id=country)
    cur_eb = ET.SubElement(cur_country, "eurobarometer")
    surveylist = []
    for survey in all_eurobarometer_data.source:
        if not survey in surveylist:
            cur_survey = ET.SubElement(cur_eb, "survey", id=survey)
            surveylist.append(survey)
            cur_survey_data = subset.loc[subset['source'] == survey]
            for index, datum in cur_survey_data.iterrows():
                if not datum.question == "who_is_responsible":
                    cur_question = ET.SubElement(cur_survey, "question", id=datum.question)
                    ET.SubElement(cur_question, "response").text = str(datum[country])
                else:
                    if cur_survey.find('question[@id="who_is_reponsible"]') is None:
                        cur_question = ET.SubElement(cur_survey, "question", id="who_is_responsible")
                    ET.SubElement(cur_question, "response", id=datum['answer/countries']).text = str(datum[country])

for country in data_annuals['geo\\time']:
    cur_country_node = root.find('country[@id="%s"]' % country)
    if not cur_country_node == None:
        country_data = data_annuals.loc[data_annuals['geo\\time'] == country]
        print(country_data)
        colnames = list(country_data)
        for index, row in country_data.iterrows():
            if row.source == 'share_renewable':
                if cur_country_node.find('share_renewable') is None:
                    cur_dataset = ET.SubElement(cur_country_node, 'share_renewable')
                    i = 0
                    for datum in row[0:17]:
                        ET.SubElement(cur_dataset, 'value', id=colnames[i]).text = str(datum)
                        i += 1
            elif row.source == 'ghg_emissions':
                if cur_country_node.find('ghg_emissions') is None:
                    cur_dataset = ET.SubElement(cur_country_node, 'ghg_emissions')
                    i = 0
                    for datum in row[0:17]:
                        ET.SubElement(cur_dataset, 'value', id=colnames[i]).text = str(datum)
                        i += 1

tree = ET.ElementTree(root)
tree.write('mashup.xml')
x = etree.parse('mashup.xml')
x = etree.tostring(x, pretty_print=True, encoding='unicode')
out = open('processed_data/mashup/mashup.xml', 'w+')
out.write(x)