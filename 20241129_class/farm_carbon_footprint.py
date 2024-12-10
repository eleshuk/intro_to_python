import math

class Farm:
    def __init__(self, name, area_hectares):
        """Initialize the farm with a name and area in hectares."""
        self.name = name
        self.area_hectares = area_hectares
        self.activities = []

    def add_activity(self, activity, emissions_per_unit, units):
        """Add an activity with emissions in kg CO2e per unit and units."""
        self.activities.append((activity, emissions_per_unit, units))

    def total_emissions(self):
        """Calculate total carbon emissions from all activities."""
        return sum(emissions_per_unit * units for _, emissions_per_unit, units in self.activities)

    def emissions_per_hectare(self):
        """Calculate carbon emissions per hectare."""
        if self.area_hectares == 0:
            raise ValueError("Farm area cannot be zero.")
        return self.total_emissions() / self.area_hectares

    def radius_circle_with_farm_area(self):
        """ Calculate the radius (in meters) of a circle that has the same area as the farm"""
        return(math.sqrt(self.area_hectares/3.1459)*100)