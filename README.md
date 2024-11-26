# FlightEnvironmentProperties
A comprehensive environmental model for the conditions a 10k or 30k ft rocket would encounter. The model is very accurate within the troposphere (up to ~11 km, or 36k ft), but could easily be extended to higher altitudes.

This repository contains:

    - Python code for calculating local atmospheric properties, the local gravitational force, and a few aerodynamic flow properties
    - A Locations class for storing attributes of a location for use in the aforementioned calculations
    - Initializations of that class for the environments encountered at Spaceport America Cup and Launch Canada
    - An Excel file with the atmospheric conditions at SAC and LC at different altitudes
    - Jupyter notebooks detailing the theory behind the code (WIP)

To be added:

    - Jupyter notebooks for learning how to use the code


Future updates

- Finish up atmospheric_conditions.ipynb
- .ipynb for gravity theory, short and sweet
- Note in atmospheric_conditions.ipynb how humidity changes things by a very small (note just how small) amount in the worst case scenarios, and that we can effectively ignore it
- add notes somewhere for where/how to find the attributes needed to initialize a Location class for a given location
- add humidity functions (some like temp at alt don't need to be changed), use in ipynb description of why you can efffectively ignore it
- add an ipynb for showing how to use the code for those that aren't familiar with python - ask a recruit to do it?

Possible future updates, or maybe in some other knowledge repo

- Note somewhere how wind data for SAC can be found, both live from comp and historical data
- Add API for finding humidity?
- Add API for finding wind data?
- Another location class initialization for wherever the test launch is going to happen
- Another location class initialization for where we do cert flights in Michigan