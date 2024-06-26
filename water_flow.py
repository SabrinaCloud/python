def water_column_height(tower_height, tank_height):
    """
    Calculate the height of the water column in a tank on top of a tower.
    
    Args:
    -tower_height:Height of the tower in meters(float).
    -tank_height:Height of the tank walls in meter(float).

    Returns:
    -Height of the water column in meters(float).
    """
    water_height=tower_height+(3/4)*tank_height
    return water_height

def pressure_gain_from_water_height(height):
    """
    Calculate the pressure caused by Earth's gravity on the water height.
    
    Args:
    -height: Height of the water column in meters(float).

    Returns:
    -Pressure in kilopascals(float).
    """

    density_water=998.2 #kg/m^3
    gravity=9.80665 #m/s^2
    pressure=density_water*gravity*height/1000
    return pressure

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    """
    Calculate the pressure lost because of the friction in a pipe.

    Args:
    -pipe_diameter:Diameter of the pipe in meters(float).
    -pipe_length:Length of the pipe in meters(float).
    -friction_factor: Friction factor of the pipe(float).
    -fluid_velocity:Velocity of the fluid in the pipe in meters/second(float).

    Returns:
    -Pressure loss the kilopascals(float).
    """

    #Constants
    density_water=998.2 #kg/m^3
    pressure_loss=(-friction_factor*pipe_length*density_water*fluid_velocity**2)/(2000*pipe_diameter)

    return pressure_loss

def pressure_loss_from_fittings(fluid_velocity, quantity_fittings):
    """
    Calculate the pressure loss from fittings in the pipeline.
    """
    density_water=998.2 #kg/m^3
    fitting_loss=(-0.04*density_water*fluid_velocity**2*quantity_fittings)/2000
    return(fitting_loss)

def reynolds_number(hydraulic_diameter, fluid_velocity):
    """
    Calculate the Reynolds number for a pipe with water flowing through it.
    """
    density_water=998.2 #kg/m^3
    viscosity_water=0.0010016 #Pascal seconds
    number_of_reynold=(density_water*hydraulic_diameter*fluid_velocity)/viscosity_water
    return(number_of_reynold)

def pressure_loss_from_pipe_reduction(larger_diameter, fluid_velocity, reynolds_number, smaller_diameter):
    """
    Calculate the pressure loss due to a reduction in pipe diameter.
    """
    density_water=998.2 #kg/m^3
    k=0.1+50/reynolds_number*((larger_diameter/smaller_diameter)**4-1)
    reduction_loss=(-k*density_water*fluid_velocity**2)/2000
    return(reduction_loss)

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = float(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
if __name__ == "__main__":
    main()