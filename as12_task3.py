
def my_sort(numbers):
    """Sort a list in ascending order using selection sort.

    Args:
        numbers (list): The list of numbers to sort. The list is
            modified in place.

    Returns:
        tuple: A tuple containing the sorted list and the number
            of element comparisons performed.
    """
    comparisons = 0
    n = len(numbers)

    for i in range(n):
        smallest = i

        for j in range(i + 1, n):
            comparisons += 1

            if numbers[j] < numbers[smallest]:
                smallest = j

        numbers[i], numbers[smallest] = numbers[smallest], numbers[i]

    return numbers, comparisons
# списки для проверки метода
short_list = [5, 2, 9, 1]
long_list = [23, 1, 45, 12, 8, 34, 2, 19, 7, 15]

sorted_short, comp_short = my_sort(short_list)
print(sorted_short, comp_short)

sorted_long, comp_long = my_sort(long_list)
print(sorted_long, comp_long)