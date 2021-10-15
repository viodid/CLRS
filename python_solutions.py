from numpy import random


def main():
    """
    CLRS : Introduction to Algorithms

    Exercises page 22

    2.1-2
    """
    myList = random.randint(20, size=100).tolist()
    for i in range(1, len(myList)):
        key = myList[i]
        j = i - 1
        while j >= 0 and myList[j] < key:
            myList[j + 1] = myList[j]
            j -= 1
        myList[j + 1] = key

    # print(myList)
    # Θ(n**2), Ω(n)

    """
    ------

    Exercises page 29

    2.2-1
    #Θ(n**3)


    2.2-2
    """
    myList = random.randint(5, size=20).tolist()
    # print("input:", myList)

    for j in range(len(myList) - 1):
        number = myList[j]
        for i in range(j + 1, len(myList)):
            if number > myList[i]:
                number = myList[i]
        myList[myList.index(number, j)] = myList[j]
        myList[j] = number

    # print("\noutput:", myList)
    """
    Θ(n**2)
    The last element is already sorted when the secnod last element is sorted in selection sort.
    Ω(n**2), Θ(n**2)
    """

    """
    2.2-3
    Θ(n)

    2.2-4
    For a good best-case running time, modify an algorithm to first randomly produce output and 
    then check whether or not it satisfies the goal of the algorithm. If so, produce this output and halt.
    """


main()
