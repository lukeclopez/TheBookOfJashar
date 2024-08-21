import pandas as pd
import os

# Load the blessing data from the CSV file
csv_file_path = './data/blessings-spiritual.csv'
spiritual_blessing_data = pd.read_csv(csv_file_path)

csv_file_path = './data/blessings-conquest.csv'
conquest_blessing_data = pd.read_csv(csv_file_path)


# Define the file path for the template
page_template_path = './templates/blessing-page-template.html'
qr_card_template_path = './templates/blessing-qr-card-template.html'

# Load the HTML templates
with open(page_template_path, 'r') as file:
    page_template = file.read()

# Load the HTML templates
with open(qr_card_template_path, 'r') as file:
    qr_card_template = file.read()

# Function to generate blessing-specific HTML files
def generate_blessing_files(blessing_data, blessing_type):
    page_output_dir = f'./pages/blessings/{blessing_type}/'
    qr_card_output_dir = f'./qr-code-cards/blessings/{blessing_type}/'

    os.makedirs(page_output_dir, exist_ok=True)
    
    for _, row in blessing_data.iterrows():
        title = row['Title']
        usage = row['Usage']
        effect = row['Effect']
        quantity = row['Quantity in Deck']

        title_lowercase_hyphens = title.lower().replace(" ", "-")
        
        # Replace placeholders in the blessing card template
        page_content = page_template.replace('{TITLE_TITLE_CASE}', title)
        page_content = page_content.replace('{TITLE_LOWERCASE}', title_lowercase_hyphens)
        page_content = page_content.replace('{USAGE}', usage)
        page_content = page_content.replace('{EFFECT}', effect)
        page_content = page_content.replace('{BLESSING_TYPE}', blessing_type)

        qr_card_content = qr_card_template.replace('{TITLE_TITLE_CASE}', title)
        qr_card_content = qr_card_content.replace('{TITLE_LOWERCASE}', title_lowercase_hyphens)
        qr_card_content = qr_card_content.replace('{BLESSING_TYPE}', blessing_type)

        
        # Save the output file with a filename based on the title
        output_file_name = title_lowercase_hyphens
        page_output_file_path = os.path.join(page_output_dir, output_file_name)
        qr_card_output_file_path = os.path.join(qr_card_output_dir, output_file_name)

        for i in range(quantity):
            number = i + 1
            with open(f"{qr_card_output_file_path}-{number}.html", 'w') as qr_file:
                qr_file.write(qr_card_content)
            
            print(f"Generated: {qr_card_output_file_path}")

        
        with open(f"{page_output_file_path}.html", 'w') as output_file:
            output_file.write(page_content)
        
        print(f"Generated: {page_output_file_path}.html")

# Generate the blessing-specific files
generate_blessing_files(spiritual_blessing_data, "spiritual")
generate_blessing_files(conquest_blessing_data, "conquest")
