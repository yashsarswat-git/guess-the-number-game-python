# 🎯 Python Guess the Number (Prank Edition)

This is a terminal-based Python guessing game with a twist! Guess a number between 1 and 10. If you guess it wrong, your system will display a fake countdown and shut down. 😈

> **Disclaimer:** This is a prank script. Do **NOT** run on important systems.

---

## 🧠 How It Works

- Press any key to start.
- Press `SPACEBAR` before guessing to **cheat** and always guess correctly.
- If you don't cheat and guess wrong:
  - A fullscreen warning is displayed.
  - A 5-second countdown is shown.
  - The system will shut down using a hidden command (obfuscated with Base64).

---

## 🧪 Features

- `random.randint()` for number generation.
- `msvcrt.getch()` to check key input (spacebar cheat mode).
- `ctypes` and `os` for fullscreen terminal animation.
- `base64` encoding for hiding shutdown command.
- Simulated dramatic countdown using `time.sleep()`.

---

## 🚨 Warning

> This script contains a shutdown command (`shutdown /s /f /t 0`) hidden via base64. It's for fun or controlled demo use **only**.

---

## 🛠️ Requirements

- Windows OS
- Python 3.x

---

## 🚀 Run It

```bash
python guess_game.py
