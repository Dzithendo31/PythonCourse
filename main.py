r = int(input("Enter %:"))
R = r//10
strg = "="*R
print(f"[{strg:<10}]")

#version 02
space = " "*(10 - R)
print(f"[{strg}{space}]")
quote = "wdwvwqfwfqfwdqqfq"
print(quote[-2:-1])
#I need more Code
# Example 1: Basic string slicing
my_string = "Hello, World!"
slice_result = my_string[7:12]
print(slice_result)  # Output: World

# Example 2: Omitting start or stop
start_slice = my_string[:5]  # Equivalent to my_string[0:5]
end_slice = my_string[7:]    # Equivalent to my_string[7:len(my_string)]
print(start_slice)  # Output: Hello
print(end_slice)    # Output: World!

# Example 3: Negative indices
last_five_chars = my_string[-5:]  # Last five characters
print(last_five_chars)  # Output: World!

# Example 4: Slicing with a step
every_second_char = my_string[::2]
print(every_second_char)  # Output: Hlo o!

# Example 5: Reversing a string
reverse_string = my_string[::-1]
print(reverse_string)  # Output: !dlroW ,olleH