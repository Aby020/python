input_string = input("Enter a string: ")
first_char = input_string[0]
modified_string = first_char + input_string[1:].replace(first_char, '$')
print("Modified string:", modified_string)