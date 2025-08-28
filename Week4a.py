# Part 1: File Read & Write Challenge

# Open the input file for reading ('r')
with open('input.txt', 'r') as file_in:
    # Read the entire content of the file
    content = file_in.read()

# Convert the content to uppercase
modified_content = content.upper()

# Open the output file for writing ('w')
with open('output.txt', 'w') as file_out:
    # Write the modified content to the new file
    file_out.write(modified_content)

print("File successfully modified and written to 'output.txt'.")
