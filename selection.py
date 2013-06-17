#!/usr/bin/python
def insert_elements():
    a=[]
    print "enter the numbers :"
    print "-1 is the escape character"
    while(1):
        x=int(raw_input())
        if(x== -1):
            break
        a.append(x)
    return(a)

def selection(a):
    N=len(a)
   
    for i in range(0,N):
        min=i
        for j in  range(i,N):
            if (a[j]<a[min]):
                min=j
        temp=a[min]
        a[min]=a[i]
        a[i]=temp
          
    return a

if(__name__=='__main__'):
    print "Selection sort:"
    
    x=insert_elements()
    print "the unsorted elements are:"
    print x
    y=selection(x)
    print"\nthe sorted elements are: "
    print y
