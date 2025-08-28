"""database encapsulating collections of near-Earth objects and their close approaches."""


class NEODatabase:
    """A database of near-Earth objects and their close approaches."""
        
    def __init__(self, neos, approaches):
        """`NEODatabase`, for collections of NEOs and close approaches. 
        constructor modifies them to link them."""
           
        self._neos = neos
        """parameter for collection of `NearEarthObject`s."""
         
        self._approaches = approaches
        """parameter for collection of `CloseApproach`es."""
        
        self.designation_map = {}
        self.name_map = {}

        for neo in self._neos:
            if neo.designation:
                self.designation_map[neo.designation] = neo
            if neo.name:
                #get_neo_by_name
                self.name_map[neo.name] = neo
                
        # Link each approach to its corresponding near-Earth object.
        for approach in self._approaches:
            #if approach.designation in map
                neo = self.designation_map[approach.designation]
                approach.neo = neo
                neo.approaches.append(approach)
                                 
        """Link together the NEOs and their close approaches."""
                
    def get_neo_by_designation(self, designation):
        """Find & return an NEO by its primary designation.Not found 'None'."""
        return self.designation_map.get(designation) if designation else None
    
    def get_neo_by_name(self, name):    
        """Find and return an NEO by its name. Return `None` if not found.
        Not every NEO in the data set has a name.Name as a string 
        return-The `NearEarthObject` with the desired name, or `None`"""
        return self.name_map.get(name) if name else None
        
    def query(self, filters=()):
        """Query close approaches to generate those that match a collection of filters generates a stream of `CloseApproach` objects that match 
        Filters capturing user-specified criteria. Returns stream of matching objects.
        """
        for approach in self._approaches:
            if all(map(lambda f: f(approach), filters)):
                yield approach
            else:
                for approach in self._approaches:
                    yield approach
