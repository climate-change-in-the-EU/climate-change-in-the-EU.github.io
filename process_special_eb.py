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
# TODO: QB5 from special_eb_322 is not usable because it is a differently worded question/answers,
#  but this sheet name is correct for special_eb_490

# Directory for input/original data and output/processed data
dir_original_eb = 'original_data/special_eb/'
dir_processed_eb = 'processed_data/special_eb/data/'


def extract_to_csv(special_eb_file, sheet, question_short):
    """
    Helper function to extract cells from a selected XLS sheet and write them to a CSV file
    """

    answers = []

    # Get the rows containing the answers (they always fill the sheet from row 8 until the last row)
    for i in range(8, sheet.nrows):
        # For the first row which contains the countries, insert headings for more columns
        if i == 8:
            row_values = sheet.row_values(i)
            row_values[0] = 'question'
            row_values[1] = 'answer/countries'
            row_values.insert(0, 'source')
        # Add the file it was taken from and short form of the question to each row
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


def write_to_csv(output_path, data):
    with open(output_path, 'wt') as f:
        csv_writer = csv.writer(f)
        csv_writer.writerows(data)


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
                    extract_to_csv(special_eb_file, sheet, question_short)


def filter_interesting_data():
    """
    Process the files depending on the table structure of the question they are about and the part of the data
    needed for the visualizations, i.e. take only specific rows from the CSV file
    """

    # Go through all sub-directories in the directory
    for question_short in os.listdir(dir_processed_eb + '1_all_answers/'):

        # Go through all files in the directory
        for all_data_csv in os.listdir(dir_processed_eb + '1_all_answers/' + question_short):
            csv_reader_filename = dir_processed_eb + '1_all_answers/' + question_short + '/' + all_data_csv
            csv_writer_filename = dir_processed_eb + '2_selected_answers/' + question_short + '/' + all_data_csv + '_selection.csv'

            # Wanted from this question: the percentage of respondents from each country who said "climate change"
            if question_short == 'most_serious_problem':
                rows = []
                with open(csv_reader_filename, 'r') as f:
                    csv_reader = csv.reader(f)
                    for i, row in enumerate(csv_reader):
                        if i == 0:
                            rows.append(row)
                        if i == 3:
                            row[2] += ' (percentage)'
                            rows.append(row)

                # Write to CSV file
                write_to_csv(csv_writer_filename, rows)

            # Wanted from this question: the average rating given by the respondents from each country
            elif question_short == 'severity_of_problem':
                rows = []
                with open(csv_reader_filename, 'r') as f:
                    csv_reader = csv.reader(f)
                    last_row = []
                    for i, row in enumerate(csv_reader):
                        if i == 0:
                            rows.append(row)
                        else:
                            last_row = row
                            last_row[2] = 'Average'
                    rows.append(last_row)

                write_to_csv(csv_writer_filename, rows)

            # Wanted from this question: the percentage of respondents from each country for the five main answers
            elif question_short == 'who_is_responsible':
                rows = []
                with open(csv_reader_filename, 'r') as f:
                    csv_reader = csv.reader(f)
                    for i, row in enumerate(csv_reader):
                        if i == 0:
                            rows.append(row)
                        if i in [3, 5, 9, 11, 13]:
                            row[2] += ' (percentage)'
                            rows.append(row)

                write_to_csv(csv_writer_filename, rows)

            # Wanted from this question: the percentage of respondents from each country who said "yes"
            elif question_short == 'personally_taken_action':
                rows = []
                with open(csv_reader_filename, 'r') as f:
                    csv_reader = csv.reader(f)
                    for i, row in enumerate(csv_reader):
                        if i == 0:
                            rows.append(row)
                        if i == 3:
                            row[2] += ' (percentage)'
                            rows.append(row)

                write_to_csv(csv_writer_filename, rows)


def combine_data():
    """
    Combine each question's data into a single file
    """

    # Go through all sub-directories in the directory
    for question_short in os.listdir(dir_processed_eb + '2_selected_answers/'):
        dataframes = []
        combined_data = pd.DataFrame()
        csv_write_filename = dir_processed_eb + '3_final/' + question_short + '/' + 'special_eb_' + question_short + '_final.csv'

        # Go through all files in the directory
        for selected_data_csv in os.listdir(dir_processed_eb + '2_selected_answers/' + question_short):
            csv_read_filename = dir_processed_eb + '2_selected_answers/' + question_short + '/' + selected_data_csv

            # Read the CSV file into a Pandas DataFrame; store DataFrames in a list
            dataframe = pd.read_csv(csv_read_filename)
            dataframes.append(dataframe)

        # Combine all DataFrames into one, Pandas takes into account the sometimes differing columns between them
        for df in dataframes:
            combined_data = combined_data.append(df, ignore_index=True, sort=False)

        # Write the DataFrame to a CSV file
        combined_data.to_csv(csv_write_filename, index=None, header=True)


# Execute functions
filter_interesting_sheets()
filter_interesting_data()
combine_data()
