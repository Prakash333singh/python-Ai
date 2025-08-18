userName="prakash singh"
print(userName.upper())
print(len(userName))
print(userName[0])
print(userName[-1])
print(userName[0:6]) #slicing
print(type(userName))
num =10;
nums=num*20

print(type(nums));

print(userName);

name="prakash"
age = 21
print(f"My name is {name} and I am {age} years old.")


print(10>5)

fruits=['apple', 'banana', 'cherry']
print(fruits[0])  # Accessing the first element 
print(fruits[-1])  # Accessing the last element
print(fruits[1:3])  # Slicing to get elements from index 1 to 2
print(fruits[1:])  # Slicing to get elements from index 1 to
print(fruits[:2])  # Slicing to get the first two elements
print(fruits[-2:])  # Slicing to get the last two elements
fruits.append('orange')  # Adding a new element
print(fruits)  # Displaying the updated list
print(fruits.count('banana'))  # Counting occurrences of 'banana'
print(fruits.index('cherry'))  # Finding the index of 'cherry'
print(fruits.pop())  # Removing and returning the last element
fruits.remove('banana')  # Removing 'banana' from the list
print(fruits)  # Displaying the list after removal

print(fruits.sort())  # Sorting the list in place
print(fruits)  # Displaying the sorted list

print(fruits.reverse())  # Reversing the list in place
print(fruits)  # Displaying the reversed list
print(fruits.clear())  # Clearing the list
print(fruits)  # Displaying the cleared list


nums = [1, 2, 3, 4]
# print(nums[::-1])       # reverse [4, 3, 2, 1]
print(nums[1])
print(nums.reverse())       # reverse [4, 3, 2, 1]
print(nums)              # display [4, 3, 2, 1]
print(nums + [5, 6])    # concatenation
print(nums)


coords=(10,20,30) #tuple
print(coords[0])


nums={1,2,2,3,4,5}
# print(nums)

a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)   # Union {1,2,3,4,5}
print(a & b)   # Intersection {3}
print(a - b)   # Difference {1,2}
