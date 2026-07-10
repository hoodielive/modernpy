def calculate_sum(numbers):
    return sum(numbers)

initial_list = [1, 2, 3, 4, 5]

print(calculate_sum(initial_list))

def calculate_area(length, width):
    area = length * width
    return area

print(calculate_area(5, 4))

# String Reversal
astring = "Larry"


def reverse_string(input_string):
    reverse_string = input_string[::-1]
    return reverse_string


print(reverse_string("Larry"))

# anagram finder
def are_anagrams(string1, string2):
    string1_cleaned_sorted = sorted(string1.replace(" ", "").lower())
    string2_cleaned_sorted = sorted(string2.replace(" ", "").lower())
    return string1_cleaned_sorted == string2_cleaned_sorted

are_anagrams("silent", "listen")
