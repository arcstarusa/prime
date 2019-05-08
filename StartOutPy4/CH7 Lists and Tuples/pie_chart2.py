# This program displays a simple pie chart. 7-28
import matplotlib.pyplot as plt

def main():
    # Create a list of sales amount.
    sales = [100, 400, 300, 600]

    # Create a list of labels for the slices.
    slice_labels = ['1st Qtr', '2nd Qtr', '3rd Qrt', '4th Qrt']

    # Create pie chart from the values.
    plt.pie(sales, labels=slice_labels)

    # Add a title.
    plt.title('Sales by Quarter')

    # Display the pie chart.
    plt.show()

# Call the main function.
main()