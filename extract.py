"""Functions to load the Nearth Earth Objects and Close Approaches from the data files."""

import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """
    Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A list of `NearEarthObject`s.
    THE 'with' keyword used with the open does exception handling and closes the CSV file
    """
    try:
        with open(neo_csv_path) as csv_file:
            # using 'reader' as a varible name
            reader = csv.DictReader(csv_file)
            
             #file open() method then read using the DictReader for csv_file.

            neos = []
            for neo in reader:
                neos.append(
                    NearEarthObject(
                        **{
                            'designation':
                            neo.get('pdes', ''),
                            'name':
                            neo.get('name') if neo.get('name') != '' else None,
                            'diameter':
                            float('nan' if neo.get('diameter') ==
                                  '' else neo.get('diameter')),
                            'hazardous':
                            bool(True if neo.get('pha') == 'Y' else False)
                        }))
            return neos
    except Exception as e:
        print(f"Error: Unexpected error csv not load! , {e}")


def load_approaches(cad_json_path):
    """
    Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A list of `CloseApproaches.
    """
    try:
        with open(cad_json_path) as json_file:
            reader = json.load(json_file)

            # Get the fields and data for the close approaches
            fields = reader.get('fields')
            data = reader.get('data')

            close_approaches = []
            for approach in data:
                # Creating close approach dictionary wth key map
                close_approach = {
                    fields[index]: value
                    for index, value in enumerate(approach)
                }
                # Data dictionary loaded with keys "fields" key map & added it to list of close approaches
                close_approaches.append(
                    CloseApproach(
                        **{
                            'designation': close_approach.get('des'),
                            'time': close_approach.get('cd'),
                            'distance': float(close_approach.get('dist')),
                            'velocity': float(close_approach.get('v_rel'))
                        }))

        return close_approaches
    except Exception as e:
        print('Error: Unexpected error csv_file not load!!', e)