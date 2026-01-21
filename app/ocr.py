import pytesseract
import cv2

# IMPORTANT: Path to Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Yamin\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

def extract_text_from_image(image_path: str) -> str:
    
    image = cv2.imread(image_path)
    if image is None:
        return ""

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    return text.strip()
