def create_and_modify_file():
    try:
        # Try to open the source file
        with open("input_file.txt", "r") as infile:
            content = infile.read()

        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Write to a new file
        with open("output_file.txt", "w") as outfile:
            outfile.write(modified_content)

        print("✅ File read from 'input_file.txt' and modified content written to 'output_file.txt'.")

    except FileNotFoundError:
        print("❌ Error: 'input_file.txt' does not exist.")
    except IOError:
        print("❌ Error: Could not read or write the file.")


def read_existing_file():
    filename = input("📂 Enter the name of the file to read: ")

    try:
        with open(filename, "r") as file:
            content = file.read()
            print("\n📄 File Content:\n" + content)

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' does not exist.")
    except IOError:
        print(f"❌ Error: The file '{filename}' could not be read.")


# Main program starts here
print("🔍 What would you like to do?")
print("1. Create and modify a file")
print("2. Read an existing file")

choice = input("Enter 1 or 2: ")

if choice == "1":
    create_and_modify_file()
elif choice == "2":
    read_existing_file()
else:
    print("❌ Invalid choice. Please enter 1 or 2.")
