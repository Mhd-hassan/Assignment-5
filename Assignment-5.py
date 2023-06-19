# In Python Take input from the user of 5 numbers and store it in a list.
ls=[] # Creating an empty list
n=int(input("Enter the value of element : ")) # No of element as input
for i in range(0,n):
    ele=int(input())
    ls.append(ele)
print(ls)
"""
Output of Take input from the user of 5 numbers and store it in a list:
Enter the value of element : 5
10
30
20
50
40
[10, 30, 20, 50, 40]
"""
# In Python calculate the sum of all the elements in the list
total=sum(ls)
print("Sum of all the elements in the list is : ",total)
"""
Output of calculate the sum of all the elements in the list:
Sum of all the elements in the list is :  150
"""
# In Python find the smallest number in the list
small=min(ls)
print("Smallest number in the list is : ",small)
"""
Output of find the smallest number in the list:
Smallest number in the list is :  10
"""
# In Python find the largest number in the list
large=max(ls)
print("Largest number in the list is : ",large)
"""
Output of find the largest number in the list:
Largest number in the list is :  50
"""
# In Python display the list in ascending order
ls.sort()
print("Number in ascending order are : ",ls)
"""
Output of display the list in ascending order:
Number in ascending order are :  [10, 20, 30, 40, 50]
"""
# In Python display the list in descending order
ls.sort(reverse=True)
print("Number in descending order are : ",ls)
"""
Output of display the list in descending order:
Number in descending order are :  [50, 40, 30, 20, 10]
"""
# In Python Convert list into tuple
tuple_lst=tuple(ls)
print("Converting list into tuple and the output is : ",tuple_lst)
"""
Output of Convert list into tuple:
Converting list into tuple and the output is :  (50, 40, 30, 20, 10)
"""
# In Python Delete the list
del ls
print("The list is deleted sucessfully.")
"""
Output of Delete the list:
The list is deleted sucessfully.
"""
"""
Output of entire program:
Enter the value of element : 5
10
30
20
50
40
[10, 30, 20, 50, 40]
Sum of all the elements in the list is :  150
Smallest number in the list is :  10
Largest number in the list is :  50
Number in ascending order are :  [10, 20, 30, 40, 50]
Number in descending order are :  [50, 40, 30, 20, 10]
Converting list into tuple and the output is :  (50, 40, 30, 20, 10)
The list is deleted sucessfully.
"""