#1Write a code to reverse a string

#code

str = "Python"
print(str[::-1])


#2Write a code to count the number of vowels in a string

#code

def count_vowels(string):
    vowels = "aeiouAEIOU"
    return sum(1 for char in string if char in vowels)


text = "The quick brown fox jumps over a lazy dog"
vowel_count = count_vowels(text)
print(f"Number of vowels in '{text}' : {vowel_count}")


#3Write a code to check if a given string is a palindrome or not

#code

def is_palindrome(s):
    
    
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    return cleaned == cleaned[::-1]


string_to_check = "A man, a plan, a canal, Panama"
if is_palindrome(string_to_check):
    print(f'"{string_to_check}" is a palindrome.')
else:
    print(f'"{string_to_check}" is not a palindrome.')




#4Write a code to check if two given strings are anagrams of each other

#code

def are_anagrams(str1, str2):

    str1 = str1.replace("" , "").lower()
    str2 = str2.replace("" , "").lower()

    return sorted(str1) == sorted(str2)

#given string
str1 = "cinema"
str2 = "iceman"

if are_anagrams(str1, str2):
    print(f"'{str}' and '{str2}' are anagrams.")
else:
    print(f"'{str1}' and '{str2}' are not anagrams")




#5Write a code to find all occurrences of a given substring within another string

#code

def find_all_occurrences(string, substring):
    start = 0
    positions = []
    
    while True:
        
        start = string.find(substring, start)
        
        if start == -1:  
            break
        
        
        positions.append(start)
        
        
        start += 1
    
    return positions


string = "This is a test. This is only a test."
substring = "test"

positions = find_all_occurrences(string, substring)

if positions:
    print(f"Substring '{substring}' found at positions: {positions}")
else:
    print(f"Substring '{substring}' not found.")




#6Write a code to perform basic string compression using the counts of repeated characters

#code

def compress_string(s):
    if not s:
        return s
    
    compressed = []
    count = 1
    

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1  
        else:
          
            compressed.append(s[i - 1] + str(count))
            count = 1 
    
    
    compressed.append(s[-1] + str(count))
    
    
    compressed_str = ''.join(compressed)
    

    return compressed_str if len(compressed_str) < len(s) else s

string = "aaabbbccaa"
compressed_string = compress_string(string)
print(f"Original: {string}")
print(f"Compressed: {compressed_string}")



#7Write a code to determine if a string has all unique characters

#code

def has_unique_characters(s):
    
    seen = set()
    
    
    for char in s:
       
        if char in seen:
            return False
       
        seen.add(char)
    
   
    return True


string = "abcdefg"
print(f"Does '{string}' have all unique characters? {has_unique_characters(string)}")

string = "aabbcc"
print(f"Does '{string}' have all unique characters? {has_unique_characters(string)}")




#8Write a code to convert a given string to uppercase or lowercase

#code

def convert_case(s, to_upper=True):
    if to_upper:
        return s.upper()  
    else:
        return s.lower()  


string = "Hello World!"


upper_string = convert_case(string, to_upper=True)
print(f"Uppercase: {upper_string}")

lower_string = convert_case(string, to_upper=False)
print(f"Lowercase: {lower_string}")




#9Write a code to count the number of words in a string

#code

def count_words(s):
    
    words = s.split()
    return len(words)


string = "The quick brown fox jump over the lazy dog"
word_count = count_words(string)
print(f"Number of words: {word_count}")




#10Write a code to concatenate two strings without using the + operator

#code

def concatenate_strings(str1, str2):
    return ''.join([str1, str2])


string1 = "Hello"
string2 = "Python"
result = concatenate_strings(string1, string2)
print(f"Concatenated string: {result}")




#11Write a code to remove all occurrences of a specific element from a list

#code

def remove_occurrences(lst, element):
    while element in lst:
        lst.remove(element)
    return lst


my_list = [1, 2, 3, 4, 2, 5, 2]
element_to_remove = 2
result = remove_occurrences(my_list, element_to_remove)
print(f"List after removal: {result}")




#12Implement a code to find the second largest number in a given list of integers

#code

def find_second_largest(lst):
    if len(lst) < 2:
        return None
    
   
    first = second = float('-inf')
    
    for num in lst:
        if num > first:
            second = first  
            first = num  
        elif num > second and num != first:
            second = num  
    
    
    if second == float('-inf'):
        return None
    
    return second


