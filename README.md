# 🤖 cyberpi-infolabQuenon

> **Le Studio de Produits Pédagogiques & Robotiques Makeblock (CyberPi & mBot2)**  
> Conçu et développé par **Laurent Quenon (InfoLab Quenon)** pour l'apprentissage de l'informatique, de la programmation tangible débranchée et des sciences connectées (STEM).

---

## 🌟 Vision du Projet

**cyberpi-infolabQuenon** est un écosystème autonome dédié à la création d'expériences d'apprentissage stimulantes sur la carte **Makeblock CyberPi** et le robot **mBot2**. 

Ce projet prouve que la robotique pédagogique peut dépasser les simples tutoriels basiques pour devenir :
1. **Tangible & Sans écran** pour le primaire et début secondaire (développer la logique sans fatigue visuelle).
2. **Ludique & Créatif** pour les clubs et ateliers (création de jeux d'arcade rétro en MicroPython).
3. **Scientifique & Citoyen** pour les laboratoires scolaires (capteurs environnementaux et données temps réel).

---

## 🚀 Les 3 Gammes de Produits Pédagogiques

```
cyberpi-infolabQuenon/
├── 01_code_and_go_explorer/   # 🐭 Gamme 1 : Exploration tangible sans écran (style Colby)
├── 02_arcade_game_dev/        # 🕹️ Gamme 2 : Développement de jeux rétro en MicroPython
├── 03_iot_smart_sensors/      # 🌡️ Gamme 3 : Station environnementale & sonomètre de classe
├── simulator/                 # 💻 Simulateur Web autonome (HTML5/Canvas)
└── docs/                      # 📖 Guides enseignants, architecture et téléversement
```

### 1. 🐭 [Code & Go Explorer](./01_code_and_go_explorer/)
* **Concept :** Une fois le code injecté, l'ordinateur est éteint. L'enfant programme les déplacements du robot directement avec le joystick de la CyberPi.
* **Moteurs encodeurs asservis :** Des pas de 25 cm et des rotations à 90° au millimètre près.
* **Matériel physique :** [Planches A4 de 36 cartes fléchées prêtes à imprimer](./01_code_and_go_explorer/cartes/cartes_a_imprimer.html).

### 2. 🕹️ [Arcade & Game Dev](./02_arcade_game_dev/)
* **Concept :** Transformer la CyberPi en console de jeux vidéo portable de poche.
* **Titres inclus :**
  * `cyber_snake.py` : Le classique Snake sur écran IPS 128x128.
  * `cyber_tilt_maze.py` : Labyrinthe gyroscopique exploitant l'inclinaison physique 6 axes.

### 3. 🌡️ [IoT & Smart Sensors](./03_iot_smart_sensors/)
* **Concept :** Station de monitoring sonore et lumineux en direct pour la classe.
* **Fonctions :** Feedback visuel feu tricolore sur 5 LEDs RGB, oscillo-graphe du bruit et sonomètre en direct.

---

## 💻 Simulateur Web Intégré

Envie de tester sans matériel physique ?  
Ouvrez simplement [`simulator/index.html`](./simulator/index.html) dans votre navigateur pour manipuler la CyberPi virtuelle avec ses LEDs, son joystick et son écran couleur !

---

## 🛠️ Démarrage Rapide

### Prérequis
* Un robot **Makeblock mBot2** avec son micro-ordinateur **CyberPi**.
* Le logiciel **mBlock 5** (Desktop ou Web) avec l'extension Python / CyberPi.

### Téléverser un script :
1. Ouvrez **mBlock 5** et connectez votre CyberPi en USB (port COM).
2. Basculez en mode **Python**.
3. Copiez-collez l'un des scripts du dossier `python/` (ex: `01_code_and_go_explorer/python/mbot2_code_and_go.py`).
4. Cliquez sur **Téléverser**. Le robot est immédiatement autonome !

---

## 📜 Licence
Projet open-source publié sous licence MIT — Conçu par Laurent Quenon.
