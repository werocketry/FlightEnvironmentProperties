import numpy as np

def get_local_gravity(latitude, h = 0):
    """
    Calculate the acceleration due to gravity at a given latitude and altitude above sea level.

    Args
    ----
    latitude : float
        Latitude in degrees.
    h : float
        Ground level elevation above sea level in meters. Defaults to 0.

    Returns
    -------
    float
        Acceleration due to gravity in meters per second squared.

    References
    ----------
    Based on the International Gravity Formula 1980 (IGF80) model, as outlined in https://en.wikipedia.org/wiki/Theoretical_gravity#International_gravity_formula_1980
    """

    phi = np.deg2rad(latitude)

    # Coefficients for the gravity formula for the Earth as an oblate spheroid
    gamma_a = 9.780327  # m/s^2
    c1 = 0.0052790414
    c2 = 0.0000232718
    c3 = 0.0000001262
    c4 = 0.0000000007

    gamma_0 = gamma_a * (1 + c1 * np.sin(phi)**2 + c2 * np.sin(phi)**4 + c3 * np.sin(phi)**6 + c4 * np.sin(phi)**8)

    # Coefficients for the free air correction (the correction for the height above sea level)
    k1 = 3.15704e-07  # 1/m
    k2 = 2.10269e-09  # 1/m
    k3 = 7.37452e-14  # 1/m^2

    return gamma_0 * (1 - (k1 - k2 * np.sin(phi)**2) * h + k3 * h**2)