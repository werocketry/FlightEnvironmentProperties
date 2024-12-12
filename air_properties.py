import numpy as np
import constants as con

def temp_at_altitude(h, reference_temp, lapse_rate = con.T_lapse_rate):
    """
    Calculate the temperature at a given altitude above a reference point. Within the troposphere, temperature decreases linearly with increasing altitude at a rate known as the lapse rate. The lapse rate is typically around 6.5 degrees Celsius per kilometer, but it can vary depending on location, time of year, and other factors.

    Args
    ----
    h : float
        Altitude above the reference point in meters.
    reference_temp : float
        Temperature at the reference altitude in Celsius or Kelvin.
    lapse_rate : float, optional
        Rate at which temperature decreases with increasing altitude in degrees Celsius or Kelvin per meter. Defaults to the standard lapse rate of -0.0065.

    Returns
    -------
    float
        Temperature at the given altitude above the reference point in Celsius or Kelvin (same unit as input).
    """
    return reference_temp + (h * lapse_rate)

def pressure_at_altitude(h, reference_temp, reference_pressure, lapse_rate = con.T_lapse_rate, F_gravity = con.F_gravity):
    """
    Calculate the air pressure at a given altitude above a reference point.

    Args
    ----
    h : float
        Altitude above the reference point in meters.
    reference_temp : float
        Temperature at the reference point in Kelvin.
    reference_pressure : float
        Air pressure at the reference point in Pascals.
    lapse_rate : float, optional
        Rate at which temperature decreases with increasing altitude in Kelvin per meter. Defaults to the standard lapse rate of 0.0065 K/m.
    F_gravity : float, optional
        Magnitude of the force of gravity in Newtons. Defaults to the standard value of 9.80665 N.

    Returns
    -------
    float
        Air pressure at the given altitude in Pascals.
    """
    return reference_pressure * pow(
        (1 - (h * lapse_rate / reference_temp)),
        (F_gravity / (con.R_specific_air * lapse_rate))
    )

def air_density_fn(pressure, temp):
    """
    Calculate the density of air at a given pressure and temperature.

    Args
    ----
    pressure : float
        Pressure in Pascals.
    temp : float
        Temperature in Kelvin.

    Returns
    -------
    float
        Air density in kilograms per cubic meter.
    """
    return pressure / (con.R_specific_air * temp)

def air_density_optimized(temp, multiplier, exponent):
    """
    Calculate the density of air at a given height above a reference point.

    Args
    ----
    temp : float
        Temperature at the given height above the reference point in Kelvin.
    multiplier : float
        A constant derived from the temperature and pressure at the reference point, the lapse rate, the specific gas constant for air, and the magnitude of the force of gravity. Calculated at initialization of Location objects. Equal to ground_pressure / (R_air * pow(ground_temperature, - F_gravity / (R_air * T_lapse_rate))).
    exponent : float
        A constant derived from the lapse rate, the specific gas constant for air, and the magnitude of the force of gravity. Calculated at initialization of Location objects. Equal to - F_gravity / (R_air * T_lapse_rate) - 1.

    Returns
    -------
    float
        Air density at the given height in kilograms per cubic meter.
    """
    return multiplier * pow(temp, exponent)

def lookup_dynamic_viscosity(temp):
    """
    Look up the dynamic viscosity of air at a given temperature.

    Args
    ----
    temp : float
        Temperature in Kelvin.

    Returns
    -------
    float
        Dynamic viscosity in kilograms per meter-second.

    References
    ----------
    Source of lookup table: https://www.me.psu.edu/cimbala/me433/Links/Table_A_9_CC_Properties_of_Air.pdf
    Temperatures converted from source (Celsius to Kelvin).
    """
    # Lookup table for dynamic viscosity
    temps = np.array([173.15, 223.15, 233.15, 243.15, 253.15, 263.15, 273.15, 278.15, 283.15, 288.15, 293.15, 298.15, 303.15, 308.15, 313.15, 318.15, 323.15, 333.15, 343.15])
    viscosities = np.array([1.189e-6, 1.474e-5, 1.527e-5, 1.579e-5, 1.630e-5, 1.680e-5, 1.729e-5, 1.754e-5, 1.778e-5, 1.802e-5, 1.825e-5, 1.849e-5, 1.872e-5, 1.895e-5, 1.918e-5, 1.941e-5, 1.963e-5, 2.008e-5, 2.052e-5])
    
    # Interpolate to find dynamic viscosity at the given temperature
    return np.interp(temp, temps, viscosities)

def speed_of_sound(temp):
    """
    Calculate the speed of sound in air at a given temperature.

    Args
    ----
    temp : float
        Temperature in Kelvin.

    Returns
    -------
    float
        Speed of sound in meters per second.
    """
    return np.sqrt(con.adiabatic_index_air_times_R_specific_air * temp)


# Humidity functions - these functions are primarily for interest, as for our project, it's not worth it to consider humidity's effect on air properties.
