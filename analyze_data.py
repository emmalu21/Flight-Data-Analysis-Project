import pandas as pd

def analyze_data(df):
    print("Summary Statistics:")
    print(df.describe())
    correlation_matrix = df.corr()
    print("\nCorrelation Matrix:")
    print(correlation_matrix)
    return correlation_matrix

if __name__ == "__main__":
    flight_data = pd.read_csv('flight_data.csv')
    analyze_data(flight_data)
