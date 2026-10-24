# 🐭 mBot2 Code & Go Explorer (Tangible & Screen-Free)

> **Inspiré du célèbre jeu éducatif *Code & Go Robot Mouse*, ce produit transforme le Makeblock mBot2 en robot d'exploration tangible, 100% débranché sans écran pendant le jeu.**

---

## 🌟 Le Concept
Une fois le code MicroPython téléversé, l'ordinateur est éteint :
* **Saisie intuitive :** L'enfant utilise le joystick 5 directions de la CyberPi pour programmer sa séquence de mouvements (Avancer, Reculer, Pivoter à gauche, Pivoter à droite, Action surprise).
* **Feedback visuel & audio :** L'écran couleur 1.44" affiche les flèches ordonnées et le buzzer émet des tonalités distinctes par ordre.
* **Moteurs encodeurs asservis :** Avance avec une précision millimétrique de 25 cm (taille standard d'une dalle de jeu) et rotations parfaites à 90°.
* **Détection du trésor :** Le capteur ultrasons détecte l'arrivée devant l'objectif et déclenche une fanfare lumineuse.

---

## 📂 Contenu du Produit
* [`python/mbot2_code_and_go.py`](./python/mbot2_code_and_go.py) : Script MicroPython complet pour CyberPi & mBot2.
* [`cartes/cartes_a_imprimer.html`](./cartes/cartes_a_imprimer.html) : Planches A4 de 36 cartes physiques prêtes à découper (flèches, départs, trésors, obstacles).

---

## 🎮 Commandes de Jeu sur la CyberPi
| Commande | Action | Description |
| :---: | :---: | :--- |
| **Joystick Haut** | ⬆️ Avancer | Avance d'une dalle (25 cm) |
| **Joystick Bas** | ⬇️ Reculer | Recule d'une dalle (25 cm) |
| **Joystick Gauche**| ⬅️ Gauche | Pivot sur place de 90° à gauche |
| **Joystick Droite**| ➡️ Droite | Pivot sur place de 90° à droite |
| **Joystick Clic**  | ⭐ Action | Déclenche un son et un jeu de lumière |
| **Bouton A**       | ▶️ Exécuter | Lance la séquence programmée |
| **Bouton B**       | 🔄 Reset | Efface la mémoire et réinitialise |
