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
    
    with open(neo_csv_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        neos = []
            
        #file open() method then read using the DictReader for csv_file.
        for neo in reader: 
            neo['designation']= neo['pdes'] or ''
            neo['name'] = neo['name'] or None
            neo['diameter'] = float(neo['diameter']) if neo['diameter'] else None
            neo['pha'] = False if neo['pha'] in ['', 'N'] else True
            try:
                neo = NearEarthObject(
                    designation = neo['pdes'],
                    name = neo['name'],
                    diameter = neo['diameter'],
                    hazardous = neo['pha'],
                )
                
            except Exception as e:
                print(e)
            else:
                 neos.append(neo)
            
    return neos
    #except Exception as e:
    #   print("Error: Unexpected error not load! ", e)
        
    


def load_approaches(cad_json_path):
    """
    Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A list of `CloseApproaches.
    """
      
    with open(cad_json_path) as json_file:
        reader = json.load(json_file)
        reader = [dict(zip(reader['fields'], data)) for data in reader['data']]
        
        #fields = reader.get('fields')
        #data = reader.get('data')
        #self._designation_to_neo = {neo.designation: neo for neo in self._neos}
        #self._name_to_neo = {neo.name: neo for neo in self._neos if neo.name is not None}
                
        """
        for neo in fields, data:
            reader= [dict(zip(reader['fields'], data)) for data in reader['data']]
            #close_approaches.ap
            # append

            neo=CloseApproach(
                
                   designation=neo.get['des'],
                   time=neo.get['cd'],
                   distance=float(neo.get['dist']), #convert to float
                   velocity=float(neo.get['v_rel']), #convert to float
                )   
            close_approaches.append(neo)
            neo = neo
            #Assigning NEOs to CloseApproach
                        
                    
            
            # Creating close approach dictionary wth key map 
            #reader = [dict(zip(reader["fields"], data)) for data in reader["data"]]

            
            # Data dictionary loaded with keys "fields" key map & added it to list of close approaches"
                    
            
            #close_approaches.append(approach)
            #Assigning NEOs to CloseApproach
            """
        approaches = []
        for neo in reader:
            
                # Assigning NEOs to CloseApproach
                #approach = CloseApproach(
                #    designation=approach.get("des"),
                #    time=approach.get("cd"),
                #    distance=float(approach.get("dist")),
                #    velocity=float(approach.get("v_rel")),
                #)
                
                # Creating close approach dictionary wth key map 
                #reader = [dict(zip(reader["fields"], data)) for data in reader["data"]] 
            #close_approaches.append(approach)
            try:
                approach = CloseApproach(
                    
                    designation = neo['des'],
                    time = neo['cd'],
                    distance = float(neo['dist']),  # corrected to use 'dist'
                    velocity = float(neo['v_rel']),  # corrected to use 'v_rel'
                    #neo = neo['neo']  # Assigning NEOs to CloseApproach
                    )
                approaches.append(approach)
            except Exception as e:
                 print(e)    
        
                #return close_approaches  
        return approaches
    
        

