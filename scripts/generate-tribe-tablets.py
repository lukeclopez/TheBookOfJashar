import os

# Define the list of tribes
tribes = ["Judah", "Naphtali", "Zebulun", "Gad"]

# File paths
template_path = "templates/tribe-tablet-template.html"
output_dir = "tribe-tablets"

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Read the template content
with open(template_path, "r") as template_file:
    template_content = template_file.read()

# Generate the HTML files for each tribe
for tribe in tribes:
    # Prepare placeholder values
    tribe_name_title_case = tribe
    tribe_name_lower_case = tribe.lower()

    # Replace placeholders in the template
    filled_content = template_content.replace("{TRIBE_NAME_TITLE_CASE}", tribe_name_title_case)
    filled_content = filled_content.replace("{TRIBE_NAME_LOWER_CASE}", tribe_name_lower_case)

    # Save the generated HTML file
    output_file_path = os.path.join(output_dir, f"{tribe_name_lower_case}.html")
    with open(output_file_path, "w") as output_file:
        output_file.write(filled_content)

    print(f"Generated: {output_file_path}")
