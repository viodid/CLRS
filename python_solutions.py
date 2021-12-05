from typing import Counter
from numpy import e, random

"""
CLRS : Introduction to Algorithms
"""


class customError(Exception):
    pass


def main():
    # creating random list
    myList = random.randint(2, size=4).tolist()
    solution = []  # to store some algorithms solutions
    # comparing input list vs output afterwards
    # print(f"input: {myList}")
    # sorting functions (toggle True to apply)
    insertionSort(myList)
    selectionSort(myList)
    mergeSort(myList)
    existSum([1, 7, 9, 4], 5, solution)
    # return_list = heapSort(myList)
    # print(f"output:{solution}")


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


"""
Exercises page 39

2.3-5
"""


def mergeSort(Arr, toggle=False):

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
    # assuming array starts at index 0
    # if index i is bigger than the parent of the last leaf
    if i > (len(A) // 2) - 1:
        return

    root = i
    left = (i * 2) + 1

    # assuming last leaf is "right leaf orphan" i.e ony one child (left)
    try:
        right = (i + 1) * 2
        A[right]
    except IndexError:
        if A[left] - A[root] > 0:
            A[root], A[left] = A[left], A[root]
        return

    # select the most significant leaf
    if (A[left] - A[root]) >= (A[right] - A[root]) and (A[left] - A[root]) > 0:
        A[root], A[left] = A[left], A[root]
        max_heapify(A, left)

    elif (A[right] - A[root]) >= (A[left] - A[root]) and (A[right] - A[root]) > 0:
        A[root], A[right] = A[right], A[root]
        max_heapify(A, right)

    return


def build_max_heap(Arr):
    for i in range((len(Arr) - 1) // 2, -1, -1):
        max_heapify(Arr, i)


def build_min_heap(Arr):
    for i in range((len(Arr) - 1) // 2, -1, -1):
        min_heapify(Arr, i)


""" Exercise 6.2-1 page 156
    [27, 17, 10, 16, 13, 9, 1, 5, 7, 12, 4, 8, 3, 0]
"""

"""
    6.2-2
"""


def min_heapify(A, i):
    # assuming array starts at index 0
    if i > (len(A) // 2) - 1:
        return

    root = i
    left = (i * 2) + 1
    # assuming last leaf is "right leaf orphan" i.e ony one child (left)
    try:
        right = (i + 1) * 2
        A[right]
    except IndexError:
        if A[left] - A[root] < 0:
            A[root], A[left] = A[left], A[root]
        return

    # select the most significant leaf
    if (A[left] - A[root]) <= (A[right] - A[root]) and (A[left] - A[root]) < 0:
        A[root], A[left] = A[left], A[root]
        min_heapify(A, left)

    elif (A[right] - A[root]) <= (A[left] - A[root]) and (A[right] - A[root]) < 0:
        A[root], A[right] = A[right], A[root]
        min_heapify(A, right)

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
    # i = length.heap decrement by 1 each loop iteration
    for i in range(len(A) - 1, -1, -1):
        # swap last heap element with the heap's root
        A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
        return_list[i] = A.pop()
        print(A, Stack.mapping)
        max_heapify(A, 0)

    return return_list


"""
exercise 6.5-1
"""


def heap_extract_max(A):
    if len(A) <= 1:
        raise customError("array must be longer than 1")
    maximum = A[0]
    # - 1 to access the last element in the list (len(list) out of range)
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    A.pop()
    max_heapify(A, 0)
    return maximum


def heap_increase_key(A, i, key):

    if len(A) <= 0:
        raise customError("array must be longer than 0")

    if key < A[i]:
        raise customError("new key is smaller than current key")

    A[i] = key

    def heap_increase_key_recursive(A, i, key):

        if i <= 0:
            return

        currentNode = i
        parentNode = ((i + 1) // 2) - 1

        if A[parentNode] < A[currentNode]:
            A[currentNode], A[parentNode] = A[parentNode], A[currentNode]
            heap_increase_key_recursive(A, parentNode, key)

        return

    heap_increase_key_recursive(A, i, key)

    return


def max_heap_insert(A, key):
    # assuming positive natural numbers list
    A.append(-1)
    heap_increase_key(A, len(A) - 1, key)


"""
Exercise 6.5-2
"""
heap = [15, 13, 9, 5, 12, 8, 7, 4, 0, 6, 2, 1]

"""
Exercise 6.5-3
"""


def heap_minimun(A):
    build_min_heap(A)
    return A[0]


def heap_extract_min(A):
    if len(A) <= 1:
        raise customError("array must be longer than 1")
    build_min_heap(A)
    minimun = A[0]
    # - 1 to access the last element in the list (len(list) out of range)
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    A.pop()
    min_heapify(A, 0)
    return minimun


def min_heap_insert(A, key):

    build_min_heap(A)

    def heap_decrease_key(A, i, key):
        if len(A) <= 0:
            raise customError("array must be longer than 0")

        if key > A[i]:
            raise customError("new key is bigger than current key")

        A[i] = key

        def heap_decrease_key_recursive(A, i, key):

            if i <= 0:
                return

            currentNode = i
            parentNode = ((i + 1) // 2) - 1

            if A[parentNode] > A[currentNode]:
                A[currentNode], A[parentNode] = A[parentNode], A[currentNode]
                heap_decrease_key_recursive(A, parentNode, key)

            return

        heap_decrease_key_recursive(A, i, key)

        return

    # assuming positive natural numbers list
    A.append(1000000)  # I don't like it but...
    heap_decrease_key(A, len(A) - 1, key)


"""
Exercise 6.5-4

To not break the heap property and to have two different functions working fine both together and alone.
"""

"""
Execise 6.5-7
"""


class Stack:
    counter = 0
    mapping = {}

    def __init__(self, name):
        self.name = name

    def push(self, A):
        Stack.counter += 1
        max_heap_insert(A, self.counter)
        Stack.mapping[self.counter] = self.name

    @staticmethod
    def pop(A):
        return Stack.mapping[heap_extract_max(A)]


class Queue:
    counter = 0
    mapping = {}

    def __init__(self, name):
        self.name = name

    def push(self, A):
        Queue.counter += 1
        min_heap_insert(A, self.counter)
        Queue.mapping[self.counter] = self.name

    @staticmethod
    def pop(A):
        return Queue.mapping[heap_extract_min(A)]


"""
6.5-8
"""


def heap_delete(A, i):

    if len(A) <= 0:
        raise customError("array must be longer than 0")
    # exchange current index/node with the last element/node
    A[i], A[len(A) - 1] = A[len(A) - 1], A[i]
    # delete last element (node we want to remove)
    A.pop()
    # restart the heap property
    max_heapify(A, i)
    # O(log n) time complexity


"""
Problem 6-1
  a. No, because in max-heap-insert we are inserting the elements into the heap through the last branch/node and in max-heapify 
  we are iterating through every element and changing them in their array position.
"""

main()
