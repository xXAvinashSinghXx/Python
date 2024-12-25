import qrcode

# Send to payment location
file_url = "https://drive.google.com/file/d/1jB-vSYkSqhU6RhV9H5dDRt5ITXuGSyh6/view?usp=sharing"   

# Generate the QR code
qr = qrcode.QRCode(
    version=1,  # Size of the QR Code
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data(file_url)
qr.make(fit=True)

# Create and save the QR Code as an image
img = qr.make_image(fill_color="black", back_color="white")
img.save("Completed\QR Code\qr_image.png")
Done = "Created Successfully!" 
print(Done)