import os

# Define the directory containing the files
directory = "./cities"

# Define the content to replace in each file
new_content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Redirect</title>
    <script src="../scripts/redirect-to-city-page.js" defer></script>
  </head>
  <body>
    Redirecting...
  </body>
</html>
"""

# Iterate through all files in the directory
for filename in os.listdir(directory):
    # Check if the file has an HTML extension
    if filename.endswith(".html"):
        # Construct the full file path
        file_path = os.path.join(directory, filename)
        
        # Open the file in write mode and replace its contents
        with open(file_path, "w") as file:
            file.write(new_content)

print("All files have been updated.")
