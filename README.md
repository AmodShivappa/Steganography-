# Image Steganography Tool
## This tool allows you to embed a secret message into an image and later decrypt it using a password. It uses a simple encryption mechanism to hide the message within the pixel values of the image.

## Features
Encrypts a secret message into an image
Decrypts the message from the image using a password
Displays the decrypted message on the image
Saves the decrypted message to a text file
## Requirements
Python 3.x
OpenCV (cv2)
## Installation
Clone the repository:

### Copy code
git clone https://github.com/yourusername/ImageSteganographyTool.git
cd ImageSteganographyTool
Install the required Python packages:

### Copy code
pip install opencv-python
Ensure you have an image file named rr.jpg in the same directory as the script.

## Usage
Run the script:


## Copy code
python og.py
Enter the secret message you want to hide in the image when prompted.

Enter a password for encrypting the message.

The script will create a new image file named Encryptedmsg.jpg with the encrypted message.

To decrypt the message, run the script again and enter the passcode when prompted.

If the passcode is correct, the decrypted message will be displayed on the image and saved to DecryptedMessage.txt.

## How It Works
Encryption: The script reads the image and the secret message. It then encodes the message into the pixel values of the image.
Decryption: The script reads the encrypted image and uses the provided passcode to retrieve the original message. If the passcode is correct, it displays and saves the decrypted message.
Notes
The image file rr.jpg must be present in the same directory as the script for the encryption and decryption to work.
The encrypted image will be saved as Encryptedmsg.jpg in the same directory.
The decrypted message will be saved to DecryptedMessage.txt in the same directory.
Example
Encrypting a message:

plaintext
Copy code
Enter secret message: Hello, World!
Enter password: mypassword
Decrypting the message:

plaintext
Copy code
Enter passcode for Decryption: mypassword
Decryption message: Hello, World!
