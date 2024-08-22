import sys
import os
import qrcode
from PIL import Image
from urllib.parse import urlparse, unquote

def extract_file_name(url):
    path = urlparse(url).path
    file_name = os.path.basename(path)
    # Decode URL-encoded characters and remove the `.html` extension
    file_name = unquote(file_name).replace('.html', '')
    return file_name + '.png'

def calculate_box_size(desired_size, version, border):
    # Calculate the number of modules in the QR code for the given version
    num_modules = 21 + 4 * (version - 1)
    
    # Calculate the required box size to achieve the desired image size
    return (desired_size - 2 * border) / num_modules

def generate_qr_codes(file_path, desired_size, color, transparent, version=1, border=4):
    try:
        # Ensure the output directory exists
        output_dir = './qr-codes'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Calculate the box size needed to achieve the desired image size
        box_size = calculate_box_size(desired_size, version, border)

        with open(file_path, 'r') as file:
            urls = file.readlines()

        for url in urls:
            url = url.strip()
            if not url:
                continue

            # Extract the file name for the QR code
            file_name = extract_file_name(url)

            # Create QR code
            qr = qrcode.QRCode(
                version=version,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=box_size,
                border=border,
            )
            qr.add_data(url)
            qr.make(fit=True)
            img = qr.make_image(fill_color=color, back_color='transparent' if transparent else 'white')

            # Save QR code image in the ./qr-codes directory
            img.save(os.path.join(output_dir, file_name))

        print("QR codes generated successfully.")
    
    except FileNotFoundError:
        print(f"The file '{file_path}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python generate_qr_codes.py <file_path> <desired_size> <color> <transparent>")
        print("Example: python generate_qr_codes.py urls.txt 300 '#000000' True")
    else:
        file_path = sys.argv[1]
        desired_size = int(sys.argv[2])
        color = sys.argv[3]
        transparent = sys.argv[4].lower() in ['true', '1', 'yes']

        generate_qr_codes(file_path, desired_size, color, transparent)
