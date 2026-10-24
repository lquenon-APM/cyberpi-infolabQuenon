# ==============================================================================
# Station Environnementale & Sonomètre de Classe (CyberPi)
# Conçu par InfoLab Quenon
# ==============================================================================
import cyberpi
import time

class ClassEnvironmentStation:
    def __init__(self):
        self.history_loudness = [0] * 60  # Historique sur 60 mesures
        cyberpi.display.clear()

    def update_sensors(self):
        # Mesure du volume sonore (0 à 100) et de la lumière ambiante (0 à 100)
        loudness = cyberpi.get_loudness()
        light = cyberpi.get_brightness()

        self.history_loudness.pop(0)
        self.history_loudness.append(loudness)

        # Gestion des 5 LEDs RGB selon le seuil de bruit
        if loudness < 35:
            # Calme : Vert
            cyberpi.led.on(0, 200, 0)
        elif loudness < 65:
            # Niveau moyen : Orange
            cyberpi.led.on(255, 140, 0)
        else:
            # Alerte bruit : Rouge clignotant + bip d'avertissement
            cyberpi.led.on(255, 0, 0)
            cyberpi.audio.play_tone(440, 0.08)

        return loudness, light

    def draw_dashboard(self, loudness, light):
        cyberpi.display.clear()

        # En-tête
        cyberpi.display.set_color(100, 200, 255)
        cyberpi.display.show_label("INFOLAB CLASSE", 14, 10, 5)

        # Indicateurs numériques
        cyberpi.display.set_color(255, 255, 255)
        cyberpi.display.show_label(f"Bruit : {int(loudness)} %", 12, 10, 28)
        cyberpi.display.show_label(f"Lumière: {int(light)} %", 12, 10, 46)

        # Graphique temporel du bruit (zone inférieure)
        cyberpi.display.set_color(80, 80, 100)
        cyberpi.display.draw_line(10, 115, 118, 115)  # Ligne de base

        # Tracé des barres d'historique
        for i, val in enumerate(self.history_loudness):
            bx = 10 + (i * 108 // 60)
            bar_h = min(45, val * 45 // 100)
            by = 115 - bar_h

            if val > 65:
                cyberpi.display.set_color(255, 50, 50)
            elif val > 35:
                cyberpi.display.set_color(255, 200, 0)
            else:
                cyberpi.display.set_color(50, 220, 50)

            cyberpi.display.draw_line(bx, 115, bx, by)

station = ClassEnvironmentStation()

while True:
    loudness, light = station.update_sensors()
    station.draw_dashboard(loudness, light)
    time.sleep(0.15)
