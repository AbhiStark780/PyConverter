# ⚖️ PyConverter

A simple, pure Python Command Line Interface (CLI) tool that converts units of measurement. This project was built to practice Python control flow, dictionaries, and error handling without relying on external libraries.

## 🚀 Features
* **Distance:** Converts between [e.g., Kilometers and Miles].
* **Weight:** Converts between [e.g., Kilograms and Pounds].
* **Input Validation:** Prevents crashes when users enter invalid text or unsupported units.
* **Continuous Loop:** Allows the user to perform multiple conversions without restarting the program.

## 🧠 How It Works
The program uses a **Dictionary-based architecture** to store conversion factors, making it easy to add new units in the future without rewriting the logic.

1. The user selects a category.
2. The user inputs the **Source Unit** and **Target Unit**.
3. The program looks up the conversion factor in the dictionary.
4. It calculates the result and displays it formatted to 2 decimal places.

## 🛠️ Tech Stack
* **Language:** Python 3.11.5
* **Concepts Used:** Dictionaries, `while` loops, `try/except` blocks, f-strings.

## 📸 Usage Example
```text
Example:
Welcome to PyConverter!
1. Length
2. Weight
Select a category: 1

Convert from: km
Convert to: miles
Amount: 10

Result: 10 km = 6.21 miles