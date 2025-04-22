# selection sort program
def selection_sort(a):
    b=len(a)
    for i in range(0,b-1):
        min_value=i
        for j in range( i+1,b):
            if( a[j] < a[min_value] ):
                min_value=j
        value=a.pop(min_value)
        a.insert(i,value)
    print(a)
selection_sort([64,34,25,5,22,11,90,12])

        
