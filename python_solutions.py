from numpy import random

"""
CLRS : Introduction to Algorithms
"""


def main():
    # creating random list
    myList = random.randint(5, size=1).tolist()
    # comparing input list vs output afterwards
    # print(f"input: {myList}")
    # sorting functions (toggle True to apply)
    insertionSort(myList)
    selectionSort(myList)
    merge([2, 3, 4, 5, 6])
    print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 20, 31, 42, 55, 70], 1))
    # print(f"output:{myList}")


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


def merge(myList):

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
            A[k] = R[0..n2]
        else if R.lenght is 0
            A[k] = L[0..n1]
        else if L[0] <= R[0]
            A[k] = L[0]
            remove L[0] element from L
        else
            A[k] = R[0]
            remove R[0] element from R
    *Array
    **indices such that p <= q < r assuming that the subarrays A[p...q] and A[q+1...r] are in sorted order.
    """
    # handle center of the list
    c = float(len(myList)) / 2  # center of the list
    if c % 2 != 0:
        c += 0.5
    c = int(c)
    n1 = c  # number of items firs half of the list
    n2 = len(myList) - c  # number of items second half of the list
    L = [None] * n1  # initialize left and right list
    R = [None] * n2
    # populate lists
    for i in range(n1):
        L[i] = myList[i]
    for j in range(n2):
        R[j] = myList[j + c]
    # sort and merge both lists
    for k in range(len(myList)):
        if len(L) == 0:
            myList[k:] = R
            break
        elif len(R) == 0:
            myList[k:] = L
            break
        elif L[0] <= R[0]:
            myList[k] = L[0]
            L.remove(L[0])
        else:
            myList[k] = R[0]
            R.remove(R[0])

    """
    Exercises page 39

    2.3-5
    """


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
    print(myList)
    if len(myList) % 2 != 0:
        c = int((len(myList) / 2) - 0.5)  # c = center of the list
    else:
        c = int(len(myList) / 2)

    if v == myList[c]:
        return "found"
    elif len(myList) == 1:
        return None
    elif v < myList[c]:
        # del myList[n:]
        return binarySearch(myList[:c], v)
    elif v > myList[c]:
        # del myList[:n]
        return binarySearch(myList[c + 1 :], v)


main()
