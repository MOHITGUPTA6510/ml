# Insertion Sorting

def insertion_sort(a):
    b=len(a)
    for i in range(0,b):
        index=i
        pop_value=a.pop(i)
        for j in range(i-1,-1,-1):
            if ( a[j] > pop_value):
                index = j
        a.insert(index , pop_value)

    print(a)
insertion_sort([64,34,25,12,22,11,90,334,2,1,43,12,6,8,9,67,9784,643623,1,1,5])
        
