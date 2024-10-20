import cv2
from paddleocr import PaddleOCR

class Camera:
    def __init__(self):
        self.ocr = PaddleOCR(use_angle_cls=True, lang='en')
    
    def snap_and_process(self):
        cap = cv2.VideoCapture(0)
        for _ in range(5):
            ret, frame = cap.read()
        cap.release()
        if ret:
            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            texts = self.ocr.ocr(gray_frame, cls=True)
        
        processed_texts = []
        for text in texts[0]:
            processed_texts.append(text[1][0])
        
        print(processed_texts)
        return "\n".join(processed_texts)
