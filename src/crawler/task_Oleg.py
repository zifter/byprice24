A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def iterate_left(A):
    if not A:
        return
    else:
        first = A[0]
        print(first)
        A = A[1:]
        iterate_left(A)

iterate_left(A)

def iterate_right(A):
    if not A:
        return
    else:
        first = A[-1]
        print(first)
        A = A[:-1]
        iterate_right(A)

iterate_right(A)

# def iterate(A, first=None):
#     if first == None:
#         first = len(A) - 1
#     if first > 0:
#         iterate(A, first - 1)
#     print(A[first])
#
# iterate(A)

B = [i for i in range(1000)]
print(B)
iterate_left(B)
