import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_data(df):
    sns.set(style="whitegrid")

    plt.figure(figsize=(10, 6))
    sns.histplot(df['Altitude'], kde=True, color='blue')
    plt.title('Distribution of Altitude')
    plt.xlabel('Altitude (feet)')
    plt.ylabel('Frequency')
    plt.show()

    plt.figure(figsize=(10, 6))
    sns.histplot(df['Speed'], kde=True, color='green')
    plt.title('Distribution of Speed')
    plt.xlabel('Speed (mph)')
    plt.ylabel('Frequency')
    plt.show()

    sns.pairplot(df)
    plt.show()

if __name__ == "__main__":
    flight_data = pd.read_csv('flight_data.csv')
    plot_data(flight_data)
