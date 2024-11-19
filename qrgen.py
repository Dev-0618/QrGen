import qrcode
from PIL import Image
import os

def create_qr_code(data, qr_color="black", bg_color="white", logo_path=None, file_name="qrcode.png"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (higher = bigger)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # error correction level
        box_size=10,  # size of each box in the QR code grid
        border=4,  # border width
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image for the QR code with customizable colors
    img = qr.make_image(fill=qr_color, back_color=bg_color)

    # Add logo if path is provided
    if logo_path:
        try:
            logo = Image.open(logo_path)
            # Calculate dimensions for the logo
            logo_size = int(img.size[0] / 5)  # logo will take up 1/5th of QR code size
            logo = logo.resize((logo_size, logo_size))

            # Calculate the position to place the logo in the center
            logo_position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)

            # Paste the logo onto the QR code
            img.paste(logo, logo_position, logo.convert("RGBA"))  # Ensure transparency is handled
        except Exception as e:
            print(f"Error loading logo: {e}")
    
    # Save the QR code to a file
    img.save(file_name)
    print(f"QR code saved as {file_name}")

def main():   
    data = input("Enter the text or URL for the QR code: ") 
    qr_color = input("Enter the QR code color (default: black): ") or "black"  
    bg_color = input("Enter the background color (default: white): ") or "white" 
    logo_path = input("Enter the path to a logo image (optional, press Enter to skip): ") or None
    file_name = input("Enter the file name to save the QR code (default: qrcode.png): ") or "qrcode.png"
    create_qr_code(data, qr_color, bg_color, logo_path, file_name)

if __name__ == "__main__":
    main()
    #dev@127.4.7.8

