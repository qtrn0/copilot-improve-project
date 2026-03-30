def calculate_difference(a, b):
    """Return absolute difference between two numbers."""
    return a - b if a > b else b - a

def add_sequence(base, count=10):
    """Add numbers from 0 to count-1 to base."""
    result = base
    for i in range(count):
        result += i
    return result

def process_pairwise_distances(data):
    """Calculate absolute differences between all pairs."""
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            result.append(abs(data[i] - data[j]))
    return result

def main():
    print(calculate_difference(5, 3))
    print(process_pairwise_distances([1, 4, 2, 5, 3]))

if __name__ == "__main__":
    main()