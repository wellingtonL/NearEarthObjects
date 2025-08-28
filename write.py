
"""Stream of close approaches to CSV or to JSON.
Module exports two functions: `write_to_csv` and `write_to_json`, each
accepts `results` stream of close approaches and a path to
write the data.

The functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used."""

import csv
import json

from helpers import cd_to_datetime, datetime_to_str
from datetime import datetime, timezone


def write_to_csv(results, filename):
    """an iterable of `CloseApproach` objects to a CSV file. Each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.
    The param name: A Path-like object points where the data should be saved.
   
    Writes results to a CSV file, following specification in instructions."""

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

    Writes list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes. Iterable of `CloseApproach` objects.
    Paramname is Path-like object pointing to where the data should be saved.
    """
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
