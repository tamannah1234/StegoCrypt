import cv2
import numpy as np

def decode_message(image_path, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return

    height, width, _ = img.shape

    # Extract the message length from the first pixel (0,0)
    message_length = (int(img[0, 0, 0]) << 16) + (int(img[0, 0, 1]) << 8) + int(img[0, 0, 2])

    if message_length == 0 or message_length > (height * width * 3 - 1):
        print("Error: No valid hidden message found!")
        return

    # Convert password into ASCII numbers for XOR decryption
    password_ascii = [ord(ch) for ch in password]
    password_length = len(password_ascii)

    message = ""
    n, m, z = 0, 1, 0  # Start from (0,1) to avoid reading length data

    for i in range(message_length):
        char_value = int(img[n, m, z])
        decrypted_char = char_value ^ password_ascii[i % password_length]  # XOR decryption
        message += chr(decrypted_char)

        # Move to next pixel position
        z += 1
        if z == 3:
            z = 0
            m += 1
            if m == width:
                m = 0
                n += 1
                if n == height:
                    break

    print("\n Decryption successful! Secret message:")
    print(message)

# Usage Example
image_path = input("Enter the encrypted image filename (e.g., output.png): ")
password = input("Enter the password for decryption: ")

decode_message(image_path, password)
