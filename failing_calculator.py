def divide_list(lst, divisor):
    result = []
    for item in lst:
        result.append(item / divisor)
    return result

def calculate_average(numbers):
    total = 0
    for n in numbers:
        total = total + n
    return total / len(numbers)

def main():
    print(divide_list([10, 5, 0], 0))
    print(calculate_average([]))

if __name__ == "__main__":
    main()