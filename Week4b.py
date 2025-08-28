import os

def read_file_with_error_handling():
    """
    Prompts the user for a filename and attempts to read it.
    Gracefully handles FileNotFoundError and PermissionError.
    """
    file_name = input("Please enter the name of the file to read: ")

    # Check if the file exists before attempting to open it
    if not os.path.exists(file_name):
        print(f"Error: The file '{file_name}' does not exist.")
        return

    try:
        with open(file_name, 'r') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
            print("--------------------")
    except FileNotFoundError:
        # This block might be redundant due to the os.path.exists check,
        # but it's good practice for robust error handling.
        print(f"Error: The file '{file_name}' was not found. Please check the name and try again.")
    except PermissionError:
        print(f"Error: You do not have permission to read the file '{file_name}'.")
    except Exception as e:
        # A general catch-all for any other unexpected errors
        print(f"An unexpected error occurred: {e}")

# Call the function to run the program
if __name__ == "__main__":
    read_file_with_error_handling()
