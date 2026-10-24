# ==============================================================================
# CyberTilt Maze — Labyrinthe Gyroscopique (Makeblock CyberPi)
# Conçu par InfoLab Quenon
# ==============================================================================
import cyberpi
import time

class TiltMaze:
    def __init__(self):
        self.ball_x = 20.0
        self.ball_y = 20.0
        self.target_x = 105
        self.target_y = 105
        self.radius = 4
        self.win = False
        cyberpi.led.on(0, 0, 255)  # Bleu

        # Murs (x, y, w, h)
        self.walls = [
            (0, 0, 128, 4),
            (0, 0, 4, 128),
            (124, 0, 4, 128),
            (0, 124, 128, 4),
            (40, 0, 6, 80),
            (80, 50, 6, 78)
        ]

    def update(self):
        if self.win:
            if cyberpi.controller.is_press('a'):
                self.__init__()
            return

        # Lecture de l'inclinaison (roll / pitch) du gyroscope CyberPi
        pitch = cyberpi.get_pitch()
        roll = cyberpi.get_roll()

        # Vitesse proportionnelle à l'inclinaison
        vx = roll * 0.15
        vy = -pitch * 0.15

        # Déplacement prédictif
        nx = self.ball_x + vx
        ny = self.ball_y + vy

        # Test de collision simple avec les bords
        nx = max(self.radius + 4, min(124 - self.radius, nx))
        ny = max(self.radius + 4, min(124 - self.radius, ny))

        self.ball_x = nx
        self.ball_y = ny

        # Victoire si la bille atteint la zone cible
        dx = self.ball_x - self.target_x
        dy = self.ball_y - self.target_y
        if (dx * dx + dy * dy) < (self.radius + 8) ** 2:
            self.win = True
            cyberpi.led.on(0, 255, 0)
            cyberpi.audio.play('level-up')

    def draw(self):
        cyberpi.display.clear()

        # Cible (Trésor vert)
        cyberpi.display.set_color(50, 255, 50)
        cyberpi.display.draw_circle(self.target_x, self.target_y, 8, True)

        # Murs
        cyberpi.display.set_color(150, 150, 200)
        for wx, wy, ww, wh in self.walls:
            cyberpi.display.draw_rect(wx, wy, ww, wh, True)

        # Bille du joueur (Orangée)
        cyberpi.display.set_color(255, 165, 0)
        cyberpi.display.draw_circle(int(self.ball_x), int(self.ball_y), self.radius, True)

        if self.win:
            cyberpi.display.set_color(255, 255, 255)
            cyberpi.display.show_label("BRAVO !", 16, 30, 50)
            cyberpi.display.show_label("A: Rejouer", 12, 30, 80)

game = TiltMaze()

while True:
    game.update()
    game.draw()
    time.sleep(0.04)  # ~25 FPS réactif
