
import pyautogui
import keyboard
import time

def main():
    print("Script pour la r�gion 2 pr�t.")
    print("Appuyez sur 'c' pour cliquer au centre de cette r�gion.")
    while True:
        if keyboard.is_pressed('c'):
            pyautogui.moveTo(617, 407)
            pyautogui.click()
            print(f"Clic effectu� au centre de la r�gion 2 : (617, 407)")
            break
        time.sleep(0.1)

if __name__ == "__main__":
    main()
