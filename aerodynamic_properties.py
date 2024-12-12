def calculate_dynamic_pressure(fluid_density, speed):
    """
    Calculate the dynamic pressure imparted on a solid moving through a fluid.

    Args
    ----
    fluid_density : float
        Density of the fluid.
    speed : float
        Relative speed between the solid and the fluid.

    Returns
    -------
    float
        Dynamic pressure on the solid.
    """
    return 0.5 * fluid_density * (speed ** 2)

def calculate_mach_number(speed, speed_of_sound):
    """
    Calculate the Mach number of a solid moving through a fluid.

    Args
    ----
    speed : float
        Relative speed between the solid and the fluid.
    speed_of_sound : float
        Speed of sound in the fluid.

    Returns
    -------
    float
        Mach number of the solid.
    """
    return speed / speed_of_sound

def calculate_reynolds_number(fluid_density, speed, len_characteristic, dynamic_viscosity):
    """
    Calculate the Reynolds number of a solid moving through a fluid.

    Args
    ----
    fluid_density : float
        Density of the fluid.
    speed : float
        Relative speed between the solid and the fluid.
    len_characteristic : float
        Characteristic length of the solid.
    dynamic_viscosity : float
        Dynamic viscosity of the fluid.

    Returns
    -------
    float
        Reynolds number of the solid moving through the fluid.
    """
    return fluid_density * speed * len_characteristic / dynamic_viscosity