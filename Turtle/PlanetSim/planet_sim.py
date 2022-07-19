from sun import Sun
from solar_system import SolarSystem
from planet import Planet


# Create a SolarSystem
solar_sys = SolarSystem(2, 2)

# Create sun
sun = Sun('Sun', 5000, 40, 1000)
solar_sys.add_sun(sun)

# Create planets
p = Planet('Mercury', 1, 500, 0.15, (0, 2), 'black')
solar_sys.add_planet(p)
p = Planet('Venus', 1, 500, 0.25, (0, 2), 'purple')
solar_sys.add_planet(p)
p = Planet('Earth', 1, 700, 0.5, (0, 2), '#2152a6')
solar_sys.add_planet(p)
p = Planet('Mars', 1, 700, 0.6, (0, 2), '#b32b10')
solar_sys.add_planet(p)

solar_sys.show_planets()

num_time_periods = 1000
for _ in range(num_time_periods):
    solar_sys.move_planets()

solar_sys.freeze()