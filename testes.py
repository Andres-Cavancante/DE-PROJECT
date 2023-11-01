import csv
import json

# Open the CSV file for reading
with open('input.csv', 'r') as csv_file:
    # Create a JSONL file for writing
    with open('output.jsonl', 'w') as jsonl_file:
        # Create a CSV reader
        csv_reader = csv.DictReader(csv_file)

        # Iterate through each row in the CSV and write as JSONL
        for row in csv_reader:
            json.dump(row, jsonl_file)
            jsonl_file.write('\n')