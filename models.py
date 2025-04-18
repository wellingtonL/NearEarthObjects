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
    # TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        
        self.designation = info.get('designation') if info.get('designation') != '' else None
        self.name = str(info.get('name')) if info.get('name') else None
        self.time = cd_to_datetime(info.get('time'))  # TODO: Use the cd_to_datetime function for this attribute.
        self.diameter = float(info.get('diameter'))

        # If the diameter is not provided, set it to NaN.
        if self.diameter is None or math.isnan(self.diameter): self.diameter = float('nan')
        self.hazardous = info.get('hazardous')
        if self.hazardous:
            self.hazardous = self.hazardous.lower() == 'y'
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
            'potentially_hazardous': self.hazardous
        }

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # TODO: Use self.designation and self.name to build a fullname for this object.
        #self.fullname
        # If the name is None, return only the designation.
        #name = self.name
        if self.name is None:
            return f"{self.designation}"
        else:
            return f"{self.designation} ({self.name})"
        

    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        #hazard_status = 'is' if self.hazardous else 'is not'
        support_string = 'is' if not self.hazardous else 'is not'
        return f"NEO as {self.designation}, named {self.name} has diameter of {self.diameter:.3f} km and is {support_string} hazardous."
        
    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation='{self.designation!r}', name='{self.name!r}', " \
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
            "potentially_hazardous": self.hazardous,
        }
    

class CloseApproach:
    """A close approach to Earth by an NEO.

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
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """
        # TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        self._designation = info.get('designation','')  # The designation is initially a string.')
        if self._designation == '':  # The designation is initially a string.
            self._designation = None
        #self.time = info.get('time', None)  # The time is initially a string.
        if self.time:
            self.time = cd_to_datetime(self.time)  # Use the cd_to_datetime function for this attribute.
        self.distance = info.get('distance', float('nan'))
        self.velocity = info.get('velocity', float('nan'))       
        # Create an attribute for the referenced NEO, originally None.
        self.neo = None
        
   
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
        if not self.time:
            return ''
        return_value = f'Time: {datetime_to_str(self.time)}' 
        if self.neo:
            return_value += f'Name {self.neo.name} Designation {self.neo.designation}'
        return return_value# Updated to include formatted time
        
    def __str__(self):
        """Return `str(self)`."""
        # TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return (f"""A CloseApproach at {self.time_str!r}, {self.neo.fullname} approaches Earth """
                f"""at a distance of {self.distance:.2f} au and a velocity of"""
                f""" {self.velocity:.2f} km/s""")
    def __repr__(self):
        ("""Return 'repr(self)`, a computer-readable string representation of this object.""")
        return (f"CloseApproach(time={self.time_str!r},"
                f"distance={self.distance:.2f}, velocity={self.velocity:.2f},"
                f"neo={self.neo!r})")
    
    def serialize(self):
        """Return a dict representation of self attributes.
            Returns:
            [dict]: Keys associated with self attributes.
        """
        return {
            "datetime_utc": self.time.strftime('%Y-%m-%d %H:%M'),
            "distance_au": self.distance or float('nan'),
            "velocity_km_s": self.velocity or float('nan'),
        }