My first Fluid Mechanics code - Bernoulli Equation
# P + 0.5*rho*v^2 + rho*g*h = constant

def bernoulli_pressure(rho, v1, p1, v2):
    """Calculate pressure at point 2"""
    p2 = p1 + 0.5 * rho * (v1**2 - v2**2)
    return p2

# Example: Water flowing in a pipe
density = 1000  # kg/m3 for water
velocity_1 = 2.0  # m/s
pressure_1 = 101325  # Pa
velocity_2 = 4.0  # m/s when pipe gets narrow

pressure_2 = bernoulli_pressure(density, velocity_1, pressure_1, velocity_2)
print(f"Pressure at narrow section: {pressure_2} Pa")
print("Welcome to Fluid Mechanics with Python!")
