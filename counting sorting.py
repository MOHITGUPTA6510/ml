# Counting Sorting

def counting_sort(a):
    sec_a=[]
    #print(max_val)
    while (len(a) > 0):
        b=len(a)
        min_val=min(a)
    #   print(max_val)
        count=a.count(min_val)
        for i in range(0,count):
            a.remove(min_val)
            sec_a.append(min_val)
       
    print(sec_a)

unsort=[12,43,56,7,435,6,7,5332,54,365,34,5,45,2,453]
counting_sort(unsort)
