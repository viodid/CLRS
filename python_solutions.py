from numpy import random

"""
CLRS : Introduction to Algorithms
"""


def main():
    # creating random list
    myList = random.randint(5, size=16).tolist()
    # comparing input list vs output afterwards
    print(f"input: {myList}")
    # sorting functions (toggle True to apply)
    insertionSort(myList)
    selectionSort(myList)
    print(f"output:{myList}")


"""
Exercises page 22

2.1-2
"""


def insertionSort(myList, toggle=False):
    if toggle:
        for i in range(1, len(myList)):
            key = myList[i]
            j = i - 1
            while j >= 0 and myList[j] < key:
                myList[j + 1] = myList[j]
                j -= 1
            myList[j + 1] = key
        """
        Θ(n**2), Ω(n)
        """
    return None


"""
Exercises page 29

2.2-1
#Θ(n**3)


2.2-2
    """


def selectionSort(myList, toggle=False):
    if toggle:
        for j in range(len(myList) - 1):
            number = myList[j]
            for i in range(j + 1, len(myList)):
                if number > myList[i]:
                    number = myList[i]
            myList[myList.index(number, j)] = myList[j]
            myList[j] = number
    return None


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

"""
Exercises page 37 - 39

2.3-2
"""


def merge(myList, toggle=False):

    """
    merge(A*[p, q, r**])
    n1 = q - p + 1
    n2 = r - q


    *Array
    **indices such that p <= q < r assuming that the subarrays A[p...q] and A[q+1...r] are in sorted order.
    """


main()
