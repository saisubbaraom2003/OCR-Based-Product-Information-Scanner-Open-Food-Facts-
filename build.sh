#!/usr/bin/env bash
# Exit immediately if a command exits with a non-zero status
set -e

# Update package lists and install Tesseract OCR package (Linux)
apt-get update && apt-get install -y tesseract-ocr

# Install Python dependencies from requirements.txt
pip install -r requirements.txt

