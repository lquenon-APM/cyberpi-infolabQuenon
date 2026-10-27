# 🎮 Cahier des Niveaux & Défis Ludiques

Voici la progression pédagogique en 4 niveaux avec des défis directement transposables sur le **Plateau de Simulation de Table (A4 Paysage, cases A1 à C4)** puis sur l'arène au sol.

---

## 🟢 NIVEAU 1 : Premiers Pas de l'Explorateur (Lignes & Translations)
*Objectif pédagogique : Maîtriser le comptage, le séquençage linéaire et l'association Carte $\leftrightarrow$ Joystick du robot.*

### Défi 1.1 : La Course en Ligne Droite
* **Mise en place sur le plateau :**
  * Départ : Case **A1** (orienté vers la droite, regard vers A2).
  * Trésor : Case **A4**. Aucun obstacle.
* **Phase sur table :** L'enfant fait glisser sa petite voiture de A1 vers A4 en comptant les bonds : *« 1 pas vers A2, 2 pas vers A3, 3 pas vers A4 ! »*.
* **Cartes sur le Tapis :** `[Avancer] -> [Avancer] -> [Avancer]` (3 pas).
* **Validation CyberPi :** 3 coups de joystick vers le Haut $\rightarrow$ Appui sur **A (GO)**.

### Défi 1.2 : Marche Arrière de Dégagement
* **Mise en place :** Robot en **B3**, regard vers B4 face à un mur en B4. Le trésor est en arrière en **B1**.
* **Mission :** Revenir au trésor en marche arrière sans faire demi-tour.
* **Cartes sur le Tapis :** `[Reculer] -> [Reculer]` (2 pas).

### Défi 1.3 : La Ligne avec Célébration
* **Mise en place :** Départ en **C1**, Trésor en **C4**.
* **Mission :** Rejoindre le trésor et déclencher la fête à l'arrivée !
* **Cartes sur le Tapis :** `[Avancer] -> [Avancer] -> [Avancer] -> [Action Magique]`.

---

## 🔵 NIVEAU 2 : Le Maître des Virages (Rotations à 90°)
*Objectif pédagogique : Dépasser le réflexe égocentrique et assimiler que la rotation se fait sur place sans avance.*

### Défi 2.1 : Le Coude en L
* **Mise en place :**
  * Départ : Case **A1** (orienté vers le bas, regard vers B1).
  * Trésor : Case **C2**.
* **Phase sur table :** L'enfant avance sa voiturette en B1, puis en C1. Arrivé en C1, il la fait pivoter à gauche face à C2, puis avance sur C2.
* **Cartes sur le Tapis :** `[Avancer] -> [Avancer] -> [Tourner Gauche] -> [Avancer]`.
* **Discussion Débogage :** Si l'enfant oublie le dernier pas en pensant que « Tourner » fait aussi avancer d'une case, on lui montre sur la voiturette que tourner pivote sur place.

### Défi 2.2 : Le Contournement du Rocher
* **Mise en place :**
  * Départ : Case **B1** (regard vers B2).
  * Obstacle Mur : Case **B2**.
  * Trésor : Case **B4**.
* **Mission :** Faire un crochet par la ligne A ou C pour contourner l'obstacle en B2.
* **Algorithme possible (par le haut) :**
  `[Tourner Gauche] -> [Avancer] -> [Tourner Droite] -> [Avancer] -> [Avancer] -> [Tourner Droite] -> [Avancer] -> [Tourner Gauche]`.

### Défi 2.3 : Le Retour vers l'Enfant (Le Test de Décentration)
* **Mise en place :** Le robot est en **A3**, orienté vers le bas (il « regarde » l'enfant assis devant le plateau). Il doit tourner pour aller en **A1**.
* **Le piège :** Pour aller vers la gauche de l'enfant, le robot doit tourner sur sa propre **droite** !
* **Astuce avec la mascotte 3D :** L'enfant regarde le flanc orange 🟧 de la mascotte mBot2 pour confirmer sans hésiter : *« Sa droite c'est par là ! »*.

---

## 🟡 NIVEAU 3 : Le Labyrinthe Mystère & Mode Radar
*Objectif pédagogique : Planifier un parcours complexe avec plusieurs obstacles et vérifier la faisabilité sur table.*

### Défi 3.1 : Le Grand Slalom en S
* **Mise en place :**
  * Départ : **A1** (regard vers A2).
  * Murs : **A3**, **B2**, **C3**.
  * Trésor : **C4**.
* **Mission :** Trouver le seul chemin libre reliant A1 à C4.
* **Phase sur table :** L'enfant trace le chemin du doigt avec la voiturette, puis pose ses 8 cartes sur la réglette 3×3.

### Défi 3.2 : Le Radar Détecteur d'Embûches (Capteur Ultrasons actif)
* **Règle :** Si le mBot2 arrive à moins de 8 cm d'un mur non anticipé, il s'arrête net, émet un signal d'alerte et recule d'un pas. L'enfant gagne une étoile de débogage s'il modifie sa séquence pour contourner l'obstacle.

---

## 🔴 NIVEAU 4 : Le Jeu de Société Coopératif "Le Donjon du mBot"
*2 Joueurs : Père & Fils (ou Binôme Pilote / Navigateur) contre le Donjon !*

### Matériel de jeu :
* Le Plateau de Simulation A4 et la voiturette.
* 1 dé à 6 faces.
* 6 cartes Murs et le Trésor.

### Déroulement de la partie :
1. **Construction secrète :** Le joueur 1 (ex. le père) pose 3 murs et le trésor sur le plateau.
2. **Phase d'énergie (Lancer de dé) :** Le joueur 2 (le fils) lance le dé : le chiffre obtenu indique le nombre maximal de cartes de commande qu'il a le droit de programmer pour ce tour.
3. **Planification conjointe :** Ils déplacent la mascotte sur la table et décident du meilleur coup.
4. **Exécution :** Le mBot2 avance. Dès qu'il atteint le fromage avant d'avoir épuisé les réserves d'énergie, la victoire est remportée !
