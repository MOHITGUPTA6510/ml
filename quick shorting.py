# Quick Sorting

def quick_sort(a):

    if(len(a)<=1):
        return a
    #last elemet as pivot
    last_element=a[len(a)//2]

    left =[]
    right=[]
    middle=[]

    b=len(a)
    for i in range(0,b):
        if( a[i]<last_element):
            left.append(a[i])
        elif(a[i]>last_element):
            right.append(a[i])
        else:
            middle.append(a[i])
    return quick_sort(left) + middle + quick_sort(right)

a = [3,6,8,10,1,2,1,34,2,132,5,46,674]
sort_list = quick_sort(a)
print("Sorted list : ", sort_list)
