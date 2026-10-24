# ==============================================================================
# Projet : mBot2 Code & Go Explorer (Tangible & Screen-Free Coding)
# Carte : CyberPi (Makeblock mBot2)
# Langage : MicroPython / mBlock Python
# ==============================================================================
# Ce script permet au mBot2 de fonctionner comme la souris robot "Colby" :
# 1. Enregistrement des pas via le joystick de la CyberPi
# 2. Visualisation en temps réel de la séquence sur l'écran IPS
# 3. Exécution avec le bouton A (GO)
# 4. Réinitialisation avec le bouton B (CLEAR)
# 5. Détection de collision intelligente via le capteur à ultrasons
# ==============================================================================

import time
import cyberpi

# ------------------------------------------------------------------------------
# CONFIGURATION DU JEU (Personnalisable)
# ------------------------------------------------------------------------------
STEP_DISTANCE_CM = 25     # Taille d'une case sur votre grille (en cm)
ROBOT_SPEED = 40          # Vitesse de déplacement (0 à 100) - 40 assure une bonne précision
MAX_STEPS = 40            # Nombre maximum d'ordres en mémoire
MIN_OBSTACLE_DIST = 8     # Distance d'arrêt d'urgence devant un mur (en cm)

# Liste stockant les ordres en mémoire ('F', 'B', 'L', 'R', 'A')
commands = []

# Dictionnaire des icônes d'affichage
SYMBOLS = {
    'F': "[^] Avance",
    'B': "[v] Recul",
    'L': "[<] Gauche",
    'R': "[>] Droite",
    'A': "[*] Action"
}

def wait_release(button_name):
    """Anti-rebond : attend que le joueur relâche le bouton avant de continuer."""
    while cyberpi.controller.is_press(button_name):
        time.sleep(0.05)

def update_screen(status="En attente"):
    """Met à jour l'écran couleur de la CyberPi."""
    cyberpi.console.clear()
    cyberpi.console.println("== MBOT EXPLORER ==")
    cyberpi.console.println("Statut: " + status)
    cyberpi.console.println("Ordres (" + str(len(commands)) + "/" + str(MAX_STEPS) + ") :")
    
    # Affichage des dernières instructions
    if len(commands) == 0:
        cyberpi.console.println("- (Vide) -")
    else:
        # Affiche jusqu'aux 5 derniers ordres pour ne pas déborder
        recent = commands[-5:]
        line = " ".join([c for c in recent])
        cyberpi.console.println("Derniers: " + line)
    
    cyberpi.console.println("A: GO | B: EFFACER")

def flash_leds(r, g, b):
    """Allume toutes les LED d'une couleur précise."""
    cyberpi.led.on(r, g, b, "all")

def clear_all():
    """Efface la mémoire et réinitialise l'état."""
    global commands
    commands = []
    flash_leds(255, 100, 0)
    cyberpi.audio.play_tone(300, 0.2)
    time.sleep(0.2)
    flash_leds(0, 0, 0)
    update_screen("Memoire effacee")

def add_command(cmd_char, r, g, b):
    """Ajoute une commande dans la séquence si la limite n'est pas atteinte."""
    if len(commands) < MAX_STEPS:
        commands.append(cmd_char)
        flash_leds(r, g, b)
        cyberpi.audio.play_tone(600, 0.1)
        time.sleep(0.1)
        flash_leds(0, 0, 0)
        update_screen("Saisie...")
    else:
        # Mémoire pleine : petit son d'avertissement
        cyberpi.audio.play_tone(200, 0.3)
        update_screen("MEMOIRE PLEINE !")

