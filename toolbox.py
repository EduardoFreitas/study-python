def exterior(n):
    """ Example of inner function """

    def inner(x):
        return n * x

    return inner


def default_value(number, pow=2):
    """ Example of default value"""
    return number ** pow


def count(*args):
    """ Example of args"""
    sum_all = 0
    for i in args:
        sum_all += i

    return sum_all


def print_all(**kwargs):
    for key, value in kwargs.items():
        print('Key: {} - Value: {}'.format(key, value))


def print_all_names(name, age=5):
    print('name: {} - age: {}'.format(name, age))


if __name__ == '__main__':
    square = exterior(2)
    print(square(3))

    print('default: {} - add value {} '.format(default_value(2), default_value(2, 4)))

    print(count(1, 2, 3, 4, 5))
    print_all(name='Fulano', age=15)
    print_all_names(name='Fulano 1')
    print_all_names(name='Fulano 2', age=22)
    print_all_names('Fulano 3', 25)
