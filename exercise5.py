# exercise 5
import numpy as np
import matplotlib.pyplot as plt
def load_data(file_path):
    """Load experimental data from a CSV file."""
    try:
        return np.loadtxt(file_path, delimiter=',', skiprows=1)
    except OSError:
        raise FileNotFoundError("Your file was not found!")

def plot_free_fall(data, save_path='free_fall_plot.png'):
    """Generate and save the free fall plot."""
    # Constants
    g = 9.8  
    t = np.arange(0, 5.5, 0.5)
    h0 = 125  
    v0 = 0  

    # Theoretical curve
    theoretical = h0 + v0 * t - 0.5 * g * t**2

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(data[:, 0], data[:, 1], 'ko', color = "blue", label='Experimental Data')
    plt.plot(t, theoretical, 'orange', label='Theoretical: h(t)= h0 - 0.5 * g * t^2', linewidth=2) 
    plt.axhline(y=0, color='blue', linestyle='-', linewidth=2)

    # Labels and Title
    plt.title('Object in Free fall : Experimental vs Theoretical', fontsize=16)
    plt.xlabel('Time (s)', fontsize=14)
    plt.ylabel('Vertical Position (m)', fontsize=14)
    plt.xlim(0, 5.5)
    plt.ylim(0, 140)
    plt.legend()
    plt.grid(True)

    # Save Plot
    try:
        plt.savefig(save_path)
    except FileExistsError:
        raise FileExistsError(f"The file {save_path} already exists.")
    plt.close()


def main():
    data_file = 'free_fall_experimental_data.csv'
    data = load_data(data_file)
    plot_free_fall(data)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    main()