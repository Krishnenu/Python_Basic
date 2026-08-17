list1 = [2, 3, 5, 4, 3, 4, 6, 8, 75, 323]

def secondLargest(l):
    first = 0
    second = 0
    
    for i in range(len(l)):       
        if l[i] > first:
            second = first 
            first = l[i]    
        elif l[i] > second and l[i] < first:
            second = l[i]  
    return second
         
print(secondLargest(list1))