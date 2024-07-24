import cv2
import os

img = cv2.imread("rr.jpg")

secret_message = input("Enter secret message: ")
password = input("Enter password: ")

char_to_int = {}
int_to_char = {}

for i in range(255):
    char_to_int[chr(i)] = i
    int_to_char[i] = chr(i)

n = 0
m = 0
z = 0

# Encryption
for i in range(len(secret_message)):
    img[n, m, z] = char_to_int[secret_message[i]]
    n = n + 1
    m = m + 1
    z = (z + 1) % 3

cv2.imwrite("Encryptedmsg.jpg", img)
os.system("start Encryptedmsg.jpg")

# Decryption
decrypted_message = ""
n = 0
m = 0
z = 0

passcode = input("Enter passcode for Decryption: ")

if password == passcode:
    for i in range(len(secret_message)):
        decrypted_message = decrypted_message + int_to_char[img[n, m, z]]
        n = n + 1
        m = m + 1
        z = (z + 1) % 3
    print("Decryption message:", decrypted_message)

    print("Opening the image with decrypted message...")
    img_with_text = img.copy()
    cv2.putText(img_with_text, decrypted_message, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Decrypted Message", img_with_text)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    with open("DecryptedMessage.txt", "w") as text_file:
        text_file.write(decrypted_message)
    print("Decrypted message saved to DecryptedMessage.txt")

else:
    print("Invalid passcode")
