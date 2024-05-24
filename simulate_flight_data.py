import numpy as np
import pandas as pd

def simulate_flight_data():
    np.random.seed(42)
    data = {
        'FlightNumber': np.arange(1, 101),
        'Altitude': np.random.normal(35000, 1000, 100),
        'Speed': np.random.normal(500, 50, 100),
        'Distance': np.random.normal(1500, 300, 100),
        'Duration': np.random.normal(3, 0.5, 100)
    }
    df = pd.DataFrame(data)
    df.to_csv('flight_data.csv', index=False)
    return df

if __name__ == "__main__":
    simulate_flight_data()
