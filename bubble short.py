#this is bubble sort program
def bubble_sort(a):
    b=len(a)
    for j in range(b):
        c=1
        for i in range(0,b-1):
            #print(i,"end")
            if( a[i] > a[i+1] ):
                a[i],a[i+1]=a[i+1],a[i]
                #print(a[i]," , ",a[i+1])
                c=0
            elif( a[i] == a[i+1]):
                continue
            else:
                continue
    
    print(a)
bubble_sort([5,465,3,42,1,2,42,35,57,455321,1])
