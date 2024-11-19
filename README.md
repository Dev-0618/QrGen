# QrGen

**QrGen** is a simple and customizable QR code generator tool written in Python. It allows you to create QR codes with custom text, URLs, background colors, and optional logo images. The generated QR codes can be saved as PNG files with your desired filename.

## Features

- **Generate QR codes** from any text or URL.
- **Customize background color** for the QR code.
- **Add a logo** (optional) to the center of the QR code.
- **Specify the output file name** for the generated QR code.
- **Easy-to-use command-line interface**.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Dev-0618/QrGen.git
   cd QrGen
   ```

2. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the script using the following command:

```bash
python qrgen.py
```

### Input Prompts:
1. **Enter the text or URL for the QR code**: The main content for the QR code (text or URL).
2. **Enter the background color**: Choose a background color for the QR code (default is white).
3. **Enter the path to a logo image (optional)**: Add an optional logo to the center of the QR code (provide the path to a `.png` logo).
4. **Enter the file name to save the QR code**: Choose the filename to save the generated QR code (default is `qrcode.png`).

Example:

```bash
Enter the text or URL for the QR code: https://www.example.com
Enter the background color (default: white): yellow
Enter the path to a logo image (optional, press Enter to skip): 
Enter the file name to save the QR code (default: qrcode.png): custom_qr.png
QR code saved as custom_qr.png
```

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` library

To install dependencies:

```bash
pip install -r requirements.txt
```
