import matplotlib.pyplot as plt

def graphSnowfall(t):
    # Initialize a dictionary to store the count of snowfall accumulations in each range
    snowfall_ranges = {
        '0-10': 0,
        '11-20': 0,
        '21-30': 0,
        '31-40': 0,
        '41-50': 0
    }

    # Read data from the file and aggregate snowfall accumulations into ranges
    with open(t, 'r') as file:
        for line in file:
            snowfall = int(line.strip())
            if snowfall <= 10:
                snowfall_ranges['0-10'] += 1
            elif snowfall <= 20:
                snowfall_ranges['11-20'] += 1
            elif snowfall <= 30:
                snowfall_ranges['21-30'] += 1
            elif snowfall <= 40:
                snowfall_ranges['31-40'] += 1
            else:
                snowfall_ranges['41-50'] += 1

    # Extract x and y values for plotting
    x = list(snowfall_ranges.keys())
    y = list(snowfall_ranges.values())

    # Plotting the bar chart
    plt.bar(x, y, color='skyblue')
    plt.xlabel('Snowfall Ranges (cm)')
    plt.ylabel('Number of Occurrences')
    plt.title('Snowfall Accumulation Distribution')
    plt.show()

# Example usage:
# graphSnowfall('snowfall_data.txt')
