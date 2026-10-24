# 🕹️ CyberPi Arcade & Game Dev

> **Apprendre la pensée computationnelle par le développement de jeux vidéo rétro sur CyberPi.**

---

## 🌟 Pourquoi la CyberPi est une console de poche idéale
* **Écran couleur IPS 1.44" (128x128 pixels)** : Parfait pour le pixel art et les grilles de tuiles.
* **Joystick 5 directions** : Ergonomie manette de jeu arcade instantanée.
* **Capteur de mouvement 6 axes (IMU)** : Accéléromètre et gyroscope pour jeux basés sur l'inclinaison physique.
* **Buzzer haute fidélité & bande de 5 LEDs RGB** : Bruitages 8-bit et alertes lumineuses dynamiques.

---

## 🎮 Jeux Disponibles
1. **CyberSnake ([`python/cyber_snake.py`](./python/cyber_snake.py))** :
   * Le classique Snake avec boucle de rafraîchissement, tableau de positions, gestion des collisions et score.
2. **CyberTilt Maze ([`python/cyber_tilt_maze.py`](./python/cyber_tilt_maze.py))** :
   * Labyrinthe gyroscopique où la bille roule selon l'angle physique de la carte CyberPi (`get_pitch()`, `get_roll()`).

---

## 💡 Objectifs Pédagogiques
* Comprendre le cycle fondamental d'un jeu vidéo : `Input` $\rightarrow$ `Update` $\rightarrow$ `Draw`.
* Manipuler des listes, des tuples de coordonnées `(x, y)` et des détections de collision.
* Découvrir la physique du mouvement appliquée aux capteurs inertiels.
