def printStatsDecorator(func):
    def wrapper(numbers):
        print("Numbers:", numbers)
        print("Count:", len(numbers))
        if len(numbers) > 0:
            print("Average:", sum(numbers) / len(numbers))
            print("Maximum:", max(numbers))
    return wrapper

@printStatsDecorator
def printStats(numbers):
    pass

def process_line(line):
    return [int(num) for num in line.strip().split()]

def process_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            numbers = process_line(line)
            printStats(numbers)