numbers = [12, 35, 1, 10, 34, 1]
second_largest = find_second_largest(numbers)
print(f"The second largest number is: {second_largest}")




#13Create a code to count the occurrences of each element in a list and return a dictionary with elements as keys and their counts as values

#code

from collections import Counter

def count_occurrences(lst):
    return dict(Counter(lst))


my_list = [1, 2, 2, 3, 3, 3, 4]
result = count_occurrences(my_list)
print(result)



#14Write a code to reverse a list in-place without using any built-in reverse functions

#code

def reverse_list_in_place(lst):
    
    start, end = 0, len(lst) - 1
  
    while start < end:
       
        lst[start], lst[end] = lst[end], lst[start]
       
        start += 1
        end -= 1

my_list = [1, 2, 3, 4, 5]
reverse_list_in_place(my_list)
print(f"Reversed list: {my_list}")




#15Implement a code to find and remove duplicates from a list while preserving the original order of elements

#code

def remove_duplicates(lst):
    seen = set()  
    result = []   
    
    for item in lst:
        
        if item not in seen:
            result.append(item)  
            seen.add(item)       
            return result


my_list = [1, 2, 2, 3, 4, 3, 5]
result = remove_duplicates(my_list)
print(f"List after removing duplicates: {result}")




#16Create a code to check if a given list is sorted (either in ascending or descending order) or not

#code

def is_sorted(lst):

    ascending = all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))
    
 
    descending = all(lst[i] >= lst[i + 1] for i in range(len(lst) - 1))
    
   
    if ascending:
        return "Ascending"
    elif descending:
        return "Descending"
    else:
        return "Not Sorted"


my_list1 = [1, 2, 2, 3, 4]
my_list2 = [5, 4, 3, 2, 1]
my_list3 = [1, 3, 2, 4]

print(f"List 1 is: {is_sorted(my_list1)}") 
(f"List 2 is: {is_sorted(my_list2)}") 
print(f"List 3 is: {is_sorted(my_list3)}") 




#17Write a code to merge two sorted lists into a single sorted list

#code

def merge_sorted_lists(list1, list2):
    
    i, j = 0, 0
    merged_list = [ ]
    
   
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
    
    
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
    
    
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    
        return merged_list


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
result = merge_sorted_lists(list1, list2)
print(f"Merged sorted list: {result}")




#18Implement a code to find the intersection of two given lists

#code

def find_intersection(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    
    
    return list(set1 & set2)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = find_intersection(list1, list2)
print(f"Intersection: {result}")




#19Create a code to find the union of two lists without duplicates

#code

def union_of_lists(list1, list2):
  
    set1 = set(list1)
    set2 = set(list2)
    
    
    union_set = set1 | set2  
    
    
    return list(union_set)


list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
result = union_of_lists(list1, list2)
print(f"Union of lists: {result}")




#20Write a code to shuffle a given list randomly without using any built-in shuffle functions

#code

import random

def shuffle_list(lst):
    
    n = len(lst)
    
    for i in range(n - 1, 0, -1): 
        j = random.randint(0, i)
        
       
    lst[i], lst[j] = lst[j], lst[i]
    
    return lst


my_list = [1, 2, 3, 4, 5]
shuffled_list = shuffle_list(my_list)
(f"Shuffled list: {shuffled_list}")




#21Write a code that takes two tuples as input and returns a new tuple containing elements that are common to both input tuples

#code

def common_elements(tuple1, tuple2):
    
    set1 = set(tuple1)
    set2 = set(tuple2)
    
    
    common_set = set1.intersection(set2)
    
    
    return tuple(common_set)


tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)

result = common_elements(tuple1, tuple2)
print(result)  




#22Create a code that prompts the user to enter two sets of integers separated by commas. Then, print the intersection of these two sets

#code

def get_set_from_input(prompt):

    user_input = input(prompt)
    

    int_list = [int(x.strip()) for x in user_input.split(',')]
    
    
    return set(int_list)

def main():
    
    set1 = get_set_from_input("Enter the first set of integers separated by commas: ")
    set2 = get_set_from_input("Enter the second set of integers separated by commas: ")
    
    
    intersection = set1.intersection(set2)
    
    
    print(f"The intersection of the two sets is: {intersection}")

