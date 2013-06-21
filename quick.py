#!/usr/bin/python
def insert_elements():
    print "Do you want to enter numbers Manually(Yes - 1/ No- 0):?"
    x=input()
    a=[]
    if(x==0):
        a=[3,2,4,5,9,6,7,1,5,7,31,2,-1,4,1,2,3,1,2,1,3]
    elif(x==1):
        print "please enter input: "
        print "press -1 to exit "
        x=input()
        while(x!= -1):
            a.append(x)
            x=input()
    else:
        print "Not a avalid input"
    return a

def lop(a,l,r):
    p=0
    N=len(a)
    if(l<r):
        print "########################"
        x=a[l]   
        print "l r ",(l,r)
        p=l+1
        q=r
        print a
        flag=False      
        while(p<q and p<N and q>0):        
            if(x>=a[p]):
                p=p+1
                print ">"
            elif(x<=a[q]):
                q=q-1
                print "<"
            elif(x<a[p]and x>a[q] and p<q):
                if(a[p]>a[q]):
                    temp=a[p]
                    a[p]=a[q]
                    a[q]=temp                                          
                print "interchanged", a
                      
            print " p,q" ,(p,q,a[p],a[q])
        
        if(p>=q and flag==False):
            if(x>a[p]):
                pass
            else:
                p=p-1
            
        print "element",x," inserted at pos.",p
        temp=a[p]
        a[p]=x
        a[l]=temp
        mid=p
       
        lop(a,l,mid-1)
        lop(a,mid+1,r)
        print a

        
if(__name__=='__main__'):
    a=insert_elements()
    print "\n the array elements are:"
    print a
    N=len(a)
    lop(a,0,N-1)
    print " "
    print " "
    print "the sorted array "
    print a

    

