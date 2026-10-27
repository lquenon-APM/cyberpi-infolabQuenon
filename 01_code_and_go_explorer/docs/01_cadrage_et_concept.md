# 🚀 Cadrage & Vision : Projet "mBot2 Code & Go Explorer"

## 1. Contexte & Intention
L'objectif de ce projet est de transposer l'univers et les vertus pédagogiques du célèbre jouet éducatif **Code & Go® Robot Mouse** (apprentissage de la programmation tangible, débranchée et spatiale) sur le robot éducatif **Makeblock mBot2** (équipé de la carte contrôleur **CyberPi**).

Le projet est conçu pour être partagé en famille ou en classe (début primaire / CP-CE1 / 6-8 ans) :
* Offrir une expérience de jeu **sans écran** (*screen-free*) une fois le programme injecté dans le robot.
* Développer la **pensée informatique** (séquençage, abstraction, décomposition de problème, débogage).
* Manipuler du matériel physique :
  * Un **plateau de simulation sur table A4** avec une petite voiture / mascotte 3D pour éprouver physiquement les déplacements.
  * Un **tapis de programmation 3×3** pour aligner les cartes de codage.
  * Des **cartes carrées 60×60 mm** hautement visuelles avec pictogrammes vectoriels.
  * Des dalles modulaires de 25 cm et des murs pour l'arène au sol.
* Évoluer d'un jeu de manipulation simple jusqu'à un véritable jeu de société coopératif.

---

## 2. Tableau de Transposition : Code & Go vs mBot2 Explorer

| Fonctionnalité | Code & Go Mouse (Colby) | mBot2 Explorer (CyberPi) |
| :--- | :--- | :--- |
| **Boutons de saisie** | 4 flèches physiques sur le dos | **Joystick 5 directions** de la CyberPi (Haut, Bas, Gauche, Droite, Clic central) |
| **Bouton Exécuter (GO)** | Bouton vert central | **Bouton physique A** de la CyberPi |
| **Bouton Effacer (CLEAR)** | Bouton jaune | **Bouton physique B** de la CyberPi |
| **Retour visuel du code** | Aucun (mémoire aveugle) | **Écran couleur IPS** : affiche la suite des flèches en direct et le numéro d'étape ! |
| **Effets sonores & animations** | Couinements aléatoires (Bouton Action) | **Haut-parleur HD & 5 LED RGB** : sons joyeux, fanfare de victoire, animations lumineuses |
| **Action Magique** | Rotation aléatoire | **Danse festive asservie** : pivot gauche/droite avec retour strict à l'orientation initiale (0°) |
| **Précision des déplacements**| Moteurs CC à friction (dérive possible) | **Moteurs encodeurs asservis** : pas précis de 25 cm et virages précis à 90° |
| **Détection du but / murs** | Visuelle uniquement (l'enfant regarde) | **Capteur à ultrasons 2** : détection automatique des obstacles et du trésor |
| **Simulation sur table** | Non incluse | **Plateau A4 Paysage (cases 52×49 mm)** + mascotte papercraft 3D avec repères visuels |
| **Taille d'une case au sol** | 12,5 cm $\times$ 12,5 cm | **25 cm $\times$ 25 cm** (adaptée au gabarit de rotation du mBot2) |

---

## 3. Les Piliers Didactiques & Pédagogiques

### A. La boucle en 3 temps (Du concret à l'exécution)
1. **Temps 1 — Simulation sur table :** L'enfant place sa figurine / petite voiture sur le plateau de simulation A4. Il la déplace manuellement pour tester la route et anticiper les virages.
2. **Temps 2 — Encodage tangible sur le Tapis :** À chaque pas de la voiturette, il dépose la carte correspondante (60×60 mm) sur les cases du tapis de programmation.
3. **Temps 3 — Saisie CyberPi & Validation au sol :** Il recopie sa séquence sur le joystick de la CyberPi, pose le robot sur la piste au sol et appuie sur **A (GO)**.
4. **Temps 4 — Débogage bienveillant :** Si le robot heurte un mur ou rate le trésor, on compare le comportement du robot avec la ligne de cartes, on identifie l'erreur, on efface avec **B** et on corrige.

### B. Les compétences cognitives mobilisées
* **Décentration spatiale :** Comprendre que tourner à gauche ou à droite se fait *du point de vue du robot*.
* **Distinction rotation / translation :** Assimiler qu'un ordre "Tourner" pivote sur place à 90° sans changer de case.
* **Structuration spatiale & géométrie :** Utilisation d'un repère orthonormé simple (colonnes 1 à 4, lignes A à C).

---

## 4. Feuille de Route & Livrables Réalisés

- [x] **Étape 1 :** Cadrage du concept et documentation fondatrice.
- [x] **Étape 2 :** Kit de 36 cartes physiques (60×60 mm) + Tapis 3×3 en 4 planches A4 (zéro page blanche, motifs vectoriels intégrés).
- [x] **Étape 3 :** Plateau de simulation de table A4 Paysage (4×3 cases de 52×49 mm) et mascotte mBot2 Papercraft 3D pliable.
- [x] **Étape 4 :** Script MicroPython asservi avec chorégraphie d'Action Magique à somme nulle d'angles (`mbot2_code_and_go.py`).
- [x] **Étape 5 :** Cahier de progression pédagogique et défis modulaires.
