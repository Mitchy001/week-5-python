# file_handling_assignment.py

def create_file():
    try:
        # Create a new text file in write mode
        with open("my_file.txt", "w") as file:
            file.write("Hello, World!\n")  # String
            file.write("This is line two.\n")  # String
            file.write("12345\n")  # Number as a string
        print("File created and data written successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error while creating the file: {e}")
    finally:
        print("Finished attempting to create the file.")

def read_file():
    try:
        # Read the contents of the file
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File content:")
            print(content)
    except FileNotFoundError:
        print("Error: The file does not exist.")
    except PermissionError as e:
        print(f"Error while reading the file: {e}")
    finally:
        print("Finished attempting to read the file.")

def append_to_file():
    try:
        # Open the file in append mode
        with open("my_file.txt", "a") as file:
            file.write("Appending line four.\n")  # String
            file.write("Appending line five.\n")  # String
            file.write("67890\n")  # Number as a string
        print("Data appended successfully.")
    except (PermissionError, IOError) as e:
        print(f"Error while appending to the file: {e}")
    finally:
        print("Finished attempting to append to the file.")

# Execute the functions
create_file()
read_file()
append_to_file()
read_file()  # Read again to show the updated content
