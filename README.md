---

# PDF Password Crack

---

## Description
This Python script is designed to assist in decrypting and recovering the password for encrypted PDF files. There are two approaches beind used,
a brute force approach to systematically try different combinations of characters until the correct password is found and a dictionary read to read all possible passwords from a dictionary.  
This can be useful if you have forgotten the password to a PDF file that you encrypted yourself and need to regain access to its contents.

## Features (`BruteForce`)
- Brute force approach to password recovery
- Supports specifying minimum and maximum password lengths
- Customizable character set for generating password combinations
- Progress tracking to monitor attempts and elapsed time

## Features (`Dictionary`)
- Dictionary password hit and miss
- Reads all passwords in a dictionary line by line and returns which opens file
- Supports an existing dictionary or customizable dictionary 

## Usage
1. Install the required dependencies:
   ```sh
   pip install pikepdf
   ```

2. Update the script with the path to your encrypted PDF file and specify the desired password length (optional).

3. Run the script:
   ```sh
   python Bruteforce_crack.py
   ```
   `or`
   ```sh
   python Dictionary_crack.py
   ```

5. Wait for the script to finish running. If the correct password is found, it will be printed along with the elapsed time.

## License
This project is licensed under the [MIT License](LICENSE).

## Contributing
Contributions are welcome! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

## Acknowledgements
- This script utilizes the [pikepdf](https://github.com/pikepdf/pikepdf) library for working with PDF files.

> [!IMPORTANT]
> This script is provided for educational and informational purposes only. Use it responsibly and ensure that you have the legal right to access the PDF file you are attempting to decrypt.
