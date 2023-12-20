## CODING CHALLENGE
# 25 MARKS
"""
A] Design a parent class called Planet

It must have:
- General attributes: name, distance_from_sun, planet_type
- A get_distance_to_earth() method that gives you the absolute distance from the Earth.

!!! You can take the distance from the Sun to the Earth as 147 million kilometres !!!

For example, if the planet’s distance_from_sun was 148 million kilometres when you call the get_distance_from_earth()
method, it should give us the distance like this: {'distance to earth’': 1000000} where the implied unit is kilometres.
This means that the planet is 1 million kilometres away from Earth.

   > This question uses an oversimplification of the solar system model, not taking into account orbit position or the
    eccentricity of the orbit, so in reality the result will be an approximate value with a reasonable margin of error.
"""

class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    distance_earth_sun = 147000000 # Absolute distance from Sun to Earth
    def get_distance_to_earth(self):
        distance_to_earth = abs(self.distance_from_sun - self.distance_earth_sun)

        # Return the distance of any planet to Earth
        return {'distance_to_earth': distance_to_earth}

"""
B] Design a child class called Mercury, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class,
Your child class should also have a static method called happy_new_year(), which
would give us the information on how long a year lasts on the planet (in whatever way you wish!). 
You can take Earth Days as the implied unit.

After, create a Mercury object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT MERCURY !!!
Distance from Sun: 58 million
Planet Type: Terrestrial
Time taken for the planet to orbit the sun: 88 Earth days
!!!!!!!!!!!!!!!!!!!!

"""

class Mercury(Planet):
    def __init__(self, name, distance_from_sun=58000000, planet_type="Terrestrial"):
        super().__init__(name, distance_from_sun, planet_type)

    @staticmethod
    def happy_new_year():
        mercury_year_long = 88 # since Mercury takes 88 days to orbit the Sun an earth year is 88 days
        return f"A year in Mercury lasts {mercury_year_long} days!"

# Creating a Mercury object
mercury_planet = Mercury(name="Mercury")

## TEST CASE
print(mercury_planet.name) # It should give us "Mercury" as defined in the object
print(mercury_planet.distance_from_sun) # It should give us 58000000
print(mercury_planet.planet_type) # It should give us Terrestrial
print(mercury_planet.happy_new_year()) # It should give us 88 days
print(mercury_planet.get_distance_to_earth()) # Calculates distance to Earth which is 147 minus 58 million kilometers


"""
C] Design a child class called Jupiter, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class, as well as the additional attribute 
number_of_moons.
Your child class should also have a static method called happy_new_year(), which would give us the information on how 
long a year lasts on the planet (in whatever way you wish!). You can take Earth Days as the implied unit.

After, create a Jupiter object and print out the value of all its attributes and methods.


!!! HELPFUL INFO ABOUT JUPITER !!!
Distance from Sun: 779 million
Planet Type: Gas Giant
Time taken for the planet to orbit the sun: 4383 Earth days
Number of Moons: 80
!!!!!!!!!!!!!!!!!!!!

"""

class Jupiter(Planet):
    def __init__(self, name, distance_from_sun=779000000, planet_type="Gas Giant", number_of_moons=80):
        super().__init__(name, distance_from_sun, planet_type)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        jupiter_year_long = 4383 # since Jupiter takes 88 days to orbit the Sun an earth year is 4383 days
        return f"A year in Jupiter lasts {jupiter_year_long} days!"

# Creating a Jupiter object
jupiter_planet = Jupiter(name="Jupiter")

## TEST CASE
print(jupiter_planet.name) # It should give us "Jupiter" as defined in the object
print(jupiter_planet.distance_from_sun) # It should give us 7790000000
print(jupiter_planet.planet_type) # It should give us Gas Giant
print(jupiter_planet.happy_new_year()) # It should give us 4383 days
print(jupiter_planet.number_of_moons) # It should give us 80
print(jupiter_planet.get_distance_to_earth()) # Calculates distance to Earth which is 779 minus 147 million kilometers


