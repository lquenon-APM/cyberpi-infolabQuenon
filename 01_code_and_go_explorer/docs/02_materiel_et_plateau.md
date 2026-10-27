# 🧱 Guide Matériel, Plateaux & Éléments à Fabriquer

Pour offrir une expérience de jeu aussi immersive et attrayante que le jouet commercial, le projet s'articule autour d'un **double dispositif matériel** :
1. **À l'échelle de la table (Phase de réflexion & simulation) :** Le Plateau A4 Paysage et les figurines miniatures.
2. **À l'échelle du sol (Phase d'exécution réelle) :** Les dalles de 25 cm, les murs en relief et le robot mBot2 réel.

---

## 1. Le Plateau de Simulation de Table (A4 Paysage)

Disponible dans [`plateau_simulation_a4.html`](file:///c:/Users/admin/Documents/AI_assisted/agentic-ai/2_livrables/pedagogie/cours/Robotique_mBot2_Code_and_Go/plateau_simulation_a4.html) :

### Planche 1 : La Piste de Table Quadrillée
* **Format :** A4 Paysage (297 mm $\times$ 210 mm), conçu pour être plastifié ou glissé dans une pochette transparente.
* **Grille de 4 colonnes $\times$ 3 lignes (12 cases) :**
  * Dimensions des cases : **52 mm de large $\times$ 49 mm de haut** (calibrage sans aucune troncature).
  * Coordonnées complètes de **A1** à **C4** pour énoncer des missions précises (*« Pars de A1, évite le mur en B2, trouve le trésor en C4 »*).
  * Chaque case dispose d'une mire centrale pour positionner les véhicules.
* **Boussole Spatiale Relative (en haut à droite) :**
  * Rappelle les couleurs des commandes du robot : 🟢 AVANT (Vert), 🟦 GAUCHE 90° (Bleu), 🟧 DROITE 90° (Orange), 🟡 RECUL (Jaune/Orange).

### Planche 2 : La Mascotte mBot2 Papercraft 3D & Pions
* **La Petite Voiture mBot2 en 3D :**
  * Patron pliable avec languettes de collage.
  * **Face avant :** Écran CyberPi avec de grands yeux expressifs et le capteur ultrasons pour repérer immédiatement la direction du regard du robot.
  * **Flancs gauche (Bleu) et droit (Orange) :** Flèches de rotation 90° imprimées sur les côtés pour aider l'enfant à résoudre la décentration spatiale.
* **Pions & Pupitres d'appoint :**
  * 4 mini-cartes / jetons : Départ, Trésor, Murs.
  * 2 chevalets verticaux "Stand-Up" à plier (mBot2 Pilote et Obstacle Mur).
* **Alternative :** Vous pouvez également utiliser n'importe quelle petite voiture d'enfant (*Hot Wheels*, *Majorette*, véhicule *Lego* ou figurine) sur le plateau.

---

## 2. Le Plateau de Jeu au Sol (Pour le vrai mBot2)

### Dimensions & Gabarit
* **Largeur du mBot2 :** ~17 cm (largeur entre les roues).
* **Longueur du mBot2 :** ~18 cm.
* **Taille d'une case au sol :** **25 cm $\times$ 25 cm** (asservissement moteur précis dans le script Python).
* **Format recommandé :** Grille de 3 $\times$ 3 cases (75 cm $\times$ 75 cm) ou 4 $\times$ 4 cases (1 m $\times$ 1 m).

### Options de fabrication simples :
1. **Option A — Ruban de masquage au sol (Le plus rapide & zéro coût) :**
   * Tracer les lignes d'une grille de 25 cm au sol avec du scotch de peintre (ne laisse aucune trace sur le lino ou le carrelage).
2. **Option B — Dalles mousse emboîtables :**
   * Dalles puzzle d'éveil (souvent 30x30 cm). Très silencieuses et offrant une excellente motricité aux pneus en caoutchouc du mBot2.
3. **Option C — Nappe en toile cirée ou bâche plastique quadrillée :**
   * Toile cirée blanche de 1 m $\times$ 1 m quadrillée au marqueur indélébile. Elle se roule en 5 secondes après la séance.

---

## 3. Les Murs & Tunnels (En relief 3D)

* **Hauteur recommandée :** Entre **8 cm et 12 cm** de haut (hauteur idéale pour le capteur ultrasons du mBot2).
* **Matériaux recommandés :**
  * **Briques LEGO / DUPLO :** Fixables ou posables, parfaitement modulables.
  * **Planchettes en bois (Kapla) :** Permettent de concevoir des labyrinthes géants en quelques minutes.
  * **Cartons de récupération pliés en U ou boîtes à chaussures ouvertes** pour former des tunnels.

---

## 4. Les Cartes de Programmation (60 mm $\times$ 60 mm)

Disponibles dans [`cartes_a_imprimer.html`](file:///c:/Users/admin/Documents/AI_assisted/agentic-ai/2_livrables/pedagogie/cours/Robotique_mBot2_Code_and_Go/cartes_a_imprimer.html) :

| Symbole | Couleur | Nom de la carte | Type | Action / Rôle |
| :---: | :---: | :---: | :---: | :--- |
| **⬆️** | **Vert** | **Avancer** | Commande | Avance de +25 cm en ligne droite |
| **⬇️** | **Orange** | **Reculer** | Commande | Recule de -25 cm en marche arrière |
| **↶** | **Bleu** | **Tourner à Gauche** | Commande | Pivot de 90° à gauche sur place |
| **↷** | **Orange vif** | **Tourner à Droite** | Commande | Pivot de 90° à droite sur place |
| **⭐** | **Violet** | **Action Magique** | Commande | Danse et son festive (somme des angles = 0°) |
| **🏁** | **Turquoise** | **Départ** | Terrain | Case de départ du mBot2 |
| **🧀** | **Jaune d'or** | **Trésor** | Terrain | Case cible d'arrivée |
| **🧱** | **Rouge** | **Mur / Obstacle** | Terrain | Case interdite à contourner |
