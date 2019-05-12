from base import train01


def test7():
    def add(*args):
        total = 0
        for val in args:
            total += val
        return total
    print(add(1, 3, 5, 7, 9))


if __name__ == '__main__':
    train01.test1()
    test2()