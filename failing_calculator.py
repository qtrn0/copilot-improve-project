def divide_list(lst, divisor):
    if divisor == 0:
        return "Error: Division by zero"
    return [item / divisor for item in lst]

def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

def main():
    print(divide_list([10, 5, 0], 0))
    print(calculate_average([]))

if __name__ == "__main__":
    main()