import os
from bs4 import BeautifulSoup

# The key is the card type, the value is a tuple where the first element is the input directory and the second is the stylesheet path
card_types = {
    "blessings-conquest": {"directory": "./qr-code-cards/blessings/conquest", "stylesheet": "../styles/blessing-qr-card-styles.css"},
    "blessings-spiritual": {"directory": "./qr-code-cards/blessings/spiritual", "stylesheet": "../styles/blessing-qr-card-styles.css"},
    "cities": {"directory": "./qr-code-cards/cities", "stylesheet": "../styles/city-qr-card-styles.css"},
    "direction": {"directory": "./qr-code-cards/direction", "stylesheet": "../styles/direction-qr-card-styles.css"},
    "events": {"directory": "./qr-code-cards/events", "stylesheet": "../styles/event-qr-card-styles.css"}
}

# Output directory
output_dir = "./for-printing/"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through each card type
for card_type, paths in card_types.items():
    directory = paths["directory"]
    stylesheet_path = paths["stylesheet"]
    output_file = os.path.join(output_dir, f"{card_type}-grid.html")
    
    # Start of the output HTML file
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="stylesheet" href="{stylesheet_path}" />
        <title>{card_type.replace('_', ' ').title()} Merged HTML Grid</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 20px;
            }}
            .grid-container {{
                display: grid;
                grid-template-columns: 250px 250px 250px 250px 250px;
                row-gap: 5px;
            }}
        </style>
    </head>
    <body>
        <div class="grid-container">
    """

    # Loop through all HTML files in the current directory and add them as grid items
    for filename in sorted(os.listdir(directory)):
        if filename.endswith(".html"):
            file_path = os.path.join(directory, filename)
            with open(file_path, "r") as file:
                # Parse the HTML content
                soup = BeautifulSoup(file.read(), "html.parser")
                
                # Extract relevant content (e.g., title, main content, etc.)
                main_content = soup.body if soup.body else soup
                main_content = str(main_content)
                main_content = main_content.replace("body", "div")  # Replace <body> with <div> to preserve content layout

                # Wrap the content in a grid item
                html_content += f"""
                    {main_content}
                """

    # Close the grid container for this card type
    html_content += """
        </div>
    </body>
    </html>
    """

    # Write the combined content to the output file
    with open(output_file, "w") as output:
        html_content = html_content.replace("../../../", "../")
        output.write(html_content)

    print(f"HTML files for {card_type} merged into {output_file}")
