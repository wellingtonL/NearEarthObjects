"""database encapsulating collections of near-Earth objects and their close approaches."""


class NEODatabase:
    """A database of near-Earth objects and their close approaches."""
    def __init__(self, neos, approaches):
        self._neos = neos
        self._approaches = approaches

        self.designation_map = {}
        self.name_map = {}

        for neo in self._neos:
            if neo.designation:
                self.designation_map[neo.designation] = neo
            if neo.name:
                #get_neo_by_name
                self.name_map[neo.name] = neo
        for approach in self._approaches:
            neo = self.designation_map[approach.designation]
            approach.neo = neo
            neo.approaches.append(approach)

    def get_neo_by_designation(self, designation):
        """Find & return an NEO by its primary designation.Not found 'None'."""
        return self.designation_map.get(designation) if designation else None

    def get_neo_by_name(self, name):
        """Find and return an NEO by its name. Return `None` if not found."""
        return self.name_map.get(name) if name else None

    def query(self, filters=()):
        """ Filters capturing user-specified criteria. Returns stream of matching objects."""
        for approach in self._approaches:
            flag = False in map(lambda f: f(approach), filters)
            if not flag:
                yield approach
