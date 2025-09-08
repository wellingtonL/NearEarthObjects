"""filters to query and 'limit' max results.
query` method to generate sstream of `CloseApproach` objects that match. Arguments
from main module and user's command-line options.

Function returns a collection of instances of subclasses
of `AttributeFilter` - a 1-argument callable (on a `CloseApproach`) constructed
from a comparator (from the `operator` module), a reference value, and a class
method `get` that subclasses can override to fetch an attribute of interest from
the supplied `CloseApproach`."""

import operator
from itertools import islice


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""

class AttributeFilter:
    """superclass for filters on attributes."""

    def __init__(self, op, value):
        self.op = op
        self.value = value

    def __call__(self, approach):
        """Invoke `self(approach)`."""
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        """Get an attribute of interest from a close approach. Subclass to evaluate this filter."""
        raise UnsupportedCriterionError

    def __repr__(self):
        return f'{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})'

class DateFilter(AttributeFilter):
    """A concrete `AttributeFilter` for the `date` attribute."""
    @classmethod
    def get(cls, approach):
        """Return approach.time converted to datetime.datetime object for the date filter.
        A CloseApproach object. Returns[datetime.datetime]: Convert time to datetime object."""
        return approach.time.date()

class DistanceFilter(AttributeFilter):
    """`AttributeFilter` for the `distance` attribute."""
    @classmethod
    def get(cls, approach):
        """Return distance of the CloseApproach object for filter.""" 
        return approach.distance

class VelocityFilter(AttributeFilter):
    """A concrete `AttributeFilter` for the `velocity` attribute."""
    @classmethod
    def get(cls, approach):
        """A concrete `AttributeFilter` for the `velocity` attribute."""    
        return approach.velocity

class DiameterFilter(AttributeFilter):
    """A concrete `AttributeFilter` for the `diameter` attribute."""
    @classmethod
    def get(cls, approach):
        return approach.neo.diameter

class HazardousFilter(AttributeFilter):
    """`AttributeFilter` for the `hazardous` attribute."""
    @classmethod
    def get(cls, approach):
        """Return whether the NEO is hazardous for filter."""
        return approach.neo.hazardous

def create_filters(date=None, start_date=None, end_date=None,
                   distance_min=None, distance_max=None,
                   velocity_min=None, velocity_max=None,
                   diameter_min=None, diameter_max=None,
                   hazardous=None):

    filters = []

    for key, value in locals().items():
        if key.lower() == 'date' and value:
            filters.append(DateFilter(operator.eq, value))

        elif key.lower() == 'start_date' and value:
            filters.append(DateFilter(operator.ge, value))

        elif key.lower() == 'end_date' and value:
            filters.append(DateFilter(operator.le, value))

        elif key.lower() == 'distance_min' and value:
            filters.append(DistanceFilter(operator.ge, value))

        elif key.lower() == 'distance_max' and value:
            filters.append(DistanceFilter(operator.le, value))

        elif key.lower() == 'velocity_min' and value:
            filters.append(VelocityFilter(operator.ge, value))

        elif key.lower() == 'velocity_max' and value:
            filters.append(VelocityFilter(operator.le, value))

        elif key.lower() == 'diameter_min' and value:
            filters.append(DiameterFilter(operator.ge, value))

        elif key.lower() == 'diameter_max' and value:
            filters.append(DiameterFilter(operator.le, value))

        elif key.lower() == 'hazardous' and value is not None:
            filters.append(HazardousFilter(operator.eq, value))

    return filters

def limit(iterator, n=None):
    """Produces a limited stream of values from an iterator.
    `n` is 0 or None, doesn't limit the iterator."""
    if n == 0 or n is None:
        return islice(iterator, None)
    return islice(iterator, n)
