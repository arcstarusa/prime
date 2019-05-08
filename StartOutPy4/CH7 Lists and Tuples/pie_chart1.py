# This program displays a simple pie chart. 7-27
import matplotlib.pyplot as plt

def main():
    # Create a list of values
    values = [20, 60, 80, 40]

    # Create a pie chart from the values.
    plt.pie(values)

    # Display the pie chart.
    plt.show()

# Call the main function.
main()