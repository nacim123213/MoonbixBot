
import pyautogui
import keyboard
import time

def main():
    print("Script pour la région 2 prêt.")
    print("Appuyez sur 'c' pour cliquer au centre de cette région.")
    while True:
        if keyboard.is_pressed('c'):
            pyautogui.moveTo(617, 407)
            pyautogui.click()
            print(f"Clic effectué au centre de la région 2 : (617, 407)")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()
