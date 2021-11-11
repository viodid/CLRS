from numpy import random

"""
CLRS : Introduction to Algorithms
"""


def main():
    # creating random list
    myList = random.randint(10, size=20).tolist()
    solution = []  # to store some algorithms solutions
    # comparing input list vs output afterwards
    print(f"input: {myList}")
    # sorting functions (toggle True to apply)
    insertionSort(myList)
    selectionSort(myList)
    mergeSort(myList)
    existSum(myList, 2, solution)
    return_list = heapSort(myList)
    print(f"output:{myList}, {return_list}")


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


def existSum(Arr, v, solution, toggle=False):  # v = number to match
    def merge(Arr, left, right, v, solution):

        for k in range(len(Arr)):

            if len(left) == 0:
                Arr[k:] = right
                break

            elif len(right) == 0:
                Arr[k:] = left
                break

            elif left[0] <= right[0]:
                if left[0] + right[0] == v:
                    solution.append([left[0], right[0]])
                Arr[k] = left[0]
                left.remove(left[0])

            else:
                if right[0] + left[0] == v:
                    solution.append([left[0], right[0]])
                Arr[k] = right[0]
                right.remove(right[0])

    if toggle:
        if len(Arr) <= 1:
            return

        mid = len(Arr) // 2
        left = Arr[:mid]
        right = Arr[mid:]

        existSum(left, v, solution, True)
        existSum(right, v, solution, True)

        merge(Arr, left, right, v, solution)


def max_heapify(A, i):

    if i > len(A) // 2:
        return

    # Assuming array starts at 1
    root = A[i - 1]
    left = A[i * 2 - 1]
    # assuming last leaf is "right leaf orphan" i.e ony one child (left)
    try:
        right = A[i * 2]
    except IndexError:
        if left - root > 0:
            A[i - 1], A[i * 2 - 1] = A[i * 2 - 1], A[i - 1]
            max_heapify(A, i * 2)
        return

    # select the most significant leaf
    if (left - root) >= (right - root) and (left - root) > 0:
        A[i - 1], A[i * 2 - 1] = A[i * 2 - 1], A[i - 1]
        max_heapify(A, i * 2)

    elif (right - root) >= (left - root) and (right - root) > 0:
        A[i - 1], A[i * 2] = A[i * 2], A[i - 1]
        max_heapify(A, i * 2 + 1)

    return


def build_max_heap(Arr):
    for i in range(len(Arr) // 2, 0, -1):
        max_heapify(Arr, i)


a = [8, 7, 5, 1, 4, 9]
build_max_heap(a)
print(a)


def build_min_heap(Arr):
    for i in range(len(Arr) // 2, 0, -1):
        min_heapify(Arr, i)


""" Exercise 6.2-1 page 156
    [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]
"""

"""
    6.2-2
"""


def min_heapify(A, i):

    if i > len(A) // 2:
        return

    # Assuming array starts at 1
    root = A[i - 1]
    left = A[i * 2 - 1]
    # assuming last leaf is "right leaf orphan" i.e ony one child (left)
    try:
        right = A[i * 2]
    except IndexError:
        if left - root < 0:
            A[i - 1], A[i * 2 - 1] = A[i * 2 - 1], A[i - 1]
            min_heapify(A, i * 2)

        return

    if (left - root) <= (right - root) and (left - root) < 0:
        A[i - 1], A[i * 2 - 1] = A[i * 2 - 1], A[i - 1]
        min_heapify(A, i * 2)

    elif (right - root) <= (left - root) and (right - root) < 0:
        A[i - 1], A[i * 2] = A[i * 2], A[i - 1]
        min_heapify(A, i * 2 + 1)

    return


""" 
6.2-5
"""


def iter_max_heapify(A, i):

    while i <= len(A) // 2:

        root = A[i - 1]
        left = A[i * 2 - 1]
        try:
            right = A[i * 2]
        except IndexError:
            right = 0

        if (left - root) >= (right - root) and (left - root) > 0:
            A[i - 1], A[i * 2 - 1] = A[i * 2 - 1], A[i - 1]
            i *= 2

        elif (right - root) >= (left - root) and (right - root) > 0:
            A[i - 1], A[i * 2] = A[i * 2], A[i - 1]
            i = i * 2 + 1
        else:
            break


"""
6.4-1
"""


def heapSort(A):
    # initilize future final sorted list
    return_list = [None] * len(A)
    build_max_heap(A)
    # print(A)
    # i = length.heap decrement by 1 each loop iteration
    for i in range(len(A) - 1, -1, -1):
        # swap last heap element with the heap's root
        A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
        return_list[i] = A.pop()
        max_heapify(A, 1)
    return return_list


"""
exercise 6.5-1
"""


def heap_extract_max(A):
    if len(A) <= 1:
        raise IndexError
    max = A[0]
    # - 1 to access the last element in the list (len(list) out of range)
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    A.pop()
    max_heapify(A, 1)
    return max


heap = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]


arr2 = [5, 13, 2, 25, 7, 17, 20, 8, 4]


main()
