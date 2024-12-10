import pytest
from farm_carbon_footprint import Farm

def test_add_activity():
    farm = Farm("Green Pastures", 10)
    farm.add_activity("Tractor Usage", 50, 5)  # 50 kg CO2e per hour, 5 hours
    farm.add_activity("Fertilizer Use", 10, 20)  # 10 kg CO2e per kg, 20 kg
    assert len(farm.activities) == 2

def test_total_emissions():
    farm = Farm("Green Pastures", 10)
    farm.add_activity("Tractor Usage", 50, 5)  # 50 kg CO2e per hour, 5 hours
    farm.add_activity("Fertilizer Use", 10, 20)  # 10 kg CO2e per kg, 20 kg
    assert farm.total_emissions() == 450  # 250 + 200

def test_emissions_per_hectare():
    farm = Farm("Green Pastures", 10)
    farm.add_activity("Tractor Usage", 50, 5)  # 50 kg CO2e per hour, 5 hours
    farm.add_activity("Fertilizer Use", 10, 20)  # 10 kg CO2e per kg, 20 kg
    assert farm.emissions_per_hectare() == 45  # 450 total / 10 hectares

def test_emissions_per_hectare_zero_area():
    farm = Farm("Tiny Farm", 0)
    farm.add_activity("Tractor Usage", 50, 2)  # 50 kg CO2e per hour, 2 hours
    with pytest.raises(ValueError, match="Farm area cannot be zero."): # optional: matches Value Error message in emissions_per_hectare()
        farm.emissions_per_hectare()

def test_radius_of_circle_with_farm_area():
    farm = Farm("Circle Farm", 1)
    assert farm.radius_circle_with_farm_area() == pytest.approx(56.38, abs=0.1)
    farm = Farm("Circle Farm", 10)
    assert farm.radius_circle_with_farm_area() == pytest.approx(178.3, abs=0.01)