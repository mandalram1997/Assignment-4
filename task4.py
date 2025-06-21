#task 1
try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

    #task 2
    # Task 1: Write user input to a file
try:
    with open('output.txt', 'w') as file:
        user_input = input("Enter some text to write to the file: ")
        file.write(user_input + '\n')
    print("Data written to 'output.txt'.")
except Exception as e:
    print(f"An error occurred while writing to the file: {e}")

# Task 2: Append additional data to the same file
try:
    with open('output.txt', 'a') as file:
        additional_data = input("Enter additional text to append to the file: ")
        file.write(additional_data + '\n')
    print("Additional data appended to 'output.txt'.")
except Exception as e:
    print(f"An error occurred while appending to the file: {e}")

# Task 3: Read and display the final content of the file
try:
    with open('output.txt', 'r') as file:
        print("\nFinal content of 'output.txt':")
        for line in file:
            print(line.strip())
except Exception as e:
    print(f"An error occurred while reading the file: {e}")