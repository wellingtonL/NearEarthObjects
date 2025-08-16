"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""

from helpers import cd_to_datetime, datetime_to_str
import math


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?,
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation='', name='', diameter=float('nan'), hazardous=''):
        
        """Create a new `NearEarthObject`.
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.

        
        self.designation = str(designation)
        if name.strip() == "":
            self.name = None
        else:
            # The name is initially a string.
             self.name = str(name)
        #self.time = cd_to_datetime(info.get('time'))  # TODO: Use the cd_to_datetime function for this attribute.
        try:
            self.diameter = float(diameter) 
        except  ValueError:
            self.diameter = float('nan')

        if hazardous.lower() == "y":
           self.hazardous = True # The hazardous status is initially a boolean.
        #if self.hazardous:
        #    self.hazardous = self.hazardous  # Convert to boolean.
        else:
            self.hazardous = False  
        # Create an empty initial collection of linked approaches.
        self.approaches = []
    
    def serialize(self):
        # write output in a readable format. For the dictionary NEO data
         return {
            'designation': self.designation,
            'name': self.name,
            'diameter': self.diameter, 
            'potentially_hazardous': self.hazardous,
        }

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # TODO: Use self.designation and self.name to build a fullname for this object.
        #self.fullname
        # If the name is None, return only the designation.
        #name = self.name
        if self.name is None:
            return f"{self.designation} ({self.name})"
        else:
            return f"{self.designation}"

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        #hazard_status = 'is' if self.hazardous else 'is not'
        """
        if not self.hazardous:
            hazard = 'is not'
        else: 
            hazard = 'is' 
        if math.isnan(self.diameter):
            diameter_string = 'diameter unknown' 
        else:
        diameter_string = f"diameter of {self.diameter:.3f} km"
        return f"NEO as {self.fullname} has {diameter_string} {hazard} potentially hazardous."
        """
        return f"NEO as '{self.fullname}' is a near Earth object with a diameter "\
                f"of {self.diameter:.3f} and {'is' if self.hazardous else 'is not'} hazardous."



    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, " \
               f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")
    
    def serialize(self):
        """Return a dict representation of self attributes.
           
           Returns:
               [dict]: Keys associated with self attributes.
        """
        return {
            "designation": self.designation or '',
            "name": self.name or '',
            "diameter_km": self.diameter or float('nan'),
            "hazardous": self.hazardous,
        }
    

class CloseApproach:
    """
    A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation='', time='', distance=float('nan'), velocity=float('nan'),neo= None):
        """
        Create a new `CloseApproach`.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self.designation = designation if designation else '' # The designation is initially a string.
        #if self.designation == '':  # The designation is initially a string.
        #    self.designation = None
        self.time = cd_to_datetime(time) if (time) else None  # Use the cd_to_datetime function for this attribute.
        try:
            self.distance = float(distance) 
        except ValueError:
            self.distance = float('nan')  # The distance is initially a float.nanone
        try:
            self.velocity = float(velocity)
        except ValueError:
            self.velocity = float('nan')  # The velocity is initially a float.nanone    
        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo
    @property
    def fullname(self):    
        """
        Return a formatted representation of this `CloseApproac h`'s full name.
        """
        #if self.neo:
        return f"{self.designation} ({self.neo.name or 'N/A'})"
    
        
    def serialize(self):
        """
        Return a dict representation of self attributes.
            Returns:
            [dict]: Keys associated with self attributes.
        """
        return {
            "datetime_utc":self.time.strftime("%Y-%m-%d %H:%M"),
            "distance_au": self.distance or float('nan'),
            "velocity_km_s": self.velocity or float('nan'),
            'neo': {
                'designation': self.neo.designation,
                'name': self.neo.name,
                'diameter_km': self.neo.diameter,
                'potentially_hazardous': self.neo.hazardous
            },
        }
        return result

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # TODO: Use self.designation and self.name to build a fullname for this object.
        #if not self.time:
         #  return ''
        str_time = datetime_to_str(self.time) if self.time else ''
        #if self.neo:
        #    str_time += f' Name: {self.neo.name}, Designation: {self.neo.designation}'
        return str_time
     
              
    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"A CloseApproach at {self.time_str},  '{self.neo.fullname}' approaches Earth "\
                 f"at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s." 
    def __repr__(self):
        """Return 'repr(self)`, a computer-readable string representation of this object."""
        return f"CloseApproach(time= {self.time_str!r}, distance={self.distance:.2f}, "\
                f"velocity={self.velocity:.2f}, neo={self.neo!r})"
    
    