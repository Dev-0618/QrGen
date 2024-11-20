import qrcode
from PIL import Image
import os

def create_qr_code(data, bg_color="white", logo_path=None, file_name="qrcode.png"):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)
    bg_color = bg_color.strip() if bg_color else "white"
    img = qr.make_image(fill="black", back_color=bg_color)

    if logo_path:
        try:
            logo = Image.open(logo_path)
            logo_size = int(img.size[0] / 5)
            logo = logo.resize((logo_size, logo_size))
            logo_position = ((img.size[0] - logo.size[0]) // 2, (img.size[1] - logo.size[1]) // 2)
            img.paste(logo, logo_position, logo.convert("RGBA"))
        except Exception as e:
            print(f"Error loading logo: {e}")
    
    img.save(file_name)
    print(f"QR code saved as {file_name}")

def main():   
    data = input("Enter the text or URL for the QR code: ") 
    bg_color = input("Enter the background color (default: white): ") or "white" 
    logo_path = input("Enter the path to a logo image (optional, press Enter to skip): ") or None
    file_name = input("Enter the file name to save the QR code (default: qrcode.png): ") or "qrcode.png"
    create_qr_code(data, bg_color, logo_path, file_name)

if __name__ == "__main__":
    main()
