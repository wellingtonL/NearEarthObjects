
"""
Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json
from helpers import cd_to_datetime, datetime_to_str
from datetime import datetime, timezone


def write_to_csv(results, filename):
    """
    Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a CSV file, following the specification in the instructions.

    fieldnames = (
        'datetime_utc', 'distance_au', 'velocity_km_s',
        'designation', 'name', 'diameter_km', 'potentially_hazardous')
    
    with open(filename,'w') as csv_outfile:
        writer_csv = csv.writer(csv_outfile)
        writer_csv.writerow(fieldnames)
        for approach in results:
            row=[
                approach.time,
                approach.distance,
                approach.velocity,
                approach.neo.designation,
                approach.neo.name,
                approach.neo.diameter,
                approach.neo.hazardous
                ]
            writer_csv.writerow(row)

def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    # TODO: Write the results to a JSON file, following the specification in the instructions.
    try:
        results_outfile= []
        for approach in results:
            
            row = {
                'datetime_utc': approach.time_str,
                'distance_au': approach.distance,
                'velocity_km_s': approach.velocity,
                'neo': {
                    'designation': approach.neo.designation,
                    'name': approach.neo.name,
                    'diameter_km': approach.neo.diameter,
                    'potentially_hazardous': approach.neo.hazardous
                }
            }
            results_outfile.append(row)
        json_object=json.dumps(results_outfile, indent=4)

        with open(filename, 'w') as json_outfile:
            json_outfile.write(json_object)
            
    except Exception as e:
        print(f"Error writing JSON to {filename}: {e}")
