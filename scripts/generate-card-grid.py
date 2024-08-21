import os
from bs4 import BeautifulSoup

# Directory containing your HTML files
directory = "./qr-code-cards/cities"

# Output file
output_file = "./for-printing/card-grid.html"

# Start of the output HTML file
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="../styles/qr-card-styles.css" />
    <link rel="stylesheet" href="../styles/city-page-styles.css" />

    <title>Merged HTML Grid</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        .grid-container {
            display: grid;
            grid-template-columns: 250px 250px 250px 250px 250px;
            row-gap: 5px;
        }
    </style>
</head>
<body>
    <div class="grid-container">
"""

# Loop through all HTML files in the directory and add them as grid items
for filename in sorted(os.listdir(directory)):
    if filename.endswith(".html"):
        file_path = os.path.join(directory, filename)
        with open(file_path, "r") as file:
            # Parse the HTML content
            soup = BeautifulSoup(file.read(), "html.parser")

            # Extract relevant content (e.g., title, main content, etc.)
            title = soup.title.string if soup.title else filename
            main_content = soup.body if soup.body else soup
            main_content = str(main_content)
            main_content = main_content.replace("body", "div")

            # Wrap the content in a grid item
            html_content += f"""
                {str(main_content)}
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
