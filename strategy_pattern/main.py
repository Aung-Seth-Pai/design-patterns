from concrete_strategies import *
from context import Context

def main():
    # Sample data
    data = [1, 2, 2, 3, 4, 5, 5, 5]

    # Create context with initial strategy
    context = Context(strategy=SumStrategy())
    print("Sum:", context.execute_strategy(data))

    # Change strategy to Mean
    context.set_strategy(MeanStrategy())
    print("Mean:", context.execute_strategy(data))

    # Change strategy to Median
    context.set_strategy(MedianStrategy())
    print("Median:", context.execute_strategy(data))

    # Change strategy to Mode
    context.set_strategy(ModeStrategy())
    print("Mode:", context.execute_strategy(data))

    # Change strategy to Max
    context.set_strategy(MaxStrategy())
    print("Max:", context.execute_strategy(data))

    # Change strategy to Min
    context.set_strategy(MinStrategy())
    print("Min:", context.execute_strategy(data))

if __name__ == "__main__":
    main()