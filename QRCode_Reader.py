import cv2
from pyzbar import pyzbar
import datetime
from time import strftime

# Function for reading and storing the QRCode
def read_qrcodes(generated_frame):
    qrcodes = pyzbar.decode(generated_frame)
    display_date_time = datetime.datetime.now()
    date_time = (display_date_time.strftime("%D %H:%M%p"))
    for qrcode in qrcodes:
        x, y , w, h = qrcode.rect
        qrcode_data = qrcode.data.decode('utf-8')
        cv2.rectangle(generated_frame, (x, y),(x+w, y+h), (0, 255, 0), 2)
        font_style = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(generated_frame, 'CODE READ AND STORED IN TEXT FILE', (x + 4, y - 4), font_style, 0.5, (0, 0, 255), 1)
        # For storing the QRCode data in text file
        with open("QRCode_data.txt", mode ='w') as file:
            file.write(f"QRCode Data: \n{qrcode_data} \nDate and Time: {date_time}")
    return generated_frame

# Function for reading the QRCode using webcam
def detect_qrcodes():
    webcam = cv2.VideoCapture(0)
    running_webcam, generated_frame = webcam.read()
    # For the webcam to keep running and just stop when you press "ESC"
    while running_webcam:
        running_webcam, generated_frame = webcam.read()
        generated_frame = read_qrcodes(generated_frame)
        cv2.imshow('QRCode Reader', generated_frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    webcam.release()
    cv2.destroyAllWindows()

# Perform the function
detect_qrcodes()