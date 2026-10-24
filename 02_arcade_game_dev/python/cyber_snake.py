# ==============================================================================
# CyberSnake — Jeu Rétro Arcade pour CyberPi (Makeblock)
# Conçu par InfoLab Quenon
# ==============================================================================
import cyberpi
import time
import random

# Dimensions de la grille
GRID_W = 16
GRID_H = 16
CELL_SIZE = 8  # 16 * 8 = 128x128 pixels (résolution écran CyberPi)

class SnakeGame:
    def __init__(self):
        self.reset()

    def reset(self):
        self.snake = [(8, 8), (8, 9), (8, 10)]
        self.dir = (0, -1)  # Vers le haut au départ
        self.score = 0
        self.game_over = False
        self.spawn_apple()
        cyberpi.display.clear()
        cyberpi.led.on(0, 255, 0)  # LEDs vertes

    def spawn_apple(self):
        while True:
            self.apple = (random.randint(0, GRID_W - 1), random.randint(0, GRID_H - 1))
            if self.apple not in self.snake:
                break

    def update(self):
        if self.game_over:
            if cyberpi.controller.is_press('a'):
                self.reset()
            return

        # Contrôles via joystick
        if cyberpi.controller.is_press('up') and self.dir != (0, 1):
            self.dir = (0, -1)
        elif cyberpi.controller.is_press('down') and self.dir != (0, -1):
            self.dir = (0, 1)
        elif cyberpi.controller.is_press('left') and self.dir != (1, 0):
            self.dir = (-1, 0)
        elif cyberpi.controller.is_press('right') and self.dir != (-1, 0):
            self.dir = (1, 0)

        # Nouvelle tête
        head_x, head_y = self.snake[0]
        dx, dy = self.dir
        new_head = (head_x + dx, head_y + dy)

        # Collisions murs ou queue
        if (new_head[0] < 0 or new_head[0] >= GRID_W or
            new_head[1] < 0 or new_head[1] >= GRID_H or
            new_head in self.snake):
            self.game_over = True
            cyberpi.led.on(255, 0, 0)  # LEDs rouges
            cyberpi.audio.play('screaming')
            return

        self.snake.insert(0, new_head)

        # Manger la pomme
        if new_head == self.apple:
            self.score += 1
            cyberpi.audio.play_tone(880, 0.05)
            self.spawn_apple()
        else:
            self.snake.pop()

    def draw(self):
        if self.game_over:
            cyberpi.display.clear()
            cyberpi.display.set_color(255, 0, 0)
            cyberpi.display.show_label("GAME OVER", 16, 20, 40)
            cyberpi.display.set_color(255, 255, 255)
            cyberpi.display.show_label(f"Score: {self.score}", 14, 35, 70)
            cyberpi.display.show_label("Bouton A: Rejouer", 12, 10, 100)
            return

        cyberpi.display.clear()

        # Dessiner la pomme (rouge)
        ax = self.apple[0] * CELL_SIZE
        ay = self.apple[1] * CELL_SIZE
        cyberpi.display.set_color(255, 50, 50)
        cyberpi.display.draw_rect(ax, ay, CELL_SIZE, CELL_SIZE, True)

        # Dessiner le serpent (vert clair pour le corps, jaune pour la tête)
        for i, (sx, sy) in enumerate(self.snake):
            px = sx * CELL_SIZE
            py = sy * CELL_SIZE
            if i == 0:
                cyberpi.display.set_color(255, 255, 0)  # Tête jaune
            else:
                cyberpi.display.set_color(50, 220, 50)  # Corps vert
            cyberpi.display.draw_rect(px, py, CELL_SIZE, CELL_SIZE, True)

game = SnakeGame()

# Boucle de jeu (environ 6 à 8 FPS pour un Snake rétro accessible)
while True:
    game.update()
    game.draw()
    time.sleep(0.12)
