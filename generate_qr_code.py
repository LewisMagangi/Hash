import hashlib
import qrcode # type: ignore
import qrcode.constants

# Generate qr code with hash
def generate_qr_code_with_hash(data, file_name):
    # Calculate the hash of the data
    hash_value = hashlib.sha256(data.encode()).hexdigest()
    
    # Combine the original data and its hash
    combined_data = f"Original Data: {data}/nHash: {hash_value}"
    
    # Generate the QR code with the combined data
    qr = qrcode.QRCode(
        version=1, 
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(combined_data)
    qr.make(fit=True)
    
    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save or display the QR code image
    img.save(file_name)
    
# Example usage
original_data = "Kamau moses is testing this" # Replace with your original data
file_name = "qr_code_with_hash.png" # Nameof the QR code image file
generate_qr_code_with_hash(original_data, file_name)