# Spanish-English Flashcard App

A simple desktop application built with Python and Tkinter that helps users learn Spanish vocabulary through flashcards.

## Features

- Interactive flashcards with Spanish words on the front and English translations on the back
- Automatic card flip after 3 seconds
- Progress tracking - words marked as "known" are removed from the deck
- Progress saving - creates a separate file for remaining words to learn
- Visual feedback for correct/incorrect responses
- Completion detection when all cards are learned

## Requirements

- Python 3.x
- pandas
- tkinter (usually comes with Python)

## Installation

1. Clone this repository:

```bash
git clone https://github.com/yourusername/spanish-english-flashcards.git
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. The flashcard will show a Spanish word
3. After 3 seconds, it will flip to show the English translation
4. Click the ✓ button if you knew the word
5. Click the ✗ button if you didn't know the word
6. Words marked as known will be removed from your learning list

## Project Structure



```plaintext
spanish-english-flashcards/
│
├── main.py                # Main application file
├── data/
│   ├── spanish_words.csv  # Original word database
│   └── words_to_learn.csv # Progress tracking file
├── images/
│   ├── card_front.png     # Flashcard front template
│   ├── card_back.png      # Flashcard back template
│   ├── right.png          # Correct answer button
│   └── wrong.png          # Wrong answer button
└── requirements.txt       # Project dependencies
```
