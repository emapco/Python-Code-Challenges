import csv
import pandas as pd
import numpy as np

# merges multiple CSV files into one utilizing pandas library
def merge_csv_files(input_files, output_file_path):
    input_dfs = [pd.read_csv(file, index_col=0) for file in input_files]
    if not input_dfs:
        return

    output_df = input_dfs[0]
    for i in range(1, len(input_dfs)):
        output_df = output_df.append(input_dfs[i], ignore_index=False).replace(np.NaN, pd.NA)
        # needed due to bug (up-casts ints to floats if column contains NaN but not if NA)
        for column in input_dfs[i]:
            if input_dfs[i][column].dtype.type in (np.int64, np.int32, np.int16, np.int8):
                output_df[column] = output_df[column].astype('Int64')

    output_df.to_csv(output_file_path)


def solution(csv_list, output_path):
    # build list with all fieldnames
    fieldnames = list()
    for file in csv_list:
        with open(file, 'r') as input_csv:
            fn = csv.DictReader(input_csv).fieldnames
            fieldnames.extend(x for x in fn if x not in fieldnames)

    # write data to output file base on field names
    with open(output_path, 'w', newline='') as output_csv:
        # object to write rows to csv (includes every field name specified)
        writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
        # write first header row to file
        writer.writeheader()

        for file in csv_list:
            with open(file, 'r') as input_csv:
                # create reader to read each row
                reader = csv.DictReader(input_csv)
                for row in reader:
                    # writes row to file and if data is not given for a field
                    # writer leaves it blank/empty
                    writer.writerow(row)
