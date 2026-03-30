def mystery_func(x):
    return x * 2 - 3

def transform(data, multiplier=2):
    result = []
    for item in data:
        result.append(item * multiplier)
    return result

def calculate_something(a, b, c):
    temp = (a + b) * c
    if temp > 100:
        return temp / 2
    else:
        return temp * 2

class MysteryClass:
    def __init__(self, value):
        self.value = value
    
    def do_something(self, x):
        return self.value * x
    
    def process(self, items):
        return [self.do_something(i) for i in items]