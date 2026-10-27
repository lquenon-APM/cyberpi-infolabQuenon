# 🐭 mBot2 Code & Go Explorer (Tangible & Screen-Free)

> **Inspiré du célèbre jeu éducatif *Code & Go Robot Mouse*, ce produit transforme le Makeblock mBot2 en robot d'exploration tangible, 100% débranché sans écran pendant le jeu pour le cycle 2 (1re-2e primaire / CP-CE1, 6-8 ans).**

---

## 🌟 Le Concept
Une fois le code MicroPython téléversé, l'ordinateur est éteint :
* **Démarche en 3 temps (Montessori / Pédagogie active) :**
  1. *Simulation sur table* avec une petite voiture / mascotte papercraft 3D sur le plateau A4 Paysage.
  2. *Encodage visuel et tangible* en posant les cartes (60×60 mm) sur le Tapis de programmation 3×3.
  3. *Exécution au sol* sur l'arène quadrillée en dalles de 25 cm.
* **Saisie intuitive :** L'enfant utilise le joystick 5 directions de la CyberPi pour programmer sa séquence de mouvements (Avancer, Reculer, Pivoter à gauche, Pivoter à droite, Action Magique).
* **Feedback visuel & audio :** L'écran couleur 1.44" affiche les flèches ordonnées et le buzzer émet des tonalités distinctes par ordre.
* **Moteurs encodeurs asservis :** Avance avec une précision millimétrique de 25 cm (taille standard d'une dalle de jeu) et rotations parfaites à 90°.
* **Action Magique à somme nulle d'angles :** Danse lumineuse et sonore festive qui revient rigoureusement à son orientation initiale (0°) pour préserver l'alignement sur la grille.

---

## 📂 Contenu du Produit

* 🐍 [`python/mbot2_code_and_go.py`](./python/mbot2_code_and_go.py) : Script MicroPython complet pour CyberPi & mBot2.
* 🎴 [`cartes/cartes_a_imprimer.html`](./cartes/cartes_a_imprimer.html) : Planches A4 optimisées de 36 cartes physiques prêtes à découper (60×60 mm) + Tapis de programmation 3×3 (4 pages A4 au total, 0 page blanche).
* 🗺️ [`plateau/plateau_simulation_a4.html`](./plateau/plateau_simulation_a4.html) : Plateau de simulation sur table au format A4 Paysage (cases 52×49 mm avec coordonnées A1-C4) + Mascotte mBot2 papercraft 3D à plier et pions d'appoint.
* 📖 [`docs/cartes_de_programmation.md`](./docs/cartes_de_programmation.md) : Fiche didactique des cartes et astuces anti-pièges.
* 🧱 [`docs/02_materiel_et_plateau.md`](./docs/02_materiel_et_plateau.md) : Guide de fabrication du matériel (table & sol).
* 📖 [`docs/01_cadrage_et_concept.md`](./docs/01_cadrage_et_concept.md) : Cadrage complet et analyse comparative avec Colby.
* 🎮 [`docs/03_niveaux_et_activites.md`](./docs/03_niveaux_et_activites.md) : Livret de 10+ défis progressifs et jeu coopératif "Le Donjon du mBot".

---

## 🎮 Commandes de Jeu sur la CyberPi
| Commande | Action | Description |
| :---: | :---: | :--- |
| **Joystick Haut** | ⬆️ Avancer | Avance d'une dalle (25 cm) |
| **Joystick Bas** | ⬇️ Reculer | Recule d'une dalle (25 cm) |
| **Joystick Gauche**| ⬅️ Gauche | Pivot sur place de 90° à gauche |
| **Joystick Droite**| ➡️ Droite | Pivot sur place de 90° à droite |
| **Joystick Clic**  | ⭐ Action | Danse festive 360° sans perte d'orientation |
| **Bouton A**       | ▶️ Exécuter | Lance la séquence programmée |
| **Bouton B**       | 🔄 Reset | Efface la mémoire et réinitialise |
