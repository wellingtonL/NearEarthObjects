"""Functions to load the Nearth Earth Objects and Close Approaches from the data files."""

import csv
import json
from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    # if condition returns False, AssertionError is raised:
    
    """
    Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A list of `NearEarthObject`s.
    THE 'with' keyword used with the open does exception handling and closes the CSV file
    """
    try:
        with open(neo_csv_path, 'r') as file:
            # using 'reader' as a varible name
            reader = csv.DictReader(file)
                       
             #file open() method then read using the DictReader for csv_file.

            neos = []
            for row in reader:
                designation = row.get('pdes')
                name = row.get('name') 
                diameter = float('nan' if row.get('diameter') =='' else row.get('diameter'))
                hazardous = bool(True if row.get('pha') == 'Y' else False)
                neo = NearEarthObject(
                        designation=designation,
                        name = name if name != '' else None,
                        diameter = diameter,
                        hazardous=hazardous
                    )
        
    except Exception as e:
       print("Error: Unexpected error not load! ", e)
    
    neos.append(neo)
    return neos


def load_approaches(cad_json_path):
    """
    Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A list of `CloseApproaches.
    """
             
    try:
        with open(cad_json_path) as f:
            reader = json.load(f)

        fields = reader.get("fields")
        data = reader.get("data")
        # elf._designation_to_neo = {neo.designation: neo for neo in self._neos}
        # self._name_to_neo = {neo.name: neo for neo in self._neos if neo.name is not None}
        reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]
      
        approaches = []
        with open(cad_json_path, 'r') as file:
            data = json.load(file)
            # for approach in reader:
            for approach in data["data"]:
                approach = CloseApproach(
                designation=approach.get("des"),
                time=approach.get("cd"),
                distance=float(approach.get("dist")),
                velocity=float(approach.get("v_rel")),
            )
                approaches.append(approach)               
            # Creating close approach dictionary wth key map 
            #reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]

            
            # Data dictionary loaded with keys "fields" key map & added it to list of close approaches"
            
             
            # CloseApproach 
            """        
            for approach in reader:
                neo_approaches.append(
                    CloseApproach(
                        designation=approach.get("des"),
                        time=approach.get("cd"),
                        distance=float(approach.get("dist")),
                        velocity=float(approach.get("v_rel")),
                    )
                )
                # Assigning NEOs to CloseApproach
                if approach.get("des") in self._designation_to_neo.keys():
                    approach.neo = self._designation_to_neo[approach.get("des")]
                    self._designation_to_neo[approach.get("des")].approaches.append(approach)
                elif approach.get("name") in self._name_to_neo.keys():
                    approach.neo = self._name_to_neo[approach.get("name")]
                    self._name_to_neo[approach.get("name")].approaches.append(approach)
                else:
                    continue"
                """
            
        
    except Exception as e:
        print('Error: Unexpected error file not load!!',e )           
        return approaches
        
