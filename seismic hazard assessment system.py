import numpy as np

# Define a function to perform Probabilistic Seismic Hazard Analysis (PSHA)
def psha(magnitude, distance):
    # Example ground motion prediction equation (GMPE) parameters
    a = 0.1
    b = 0.5
    
    # Compute the seismic hazard using a simplified GMPE
    hazard = np.exp(a * magnitude - b * distance)
    return hazard

# Define earthquake parameters
magnitude = 7.0  # Magnitude of the earthquake
distance = 50.0  # Distance from the earthquake epicenter (in km)

# Perform PSHA to estimate the seismic hazard
seismic_hazard = psha(magnitude, distance)

# Print the result
print("Seismic hazard:", seismic_hazard)
