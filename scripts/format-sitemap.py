import sys

def replace_first_character(file_path, replacement_string):
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            lines = file.readlines()

        # Replace the first character of each line ending with .html
        updated_lines = []
        for line in lines:
            if line.endswith('.html\n') or line.endswith('.html'):  # Handles both Unix and Windows line endings
                if line:
                    updated_lines.append(replacement_string + line[1:])
                else:
                    updated_lines.append(line)
        
        # Write the updated content back to the file
        with open(file_path, 'w') as file:
            file.writelines(updated_lines)

        print(f"Successfully replaced the first character of lines ending with '.html' with '{replacement_string}'.")
    
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python replace_first_character.py <replacement_string>")
    else:
        replacement_string = sys.argv[1]
        replace_first_character('./sitemap', replacement_string)
