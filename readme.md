Q1: To sort a already sorted list{A} and an unsorted list {B} so that {A+B} is sorted:

Ans: Since the list {B} is unsorted , mixing it with {A} makes {A+B}unsorted. In the case if insertion sort is employed: 
1. the user has to find the minimum value element in the 2nd list {B}.
2. The min. value element found has to be compared with the elements of the 1st list until its suitable position is found.
3. When the position of element is found, the elements of {A} after the position  has to be moved right .
4. Remove the previously found min. value element from the 2nd list and go back to step 1.

Whereas , if bubble sort is employed , :
1. the entire set {A} & {B} can be assumed to be merged together to form a single unsorted list {A+B}
2. The unsorted list {A+B} has then to be bubble sorted using the bubble sort algorithm

----------------------------------------------------------------------
-----------------------------------------------------------------------

Q2: To sort a already sorted list{A} and another sorted list {B} so that{A+B} is sorted:

Ans:Here since list{A},{B} is already sorted , insertion sort is much preferred. 
1. Initially a pointer,say i  is set to 0. 
2. Since {B} is already sorted ,the user has to consider the ith index element of {B} as minimum value element .
3. The min. value element  has to be compared with the elements of the 1st list,{A} until its suitable position is found.
4. When the position of element is found, the elements of {A}, after the found position,  has to be shifted right .
5. Increment the pointer i and go back to step 2 .Repeat the same till i<len{B}


-----------------------------------------------------------------------
-------------------------------------------------------------------------
Q3: To sort a already sorted list{A} where single elements are being added by the user .

Ans:If we consider bubble sort , the method becomes to complex. Every time a new element is added , the entire list has to be rearranged. In this case ,it involves rearranging all the elements of the list to just order one new element.Hence this might not be a good way to sort elements.

Whereas, if we consider insertion sort, the new added element has to be compared with the elements already present in the list until a suitable postion of it is found. When a suitable position is found the elements to the right need to be shifted .This procedure is quite suitable, since it might not involve rearranging of  all elements of {A} .

But if we consider the selection sort, the new element is compared with the elements already present in the list .If a suitable position is found ,the element at that position is interchanged to last .This might not be a good sorting in this case , since here the elements of already sorted list are misplaced , hence calling the need to be sorted again . 




