# #  Consider a list (list = []). You can perform the following commands:
# 1-insert i e: Insert integer e at i position .
# 2-print: Print the list.
# 3-remove e: Delete the first occurrence of integer e.
# 4-append e: Insert integer e at the end of the list.
# 5-sort: Sort the list.
# 6-pop: Pop the last element from the list.
# 7-reverse: Reverse the list.
# Initialize your list and read in the value of n followed by n lines of commands where each command will be of the 7 types listed above.
#  Iterate through each command in order and perform the corresponding operation on your list.
# Example
# N = 4
# append 1
# append 2
# append 31
# print
#  append 1: append 1 to the list,arr=[1] .
#  append 2: append 2 to the list,arr=[1, 2] .
#  append 31: Insert 3 at index 1,arr=[1, 2, 3] .
# print: Print the array.
# Output:
# [1, 3, 2]
# Input Format
# The first line contains an integer, , denoting the number of commands.
# Each line  of the  subsequent lines contains one of the commands described above.
# Constraints
# The elements added to the list must be integers.
# Output Format
# For each command of type print, print the list on a new line.






if __name__ == "__main__":
    # Initialize the list
    lst = []
    
    # Read the number of commands
    n = int(input())
    
    # Iterate through each command
    for _ in range(n):
        command = input().strip().split()
        
        # Determine the command and execute the corresponding operation
        if command[0] == "insert":
            index = int(command[1])
            element = int(command[2])
            lst.insert(index, element)
        elif command[0] == "print":
            print(lst)
        elif command[0] == "remove":
            element = int(command[1])
            lst.remove(element)
        elif command[0] == "append":
            element = int(command[1])
            lst.append(element)
        elif command[0] == "sort":
            lst.sort()
        elif command[0] == "pop":
            lst.pop()
        elif command[0] == "reverse":
            lst.reverse()





# Given an integer,n , and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hasht(t).
# Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
# Input Format
# The first line contains an integer,n , denoting the number of elements in the tuple.
# The second line contains n space-separated integers describing the elements in tuple t.
# Output Format
# Print the result of hasht(t).
# Sample Input 0
# 2
# 1 2
# Sample Output 0
# 3713081631934410656







if __name__ == "__main__":
    # Read the integer n
    n = int(input().strip())
    
    # Read the n space-separated integers
    elements = list(map(int, input().strip().split()))
    
    # Convert the list to a tuple
    t = tuple(elements)
    
    # Compute the hash of the tuple
    result = hash(t)
    
    # Print the result
    print(result)




# Integers in Python can be as big as the bytes in your machine's memory. There is no limit in size as there is:2^31-1  (c++ int) or 2^63-1(C++ long long int).
# As we know, the result of a^b grows really fast with increasing b.
# Let's do some calculations on very large integers.
# Task
# Read four numbers, a, b, c, and d, and print the result of a^b+ c^d .
# Input Format
# Integers a, b, c, and d are given on four separate lines, respectively.
# Constraints
# 1<= a <=1000
# 1<= b <= 1000
# 1<= c <= 1000
# 1<= d <= 1000
# Output Format
# Print the result of a^b + c^d on one line.
# Sample Input
# 9
# 29
# 7
# 27
# Sample Output

# 4710194409608608369201743232  








if __name__ == "__main__":
    # Read the four integers from input
    a = int(input().strip())
    b = int(input().strip())
    c = int(input().strip())
    d = int(input().strip())
    
    # Calculate a^b
    power1 = a ** b
    
    # Calculate c^d
    power2 = c ** d
    
    # Sum the two results
    result = power1 + power2
    
    # Print the result
    print(result)


