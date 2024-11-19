# QrGen

This Python-based QrGen allows you to generate QR codes from any text or URL with customizable features such as color options and logo embedding. The tool is designed to be simple to use and flexible, offering options for user input and customization during execution.

## Features

- **Generate QR codes** from any text or URL.
- **Customizable colors**: Choose the QR code foreground and background colors.
- **Logo embedding**: Optionally add a logo to the center of the QR code if provided.
- **Custom file name**: Specify the name for the output file.
- **Supports various color formats**: Named colors, hexadecimal codes, or RGB tuples.

## Installation

To use the QrGen, you need Python and some required libraries. You can install the dependencies by running the following command:

```bash
pip install -r requirements.txt
```

## Usage

1. Clone the repository or download the script.
2. Run the Python script:

```bash
python qrgen.py
```

3. The script will ask for the following inputs:
   - **Text or URL**: The content to encode in the QR code.
   - **QR Code Color**: The color of the QR code (default: black).
   - **Background Color**: The background color of the QR code (default: white).
   - **Logo Image**: Optionally, provide a path to a logo image (e.g., a PNG file).
   - **File Name**: The name of the output file (default: `qrcode.png`).

After entering the details, the QR code will be generated and saved with the specified filename.

## Example

```bash
Enter the text or URL for the QR code: https://www.example.com
Enter the QR code color (default: black): blue
Enter the background color (default: white): white
Enter the path to a logo image (optional, press Enter to skip): logo.png
Enter the file name to save the QR code (default: qrcode.png): my_qrcode.png
QR code saved as my_qrcode.png
```

## Requirements

- Python 3.x
- `qrcode` and `Pillow` libraries (listed in `requirements.txt`)
