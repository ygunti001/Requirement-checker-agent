def add_two_numbers(a, b):
    """Add two numbers together."""
    return a + b


def add_multiple_numbers(*numbers):
    """Add any number of arguments together."""
    return sum(numbers)


def add_from_list(numbers_list):
    """Add all numbers in a list."""
    return sum(numbers_list)


if __name__ == "__main__":
    # Example 1: Adding two numbers
    result1 = add_two_numbers(5, 3)
    print(f"5 + 3 = {result1}")

    # Example 2: Adding multiple numbers
    result2 = add_multiple_numbers(10, 20, 30, 40)
    print(f"10 + 20 + 30 + 40 = {result2}")

    # Example 3: Adding from a list
    numbers = [1, 2, 3, 4, 5]
    result3 = add_from_list(numbers)
    print(f"Sum of {numbers} = {result3}")

    # Example 4: Adding different types of numbers
    result4 = add_multiple_numbers(15.5, 20.3, 10)
    print(f"15.5 + 20.3 + 10 = {result4}")

    def add_with_default(a, b=0):
    """Add two numbers with a default value for b."""
    return a + b
