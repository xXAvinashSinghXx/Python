import qrcode
import os  
from config import file_url

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(file_url)
qr.make(fit=True)

# Ensure the directory exists
directory = r"QR Code"
os.makedirs(directory, exist_ok=True)

# Create and save the QR Code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save(f"{directory}/qr_image.png")  

Done = "Created Successfully!"
print(Done)
