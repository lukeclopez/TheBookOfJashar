import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith("https---") and filename.endswith(".png"):
            # Extract the city name from the filename
            city_name = filename.split("-")[-2]  # Extracts 'laish' from the filename
            new_filename = f"{city_name}.png"
            
            # Construct full file paths
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

directory_path = './qr-codes'
rename_files(directory_path)
