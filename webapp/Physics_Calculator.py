
'''
Equations used:
    The second law of Newton: F = M * A [N] when F is force, M is mass and A is acceleration

    Velocity in a constent acceleration movement: V = A * T [M/S] when V is velocity, A is acceleration and T is time

    Location in a certin time in a constent acceleration movement: X = 0.5 * A * T**2 + V(t = 0) * t + X(t = 0) when X is location, A is acceleration and T is time

'''

PLANE_INIT_MASS = 35_000 #The mass of the plane without the cargo, [KG]
REQUIRED_SPEED_FOR_TAKE_OFF = 140 #[M / S]
ENGINES_FORCE = 100_000 #[N/S]
MAX_TAKE_OFF_TIME = 60 #[S]

def check_burn(cargo_mass):
    '''
    Calculating the amount of mass required to burn in order to take off in under 60 seconds
    Input: cargo_mass_input - the cargo mass[KG]
    Output: int - the amount of weight to burn[N]
    '''
    acceleration = REQUIRED_SPEED_FOR_TAKE_OFF / MAX_TAKE_OFF_TIME #Using Velocity equation

    cargo_mass_max = (ENGINES_FORCE / acceleration) - PLANE_INIT_MASS #The second law of Newton

    mass_to_burn = cargo_mass - cargo_mass_max
    return mass_to_burn #[KG]
    

def calc_time(mass):
    '''
    Calculating the take off time using velocity equation and the second law of Newton
    Input: mass - the mass of the cargo
    Output: int - the amount of seconds required for take off, int - the acceleration of the plane during take off(required for calculating distance)
    '''
    acceleration = ENGINES_FORCE / (mass + PLANE_INIT_MASS) #The second law of Newton

    time = REQUIRED_SPEED_FOR_TAKE_OFF / acceleration #The velocity equation
    return time, acceleration #[S], [M / S**2]

def calc_distance(time, acceleration):
    '''
    Calculating the take off distance using location equation
    Input: time - the time required for take off, acceleration - the acceleration of the plane
    Output: int - the distance of road requierd for take off
    '''

    #Because X(t = 0) = 0 the distance of the road is only X(t = time)
    #In take off the plane starts from standing still in place so V(t = 0) = 0
    distance = 0.5 * acceleration * (time ** 2) #All the other parts of the equation equels to 0, [M]
    return distance
    

def calc_results(cargo_mass : int):
    '''
    Calculating the take off time and the distance for take off
    Input: cargo_mass - the mass of the cargo
    Output: A list containing: time_for_take_off, distance, weight_to_burn_in_order_to_take_off - the results
    '''
    time_for_take_off = 0
    distance = 0
    acceleration = 0
    mass_to_burn_in_order_to_take_off = 0

    try:
        if cargo_mass < 0:
            raise ValueError()

    except ValueError:
        return [-1,-1,-1]

    time_for_take_off, acceleration = calc_time(cargo_mass)

    distance = calc_distance(time_for_take_off, acceleration)

    if(time_for_take_off > MAX_TAKE_OFF_TIME):
        mass_to_burn_in_order_to_take_off = check_burn(cargo_mass)
    
    return [time_for_take_off, distance, mass_to_burn_in_order_to_take_off]

if __name__ == '__main__':
    calc_results()
    
