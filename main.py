import time
import pyautogui


if __name__ == '__main__':
    print("Checking for 'download' and 'slow download' buttons...")
    while True:
        time.sleep(3)

        try:
            x, y = pyautogui.locateCenterOnScreen('./assets/download.png', confidence=0.9)
            pyautogui.click(x, y)
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"[{current_time}] Clicked 'download button' at {x}, {y}.")

        except pyautogui.ImageNotFoundException:
            pass

        time.sleep(3)

        try:
            x, y = pyautogui.locateCenterOnScreen('./assets/slow_download.png', confidence=0.8, grayscale=True)
            pyautogui.click(x, y)
            current_time = time.strftime("%H:%M:%S", time.localtime())
            print(f"[{current_time}] Clicked 'slow download' button at {x}, {y}.")

        except pyautogui.ImageNotFoundException:
            continue
