
import pyautogui
import keyboard
import time

def main():
    print("Script pour la r�gion 1 pr�t.")
    print("Appuyez sur 'c' pour cliquer au centre de cette r�gion.")
    while True:
        if keyboard.is_pressed('c'):
            pyautogui.moveTo(195, 410)
            pyautogui.click()
            print(f"Clic effectu� au centre de la r�gion 1 : (195, 410)")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()
