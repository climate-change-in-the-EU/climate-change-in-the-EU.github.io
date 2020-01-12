import csv
import os
import pandas as pd
import xlrd

# The names of the sheets with the questions we are interested in:
# "Which of the following do you consider to be the single most serious problem facing the world as a whole?"
# "And how serious a problem do you think climate change is at this moment?"
# "In your opinion, who within the EU is responsible for tackling climate change?"
# "Have you personally taken any action to fight climate change over the past six months?"
sheets_interesting = {'most_serious_problem': ['QA1a', 'QB1a', 'QC1a', 'QE1a1', 'QE1a', 'QD1a'],
                      'severity_of_problem': ['QA2.1', 'QA2', 'QB2', 'QC2', 'QE2a.1', 'QE2', 'QB2.1'],
                      'who_is_responsible': ['QA3', 'QB3', 'QC3'],
                      'personally_taken_action': ['QA5', 'QB5', 'QC5']}

# Directory for input/original data and output/processed data
dir_original_eb = 'original_data/special_eb/'
dir_processed_eb = 'processed_data/special_eb/data/'


def extract_all_to_csv(special_eb_file, sheet, question_short):
    """
    Extract the cells from a selected XLS sheet and write to CSV file
    """

    answers = []

    # Get the rows containing the answers (they always fill the sheet from row 8 until the last row)
    for i in range(8, sheet.nrows):
        # For the first row which contains the countries
        if i == 8:
            row_values = sheet.row_values(i)
            row_values[0] = 'question'
            row_values[1] = 'answer/countries'
            row_values.insert(0, 'source')
        else:
            row_values = sheet.row_values(i)
            row_values[0] = question_short
            row_values.insert(0, special_eb_file)
        answers.append(row_values)

    # Write to CSV file
    csv_filename = dir_processed_eb + '1_all_answers/' + question_short + '/' + special_eb_file + '_' + question_short + '.csv'
    with open(csv_filename, 'wt') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(answers)


def filter_interesting_sheets():
    """"
    Select the sheets with the questions we are interested in
    """

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
                    extract_all_to_csv(special_eb_file, sheet, question_short)


def filter_interesting_data():
    """
    Select the data needed for visualizations
    """

    for question_short in sheets_interesting.keys():

        if question_short == 'most_serious_problem':
            for special_eb_file in os.listdir(dir_processed_eb + '1_all_answers/' + question_short):
                csv_reader_filename = dir_processed_eb + '1_all_answers/' + question_short + '/' + special_eb_file

                rows = []

                with open(csv_reader_filename, 'r') as f:
                    csv_reader = csv.reader(f)
                    for i, row in enumerate(csv_reader):
                        if i == 0:
                            rows.append(row)
                        if i == 3:
                            row[2] += ' (percentage)'
                            rows.append(row)

                csv_writer_filename = dir_processed_eb + '2_selected_answers/' + question_short + '/' + special_eb_file + '_selection.csv'
                with open(csv_writer_filename, 'wt') as f:
                    csv_writer = csv.writer(f)
                    csv_writer.writerows(rows)


def combine_data():
    for question_short in os.listdir(dir_processed_eb + '2_selected_answers/'):
        dataframes = []
        combined_data = pd.DataFrame()

        for selected_data_csv in os.listdir(dir_processed_eb + '2_selected_answers/' + question_short):
            csv_read_filename = dir_processed_eb + '2_selected_answers/' + question_short + '/' + selected_data_csv
            dataframe = pd.read_csv(csv_read_filename)
            dataframes.append(dataframe)

        for df in dataframes:
            combined_data = combined_data.append(df, ignore_index=True, sort=False)

        csv_write_filename = dir_processed_eb + '3_final/' + question_short + '/' + 'special_eb_' + question_short + '_final.csv'
        combined_data.to_csv(csv_write_filename, index=None, header=True)


# Execute functions
filter_interesting_sheets()
filter_interesting_data()
combine_data()
