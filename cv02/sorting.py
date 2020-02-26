import random

def random_list(n):
    return [random.randrange(0,1000) for _ in range(n)]


# Sort list using select sort
def select_sort(alist):
    # Until list is sorted
        # Select minimum from unsorted part
        # Swap minimum with first unsorted element
    return alist

alist = random_list(20)
print(alist)
print(select_sort(alist))