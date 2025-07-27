

# 🔐 Password Strength Analyzer with Custom Wordlist Generator

This is a cybersecurity project developed as part of an internship assignment. It includes two main tools:

- A **password strength analyzer** that checks the robustness of passwords using the `zxcvbn` library.
- A **custom wordlist generator** that creates personalized password guesses using user-provided information.

## 📌 Features

- Analyze password strength (score from 0 to 4) with suggestions.
- Generate a custom wordlist using personal data like names, birth years, pet names, etc.
- Realistic password mutations such as:
  - Leetspeak replacements (e.g., `a` → `@`, `e` → `3`)
  - Reversed strings (e.g., `alice` → `ecila`)
  - Capitalization
  - Appending numbers or dates (e.g., `alice123`, `9/12/1997123`)
- Export wordlist to a `.txt` file.
- Optional GUI using Tkinter for easy interaction.

---

## 🛠️ Tools & Technologies Used

- Python 3
- [zxcvbn](https://github.com/dropbox/zxcvbn) – for password strength checking
- argparse – for command-line argument parsing
- Tkinter – for GUI (optional)
- File I/O – for saving wordlist to text file

---

## 📁 Project Structure

```
password-strength-analyzer/
│
├── analyzer.py                    # Main script to check password strength
├── wordlist_generator.py          # Wordlist generator from user info
├── gui.py                         # Optional: Tkinter GUI
├── wordlist.txt                   # Output: generated wordlist
├── Password_Analyzer_Project_Report.pdf   # Final 2-page project report
└── README.md                      # This file
```

---

## 📦 Sample Wordlist Output

Your `wordlist.txt` may include results like:

```
alice
Alice
alice123
ecila
@lic3
9/12/1997
9/12/1997123
7991/21/9
max
Max
max123
xam
m@x
```

These variations are generated automatically using the inputs provided by the user (e.g., name, birthday, pet name).

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/password-strength-analyzer.git
cd password-strength-analyzer
```

### 2. Install Required Libraries
```bash
pip install zxcvbn argparse
```

> For GUI:
```bash
pip install tk
```

### 3. Run the Analyzer (CLI)
```bash
python analyzer.py
```

### 4. Run the Wordlist Generator
```bash
python wordlist_generator.py
```

### 5. (Optional) Run the GUI Interface
```bash
python gui.py
```

---

## 📄 Report

📘 **Project Report 🔐 Password Strength Analyzer with Custom Wordlist Generator**  
Includes Introduction, Abstract, Tools Used, Steps, and Conclusion.

---

## 🧑‍💻 Author

**Ishrat Jahan**  
Cybersecurity Intern  
July 2025

---
