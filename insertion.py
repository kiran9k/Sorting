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

def insertion(a):
    N=len(a)
    for i in range(N):
        for j in  range(i):
            if (a[j]>a[j+1]):
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    return a

if(__name__=='__main__'):
    print "insertion sort:"
    
    x=insert_elements()
    print "the unsorted elements are:"
    print x
    y=insertion(x)
    print"\nthe sorted elements are: "
    print y
    

