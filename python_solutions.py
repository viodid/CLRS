from numpy import random

"""
CLRS : Introduction to Algorithms
"""


def main():
    # creating random list
    myList = random.randint(5, size=30).tolist()
    # comparing input list vs output afterwards
    print(f"input: {myList}")
    # sorting functions (toggle True to apply)
    insertionSort(myList)
    selectionSort(myList)
    mergeSort(myList, True)
    print(f"output:{myList}")


# [p=4, 5, q=6, q+1=1, 2, r=3]

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
Exercises page 37

2.3-22
"""


def merge(Arr, left, right):

    """
    merge(A*[p, q, r**])
    n1 = q - p + 1
    n2 = r - q
    let L[n1] and R[n2] be new arrays
    for i = 0 to n1
        L[i] = A[p + i]
    for j = 0 to n2
        R[i] = A[q + j]

    for k = p to r
        if L.lenght is 0
            A[k..n] = R
        else if R.lenght is 0
            A[k..n] = L
        else if L[0] <= R[0]
            A[k] = L[0]
            remove L[0] element from L
        else
            A[k] = R[0]
            remove R[0] element from R
    *Array
    **indices such that p <= q < r assuming that the subarrays A[p...q] and A[q+1...r] are in sorted order.
    """
    for k in range(len(Arr)):

        if len(left) == 0:
            Arr[k:] = right
            break

        elif len(right) == 0:
            Arr[k:] = left
            break

        elif left[0] <= right[0]:
            Arr[k] = left[0]
            left.remove(left[0])

        else:
            Arr[k] = right[0]
            right.remove(right[0])


def mergeSort(Arr, toggle=False):

    """
    Exercises page 39

    2.3-5
    """
    if toggle:
        if len(Arr) <= 1:
            return

        mid = len(Arr) // 2
        left = Arr[:mid]
        right = Arr[mid:]

        mergeSort(left, True)
        mergeSort(right, True)

        merge(Arr, left, right)
    return None


def binarySearch(myList, v):
    """
    A[a1, a2...an] sorted secuence
    v = number to match

    ### Recursive ###
    n = A.length
    if v == A[n / 2]:
        return "found"
    else if A.length == 1:
        return NULL
    else if v < A[n/2]:
        return binarySearch(A[0...n/2])
    else if v > A[n/2];
        return binarySearch(A[n/2...n])

    ### Iterative ###
    Create a copy of the secuence
    A1 = A.copy
    n = A1.length
    while true:
        if v == A1[n / 2]:
            return "found"
        else if A1.length == 1:
            return NULL
        else if v < A1[n/2]:
            A1.drop(A1[n/2...n])
        else if v > A1[n/2];
            A1.drop(A1[0...n/2])
    """
    c = len(myList) // 2  # c = center of the list
    if v == myList[c]:
        return "found"
    elif len(myList) == 1:
        return None
    elif v < myList[c]:
        return binarySearch(myList[:c], v)
    elif v > myList[c]:
        return binarySearch(myList[c + 1 :], v)
    # Θ(logn), Ω(1)


"""
Exercise 2.3-7⋆
"""


def existSum(myList, v):  # v = number to match
    pass


main()
