import cv2

# Load Haar cascade (Ensure the XML path is correct and trained for hands)
hand_cascade = cv2.CascadeClassifier('C:/Users/HP/Downloads/haarcascade_hand.xml')

# Check if the cascade loaded correctly
if hand_cascade.empty():
    print("Error loading Haar cascade file. Check the file path.")
    exit()

# Access the webcam
cap = cv2.VideoCapture(0)

# Set webcam resolution (improves detection in some cases)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break

    # Convert to grayscale (Haar cascades work better on grayscale images)
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect hands (tune scaleFactor and minNeighbors for better accuracy)
    hands = hand_cascade.detectMultiScale(gray_frame, scaleFactor=1.05, minNeighbors=7, minSize=(100, 100))

    # Draw rectangles around detected hands
    for (x, y, w, h) in hands:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        cv2.putText(frame, "Hand", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # Display the output frame
    cv2.imshow('Hand Detection', frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
