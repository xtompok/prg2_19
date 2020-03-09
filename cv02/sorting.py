import random

def random_list(n):
    return [chr(random.randrange(65,65+26)) for _ in range(n)]


# Sort list using select sort
def select_sort(alist):
    # Until list is sorted
        # Select minimum from unsorted part
        # Swap minimum with first unsorted element
    return alist

# Sort list using quick sort
def quick_sort(alist):
    qs(alist,0,len(alist))

def qs(alist,l,r):
    # Check if list is long enough
    # Choose pivot
    # call presort_list
    # Prepare inidices to the left and right part
    # Recursively sort left and right part


def presort_list(alist,l,r,pivot):
    # move right index to the left by one

    # while True:
        # While left index < (right boundary-1) and left element <= pivot:
            # move left index to the right
        # While right index > left boundary and right element >= pivot:
            # move right index to the left
        # if left index >= right index
            # break
        # swap elements on left and right index
    #return (right index, left index) # in the end, right index <= left index

alist = random_list(20)
blist = alist[:] # Copy all elements, not only reference
print(alist)
print(select_sort(alist))
quick_sort(blist)
print(blist)