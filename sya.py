#mouse position 
import pyautogui
import keyboard

def get_mouse_position():
    print("Move your mouse to the desired position and press 'p' to get the position.")
    while True:
        if keyboard.is_pressed('p'):
            # Get the current mouse position
            x, y = pyautogui.position()
            print(f"Mouse position: ({x}, {y})")
            break

get_mouse_position()
#####################################################################################################
#code to run

import pyautogui
import time

def automate_typing_and_clicks(click_position, text_to_type, repetitions, delay):
    # Perform the loop
    for _ in range(repetitions):
        # Click at the specified position
        pyautogui.click(click_position)

        # Type the specified text
        pyautogui.write(text_to_type)

        # Press Enter
        pyautogui.press('enter')

        # Wait for the specified delay
        time.sleep(delay)

# Example usage
time.sleep(4)
click_position = (1328, 936) # Replace with your click position
text_to_type = "sorryyyyyyyyyyyy"  # Replace with the text you want to type
repetitions = 94
delay = 0.4 # Delay in seconds

automate_typing_and_clicks(click_position, text_to_type, repetitions, delay)
