#!/usr/bin/python
import math

def insert_elements():
    print "Do you want to enter numbers Manually(Yes - 1/ No- 0):?"
    x=input()
    a=[]
    if(x==0):
        a=[3,2,4,5,9,1,3]
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



def append(a):
    ######################################################
    #appending large numbers to the list to make it a power of 2
    #####################################################
    N=len(a)
    y=0
    if(N>0):
        global y
        y=float(math.log(N)/(math.log(2)))
        y=math.ceil(y)
        while((2**y) > N):
            a.append(9999)
            N=len(a)
    return(a)



def merge(a):    
    global y
    y=int(y)
    print y
    i=1
    l=0
    m=2**i
    x=2**i
    b=[]
    N=len(a)
    if(N==1):
        return a
    flag=True
    for i in range (1,y+1):
        #the sorted numbers are stored in list b  
        l=0
        m=2**i
        x=2**i
        flag1=True
        print"#######################################"
        print "m  & l :",(m,l)
        if(flag==True):        
            print "the unsorted list at the stage ",i,"is:"
            print a
            while(flag==True and m<=N):
                p=l
                q=m-(x/2)
                print "p & q",(p,q)
                while((p<(m-(x/2))) and q< m):
                    #global b
                    if(a[p]<a[q]):
                        b.append(a[p])
                        p=p+1                   
                    else :
                        b.append(a[q])
                        q=q+1
                while( q<m):
                    b.append(a[q])
                    q=q+1
                while(p<(m-(x/2))):
                    b.append(a[p])
                    p=p+1
                l=m
                m=m+x
                print b
            flag1=False
            flag=False
    
        else:
            #the sorted numbers are stored in list a
            a=[]          
            print "the unsorted list at the stage ",i,"is:"
            print b
            if(flag1==True):
                while(m<=N):
                    p=l
                    q=m-(x/2)
                    print "p & q",(p,q)
                    while((p<(m-(x/2))) and q< m):
                        
                        if(b[p]<b[q]):
                            a.append(b[p])
                            p=p+1
                
                        else :
                            a.append(b[q])
                            q=q+1
               
                    while( q<m):
                        a.append(b[q])
            
                        q=q+1
                    while(p<(m-(x/2))):
                        a.append(b[p])
                        p=p+1
                    l=m
                    m=m+x
                    print a
            b=[]
            flag=True
            

    if(i%2==0):
        print "done"
        return a
    else :
        print "done"
        print i
        print b
        return b
    


    
if(__name__=='__main__'):
    a=insert_elements()
    N=len(a)
    y=0
    
    print "the input array is:"
    print a
    a=append(a)    
    print "The input array after appending some numbers"
    print a
    a=merge(a)
    print"#############################"
    print("sorted array is:")
    print a
    

        
            
            

