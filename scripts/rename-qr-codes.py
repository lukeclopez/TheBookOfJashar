import os

base_url = "https---lukeclopez.github.io-TheBookOfJashar-pages-"

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.startswith("https---") and filename.endswith(".png"):
            new_filename = filename.replace(base_url, "")
            new_filename = new_filename.replace(".html", "")
            new_filename = new_filename.replace("cities-", "")
            new_filename = new_filename.replace("blessings-spiritual-", "")
            new_filename = new_filename.replace("blessings-conquest-", "")
            new_filename = new_filename.replace("direction-", "")
            new_filename = new_filename.replace("events-", "")

            # Construct full file paths
            old_file_path = os.path.join(directory, filename)
            new_file_path = os.path.join(directory, new_filename)
            
            # Rename the file
            os.rename(old_file_path, new_file_path)
            print(f"Renamed: {filename} -> {new_filename}")

directory_path = './qr-codes'
rename_files(directory_path)