if __name__ == "__main__":
    main()




#23Write a code to concatenate two tuples. The function should take two tuples as input and return a new tuple containing elements from both input tuples

#code

def concatenate_tuples(tuple1, tuple2):
 
    result_tuple = tuple1 + tuple2
    return result_tuple


tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)

result = concatenate_tuples(tuple1, tuple2)
print(result) 



#24Develop a code that prompts the user to input two sets of strings. Then, print the elements that are present in the first set but not in the second set

#code

def get_set_from_input(prompt):
   
    user_input = input(prompt)
    
    
    string_set = {x.strip() for x in user_input.split(',')}
    
    
    return string_set

def main():

    set1 = get_set_from_input("Enter the first set of strings separated by commas: ")
    set2 = get_set_from_input("Enter the second set of strings separated by commas: ")
    

    difference = set1.difference(set2)
    

    print(f"The elements in the first set but not in the second set are: {difference}")

if __name__ == "__main__":
    main()




#25Create a code that takes a tuple and two integers as input. The function should return a new tuple containing elements from the original tuple within the specified range of indices

#code

def extract_range_from_tuple(original_tuple, start, end):
  
                if start < 0 or end > len(original_tuple) or start > end:
                        raise ValueError("Invalid index range")
    
   
                        return original_tuple[start:end]


original_tuple = (10, 20, 30, 40, 50, 60, 70, 80)


start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))


try:
    new_tuple = extract_range_from_tuple(original_tuple, start_index, end_index)
    print(f"The new tuple is: {new_tuple}")
except ValueError as e:
    print(e)





#26Write a code that prompts the user to input two sets of characters. Then, print the union of these two sets

#code

def get_set_from_input(prompt):
    
    user_input = input(prompt)
    
   
    char_set = set(user_input.strip())
    
  
    return char_set

def main():

    set1 = get_set_from_input("Enter the first set of characters: ")
    set2 = get_set_from_input("Enter the second set of characters: ")
    

    union_set = set1.union(set2)
    

    print(f"The union of the two sets is: {union_set}")

if __name__ == "__main__":
    main()




#27Develop a code that takes a tuple of integers as input. The function should return the maximum and minimum values from the tuple using tuple unpacking

#code

def find_max_min(values_tuple):
    
    max_val, min_val = max(values_tuple), min(values_tuple)
    
  
    return max_val, min_val

def main():
    
    user_input = input("Enter a tuple of integers separated by commas: ")
    
   
    values_tuple = tuple(map(int, user_input.split(',')))
    
   
    max_val, min_val = find_max_min(values_tuple)
    

    print(f"The maximum value is: {max_val}")
    print(f"The minimum value is: {min_val}")

if __name__ == "__main__":
    main()





#28Create a code that defines two sets of integers. Then, print the union, intersection, and difference of these two sets

#code

def main():
    
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    
    union_set = set1.union(set2)
    
   
    intersection_set = set1.intersection(set2)
    
  
    difference_set = set1.difference(set2)
    

    print(f"Union of the two sets: {union_set}")
    print(f"Intersection of the two sets: {intersection_set}")
    print(f"Difference of set1 and set2 (set1 - set2): {difference_set}")

if __name__ == "__main__":
    main()




#29Write a code that takes a tuple and an element as input. The function should return the count of occurrences of the given element in the tuple

#code

def count_occurrences(input_tuple, element):

                return input_tuple.count(element)

def main():

    user_input = input("Enter a tuple of integers separated by commas: ")
    

    input_tuple = tuple(map(int, user_input.split(',')))
    

    element = int(input("Enter the element to count: "))
    

    occurrences = count_occurrences(input_tuple, element)
    

    print(f"The element {element} appears {occurrences} time(s) in the tuple.")

if __name__ == "__main__":
    main()




#30Develop a code that prompts the user to input two sets of strings. Then, print the symmetric difference of these two sets

#code


def get_set_from_input(prompt):

    user_input = input(prompt)
    

    string_set = {x.strip() for x in user_input.split(',')}
    
 
    return string_set

def main():

    set1 = get_set_from_input("Enter the first set of strings (separated by commas): ")
    set2 = get_set_from_input("Enter the second set of strings (separated by commas): ")

    symmetric_diff = set1.symmetric_difference(set2)
    

    print(f"The symmetric difference of the two sets is: {symmetric_diff}")

