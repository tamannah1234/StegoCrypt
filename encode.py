import cv2
import numpy as np

def encode_message(image_path, output_path, message, password):
    img = cv2.imread(image_path)

    if img is None:
        print("Error: Image not found!")
        return
    
    height, width, _ = img.shape

    # Convert message to ASCII and store its length in the first pixel (0,0)
    message_length = len(message)
    if message_length > (height * width * 3 - 1):  # Ensure message fits in image
        print("Error: Message too large to fit in the image!")
        return

    # Encode the message length in the first pixel (0,0)
    img[0, 0] = [message_length >> 16, (message_length >> 8) & 255, message_length & 255]

    # Convert the password into ASCII numbers for XOR encryption
    password_ascii = [ord(ch) for ch in password]
    password_length = len(password_ascii)

    n, m, z = 0, 1, 0  # Start from (0,1) to avoid overwriting length data

    for i, char in enumerate(message):
        encrypted_char = ord(char) ^ password_ascii[i % password_length]  # XOR encryption
        img[n, m, z] = encrypted_char  # Store encrypted ASCII value

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

    cv2.imwrite(output_path, img)
    print(f"Message successfully hidden in {output_path}")

# Usage Example
image_path = input("Enter the image filename (e.g., input.png): ")
output_path = input("Enter the output filename (e.g., output.png): ")
message = input("Enter the secret message: ")
password = input("Enter a password for encryption: ")

encode_message(image_path, output_path, message, password)
