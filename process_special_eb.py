import csv
import os
import xlrd

# The names of the sheets with the questions we are interested in:
# "Which of the following do you consider to be the single most serious problem facing the world as a whole?"
# "And how serious a problem do you think climate change is at this moment?"
# "In your opinion, who within the EU is responsible for tackling climate change?"
# "Have you personally taken any action to fight climate change over the past six months?"
sheets_interesting = {'most_serious_problem': ['QA1a', 'QB1a', 'QC1a', 'QE1a1', 'QE1a', 'QD1a'],
                      'how_serious': ['QA2.1', 'QA2', 'QB2', 'QC2', 'QE2a.1', 'QE2', 'QB2.1'],
                      'who_is_responsible': ['QA3', 'QB3', 'QC3'],
                      'personally_taken_action': ['QA5', 'QB5', 'QC5']}

# Directory for input/original data and output/processed data
dir_original_eb = 'original_data/special_eb/'
dir_processed_eb = 'processed_data/special_eb/'


def extract_to_csv(special_eb_file, sheet, question_short):
    question = []
    answers = []

    # Get the cell containing the question in English
    if sheet.cell(2, 11).value != "":
        question.append(sheet.cell(2, 11).value)
    else:
        question.append(sheet.cell(2, 10).value)

    # Get the rows containing the answers (Answers always fill the sheet from row 8 until the last row)
    for i in range(8, sheet.nrows):
        answers.append(sheet.row_values(i))

    # Write to CSV file
    csv_filename = dir_processed_eb + special_eb_file + '_' + question_short + '.csv'
    with open(csv_filename, 'wt') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerow(question)
        csv_writer.writerows(answers)


def process_special_eb():
    # Go through all files in the directory
    for special_eb_file in os.listdir(dir_original_eb):

        # Open the file as a workbook
        workbook = xlrd.open_workbook(dir_original_eb + special_eb_file)

        # Go through each sheet of the workbook
        for sheet_name in workbook.sheet_names():
            sheet = workbook.sheet_by_name(sheet_name)

            # Filter out a sheet and extract its data to CSV if it contains one of the specified questions
            for question_short, sheet_interesting in sheets_interesting.items():
                if sheet_name in sheet_interesting:
                    extract_to_csv(special_eb_file, sheet, question_short)


process_special_eb()