import pandas as pd
import os

# Load the direction data from the CSV file
csv_file_path = './data/direction.csv'
direction_data = pd.read_csv(csv_file_path)

# Define file paths for the templates
qr_template_path = './templates/direction-qr-card-template.html'
direction_page_template_path = './templates/direction-page-template.html'

# Load the HTML templates
with open(qr_template_path, 'r') as file:
    qr_template = file.read()

with open(direction_page_template_path, 'r') as file:
    direction_page_template = file.read()

# Function to generate direction-specific HTML files
def generate_direction_files(direction_data):
    qr_card_output_dir = './qr-code-cards/direction/'
    direction_page_output_dir = './pages/direction/'

    os.makedirs(qr_card_output_dir, exist_ok=True)
    os.makedirs(direction_page_output_dir, exist_ok=True)
    
    for _, row in direction_data.iterrows():
        direction_name_title_case = row['Title']
        direction_name_lowercase = direction_name_title_case.lower().replace(" ", "-")
        details = row.get('Details', '') if pd.notna(row['Details']) else ''
        quantity_in_deck = row.get('Quantity in Deck', '') if pd.notna(row['Quantity in Deck']) else ''
        
        # Replace placeholders in the QR card template
        qr_card_content = qr_template.replace('{DIRECTION_NAME_TITLE_CASE}', direction_name_title_case)
        qr_card_content = qr_card_content.replace('{DIRECTION_NAME_LOWERCASE}', direction_name_lowercase)
        
        # Replace placeholders in the direction page template
        direction_page_content = direction_page_template.replace('{DIRECTION_NAME_TITLE_CASE}', direction_name_title_case)
        direction_page_content = direction_page_content.replace('{DIRECTION_NAME_LOWERCASE}', direction_name_lowercase)
        direction_page_content = direction_page_content.replace('{DETAILS}', details)
        
        # Save the output files
        for i in range(quantity_in_deck):
            number = i + 1
            with open(f"{qr_card_output_dir}{direction_name_lowercase}-{number}.html", 'w') as qr_file:
                qr_file.write(qr_card_content)
        
        with open(f"{direction_page_output_dir}{direction_name_lowercase}.html", 'w') as city_page_file:
            city_page_file.write(direction_page_content)

# Generate the city-specific files
generate_direction_files(direction_data)
