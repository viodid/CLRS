from numpy import random
import time

"""
CLRS : Introduction to Algorithms
"""


class customError(Exception):
    pass


def main():
    # creating random list
    # myList = random.randint(2, size=4).tolist()
    # insertionSort(myList)
    # selectionSort(myList)
    # mergeSort(myList)
    # print(f"output:{myList}")
    return 0


"""
Exercises page 22

2.1-2
"""


def insertionSort(myList):

    for i in range(1, len(myList)):
        key = myList[i]
        j = i - 1
        while j >= 0 and myList[j] > key:
            myList[j + 1] = myList[j]
            j -= 1
        myList[j + 1] = key

    return None
    """
    Θ(n^2), Ω(n)
    """


"""
Exercises page 29

2.2-1
#Θ(n^3)


2.2-2
"""


def selectionSort(myList):
    for j in range(len(myList) - 1):
        number = myList[j]
        for i in range(j + 1, len(myList)):
            if number > myList[i]:
                number = myList[i]
        myList[myList.index(number, j)] = myList[j]
        myList[j] = number

    return None


"""
Θ(n^2)
The last element is already sorted when the secnod last element is sorted in selection sort.
Ω(n^2), Θ(n^2)
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


def mergeSort(Arr):

    if len(Arr) <= 1:
        return

    mid = len(Arr) // 2
    left = Arr[:mid]
    right = Arr[mid:]

    mergeSort(left)
    mergeSort(right)

    merge(Arr, left, right)

    return None


def binarySearch(myList, v):
    c = len(myList) // 2  # c = center of the list
    if v == myList[c]:
        return "found"
    elif len(myList) == 1:
        return None
    elif v < myList[c]:
        return binarySearch(myList[:c], v)
    elif v > myList[c]:
        return binarySearch(myList[c + 1 :], v)
    """Θ(logn), 
        Ω(1)"""


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


""" ---------------- HEAP SORT ---------------- """


def max_heapify(A, i):
    # assuming array starts at index 0
    # if index i is bigger than the parent of the last leaf, stop recursion
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
Exercise 6.5-7
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

    @classmethod
    def pop(cls, A):
        return cls.mapping[heap_extract_max(A)]


class Queue:
    counter = 0
    mapping = {}

    def __init__(self, name):
        self.name = name

    def push(self, A):
        Queue.counter += 1
        min_heap_insert(A, self.counter)
        Queue.mapping[self.counter] = self.name

    @classmethod
    def pop(cls, A):
        return cls.mapping[heap_extract_min(A)]


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
  a. No, because in max-heap-insert we are inserting the elements into the heap through the last branch/node and with 
  max-heapify we are iterating through every element and changing them in their array position. That makes a different
  distribution of the heap.
"""

"""
Problem 6-2
  a. parent: (index - 1) // d
     child: (parentIndex * d_ary) + leaf_node([0...d_ary - 1])
  b. 1log(d)n
"""


def d_ary_max_heapify(A, i, d):
    # assuming array starts at index 0
    # if index i is bigger than the parent of the last leaf, stop recursion
    if i > (len(A) // 2) - 1:
        return

    parent = i
    # store child - parent value
    difference = 0
    # most significant leaf
    mostSignificant = None
    # child node
    try:
        for j in range(1, d + 1):
            child = (parent * d) + j
            # select the most significant leaf
            if A[child] - A[parent] > difference:
                difference = A[child] - A[parent]
                mostSignificant = child
    except IndexError:
        pass
    # swap values
    if mostSignificant:
        A[mostSignificant], A[parent] = A[parent], A[mostSignificant]
        d_ary_max_heapify(A, mostSignificant, d)

    return


def build_max_d_heap(A, d):
    for i in range((len(A) - 1) // 2, -1, -1):
        d_ary_max_heapify(A, i, d)


def d_ary_heap_extract_max(A, d):
    if len(A) <= 1:
        raise customError("array must be longer than 1")
    maximum = A[0]
    A[0], A[len(A) - 1] = A[len(A) - 1], A[0]
    A.pop()
    d_ary_max_heapify(A, 0, d)
    return maximum


"""
d. Θ(logd n)
"""


def d_ary_max_heap_insert(A, key, d):
    # assuming positive natural numbers list
    A.append(-1)
    d_ary_heap_increase_key(A, len(A) - 1, key, d)


"""
e. Θ(logd n)
"""


def d_ary_heap_increase_key(A, i, key, d):

    if len(A) <= 0:
        raise customError("array must be longer than 0")

    if key < A[i]:
        raise customError("new key is smaller than current key")

    A[i] = key

    def d_ary_heap_increase_key_recursive(A, i, key, d):

        if i <= 0:
            return

        currentNode = i
        parentNode = (i - 1) // d

        if A[parentNode] < A[currentNode]:
            A[currentNode], A[parentNode] = A[parentNode], A[currentNode]
            d_ary_heap_increase_key_recursive(A, parentNode, key, d)

        return

    d_ary_heap_increase_key_recursive(A, i, key, d)

    return


"""
Problem 6-3
a. 
2 - 3 - 4 - 5
8 - 9 - 12- 14
16- ∞ - ∞ - ∞
∞ - ∞ - ∞ - ∞

b. If the top left element is ∞, then all the elements on the first row need to be ∞. 
But if this is the case, all other elements need to be ∞ because they are larger than the first element on their column.

If the bottom right element is smaller than ∞, all the elements on the bottom row need to be smaller than ∞.
But so are the other elements in the tableau, because each is smaller than the bottom element of its column.
"""

""" ---------------- QUICK SORT ---------------- """

"""Exercise 7.1-1"""

A = [13, 19, 9, 5, 12, 8, 7, 4, 21, 2, 6, 11]


def partition(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] <= x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    return i + 1


"""
Exercise 7.1-2
    The value of q would be r, when all values in the array A[p..q] have the same value.
"""


def partition_same_value(A, p, r):
    x = A[r]
    i = p - 1
    for j in range(p, r):
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]
    A[r], A[i + 1] = A[i + 1], A[r]
    if p - 1 == i:
        return (p + r) // 2
    return i + 1


"""
Exercise 7.1-4
    Flip the condition on line 4. From <= to >=.
"""

"""
Exercise 7.2-2
    O(n**2), since one of the partitions is always empty.
"""

"""
Exercise 7.2-3
    In a hypothetical array sorted in decreasing order, the pivot would be the smallest number in the array.
    Therefore, one partition would be always empty. O(n**2)
"""

"""
Exercise 7.2-4
    Instead of resorting the whole array, insertion sort would pick the unordered elements and put them in order. O(n)
"""

"""
Exercise 7.3-1
    Because of the property of randomness, makes no sense to expect one unique case throughout the outputs.
"""

"""
Exercise 7.3-2
    Θ(n)
"""


def quickSort(A, p, r):
    if p < r:
        q = partition(A, p, r)
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)

    return None
    """Θ(nlogn)
        O(n^2)
        Ω(nlogn)"""


