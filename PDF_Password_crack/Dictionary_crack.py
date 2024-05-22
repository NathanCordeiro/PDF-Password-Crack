import pikepdf
import time

def dictionary_crack(input_pdf, output_pdf, dictionary_file):
    attempts = 0
    start_time = time.time()

    with open(dictionary_file, 'r') as file:
        for line in file:
            password = line.strip()  # Remove any trailing whitespace/newlines
            try:
                with pikepdf.open(input_pdf, password=password) as pdf:
                    pdf.save(output_pdf)  # Save the decrypted PDF
                    elapsed_time = time.time() - start_time
                    print(f"PDF decrypted successfully with password: {password}")
                    print(f"Time taken: {elapsed_time} seconds")
                    return
            except pikepdf._qpdf.PasswordError:
                attempts += 1
                if attempts % 1000 == 0:
                    elapsed_time = time.time() - start_time
                    print(f"Attempts: {attempts}, Elapsed time: {elapsed_time:.2f} seconds")
                continue
            except Exception as e:
                print(f"An error occurred: {e}")
                return

    print("Failed to decrypt PDF with dictionary attack.")

# Example usage:
input_pdf = 'encrypted_document.pdf'
output_pdf = 'decrypted_document.pdf'
dictionary_file = 'passwords.txt'

dictionary_crack(input_pdf, output_pdf, dictionary_file)
