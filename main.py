import pandas as pd
from simulate_flight_data import simulate_flight_data
from analyze_data import analyze_data
from plot_data import plot_data
from generate_report import generate_report

if __name__ == "__main__":
    # Step 1: Simulate flight data
    flight_data = simulate_flight_data()
    
    # Step 2: Analyze the flight data
    correlation_matrix = analyze_data(flight_data)
    
    # Step 3: Plot the flight data
    plot_data(flight_data)
    
    # Step 4: Generate the report
    generate_report(flight_data, correlation_matrix)
