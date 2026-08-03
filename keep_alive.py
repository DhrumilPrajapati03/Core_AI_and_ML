import random
import time

import pyautogui


MOVE_PIXELS = 50
MOVE_DURATION = 0.5
PAUSE_BETWEEN_MOVES = 0.5

print("Keep-alive started.")
print("Press Ctrl+C in the terminal to stop.")

try:
    while True:
        # Move mouse right
        pyautogui.moveRel(
            MOVE_PIXELS,
            0,
            duration=MOVE_DURATION,
        )

        time.sleep(PAUSE_BETWEEN_MOVES)

        # Move mouse back to the original position
        pyautogui.moveRel(
            -MOVE_PIXELS,
            0,
            duration=MOVE_DURATION,
        )

        # Press Shift without typing anything
        pyautogui.press("shift")

        wait_seconds = random.randint(60, 120)

        print(
            f"Activity sent. "
            f"Mouse moved {MOVE_PIXELS}px. "
            f"Waiting {wait_seconds} seconds..."
        )

        time.sleep(wait_seconds)

except KeyboardInterrupt:
    print("\nKeep-alive stopped.")
    