import pandas as pd
import os

# Load the event data from the CSV file
csv_file_path = './data/events.csv'
event_data = pd.read_csv(csv_file_path)

# Define file paths for the templates
qr_template_path = './templates/event-qr-card-template.html'
event_page_template_path = './templates/event-page-template.html'

# Load the HTML templates
with open(qr_template_path, 'r') as file:
    qr_template = file.read()

with open(event_page_template_path, 'r') as file:
    event_page_template = file.read()

# Function to generate event-specific HTML files
def generate_event_files(event_data):
    qr_card_output_dir = './qr-code-cards/events/'
    event_page_output_dir = './events/'

    os.makedirs(qr_card_output_dir, exist_ok=True)
    os.makedirs(event_page_output_dir, exist_ok=True)
    
    for _, row in event_data.iterrows():
        event_name_title_case = row['Title']
        event_name_lowercase = event_name_title_case.lower().replace(" ", "-")
        details = row.get('Details', '') if pd.notna(row['Details']) else ''
        quantity_in_deck = row.get('Quantity in Deck', '') if pd.notna(row['Quantity in Deck']) else ''
        
        # Replace placeholders in the QR card template
        qr_card_content = qr_template.replace('{EVENT_NAME_TITLE_CASE}', event_name_title_case)
        qr_card_content = qr_card_content.replace('{EVENT_NAME_LOWERCASE}', event_name_lowercase)
        
        # Replace placeholders in the event page template
        event_page_content = event_page_template.replace('{EVENT_NAME_TITLE_CASE}', event_name_title_case)
        event_page_content = event_page_content.replace('{EVENT_NAME_LOWERCASE}', event_name_lowercase)
        event_page_content = event_page_content.replace('{DETAILS}', details)
        
        # Save the output files
        for i in range(quantity_in_deck):
            number = i + 1
            with open(f"{qr_card_output_dir}{event_name_lowercase}-{number}.html", 'w') as qr_file:
                qr_file.write(qr_card_content)
        
        with open(f"{event_page_output_dir}{event_name_lowercase}.html", 'w') as city_page_file:
            city_page_file.write(event_page_content)

# Generate the city-specific files
generate_event_files(event_data)
