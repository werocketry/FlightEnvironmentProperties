def calculate_dynamic_pressure(air_density, speed):
    """
    Calculate the dynamic pressure imparted on a solid moving through a fluid.

    Args
    ----
    air_density : float
        The density of the fluid.
    speed : float
        The relative speed between the solid and the fluid.

    Returns
    -------
    float
        The dynamic pressure on the solid.
    """
    return 0.5 * air_density * (speed ** 2)

def calculate_mach_number(speed, speed_of_sound):
    """
    Calculate the Mach number of a solid moving through a fluid.

    Args
    ----
    speed : float
        The relative speed between the solid and the fluid.
    speed_of_sound : float
        The speed of sound in the fluid.

    Returns
    -------
    float
        The Mach number of the solid.
    """
    return speed / speed_of_sound

def calculate_reynolds_number(air_density, speed, len_characteristic, dynamic_viscosity):
    """
    Calculate the Reynolds number of a solid moving through air.

    Args
    ----
    air_density : float
        The density of the air.
    speed : float
        The relative speed of the solid and the air.
    len_characteristic : float
        The characteristic length of the solid.
    dynamic_viscosity : float
        The dynamic viscosity of the air.

    Returns
    -------
    float
        The Reynolds number of the solid.
    """
    return air_density * speed * len_characteristic / dynamic_viscosity