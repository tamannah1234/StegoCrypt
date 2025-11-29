🔐 StegoCrypt – Image-Based Steganography & Encryption Tool

StegoCrypt is a lightweight and secure steganography-based encryption tool that hides secret messages inside images.
It ensures private communication by embedding text within image pixels and allowing message extraction only with a correct passcode.

This tool is perfect for learning steganography, secure communication, and basic cryptography techniques.

⭐ Features

✅ Hide secret messages inside images

🔑 Decrypt hidden messages using a passcode

🖼️ Uses pixel manipulation for steganography

⚡ Simple, lightweight, and easy to use

🧠 Built with OpenCV & NumPy for efficient processing

🧰 Technologies Used

Python

OpenCV

NumPy

🚀 How to Use
🔵 Encrypt (Hide a Secret Message)

Run the script:

python stegocrypt.py


Enter the image filename (e.g., input.png)

Type the secret message

Enter a passcode for protection

The tool will generate an encrypted image containing your hidden message

🟠 Decrypt (Extract the Hidden Message)

Run the script again:

python stegocrypt.py


Enter the encrypted image file

Provide the correct passcode

The hidden message will be revealed

📦 Installation

Install the required dependencies:

pip install opencv-python numpy


Run the program:

python stegocrypt.py
