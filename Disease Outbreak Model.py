# -*- coding: utf-8 -*-
"""
Created on Thu May 05 02:03:56 2023

@author: Phakamani Mluleki
"""

import numpy as np
import matplotlib.pyplot as plt

# Parameters
population_size = int(input("Enter population size: "))  # Total population size
initial_infected = int(input("Enter number of those infected: "))  # Number of initially infected individuals
infection_rate = float(input("Enter infection rate: "))  # Probability of infection per contact
recovery_rate = float(input("Enter recovery rate: "))  # Probability of recovery per day
simulation_days = int(input("Simulation days: "))  # Number of simulation days

# Initialize arrays
susceptible = np.zeros(simulation_days)
infected = np.zeros(simulation_days)
recovered = np.zeros(simulation_days)

# Set initial conditions
susceptible[0] = population_size - initial_infected
infected[0] = initial_infected

# Simulation
for day in range(1, simulation_days):
    # Calculate new infections and recoveries
    new_infections = np.random.binomial(susceptible[day-1], infection_rate)
    new_recoveries = np.random.binomial(infected[day-1], recovery_rate)

    # Update population counts
    susceptible[day] = susceptible[day-1] - new_infections
    infected[day] = infected[day-1] + new_infections - new_recoveries
    recovered[day] = recovered[day-1] + new_recoveries

# Plotting
plt.plot(range(simulation_days), susceptible, label='Susceptible')
plt.plot(range(simulation_days), infected, label='Infected')
plt.plot(range(simulation_days), recovered, label='Recovered')
plt.xlabel('Days')
plt.ylabel('Population')
plt.title('Disease Outbreak Modeling')
plt.legend()
plt.show()

# Analysis and Informed Decisions
peak_infected = np.max(infected)
peak_day = np.argmax(infected)

if peak_infected > 0:
    peak_infections_percent = (peak_infected / population_size) * 100
    print("Peak Infections: {} ({}%) on Day {}".format(peak_infected, peak_infections_percent, peak_day))

    # Resource Allocation Decision
    resource_threshold = 0.8 * population_size  # Threshold for resource allocation decision
    if peak_infected > resource_threshold:
        print("Resource allocation: Based on the peak infections, additional healthcare resources should be allocated to handle the surge in demand.")
    else:
        print("Resource allocation: The existing healthcare resources can adequately handle the peak infections.")

    # Intervention Strategies Decision
    intervention_threshold = 0.5 * population_size  # Threshold for intervention strategy decision
    if peak_infections_percent > intervention_threshold:
        print("Intervention strategy: Stringent measures such as social distancing, contact tracing, and quarantine should be implemented to control the spread.")
    else:
        print("Intervention strategy: Moderate measures such as public awareness campaigns and targeted testing can help contain the outbreak.")

else:
    print("No peak infections occurred.")

if recovered[-1] > 0:
    final_recovery_percent = (recovered[-1] / population_size) * 100
    print("Final Recovery: {} ({}%) on Day {}".format(recovered[-1], final_recovery_percent, simulation_days - 1))

    # Policy Planning Decision
    recovery_threshold = 0.9 * population_size  # Threshold for policy planning decision
    if final_recovery_percent > recovery_threshold:
        print("Policy planning: With a high recovery rate, considerations can be made for easing restrictions and reopening certain sectors.")
    else:
        print("Policy planning: Caution should be exercised, and restrictions should be maintained to prevent potential resurgence.")

else:
    print("No recoveries occurred.")

# Risk Assessment Decision
risk_threshold = 0.1 * population_size  # Threshold for risk assessment decision
if np.max(infected) > risk_threshold:
    print("Risk assessment: The outbreak poses a significant risk to the population, and proactive measures should be taken to mitigate the spread.")
else:
    print("Risk assessment: The outbreak is relatively contained, but continued monitoring and vigilance are essential.")

# Public Awareness Decision
public_awareness_threshold = 0.5 * population_size  # Threshold for public awareness decision
if np.max(infected) > public_awareness_threshold:
    print("Public awareness: The public should be informed about the severity of the outbreak and encouraged to follow preventive measures strictly.")
else:
    print("Public awareness: Efforts should be made to maintain public awareness and reinforce adherence to preventive measures.")

