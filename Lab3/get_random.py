from random import randrange

def get_random(number, min, max):
    return [randrange(min, max+1) for i in range(number)]

if __name__ == "__main__":
    print(get_random(10, 1, 5))