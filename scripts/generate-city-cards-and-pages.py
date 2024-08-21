import pandas as pd
import os

# Load the city data from the CSV file
csv_file_path = './data/cities.csv'
city_data = pd.read_csv(csv_file_path)

# Define file paths for the templates
qr_template_path = './templates/city-qr-card-template.html'  # Update this path
city_page_template_path = './templates/city-page-template.html'  # Update this path

# Load the HTML templates
with open(qr_template_path, 'r') as file:
    qr_template = file.read()

with open(city_page_template_path, 'r') as file:
    city_page_template = file.read()

# Function to generate city-specific HTML files
def generate_city_files(city_data):
    qr_card_output_dir = './qr-code-cards/'
    city_page_output_dir = './cities/'

    os.makedirs(qr_card_output_dir, exist_ok=True)
    os.makedirs(city_page_output_dir, exist_ok=True)
    
    for _, row in city_data.iterrows():
        city_name_title_case = row['Name']
        city_name_lowercase = city_name_title_case.lower().replace(" ", "-")
        power = row['Power']
        special = row.get('Special', 'N/A') if pd.notna(row['Special']) else 'N/A'
        description = row.get('Description', '') if pd.notna(row['Description']) else ''
        insight_link = row.get('Insight Book Link', '#') if pd.notna(row['Insight Book Link']) else '#'
        
        # Replace placeholders in the QR card template
        qr_card_content = qr_template.replace('{CITY_NAME_TITLE_CASE}', city_name_title_case)
        qr_card_content = qr_card_content.replace('{CITY_NAME_LOWERCASE}', city_name_lowercase)
        
        # Replace placeholders in the city page template
        city_page_content = city_page_template.replace('{CITY_NAME_TITLE_CASE}', city_name_title_case)
        city_page_content = city_page_content.replace('{CITY_NAME_LOWERCASE}', city_name_lowercase)
        city_page_content = city_page_content.replace('{POWER}', str(power))
        city_page_content = city_page_content.replace('{SPECIAL}', special)
        city_page_content = city_page_content.replace('{DESCRIPTION}', description)
        city_page_content = city_page_content.replace('{INSIGHT_LINK}', insight_link)
        
        # Save the output files
        with open(f"{qr_card_output_dir}{city_name_lowercase}.html", 'w') as qr_file:
            qr_file.write(qr_card_content)
        
        with open(f"{city_page_output_dir}{city_name_lowercase}.html", 'w') as city_page_file:
            city_page_file.write(city_page_content)

# Generate the city-specific files
generate_city_files(city_data)
