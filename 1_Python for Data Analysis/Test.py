tabSorted=[1,2,3,4,5,6,7,8,9]
k=0

def BinarySearch(array,a,b, searchValue):
    if(a<=b):
        mid=(a+b)//2
        if(array[mid]==searchValue):
            k=mid
            return 1, k
        elif(array[mid]>searchValue):
            BinarySearch(array, a, mid-1, searchValue)
        else:
            BinarySearch(array, mid+1, b, searchValue)
    return -1

print(BinarySearch(tabSorted,0,len(tabSorted)-1, 7))
