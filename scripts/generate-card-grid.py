import os

# Directory containing your HTML files
directory = "./qr-code-cards"

# Output file
output_file = "merged_grid.html"

# Start of the output HTML file
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Merged HTML Grid</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .grid-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .grid-item {
            border: 1px solid #ddd;
            padding: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            background-color: #f9f9f9;
        }
        iframe {
            width: 100%;
            height: 300px;
            border: none;
        }
    </style>
</head>
<body>
    <h1>Merged HTML Grid</h1>
    <div class="grid-container">
"""

# Loop through all HTML files in the directory and add them as grid items
for filename in os.listdir(directory):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        with open(file_path, "r") as file:
            content = file.read()
            # Wrap the content inside an iframe to preserve the structure
            html_content += f"""
            <div class="grid-item">
                <iframe src="./qr-code-cards/{filename}"></iframe>
            </div>
            """

# End of the output HTML file
html_content += """
    </div>
</body>
</html>
"""

# Write the combined content to the output file
with open(output_file, "w") as output:
    output.write(html_content)

print(f"HTML files merged into {output_file}")
