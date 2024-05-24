import pikepdf
from itertools import product
import string
import time

def brute_force_decrypt(input_pdf, output_pdf, min_length=5, max_length=6):
    # Define the allowed special characters
    allowed_special_chars = "!@#$%^&*()-_=+[]{}|;:',.<>?"
    # Combine uppercase, lowercase, digits, and allowed special characters
    chars = string.ascii_letters + string.digits + allowed_special_chars
    attempts = 0
    start_time = time.time()

    # Iterate over the range of password lengths
    for length in range(min_length, max_length + 1):
        # Generate all possible combinations of the given length
        for password_tuple in product(chars, repeat=length):
            password = ''.join(password_tuple)  # Convert tuple to string
            try:
                # Attempt to open the PDF with the current password
                with pikepdf.open(input_pdf, password=password) as pdf:
                    pdf.save(output_pdf)  # Save the decrypted PDF
                    elapsed_time = time.time() - start_time
                    # Print success message and password
                    print(f"PDF decrypted successfully with password: {password}")
                    print(f"Time taken: {elapsed_time} seconds")
                    return
            except pikepdf._qpdf.PasswordError:
                # Handle incorrect password and continue
                attempts += 1
                if attempts % 1000 == 0:
                    elapsed_time = time.time() - start_time
                    print(f"Attempts: {attempts}, Elapsed time: {elapsed_time:.2f} seconds")
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                return

    # Print message if no password was found
    print("Failed to decrypt PDF with brute force.")

# Example usage:
input_pdf = 'encrypted_document.pdf'    # Write the name of the pdf or the path of the file
output_pdf = 'decrypted_document.pdf'   #  Write the name of the output file

brute_force_decrypt(input_pdf, output_pdf)
