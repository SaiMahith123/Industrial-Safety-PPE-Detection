import cv2
import numpy as np
import onnxruntime as ort

session = ort.InferenceSession("model.onnx")
input_name = session.get_inputs()[0].name

cap = cv2.VideoCapture(0)
print("✅ AI Camera Active! Press 'q' to exit.")

while True:
    ret, frame = cap.read()
    if not ret: break

    resized = cv2.resize(frame, (224, 224))
    img = resized.astype(np.float32) / 255.0
    img = np.transpose(img, (2, 0, 1))  
    img = np.expand_dims(img, axis=0)   

    outputs = session.run(None, {input_name: img})
    result = np.argmax(outputs[0])

    label = "SAFE: HELMET DETECTED" if result == 0 else "WARNING: NO HELMET"
    color = (0, 255, 0) if result == 0 else (0, 0, 255)

    cv2.putText(frame, label, (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.2, color, 3)
    cv2.rectangle(frame, (20, 20), (620, 460), color, 2)
    cv2.imshow('Mahi Industrial Safety AI', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): break

cap.release()
cv2.destroyAllWindows()