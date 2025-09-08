"""Functions to load the Nearth Earth Objects and Close Approaches from the data files."""

import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """NEO information from a CSV file. Path to CSV file NEOS.
    Return:list NEOS'with' keyword used with open does err handling and closes"""

    neo_list = []  # Create an empty list to store NEOs
    with open(neo_csv_path, 'r') as f:
        csv_reader = csv.DictReader(f)
        #file open() method then read using the DictReader for csv_file.
        for row in csv_reader:
            neo_list.append(NearEarthObject(
                designation=row['pdes'],
                name=row['name'],
                diameter=float(row['diameter']) if row['diameter'] else float('nan'),
                hazardous=row['pha']  # convert to boolean
                ))
    return neo_list


def load_approaches(cad_json_path):
    """Read data JSON file. Cad_json_path: path to file containing data about close approaches."""

    approaches_list = []
    with open(cad_json_path, "r") as infile:
        json_file = json.load(infile)

        for row in json_file['data']:
            approaches_list.append(CloseApproach(
            designation=row[0],  # designation is the first element in the row
            time=row[3],  # time is the fourth element in the row
            distance=float(row[4]),  # distance is the fifth element, convert to float
            velocity=float(row[7]),  # velocity is the eighth element, convert to float
            ))
    return approaches_list
