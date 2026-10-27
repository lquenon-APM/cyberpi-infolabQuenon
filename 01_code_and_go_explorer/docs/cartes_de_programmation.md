# 🎴 Guide & Fiche Pédagogique : Les Cartes de Programmation & Le Tapis

Ce document accompagne les fichiers interactifs [`cartes_a_imprimer.html`](file:///c:/Users/admin/Documents/AI_assisted/agentic-ai/2_livrables/pedagogie/cours/Robotique_mBot2_Code_and_Go/cartes_a_imprimer.html) et [`plateau_simulation_a4.html`](file:///c:/Users/admin/Documents/AI_assisted/agentic-ai/2_livrables/pedagogie/cours/Robotique_mBot2_Code_and_Go/plateau_simulation_a4.html). Il détaille la préparation matérielle et les démarches didactiques pour animer les ateliers avec votre fils ou vos élèves.

---

## 1. Comment imprimer et préparer le kit de cartes ?

1. **Ouvrez le fichier :** Double-cliquez sur [`cartes_a_imprimer.html`](file:///c:/Users/admin/Documents/AI_assisted/agentic-ai/2_livrables/pedagogie/cours/Robotique_mBot2_Code_and_Go/cartes_a_imprimer.html) dans votre navigateur (Chrome, Edge, Firefox).
2. **Lancez l'impression :**
   * Cliquez sur **🖨️ Imprimer les 4 Pages A4** ou faites **Ctrl + P**.
   * **Paramètres d'impression :**
     * Format : **A4 Portrait**
     * Marges : **Aucune / Zéro** (la mise en page gère nativement des marges de sécurité anti-débordement)
     * Option obligatoire : Cochez **"Graphiques d'arrière-plan"** (*Background graphics*) pour conserver les dégradés et couleurs vives.
   * **Zéro gaspillage :** Le fichier est calibré pour sortir **exactement 4 feuilles A4**, sans aucune page blanche intermédiaire ni titre résiduel sur les zones de coupe.
3. **Support conseillé :**
   * Papier épais (160 g ou bristol blanc).
   * Si vous disposez d'une plastifieuse, plastifiez les planches avant découpe : les cartes seront indéchirables et résisteront aux manipulations répétées au sol.
4. **Découpage express :**
   * Grâce à l'alignement en grille 3 $\times$ 4 avec traits de coupe pointillés, 5 coups de massicot suffisent par feuille pour extraire 12 cartes carrées de **60 mm $\times$ 60 mm**.

---

## 2. Inventaire Complet du Kit (36 Cartes + 1 Tapis)

Le kit est structuré en deux grandes familles distinctes pour éviter toute confusion didactique :

### A. Les Cartes de Commande (Pour la Réglette / CyberPi) — 26 Cartes
Ces cartes composent l'algorithme sur le tapis de programmation avant encodage sur le joystick de la CyberPi :
* 🟢 **10 Cartes "Avancer" (Mouvement 1 pas - Joystick Haut) :** Déplacement asservi de +25 cm en ligne droite.
* 🟠 **4 Cartes "Reculer" (Mouvement 1 pas - Joystick Bas) :** Déplacement asservi de -25 cm en marche arrière.
* 🟦 **5 Cartes "Tourner à Gauche" (Rotation 90° - Joystick Gauche) :** Pivot sur place de 90° à gauche (sans translation).
* 🟥 **5 Cartes "Tourner à Droite" (Rotation 90° - Joystick Droite) :** Pivot sur place de 90° à droite (sans translation).
* 🟪 **2 Cartes "Action Magique" (Action Magique - Clic Joystick) :** Animation festive (LEDs arc-en-ciel + musique enjouée + frétillement gauche-droite). *Particularité didactique : la somme nette des rotations est strictement égale à 0°, garantissant que le robot conserve son alignement sur la grille !*

### B. Les Cartes de Plateau / Terrain (Pour le Sol & la Table) — 10 Cartes
Ces cartes ne s'encodent pas dans le robot : elles servent à construire le circuit et le labyrinthe :
* 🏁 **2 Cartes "Départ" (Vert d'eau / Damier) :** Balise la case de départ du mBot2.
* 🧀 **2 Cartes "Trésor" (Fromage doré souriant) :** Marque la case cible à atteindre pour remporter le défi.
* 🧱 **6 Cartes "Obstacle / Mur" (Briques Lego rouges) :** Posées sur les cases interdites pour forcer le contournement et interdire les raccourcis.

### C. La Planche 4 : Le Tapis de Programmation 3×3 (1 Planche A4)
* Dispose de **8 cases d'encodage (1er à 8e pas)** au format réel 60 mm $\times$ 60 mm reliées par des flèches directionnelles, plus une **case finale verte GO (Bouton A)**.
* L'enfant pose directement ses cartes découpées sur les cases du tapis pour matérialiser sa séquence avant de toucher la CyberPi.

---

## 3. Clés Didactiques & Démarche en 3 Temps

À cet âge (6-8 ans, 1re-2e primaire / CP-CE1), la pensée abstraite est en pleine construction. L'apprentissage de la programmation doit impérativement s'appuyer sur la manipulation concrète.

### 🔄 La progression en 3 temps (De la table au sol) :

1. **Temps 1 — Simulation sur table ([`plateau_simulation_a4.html`](file:///c:/Users/admin/Documents/AI_assisted/agentic-ai/2_livrables/pedagogie/cours/Robotique_mBot2_Code_and_Go/plateau_simulation_a4.html)) :**
   * L'enfant utilise le plateau quadrillé A4 (grille 4$\times$3) et déplace manuellement sa petite voiture (*Hot Wheels*, *Lego* ou notre mascotte mBot2 papercraft 3D).
   * Il éprouve physiquement les virages : en tournant la voiturette, il voit vers où pointent les yeux du robot.
2. **Temps 2 — Encodage sur le Tapis de programmation :**
   * À chaque déplacement de la voiturette sur la table, il dépose la carte correspondante sur le Tapis (Slot 1 : *Avancer*, Slot 2 : *Tourner Droite*, etc.).
   * Il relit sa ligne de cartes du doigt de gauche à droite.
3. **Temps 3 — Encodage sur la CyberPi & Défi au sol :**
   * L'enfant prend le robot mBot2, suit sa ligne de cartes des yeux et pousse le joystick de la CyberPi.
   * Il pose le robot sur la case départ du quadrillage au sol (dalles de 25 cm) et appuie sur **A (GO)**.
   * Si le robot atteint le trésor : victoire ! S'il touche un mur : détection d'erreur, analyse de la carte fautive, effacement avec le bouton **B** et nouvel essai.

### 🧠 Astuce anti-piège : L'orientation de la carte
Chaque carte de commande comporte en bas une étiquette noire symbolisant la manette CyberPi (ex. : `🕹️ Joystick Haut`).
> **La règle d'or pour l'enfant :** *« L'étiquette manette noire doit toujours être vers le bas, dirigée vers tes genoux ! »* Cela empêche de transformer accidentellement un ordre *Reculer* en *Avancer* ou d'intervertir *Gauche* et *Droite*.
