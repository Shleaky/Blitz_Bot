# Word Blitz Bot 🔠🤖

An intelligent, real-time automation bot that plays **Word Blitz** on Facebook Gaming using OCR, a word solver, and mouse simulation.

## Features

- Captures a live game board via screen grab
- Uses Tesseract OCR to detect each tile letter
- Solves all possible words using a Trie + DFS
- Scores each word based on Word Blitz scoring rules
- Automatically plays the top-scoring words using pyautogui

## Tech Stack

- Python 3
- OpenCV
- Tesseract OCR
- pyautogui
- Custom Trie + DFS search

## Setup

```bash
pip install -r requirements.txt

Install Tesseract:

Windows: Tesseract OCR

Mac: brew install tesseract

Then:

Maximize the game window on a dedicated monitor.

Run the script:

bash
Copy
Edit
python main.py
Press [Enter] when ready to play. 

Notes
Currently uses a general English word list.

Future versions will include bonus tile support and Word Blitz-specific dictionary filtering.

License
MIT – go flex and modify.