def run_program():
    """Exécute la séquence mémorisée pas à pas."""
    if len(commands) == 0:
        cyberpi.audio.play_tone(200, 0.2)
        update_screen("Aucun ordre !")
        return

    update_screen("EXECUTION...")
    flash_leds(0, 255, 0)
    cyberpi.audio.play_tone(880, 0.3)
    time.sleep(0.5)

    collision = False

    for idx, cmd in enumerate(commands):
        step_num = idx + 1
        cyberpi.console.clear()
        cyberpi.console.println("== EN ROUTE ! ==")
        cyberpi.console.println("Etape " + str(step_num) + "/" + str(len(commands)))
        cyberpi.console.println("Action: " + SYMBOLS[cmd])

        if cmd == 'F':
            # 1. Vérification obstacle avant d'avancer
            try:
                dist = cyberpi.ultrasonic2.get()
                if 0 < dist < MIN_OBSTACLE_DIST:
                    collision = True
                    break
            except:
                pass
            
            # 2. Avancer d'une case
            flash_leds(0, 255, 0)
            cyberpi.mbot2.straight(STEP_DISTANCE_CM, ROBOT_SPEED)

        elif cmd == 'B':
            # Reculer d'une case
            flash_leds(255, 255, 0)
            cyberpi.mbot2.straight(-STEP_DISTANCE_CM, ROBOT_SPEED)

        elif cmd == 'L':
            # Tourner à gauche de 90°
            flash_leds(0, 100, 255)
            cyberpi.mbot2.turn(-90, ROBOT_SPEED)

        elif cmd == 'R':
            # Tourner à droite de 90°
            flash_leds(255, 120, 0)
            cyberpi.mbot2.turn(90, ROBOT_SPEED)

        elif cmd == 'A':
            # Action festive / Surprise
            flash_leds(255, 0, 255)
            cyberpi.audio.play("cheerful")
            cyberpi.mbot2.turn(360, 60)
            time.sleep(0.2)

        flash_leds(0, 0, 0)
        time.sleep(0.3) # Pause entre les mouvements pour bien décomposer

    # Fin de parcours
    if collision:
        # Alerte obstacle !
        flash_leds(255, 0, 0)
        cyberpi.audio.play("sad")
        cyberpi.console.clear()
        cyberpi.console.println("== OUPS ! MUR EN VUE ==")
        cyberpi.console.println("Collision stoppee !")
        cyberpi.console.println("B: Deboguer et refaire")
        time.sleep(2)
    else:
        # Victoire !
        flash_leds(255, 215, 0)
        cyberpi.audio.play("win")
        cyberpi.console.clear()
        cyberpi.console.println("== VICTOIRE ! ==")
        cyberpi.console.println("Tresor atteint !")
        cyberpi.console.println("B: Nouveau defi")
        time.sleep(2)

    update_screen("Pret pour la suite")

# ------------------------------------------------------------------------------
# BOUCLE PRINCIPALE (Écoute des boutons en mode débranché)
# ------------------------------------------------------------------------------
update_screen("Bienvenue !")
flash_leds(0, 0, 0)

while True:
    # ⬆️ JOYSTICK HAUT -> Avancer
    if cyberpi.controller.is_press('up'):
        wait_release('up')
        add_command('F', 0, 255, 0)

    # ⬇️ JOYSTICK BAS -> Reculer
    elif cyberpi.controller.is_press('down'):
        wait_release('down')
        add_command('B', 255, 255, 0)

    # ⬅️ JOYSTICK GAUCHE -> Tourner à gauche
    elif cyberpi.controller.is_press('left'):
        wait_release('left')
        add_command('L', 0, 100, 255)

    # ➡️ JOYSTICK DROITE -> Tourner à droite
    elif cyberpi.controller.is_press('right'):
        wait_release('right')
        add_command('R', 255, 120, 0)

    # 🔘 JOYSTICK CLIC CENTRE -> Action surprise
    elif cyberpi.controller.is_press('middle'):
        wait_release('middle')
        add_command('A', 255, 0, 255)

    # 🟢 BOUTON A -> GO ! (Exécuter la séquence)
    elif cyberpi.controller.is_press('a'):
        wait_release('a')
        run_program()

    # 🟡 BOUTON B -> CLEAR (Effacer la mémoire)
    elif cyberpi.controller.is_press('b'):
        wait_release('b')
        clear_all()

    time.sleep(0.05)
