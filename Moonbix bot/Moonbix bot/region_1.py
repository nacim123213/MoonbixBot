
import pyautogui
import keyboard
import time

def main():
    print("Script pour la région 1 prêt.")
    print("Appuyez sur 'c' pour cliquer au centre de cette région.")
    while True:
        if keyboard.is_pressed('c'):
            pyautogui.moveTo(195, 410)
            pyautogui.click()
            print(f"Clic effectué au centre de la région 1 : (195, 410)")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()
