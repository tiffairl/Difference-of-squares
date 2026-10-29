"""To find the difference between the square of a sum, and the sum of que squares of the first N natural numbers."""

def square_of_sum(number):
    """First 10 natural numbers."""
    total = sum(range(1, number + 1))
    return total ** 2


def sum_of_squares(number):
    """Leads up to 385."""
    return sum(value ** 2 for value in range(1, number + 1))


def difference_of_squares(number):
    """Solution is 2640."""
    return square_of_sum(number) - sum_of_squares(number)