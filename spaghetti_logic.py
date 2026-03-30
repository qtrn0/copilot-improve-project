def do_all(a,b):
    x = a+b
    if a>b:
        x = a-b
    for i in range(10):
        x = x+i
    return x

def process_data(data):
    result = []
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] > data[j]:
                result.append(data[i] - data[j])
            else:
                result.append(data[j] - data[i])
    return result

def main():
    print(do_all(5, 3))
    print(process_data([1, 4, 2, 5, 3]))

if __name__ == "__main__":
    main()