if __name__ == "__main__":
    main()




#31Write a code that takes a list of words as input and returns a dictionary where the keys are unique words and the values are the frequencies of those words in the input list


#code

def count_word_frequencies(word_list):
   
    word_freq = {}
    
   
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    

    return word_freq

def main():

    user_input = input("Enter a list of words separated by spaces: ")
    
  
    word_list = user_input.split()
    
  
    word_frequencies = count_word_frequencies(word_list)
    

    print("Word frequencies:", word_frequencies)

if __name__ == "__main__":
    main()





#32Write a code that takes two dictionaries as input and merges them into a single dictionary. If there are common keys, the values should be added together

#code

def merge_dictionaries(dict1, dict2):
 
    merged_dict = dict1.copy() 
    
  
    for key, value in dict2.items():
        if key in merged_dict:
            
            merged_dict[key] += value
    else:
            
        merged_dict[key] = value
    

        return merged_dict

def main():
  
    dict1_input = input("Enter the first dictionary (in the form of key:value pairs, separated by commas): ")
    dict2_input = input("Enter the second dictionary (in the form of key:value pairs, separated by commas): ")
    
    
    dict1 = dict(map(lambda x: x.split(":"), dict1_input.split(",")))
    dict2 = dict(map(lambda x: x.split(":"), dict2_input.split(",")))
    
   
    dict1 = {k: int(v) for k, v in dict1.items()}
    dict2 = {k: int(v) for k, v in dict2.items()}
    
    
    merged_dict = merge_dictionaries(dict1, dict2)
    
    
    print("The merged dictionary is:", merged_dict)

if __name__ == "__main__":
    main()





#33Write a code to access a value in a nested dictionary. The function should take the dictionary and a list of keys as input, and return the corresponding value. If any of the keys do not exist in the dictionary, the function should return None

#code

def access_nested_dict(dictionary, keys):
    
    for key in keys:
       
        if isinstance(dictionary, dict) and key in dictionary:
             dictionary = dictionary[key]
        else:
           
                return None
 
    return dictionary

def main():
   
    nested_dict = {
        'a': {
            'b': {
                'c': 10
            },
            'd': 20
        },
        'e': 30
    }

    keys_input = input("Enter a list of keys separated by commas: ")
    
 
    keys = keys_input.split(",")

    result = access_nested_dict(nested_dict, keys)
    
   
    print(f"The value for the given keys is: {result}")

if __name__ == "__main__":
    main()




#34Write a code that takes a dictionary as input and returns a sorted version of it based on the values. You can choose whether to sort in ascending or descending order

#code

def sort_dict_by_value(input_dict, descending=False):
  
    sorted_dict = dict(sorted(input_dict.items(), key=lambda item: item[1], reverse=descending))
    return sorted_dict

def main():
    
    user_input = input("Enter a dictionary (key:value pairs) separated by commas: ")
    
   
    input_dict = dict(map(lambda x: x.split(":"), user_input.split(",")))
    
   
    input_dict = {k: int(v) for k, v in input_dict.items()}
    
    
    order_input = input("Do you want to sort in ascending or descending order? (a/d): ").strip().lower()
    
  
    if order_input == 'd':
        sorted_dict = sort_dict_by_value(input_dict, descending=True)
        print("Dictionary sorted in descending order:", sorted_dict)
    else:
        sorted_dict = sort_dict_by_value(input_dict, descending=False)
        print("Dictionary sorted in ascending order:", sorted_dict)

if __name__ == "__main__":
    main()




#35Write a code that inverts a dictionary, swapping keys and values. Ensure that the inverted dictionary correctly handles cases where multiple keys have the same value by storing the keys as a list in the inverted dictionary

#code


def invert_dictionary(input_dict):
    inverted_dict = {}
    
   
    for key, value in input_dict.items():
        
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            
            inverted_dict[value] = [key]
    
    return inverted_dict

def main():
  
    user_input = input("Enter a dictionary (key:value pairs) : ")
    
   
    input_dict = dict(map(lambda x: x.split(":"), user_input.split(",")))
    
    
    inverted_dict = invert_dictionary(input_dict)
    
    
    print("Inverted dictionary:", inverted_dict)

if __name__ == "__main__":
    main()






