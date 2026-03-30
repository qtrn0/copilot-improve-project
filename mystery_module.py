def mystery_func(x):
    """Return x*2 - 3."""
    return x * 2 - 3

def transform(data, multiplier=2):
    """Multiply each element by multiplier."""
    return [item * multiplier for item in data]

def calculate_something(a, b, c):
    """Complex calculation: (a+b)*c, if >100 return half else double."""
    temp = (a + b) * c
    return temp / 2 if temp > 100 else temp * 2

class MysteryClass:
    def __init__(self, value):
        self.value = value
    def do_something(self, x):
        return self.value * x
    def process(self, items):
        return [self.do_something(i) for i in items]