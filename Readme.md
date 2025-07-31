#  OCR-Based Product Information Scanner (Open Food Facts)

This project is a Streamlit web application that performs OCR (Optical Character Recognition) on uploaded product images to extract text (e.g., product name), and then uses the [Open Food Facts API](https://world.openfoodfacts.org/data) to retrieve detailed product information.

---

##  Folder Structure

```
ocr-product-scanner/
│
├── app.py             # Main Streamlit app
├── ocr_utils.py       # OCR helper functions
├── requirements.txt   # Required Python packages
└── README.md          # Project documentation
```

---

##  Requirements and Their Purpose

| Package       | Description                                                                 |
|---------------|-----------------------------------------------------------------------------|
| streamlit     | To build the interactive web interface                                       |
| pytesseract   | Wrapper for Tesseract OCR engine (used to extract text from product images) |
| Pillow        | Python Imaging Library (for handling image input)                           |
| requests      | For making HTTP requests to the Open Food Facts API                         |

These are listed in `requirements.txt`.

---

##  Installation Instructions

### 1️ Download the Project


### 2️ (Optional but Recommended) Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate     # On Windows
# OR
source venv/bin/activate  # On macOS/Linux
```

### 3️ Install Python Dependencies

```bash
pip install -r requirements.txt
```

This installs all necessary packages: `streamlit`, `pytesseract`, `Pillow`, `requests`.

---

### 4️ Install Tesseract OCR Engine

> **Note:** `pytesseract` is just a wrapper — you must install the actual Tesseract engine.

 **Windows Installation:**

- Download from: https://github.com/UB-Mannheim/tesseract/wiki
- Install it (default path: `C:\Program Files\Tesseract-OCR\tesseract.exe`)

 If Tesseract is not in your system `PATH`, set the path manually in `ocr_utils.py`:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```

---

##  How to Run the App

```bash
streamlit run app.py
```

This starts a local server and opens the app in your browser at:

```
http://localhost:8501
```

---

## How It Works

1. User uploads a product image (e.g., label, yogurt container).
2. Image is converted to grayscale to enhance text visibility.
3. `pytesseract` extracts readable text from the image.
4. That text is used to query the Open Food Facts API.
5. If a match is found:
   -  Product Name
   -  Brand
   -  Categories
   -  Nutri-Score
   -  Product Image  
   are displayed nicely in the UI.

---

##  Sample Output

```
Extracted Text:
Red Bull Energy Drink

Product Found!

Product Name: Red Bull

Brands: Red Bull

Categories: en:napoje,en:napoje-energetyczne,en:napoje-i-składniki-do-napojow,Bibite gassate,energy drink

Nutri-Score: e
```

---

##  Error Handling

| Scenario                   | Message                                                   |
|----------------------------|------------------------------------------------------------|
| No text found              | `"No readable text found. Please try another image."`     |
| No product match in API    | `"Product Not Found. Try another image or clearer text."`|
| Tesseract not installed    | Error traceback from `pytesseract`                         |

---

##  Test Notes

- This test only involves **OCR-based text extraction**.
- Barcode scanning is **not required**, so barcode libraries (e.g., `pyzbar`) are excluded.
- The focus is on:
  - Image preprocessing
  - OCR accuracy
  - API response parsing

---

##  Future Enhancements

- Barcode detection using `pyzbar`
- Translation for extracted text (non-English)
- Improved fuzzy search for better API results
- UI enhancements and multi-language support

---

##  Author

**Sai Subba Rao Mahendrakar**  
Internship Test Submission – July 2025  
OCR + Open Food Facts API Integration  
