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
"""

from helpers import cd_to_datetime, datetime_to_str


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor."""

    def __init__(self, designation='', name='', diameter=float('nan'), hazardous=''):
        """Create a new `NearEarthObject`.
        :param info: A dictionary of excess keyword arguments supplied to the constructor.
        """

        self.designation = str(designation) if designation else None
        self.name = str(name) if name else None
        self.diameter = float(diameter) if diameter else float('nan')
        self.hazardous = True if hazardous.lower() == "y" else False

        # empty initial collection of linked approaches.
        self.approaches = []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        #Use self.designation and self.name to build a fullname for the object.
        # If the name is None, returns only the designation.
        if self.name is None:
            return f"{self.designation}"
        else:
            return f"{self.designation} ({self.name})"
                                
    def __str__(self):
        """Return `str(self)`."""
        #attributes returns a readable string representation. Look at the __repr__
        #hazard_status = 'is' if self.hazardous else 'is not':
        if self.hazardous:
            return f"NEO as {self.fullname} has a diameter "\
                f"of {self.diameter:.3f} and is potentially hazardous."
        else:
            return f"NEO as {self.fullname} has a diameter "\
                f"of {self.diameter:.3f} and is not potentially hazardous."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return f"NearEarthObject({self.designation!r}, {self.name!r}, " \
               f"{self.diameter:.3f}, {self.hazardous!r})"


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
    def __init__(self, designation='', time='', distance=float('nan'), velocity=float('nan'), neo=None):
        """ Create a new `CloseApproach`."""
        #Info arguments passed to constructor onto attributes. Values to match data types.

        self.designation = str(designation) if designation else None  #initially a string.
        self.time = cd_to_datetime(time) if time else None #cd_to_datetime function attribute.
        if not isinstance(distance, (float, int)):
            raise TypeError("Distance must be a float or int.")
        self.distance = float(distance)
        if not isinstance(velocity, (float, int)):
            raise TypeError("Velocity must be a float or int.")
        self.velocity = float(velocity)
        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.
        object's `self.time` and `datetime_to_str` representation of approach time.
        Use self.designation and self.name to build a fullname for this object."""

        str_time = datetime_to_str(self.time) if self.time else ''
        return str_time
        #return datetime_to_str(self.time)


    def __str__(self):
        """Return `str(self)`string representation."""

        return f"A CloseApproach at {self.time_str},  '{self.neo.fullname}' approaches Earth "\
                 f"at a distance of {self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."

    def __repr__(self):
        """Return 'repr(self)`,readable string representation of this object."""
        return f"CloseApproach(time= {self.time_str!r}, distance={self.distance:.2f}, "\
                f"velocity={self.velocity:.2f}, neo={self.neo!r})"
