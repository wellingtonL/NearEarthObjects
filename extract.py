"""Functions to load the Nearth Earth Objects and Close Approaches from the data files."""

import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file. Create path to a CSV file containing data about near-Earth objects.
    Return:list of `NearEarthObject`s.'with' keyword used with the open does exception handling and closes the CSV file
    """
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
    """Read close approach data from a JSON file. Cad_json_path: A path to a JSON file containing data about close approaches.
    Return list of `CloseApproaches."""

    """Creating approach dictionary wth key map
        data dictionary loaded with keys "fields" key map & added it to list of close approaches"""
           
    approaches_list= [] 
    with open(cad_json_path, "r") as infile: #Assigning NEOs to Approachoaches_list = []  # Create an empty list to store CloseApproaches         
        json_file = json.load(infile)
        
        for row in json_file ['data']:
            approaches_list.append(CloseApproach(
            designation=row[0],  # designation is the first element in the row
            time=row[3],  # time is the fourth element in the row
            distance=float(row[4]),  # distance is the fifth element, convert to float
            velocity=float(row[7])  # velocity is the eighth element, convert to float
            ))
    return approaches_list


        