"""
Exercise 7.4-5
"""


def quickSortInsertion(A, p, r):
    if p < r - 2:
        q = partition(A, p, r)
        quickSortInsertion(A, p, q - 1)
        quickSortInsertion(A, q + 1, r)
    return None


def quickSortInsertionSort(A, p, r):
    quickSortInsertion(A, p, r)
    insertionSort(A)
    return None


""" ---------------- COUNTING SORT ---------------- """


def countingSort(
    A,  # A -> input array
    B,  # B -> sorted array,
    k,  # k -> the largest element in array A
):
    C = [0] * (k + 1)
    B = [None] * len(A)
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    for i in range(len(A) - 1, -1, -1):
        B[C[A[i]] - 1] = A[i]
        C[A[i]] = C[A[i]] - 1
    return B
    """Θ(k + n)"""


"""
Exercise 8.2-1
A = [6,0,2,0,1,3,4,6,1,3,2]
C = [2,2,2,2,1,0,2]
--------------------------
C=[2,4,6,8,9,9,11]
--------------------------
B=[0,0,0,0,0,2,0,0,0,0,0] -> [0,0,0,0,0,2,0,3,0,0,0] -> [0,0,0,1,0,2,0,3,0,0,0] -> [0,0,0,1,0,2,0,3,0,0,6]
C=[2,4,5,8,9,9,11]        -> [2,4,5,7,9,9,11]        -> [2,3,5,7,9,9,11]        -> [2,3,5,7,9,9,10]
and so on.
"""

"""
Exercise 8.2-3
The algorithms still works properly but it is no longer stable since repeated numbers don't preserve their first order.
"""

"""
Exercise 8.2-4
"""


def prepocess(A, k):
    C = [0] * (k + 1)
    for i in range(len(A)):
        C[A[i]] = C[A[i]] + 1
    for i in range(1, k + 1):
        C[i] += C[i - 1]
    return C


def howManyRange(A, k, a, b):  # a - b numbers range in the array A
    C = prepocess(
        A, k
    )  # array containing the number of integers less than or equal to C[i]
    return C[b] - C[a]


# t0 = time.time()
# A = random.randint(50, size=100).tolist()
print(howManyRange([6, 0, 2, 0, 1, 3, 4, 6, 1, 3, 2], 6, 0, 6))
# mergeSort(A)
# t1 = time.time()
# total = t1 - t0
# print(total)


""" ---------------- RADIX SORT ---------------- """

"""
Exercise 8.3-1
COW SEA TAB BAR
DOG TEA BAR BIG
SEA MOB EAR BOX
RUG TAB TAR COW
ROW RUG SEA DIG
MOB DOG TEA DOG
BOX DIG DIG EAR
TAB BIG BIG FOX
BAR BAR MOB MOB
EAR EAR DOG NOW
TAR TAR COW ROW
DIG COW ROW RUG
BIG ROW NOW SEA
TEA NOW BOX TAB
NOW BOX FOX TAR
FOX FOX RUG TEA
"""

"""
Exercise 8.3-2

"""


if __name__ == "__main__":
    main()
