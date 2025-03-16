import pyautogui
import keyboard
import time
import random

def get_cursor_position(prompt):
    """Attend que l'utilisateur appuie sur Entrée pour capturer la position du curseur."""
    print(prompt)
    while not keyboard.is_pressed("enter"):
        time.sleep(0.1)
    x, y = pyautogui.position()
    print(f"Position capturée : ({x}, {y})")
    time.sleep(0.5)  # Petite pause pour éviter un double enregistrement
    return x, y

def calculate_relative_position(top_left, bottom_right, horizontal_percentage, vertical_percentage):
    """Calcule une position relative dans une région avec des pourcentages horizontal et vertical."""
    width = bottom_right[0] - top_left[0]  # Largeur de la région
    height = bottom_right[1] - top_left[1]  # Hauteur de la région
    x = top_left[0] + int(width * horizontal_percentage)
    y = top_left[1] + int(height * vertical_percentage)
    return x, y

def wait_for_activation(toggle_key="q"):
    """Attend que l'utilisateur active ou désactive le mode avec la touche toggle_key."""
    print(f"Appuyez sur '{toggle_key}' pour activer/désactiver le programme.")
    active = False
    while True:
        if keyboard.is_pressed(toggle_key):
            active = not active
            state = "activé" if active else "désactivé"
            print(f"Programme {state}.")
            time.sleep(0.5)  # Petite pause pour éviter les doubles basculements
        if active:
            return

def perform_clicks_single_region(top_left, bottom_right, horizontal_percentage, vertical_percentage, duration=None, interval_range=(0.5, 1.0)):
    """
    Effectue des clics dans une position spécifique pour une seule région.
    Si une durée est fournie, clique continuellement pendant cette durée.
    """
    start_time = time.time() if duration else None
    while True:
        click_position = calculate_relative_position(top_left, bottom_right, horizontal_percentage, vertical_percentage)
        pyautogui.moveTo(click_position[0], click_position[1])
        pyautogui.click()
        print(f"Clic effectué à {click_position}")
        
        if duration and time.time() - start_time >= duration:
            print("Durée atteinte, arrêt des clics.")
            break
        
        # Pause aléatoire entre les clics
        time.sleep(random.uniform(*interval_range))

def main():
    print("Bienvenue dans le programme de définition des régions.")
    
    # Demander le nombre de machines/régions
    while True:
        try:
            num_regions = int(input("Combien de machines/régions voulez-vous définir ? "))
            if num_regions > 0:
                break
            else:
                print("Le nombre doit être supérieur à 0.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")
    
    regions = []

    # Capturer les régions
    for i in range(1, num_regions + 1):
        print(f"\nDéfinir la région pour la machine {i} :")
        top_left = get_cursor_position(f"Placez le curseur sur le coin supérieur gauche de la région {i} et appuyez sur Entrée.")
        bottom_right = get_cursor_position(f"Placez le curseur sur le coin inférieur droit de la région {i} et appuyez sur Entrée.")
        
        regions.append((top_left, bottom_right))
        print(f"Région {i} définie : coin supérieur gauche {top_left}, coin inférieur droit {bottom_right}")

    print("\nRégions définies avec succès.")

    while True:
        wait_for_activation(toggle_key="q")

        current_index = 0
        while current_index < num_regions:
            top_left, bottom_right = regions[current_index]
            print(f"\nTraitement de la machine {current_index + 1}.")

            print(f"Phase 1 : Clic à 63% Y pour la machine {current_index + 1}.")
            click_position = calculate_relative_position(top_left, bottom_right, horizontal_percentage=0.5, vertical_percentage=0.63)
            pyautogui.moveTo(click_position[0], click_position[1])
            pyautogui.click()
            print(f"Clic effectué à {click_position}")

            time.sleep(1.5)

            print(f"Phase 2 : Clic à 50% horizontal et 50% vertical pendant 47 secondes pour la machine {current_index + 1}.")
            perform_clicks_single_region(
                top_left,
                bottom_right,
                horizontal_percentage=0.5,
                vertical_percentage=0.5,
                duration=47,
                interval_range=(0.01, 0.02)
            )

            time.sleep(2)

            print(f"Phase 3 : Clic à 3.92% horizontal et 3.58% vertical pour la machine {current_index + 1}.")
            final_click_position = calculate_relative_position(top_left, bottom_right, horizontal_percentage=0.0392, vertical_percentage=0.0358)
            pyautogui.moveTo(final_click_position[0], final_click_position[1])
            pyautogui.click()
            print(f"Clic effectué à {final_click_position}")

            time.sleep(5)

            current_index += 1

        print("\nCycle complet terminé. Pause de 8 minutes avant de recommencer.")
        time.sleep(8 * 60)  # 8 minutes

if __name__ == "__main__":
    main()
