import constants as con
from gravity import get_local_gravity

class Location:
    """
    A class to represent a location, with properties that can be used to calculate atmospheric conditions at different altitudes.

    Attributes
    ----------
    ground_temperature : float
        The temperature at ground level in Kelvin.
    ground_pressure : float
        The pressure at ground level in Pascals.
    T_lapse_rate : float
        The temperature lapse rate in Kelvin per meter.
    elevation : float
        The elevation of the location in meters above sea level.
    latitude : float
        The latitude of the location in degrees.

    local_gravity : float
        The local gravity at the location in m/s^2.
    density_multiplier : float
        A constant derived from the temperature and pressure at the launchpad, the lapse rate, the specific gas constant for air, and the magnitude of the force of gravity. Used in the air_density_optimized function. Equal to ground_pressure / (R_specific_air * pow(ground_temperature, - local_gravity / (R_specific_air * T_lapse_rate))).
    density_exponent : float
        A constant derived from the lapse rate, the specific gas constant for air, and the magnitude of the force of gravity. Used in the air_density_optimized function. Equal to - local_gravity / (R_specific_air * T_lapse_rate) - 1.
    """
    def __init__(self, ground_temperature, ground_pressure, local_T_lapse_rate=con.T_lapse_rate, elevation=0, latitude=40):
        """
        Initialize a Location object.

        Parameters
        ----------
        ground_temperature : float
            The temperature at ground level in degrees Celsius.
        ground_pressure : float
            The pressure at ground level in Pascals.
        T_lapse_rate : float, optional
            The temperature lapse rate in Kelvin (or Celsius) per meter. The default is -0.0065.
        elevation : float, optional
            The elevation of the location in meters above sea level. The default is 0.
        latitude : float, optional
            The latitude of the location in degrees. The default is 40.

        Notes
        -----
        For the most accurate results, specify all parameters.
        """
        self.ground_temperature = ground_temperature + 273.15
        self.ground_pressure = ground_pressure
        self.local_T_lapse_rate = local_T_lapse_rate
        self.elevation = elevation
        self.latitude = latitude

        self.local_gravity = get_local_gravity(latitude, elevation)

        self.density_multiplier = ground_pressure / (con.R_specific_air * pow(self.ground_temperature, - self.local_gravity / (con.R_specific_air * local_T_lapse_rate)))
        self.density_exponent = - self.local_gravity / (con.R_specific_air * local_T_lapse_rate) - 1

# Location class configuration for Spaceport America Cup
T_lapse_rate_SA = -0.00817 # K/m
""" How T_lapse_rate at Spaceport America was determined

Only one source was found with the lapse rate for Spaceport America:
    - https://egusphere.copernicus.org/preprints/2023/egusphere-2023-633/egusphere-2023-633.pdf
    - luckily, they took their measurements in June
    - The lapse rates for the stratosphere for each of three flights were reported as follows:
        - June 1st 2021 -8.4 K/km
        - June 4th 2021 -7.9 K/km
        - June 6th 2021 -8.2 K/km
    - An average of these is what was chosen for the simulation
    - The linear lapse rate was valid for the first 10 km AGL

For future reference, it should be noted that time of year has a large effect on the lapse rate, as reported in:
    - https://mdpi-res.com/d_attachment/remotesensing/remotesensing-14-00162/article_deploy/remotesensing-14-00162.pdf?version=1640917080
    - https://hwbdocs.env.nm.gov/Los%20Alamos%20National%20Labs/TA%2004/2733.PDF
        - states that the average lapse rate in NM is:
            - -4.0F/1000ft (-7.3 K/km) in July
            - -2.5F/1000ft (-4.6 K/km) in January
        - -8.2 K/km is higher than the summer average, but generally desert areas have higher-than-normal lapse rates

The following was the most comprehensive source found for temperature lapse rates in New Mexico: 
- https://pubs.usgs.gov/bul/1964/report.pdf
- No values were found for Spaceport itself, but values for other locations in New Mexico were found
- the report says that in the western conterminous United States, temperature lapse rates are generally significantly less than the standard -6.5 K/km
- the report didn't include the date (or month) of the measurements, so I'd assume that it happened in the winter due to the low lapse rates, and/or the data being several decades old means that it's no longer as accurate due to the changing global climate
- has values for many locations in New Mexico (search for n. mex), and they ranged from -1.4 to -3.9 K/km
    - the closest station to SA was Datil, which had a lapse rate of -3.1 K/km
"""
launchpad_pressure_SAC = 86400 # Pa
""" How the launchpad pressure at Spaceport America was determined

- 86400 2022/06/24   WE Rocketry 2022 TeleMega/TeleMetrum data
- 86405 2022/06/23   https://github.com/ISSUIUC/flight-data/tree/master/20220623
- 86170 2023/06/21   https://github.com/ISSUIUC/flight-data/tree/master/20230621
"""
launchpad_temp_SAC = 35 # deg C
""" Ground-level temperature at Spaceport America Cup note

Flights can occur between about 07:00 and 16:30 local time, so the temperature at the time of launch can vary significantly. 35 C is about what it has been historically during the competition in mid-late June. Getting closer to launch day, it would be more accurate to use a weather forecast to get a value for expected temperature(s).

You can also consider running simulations with a range of temperatures that have been seen on launch days in the past (normally between 25 and 45 C) to see how different ground-level temperatures could affect a rocket's flight.
"""
latitude_SA = 32.99 # deg, Spaceport America's latitude
""" https://maps.app.goo.gl/rZT6MRLqHneA7wNX7 """
altitude_SA = 1401 # m, Spaceport America's elevation
""" https://www.spaceportamerica.com/faq/#toggle-id-15 """

