import pandas as pd

def generate_report(df, correlation_matrix):
    with open('flight_data_report.txt', 'w') as file:
        file.write("Flight Data Analysis Report\n")
        file.write("============================\n\n")
        file.write("Summary Statistics:\n")
        file.write(df.describe().to_string())
        file.write("\n\nCorrelation Matrix:\n")
        file.write(correlation_matrix.to_string())
    print("Report generated: flight_data_report.txt")

if __name__ == "__main__":
    flight_data = pd.read_csv('flight_data.csv')
    correlation_matrix = flight_data.corr()
    generate_report(flight_data, correlation_matrix)
