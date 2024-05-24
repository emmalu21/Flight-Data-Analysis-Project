File Descriptions:

1) simulate_flight_data.py

Purpose: This script simulates flight data, creating a dataset with random values for various flight attributes such as altitude, speed, distance, and duration.
Functionality:
Generates a synthetic dataset representing 100 flights.
Saves the generated data to a CSV file named flight_data.csv.

2) analyze_data.py

Purpose: This script performs statistical analysis on the flight data.
Functionality:
Loads the flight data from the CSV file.
Computes and prints summary statistics.
Calculates and prints the correlation matrix to understand relationships between variables.

3) plot_data.py

Purpose: This script visualizes the flight data using histograms and pair plots.
Functionality:
Plots histograms for altitude and speed distributions.
Creates pair plots to visualize relationships between all pairs of variables.

4) generate_report.py

Purpose: This script generates a text report summarizing the analysis of the flight data.
Functionality:
Loads the flight data and the correlation matrix.
Writes the summary statistics and correlation matrix to a text file named flight_data_report.txt.

5) main.py

Purpose: This script orchestrates the entire workflow of the project by calling functions from the other scripts in sequence.
Functionality:
Simulates flight data.
Analyzes the data and prints summary statistics and correlation matrix.
Visualizes the data using histograms and pair plots.
Generates a text report summarizing the analysis.

6) requirements.txt

Purpose: Lists the required Python libraries for the project.
Functionality:
Specifies the dependencies needed to run the project.

How to Run the Project
Install the required libraries:

pip install -r requirements.txt

Run the main script:
python main.py

Description:
This project demonstrates proficiency in data analysis, statistical methods, 
and data visualization. The modular structure ensures clarity and maintainability, 
which are essential for professional software development.
