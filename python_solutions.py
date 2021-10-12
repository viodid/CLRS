from numpy import random


def main():
    """
    CLRS : Introduction to Algorithms

    Exercises page 22

    2.1-2
    """
    LIST = random.randint(20, size=100).tolist()
    for i in range(1, len(LIST)):
        key = LIST[i]
        j = i - 1
        while j >= 0 and LIST[j] < key:
            LIST[j + 1] = LIST[j]
            j -= 1
        LIST[j + 1] = key

    print(LIST)

    """
    ------

    Exercises page 29

    2.2-1
    #O(n^3)

    -------

    2.2-2
    """

    for i in range(2, len(LIST)):
        number = LIST[i]
        if number > LIST[i - 1]:
            number = LIST[i - 1]


main()