location_SAC = Location(ground_temperature=launchpad_temp_SAC, ground_pressure=launchpad_pressure_SAC, local_T_lapse_rate=T_lapse_rate_SA, elevation=altitude_SA, latitude=latitude_SA)

# Location class configuration for Launch Canada
T_lapse_rate_LC = con.T_lapse_rate
""" How T_lapse_rate at Launch Canada was determined

From a really really rough analysis of the flight data here: https://github.com/UVicRocketry/Xenia1-MaGP-I/tree/main

The temperature readings couldn't be used because it looks like the flight computer never got to the temperature of the outside (unless it only dropped 4 degrees on a 10k ft flight). However, looking at the pressure data, it looks similar to what it should look like given a lapse rate quite close to the standard -6.5 K/km. This is a very rough estimate, and it would be better to get a more accurate value from real temperature measurements at the launch site around late August.
"""
launchpad_pressure_LC = 102000 # Pa
""" Ground-level pressure at Launch Canada note

I could not find historical weather data for the launch site itself. Camp Kenogaming is very close to the launch site (6km away) and at nearly the same elevation: https://www.timeanddate.com/weather/@5914408/historic?month=8&year=2024
"""
launchpad_temp_LC = 20 # deg C
""" Ground-level temperature at Launch Canada note

I could not find historical weather data for the launch site itself. Camp Kenogaming is very close to the launch site (6km away) and at nearly the same elevation: https://www.timeanddate.com/weather/@5914408/historic?month=8&year=2024

Flights can occur from fairly early in the morning to late in the afternoon, so the temperature at the time of launch can vary significantly. Getting closer to launch day, it would be more accurate to use a weather forecast to get a value for expected temperature(s).

You can also consider running simulations with a range of temperatures that have been seen on launch days in the past (normally between 15 and 30 C) to see how different ground-level temperatures could affect a rocket's flight.
"""
latitude_LC = 47.987 # deg, Launch Canada's launch site latitude
""" https://maps.app.goo.gl/n76cD331j7LiQiTB6 """
altitude_LC = 364 # m, Launch Canada's launch site elevation
""" from Google Earth 
https://earth.google.com/web/search/Launch+Canada+Launch+Pad/@47.9869503,-81.8485488,363.96383335a,679.10907018d,35y """

location_LC = Location(ground_temperature=launchpad_temp_LC, ground_pressure=launchpad_pressure_LC, local_T_lapse_rate=T_lapse_rate_LC, elevation=altitude_LC, latitude=latitude_LC)

if __name__ == "__main__":
    import air_properties as ap
    import matplotlib.pyplot as plt

    # plot the following atmospheric properties at different altitudes at SAC and LC
    altitudes = range(0, 10000, 100)

    SAC_temps = [ap.temp_at_altitude(h, location_SAC.ground_temperature, location_SAC.local_T_lapse_rate) for h in altitudes]
    SAC_pressures = [ap.pressure_at_altitude(h, location_SAC.ground_temperature, location_SAC.ground_pressure, location_SAC.local_T_lapse_rate, location_SAC.local_gravity) for h in altitudes]
    SAC_densities = [ap.air_density_optimized(temp, location_SAC.density_multiplier, location_SAC.density_exponent) for temp in SAC_temps]
    SAC_speeds_of_sound = [ap.speed_of_sound(temp) for temp in SAC_temps]
    SAC_gravities = [get_local_gravity(location_SAC.latitude, altitude) for altitude in altitudes]

    LC_temps = [ap.temp_at_altitude(h, location_LC.ground_temperature, location_LC.local_T_lapse_rate) for h in altitudes]
    LC_pressures = [ap.pressure_at_altitude(h, location_LC.ground_temperature, location_LC.ground_pressure, location_LC.local_T_lapse_rate, location_LC.local_gravity) for h in altitudes]
    LC_densities = [ap.air_density_optimized(temp, location_LC.density_multiplier, location_LC.density_exponent) for temp in LC_temps]
    LC_speeds_of_sound = [ap.speed_of_sound(temp) for temp in LC_temps]
    LC_gravities = [get_local_gravity(location_LC.latitude, altitude) for altitude in altitudes]

    # plot them on the same graph
    fig, axs = plt.subplots(2, 3, figsize=(15, 10))
    fig.suptitle("Atmospheric Properties at Different Altitudes")
    axs[0, 0].plot(altitudes, SAC_temps, label="SAC")
    axs[0, 0].plot(altitudes, LC_temps, label="LC")
    axs[0, 0].set_title("Temperature (K)")
    axs[0, 0].legend()

    axs[0, 1].plot(altitudes, SAC_pressures, label="SAC")
    axs[0, 1].plot(altitudes, LC_pressures, label="LC")
    axs[0, 1].set_title("Pressure (Pa)")
    axs[0, 1].legend()

    axs[0, 2].plot(altitudes, SAC_densities, label="SAC")
    axs[0, 2].plot(altitudes, LC_densities, label="LC")
    axs[0, 2].set_title("Density (kg/m^3)")
    axs[0, 2].legend()

    axs[1, 0].plot(altitudes, SAC_speeds_of_sound, label="SAC")
    axs[1, 0].plot(altitudes, LC_speeds_of_sound, label="LC")
    axs[1, 0].set_title("Speed of Sound (m/s)")
    axs[1, 0].legend()

    axs[1, 1].plot(altitudes, SAC_gravities, label="SAC")
    axs[1, 1].plot(altitudes, LC_gravities, label="LC")
    axs[1, 1].set_title("Local Gravity (m/s^2)")
    axs[1, 1].legend()

    axs[1, 2].axis("off")

    plt.show()