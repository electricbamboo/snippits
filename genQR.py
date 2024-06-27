import qrcode
import sys

def generate_qr_code(data, output_file):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR Code instance
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image to a file
    img.save(output_file)
    print(f"Generated QR code for: {data} -> {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_qr_codes.py <string_to_convert_to_qr_code> <output_file_path>")
        sys.exit(1)

    data = sys.argv[1]
    output_file = sys.argv[2]
    
    generate_qr_code(data, output_file)
