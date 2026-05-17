

# def beam_properties_input():
#     while True:

#         # assign variables to user inputs as float data types
#         try:
#             length = float(input("What length is the beam in meters? "))
#             distributed_load = float(input("What is the distributed load of the beam in N/m? "))
#             modulus_of_elasticity = float(input("What is the modulus of elasticity of the beam in Pa? "))
#             moment_inertia =  float(input("What is the moment of inertia of the beam in m^4? "))

#             # add user inputs to dictionary to be unpacked and processed in other functions 
#             inputs = {"beam_length": length, "beam_load": distributed_load, "modulus_elasticity": modulus_of_elasticity, "inertia_moment": moment_inertia}          

#             # check if inputs are negative or zero to ensure valid calculation of beam deflection
#             for value in inputs.values():
#                 if value <= 0:
#                     raise ValueError
#                 else:
#                     return inputs
    
#         # check if inputs are numbers
#         except ValueError:
#             print("Please enter positive numbers only.")
   

# # unpack inputs dictionary for calculation using inputs
# def beam_calculator(**inputs):

#     # calculate beam deflection, rounded to 5 decimal places
#     deflection_formula = round((5 * inputs["beam_load"] * inputs["beam_length"] ** 4)/(384 * inputs["modulus_elasticity"] * inputs["inertia_moment"]), 5)
    
#     # calculate beam midpoint
#     beam_midpoint = inputs["beam_length"] / 2
#     return deflection_formula, beam_midpoint

# # print results
# def results_output(deflection, beam_midpoint):

#     print(f"The maximum beam deflection is {deflection}m or {deflection * 1000}mm. \nThe location of the maximum deflection is {beam_midpoint}m from the ends of the beam.")

# # call functions
# inputs = beam_properties_input()
# deflection, beam_midpoint = beam_calculator(**inputs)
# results_output(deflection, beam_midpoint)

# Hi,

# Please act as a Python developer. I need to create a program that calculates the maximum deflection of a simply-supported beam under uniform load. The user will provide the load (w) in N/m, the length of the beam (L) in m, the modulus of elasticity of the material (I) in Pa, and the second moment of inertia of the beam cross-section (I) in m^4.



# README: The program requires the NumPy and Matplotlib libraries. These can be installed via pip install numpy matplotlib.

import numpy as np
import matplotlib.pyplot as plt

def calculate_max_deflection(L, w, E, I):
    """Calculates the theoretical maximum deflection and its location."""
    delta_max = (5 * w * L**4) / (384 * E * I)
    location = L / 2
    return delta_max, location

def generate_deflection_plot(L, w, E, I):
    """Generates a correctly formatted deflection plot for the assessment."""
    # Generate 100 points along the beam for a smooth curve
    x = np.linspace(0, L, 100)
    
    # Standard elastic curve equation for simply supported beam with UDL
    # y = (w*x / 24EI) * (L^3 - 2Lx^2 + x^3)
    y_meters = (w * x / (24 * E * I)) * (L**3 - 2 * L * x**2 + x**3)
    
    # Convert to mm for the plot (and flip sign so sag is downward)
    y_mm = y_meters * 1000
    
    plt.figure(figsize=(10, 6))
    plt.plot(x, -y_mm, label='Deflection Curve', color='blue', linewidth=2.5)
    
    # Add labels and styling for the assessment rubric
    plt.title(f'Beam Deflection Profile (Load: {w} N/m)', fontsize=14)
    plt.xlabel('Position along the beam (m)', fontsize=12)
    plt.ylabel('Vertical Deflection (mm)', fontsize=12)
    
    # Draw the undeformed beam line for reference
    plt.axhline(0, color='black', linestyle='-', linewidth=1)
    
    # Add a marker for the maximum deflection point
    plt.plot(L/2, -( (5 * w * L**4) / (384 * E * I) * 1000), 'ro', label='Max Deflection')
    
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    print("\n[Plotting] Displaying graph... Close the graph window to exit.")
    plt.show()

def get_positive_float(prompt, var_name):
    """Input helper with validation."""
    while True:
        try:
            val = float(input(prompt))
            if val <= 0:
                print(f"Error: {var_name} must be positive.")
                continue
            return val
        except ValueError:
            print("Error: Please enter a valid number.")

def validate_units(E, I):
    """Sanity check for common SI unit errors."""
    if E < 1e6:
        print("\n[!] WARNING: E is very low. Did you use GPa instead of Pa?")
    if I > 0.1:
        print("\n[!] WARNING: I is very high. Did you use mm^4 instead of m^4?")

def main():
    print("="*60)
    print("   STRUCTURAL ANALYSIS: BEAM DEFLECTION & PLOTTING   ")
    print("="*60)

    # Inputs
    L = get_positive_float("Beam Length (m): ", "Length")
    w = get_positive_float("Uniform Load (N/m): ", "Load")
    E = get_positive_float("Elastic Modulus (Pa): ", "E")
    I = get_positive_float("Moment of Inertia (m^4): ", "I")

    validate_units(E, I)

    # Calculations
    delta_max, midpoint = calculate_max_deflection(L, w, E, I)

    # Results Text
    print("\n" + "-"*30)
    print(f"Max Deflection: {delta_max*1000:.4f} mm")
    print(f"Location:       {midpoint:.3f} m")
    print("-"*30)

    # Visualization
    generate_deflection_plot(L, w, E, I)

if __name__ == "__main__":
    main()





