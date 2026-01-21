# AI-Powered Amount Detection API

This project is a FastAPI-based backend application that detects and classifies monetary amounts from **text input** or **uploaded bill images** using OCR and rule-based NLP logic.

---

##  Features

- Detects monetary values from raw text
- Extracts amounts from bill/invoice images using OCR
- Classifies amounts into:
  - Total
  - Paid
  - Due (Outstanding / Balance)
- Filters out dates, phone numbers, and irrelevant numbers
- Swagger UI support for easy testing

---

## Project Architecture

amount_detection_api/
│
├── main.py # FastAPI entry point
├── requirements.txt # Python dependencies
├── README.md
├── .gitignore
│
├── app/
│ ├── init.py
│ ├── ocr.py # OCR text extraction from images
│ ├── extract.py # Raw number extraction
│ ├── normalize.py # Token cleanup & normalization
│ └── classify.py # Amount classification logic
│
└── sample_images/
└── medical_bill.png # Sample test image


---

##  Setup Instructions (Local)

1.Clone the Repository
git clone <https://github.com/yaminibaskar09-stack/ai-powered-amount-detection.git>
cd amount_detection_api

2.Create virtual environment
python -m venv venv
venv\Scripts\activate

3.Install dependencies
pip install -r requirements.txt

4.Run the application
uvicorn main:app --reload

App will run at:
http://127.0.0.1:8000

#API Documentation (Swagger UI)
Open in browser:
http://127.0.0.1:8000/docs

API Endpoints
#Text-based Amount Detection

POST /detect/text

Request Body
{
  "text": "Total: INR 1200\nPaid: 1000\nDue: 200"
}

Response
{
  "currency": "INR",
  "amounts": [
    { "type": "total", "value": 1200 },
    { "type": "paid", "value": 1000 },
    { "type": "due", "value": 200 }
  ],
  "status": "ok"
}

#Image based amount detection
Same as text detection Upload a bill/invoice image (PNG/JPG) and see the response

##Sample CURL Commands
Text Detection
curl -X POST http://127.0.0.1:8000/detect/text \
-H "Content-Type: application/json" \
-d "{\"text\":\"Total: INR 1200 Paid: 1000 Due: 200\"}"


Image Detection
curl -X POST http://127.0.0.1:8000/detect/image \
-F "image=@sample_images/medical_bill.png"



Author ---Yamini Baskar