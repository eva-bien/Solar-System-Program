import unittest
from solar_system import Planet, Moon

class PlanetTest(unittest.TestCase):
    def setUp(self):
        self.planet = Planet("Earth", 5.97217e24, (0.98, 1.02), [Moon("The Moon")])

    def test_planet_is_initialized_correctly(self):
        # I found online that pytest recommend I use the test methods passed in by the unit test import.
        # This link provides more info: https://docs.python.org/3/library/unittest.html
        self.assertEqual(self.planet.name, "Earth")
        self.assertEqual(self.planet.mass, 5.97217e24)
        self.assertEqual(self.planet.distance_from_the_sun[0], 0.98)
        self.assertEqual(self.planet.distance_from_the_sun[1], 1.02)
        self.assertEqual(len(self.planet.moons), 1)
        self.assertEqual(self.planet.moons[0].name, "The Moon")

    def test_convert_mass_is_formatted_correctly(self):
        result = self.planet.convertMass(self.planet.mass)
        self.assertEqual(result, "5.97217 x 10^24 kg")   

    def test_convert_mass_rounds_up_correctly(self):
        result = self.planet.convertMass(5.972178e24)
        self.assertEqual(result, "5.97218 x 10^24 kg")  

    def test_convert_mass_rounds_down_correctly(self):
        result = self.planet.convertMass(5.972173e24)
        self.assertEqual(result, "5.97217 x 10^24 kg")  
        

if __name__ == "__main__":
    unittest.main()