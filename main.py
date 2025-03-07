import matplotlib.pyplot as plt
from utils.executeTimeGathering import gather_execution_times

def plot_results(df):
    """
    Plots execution times of different palindrome checking algorithms.

    :param df: Pandas DataFrame with execution times.
    """
    plt.figure(figsize=(10, 6))
    plt.plot(df['Size'], df['Reverse'], label='Reverse Method', marker='o')
    plt.plot(df['Size'], df['Pointers'], label='Two Pointers Method', marker='s')
    #plt.plot(df['Size'], df['Recursive'], label='Recursive Method', marker='^')

    plt.xlabel("String Size")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Palindrome Checking Algorithms Performance")
    plt.legend()
    plt.grid()
    plt.show()

if __name__ == "__main__":
    string_sizes = [100, 1000, 10000, 100000]

    df = gather_execution_times(string_sizes)
    plot_results(df)
