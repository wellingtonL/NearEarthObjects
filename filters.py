"""Provide filters for querying close approaches and limit the generated results.
`create_filters` function produces a collection of objects used by
the `query` method to generate a stream of `CloseApproach` objects that match
criteria. The arguments to `create_filters` are provided by
the main module and originate from the user's command-line options.

This function returns a collection of instances of subclasses
of `AttributeFilter` - a 1-argument callable (on a `CloseApproach`) constructed
from a comparator (from the `operator` module), a reference value, and a class
method `get` that subclasses can override to fetch an attribute of interest from
the supplied `CloseApproach`.

The `limit` function simply limits the maximum number of values produced by an
iterator.
"""

import operator
from itertools import islice


class UnsupportedCriterionError(NotImplementedError):
    """A filter criterion is unsupported."""

    
class AttributeFilter:
    """superclass for filters on comparable attributes.
    `AttributeFilter` search criteria pattern comparing some
    attribute of a close approach (or its attached NEO) to a reference value. A   callable predicate for a `CloseApproach`
    object satisfies the encoded criterion.

    A comparator operator and a reference value, and
    calling the filter (with __call__) executes `get(approach) OP value` (in
    infix notation).

    Concrete subclasses can override the `get` classmethod to provide custom
    behavior to fetch a desired attribute from the given `CloseApproach`.
    """
    
    def __init__(self, op, value):
        """Construct a `AttributeFilter` from an binary predicate and a reference value.
        Refer value will be supplied as the second (right-hand side)
        argument to the operator function. example, an `AttributeFilter`
        with `op=operator.le` and `value=10`, when called on an approach,
        evaluate `some_attribute <= 10`.
        """
        self.op = op
        self.value = value

    def __call__(self, approach):
        """Invoke `self(approach)`."""
        return self.op(self.get(approach), self.value)

    @classmethod
    def get(cls, approach):
        """Get an attribute of interest from a close approach.Subclasses must override this method to get an attribute of
        interest from the supplied `CloseApproach`, on which to evaluate this filter.
        Return: The value of an attribute of interest, comparable to `self.value` via `self.op`.
        """
        raise UnsupportedCriterionError

    def __repr__(self):
        return f'{self.__class__.__name__}(op=operator.{self.op.__name__}, value={self.value})'
    

class DateFilter(AttributeFilter):
    """A concrete `AttributeFilter` for the `date` attribute."""
    @classmethod
    def get(cls, approach):
        """Return approach.time converted to datetime.datetime object for the date filter.
        A CloseApproach object. Returns[datetime.datetime]: Convert time to datetime object.
        """
        return approach.time.date() 
    
     
class DistanceFilter(AttributeFilter): 
    """`AttributeFilter` for the `distance` attribute."""
    classmethod
    def get(cls, approach):
        """Return distance of the CloseApproach object for filter.Returns: the distance of a CloseApproach.""" 
        return approach.distance
  
    
class VelocityFilter(AttributeFilter):
    """A concrete `AttributeFilter` for the `velocity` attribute."""
    @classmethod
    def get(cls, approach):
        """A concrete `AttributeFilter` for the `velocity` attribute. Args: A CloseApproach object. Arg:Returns the velocity of a CloseApproach."""    
        return approach.velocity
    
        
class DiameterFilter(AttributeFilter):
    """A concrete `AttributeFilter` for the `diameter` attribute."""
    @classmethod
    def get(cls, approach): 
        return approach.neo.diameter 
    
      
class HazardousFilter(AttributeFilter):
    """A concrete `AttributeFilter` for the `hazardous` attribute."""
    @classmethod
    def get(cls, approach):
        """Return whether the NEO is hazardous for the hazardous filter.
        Args:approach a CloseApproach object. Returns:[bool]: Returns whether the NEO is hazardous.
        """
        return approach.neo.hazardous 

    
def create_filters(date=None, start_date=None, end_date=None, distance_min=None, distance_max=None,
                       velocity_min=None, velocity_max=None, diameter_min=None, diameter_max=None, hazardous=None):
    """Created a collection of filters from user-specified criteria.
    Each arguments is provided by the main module with a value from the
    user's options at the command line. 
    The return value must be compatible with the `query` method of `NEODatabase`
    because the main module directly passes this result to that method. A collection of `AttributeFilter`s.
    """  
    
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
    `n` is 0 or None, doesn't limit the iterator.
    n: The maximum number of values to produce.
    yields: The first (at most) `n` values from the iterator.
    """
    if n == 0 or n is None:
        return islice(iterator, None)
    else:
        return islice(iterator, n)
       
    