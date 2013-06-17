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

def bubble(a):
    N=len(a)
    for i in range(0,N):
        for j in  range(0 ,N-i-1):
            if (a[j]>a[j+1]):
                t=a[j]
                a[j]=a[j+1]
                a[j+1]=t
    return a

if(__name__=='__main__'):
    print "bubble sort:"
    x=insert_elements()
    print"the unsorted elements are: "
    print x
    y=bubble(x)
    print"\nthe sorted elements are: "
    print y
    
