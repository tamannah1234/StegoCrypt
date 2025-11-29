# 🔐 StegoCrypt – Image-Based Steganography & Encryption Tool

---

## 🚀 Overview
**StegoCrypt** is a lightweight and secure **steganography-based encryption tool** that hides secret messages inside images.  
It ensures **private communication** by embedding text within image pixels and allowing message extraction only with a correct passcode.  

This tool is perfect for learning **steganography**, **secure communication**, and **basic cryptography techniques**.

---

## ⭐ Features
- ✅ **Hide secret messages inside images**  
- 🔑 **Decrypt hidden messages using a passcode**  
- 🖼️ **Pixel-level steganography**  
- ⚡ **Simple, lightweight, and easy to use**  
- 🧠 **Built with OpenCV & NumPy for efficient processing**

---

## 🧰 Technologies Used
- **Python**  
- **OpenCV**  
- **NumPy**

---

## 🚀 How to Use

### 🔵 Encrypt (Hide a Secret Message)
1. Run the script:
```bash
python stegocrypt.py
Enter the image filename (e.g., input.png)

Type your secret message

Enter a passcode for protection

The tool will generate an encrypted image containing your hidden message

🟠 Decrypt (Extract the Hidden Message)
Run the script:

bash
Copy code
python stegocrypt.py
Enter the encrypted image file

Provide the correct passcode

The hidden message will be revealed

📦 Installation
Install the required dependencies:

bash
Copy code
pip install opencv-python numpy
Run the program:

bash
Copy code
python stegocrypt.py
📂 Project Structure
pgsql
Copy code
stegocrypt/
 ├── stegocrypt.py     # Main script for encryption/decryption
 ├── sample_input/     # Example images
 ├── output/           # Encrypted images
 └── README.md         # Documentation
🤝 Contributing
Contributions and improvements are welcome!
Feel free to fork the repository and submit a pull request.

📜 License
This project is licensed under the MIT License.

markdown
Copy code
