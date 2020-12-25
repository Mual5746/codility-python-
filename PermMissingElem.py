def solution(A):
    # write your code in Python 3.6
    N = len(A) #length is the amount of elements in array
    missing_element = -1
    #n+2 because of index = 0 and index = N
    # one for index 0 and one for the missing element
    #the lenght:  5, A = [1, 4, 5, 3, 6]
    #                 [0, 1, 0, 0, 0, 0, 0]
    # index is        [0, 1, 2, 3, 4, 5, 6]
    List_to_compare = [0]*(N+2)
    print ("the lenght: ", N, A)
    for index in range(0, N): #range is from 0-5
        #for loop couint to = 4
       # print(A[index])
       #A[index] == the element of A at index 
       #if there is a number in A at index 
       # take the numer as index in  List_to_compare
       #and change the 0 to 1 at the that index
        List_to_compare [A[index]] +=1
        print (List_to_compare)
    #check which index is equal to 0     
    for index in range(1, N+1):
      if List_to_compare[index] == 0:
         missing_element = index
    
    print("the missing nummer: " , missing_element)
    return missing_element


A = [1, 4, 5, 3, 6]
solution(A)
