def parent(i):
    return int(i/2) - 1

def left(i):
    return (2*i) + 1

def right(i):
    return (2*i) + 2

def maxHeapify(A, i):
    global heapSize
    l = left(i)
    r = right(i)
    if l < heapSize and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < heapSize and A[r] > A[largest]:
        largest = r

    if largest != i:
        temp = A[i]
        A[i] = A[largest]
        A[largest] = temp
        maxHeapify(A, largest)

def buildMaxHeap(A):
    global heapSize
    heapSize = len(A)
    for i in range(heapSize, -1, -1):
        maxHeapify(A,i)

def heapSort(A):
    global heapSize
    buildMaxHeap(A)
    for i in range(len(A)-1, 0, -1):
        temp = A[0]
        A[0] = A[i]
        A[i] = temp
        heapSize = i
        maxHeapify(A,0)

from random import randint
A = list()
for i in range(10):
    A.append(randint(0,10))

print(A)
heapSort(A)
print(A)