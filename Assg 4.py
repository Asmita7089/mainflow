#25. Find Missing Number
def find_missing_number(arr):
    n = len(arr)  
    total_sum = (n + 1) * (n + 2) // 2  
    actual_sum = sum(arr)  
    return total_sum - actual_sum  

arr = [1, 2, 4, 5, 6]  
print(find_missing_number(arr))  

#26. Check Balanced Parentheses
def is_balanced(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['} 

    for char in s:
        if char in mapping:  
            top = stack.pop() if stack else '#'  
            if mapping[char] != top:  
                return False
        else:
            stack.append(char) 
    return not stack  

print(is_balanced("({[]})"))  
print(is_balanced("({[})"))  

#27. Longest Word in a Sentence
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)  

print(longest_word("Find the longest word in this sentence"))  

#28. Count Words in a Sentence
def count_words(sentence):
    return len(sentence.split())  

print(count_words("Count the number of words here"))  

#29. Check Pythagorean Triplet
def is_pythagorean_triplet(a, b, c):
    a, b, c = sorted([a, b, c])  
    return a ** 2 + b ** 2 == c ** 2

print(is_pythagorean_triplet(3, 4, 5))  
print(is_pythagorean_triplet(5, 12, 13))  

#30. Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

print(bubble_sort([5, 1, 4, 2, 8]))  

#31. Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1 

print(binary_search([1, 2, 3, 4, 5, 6], 4))  

#32. Find Subarray with Given Sum
def subarray_sum(arr, S):
    left, curr_sum = 0, 0

    for right in range(len(arr)):
        curr_sum += arr[right]  
        while curr_sum > S:  
            curr_sum -= arr[left]
            left += 1
        if curr_sum == S:
            return (left, right) 

    return -1  

print(subarray_sum([1, 4, 20, 3, 10, 5], 33)) 


