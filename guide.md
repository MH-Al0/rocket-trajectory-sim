# Rocket Trajectory Simulator - Guide rapide

## 1️ Cloner le projet

git clone https://github.com/MH-Al0/rocket-trajectory-sim.git
cd rocket-trajectory-sim

## 2️ Créer et activer un environnement virtuel

### Linux / Mac
python -m venv venv

source venv/bin/activate

### Windows (cmd)
python -m venv venv

venv\Scripts\activate

## 3️ Installer les dépendances

pip install -r requirements.txt

## 4️ Lancer la simulation

#### Tracer la trajectoire :

python sim.py --plot

#### Opt.1 - Sauvegarder les résultats dans un CSV :
python sim.py --output result.csv

#### Opt.2 - Modifier l'angle de lancement :

python sim.py --angle 45 --plot

## 5️ Expérimentations possibles

Modifier la poussée, la masse, le coefficient de traînée ou l'angle dans sim.py.

Essayer différents profils de poussée (constant_thrust, linear_burn) depuis utils.py.

Observer comment la trajectoire change selon les paramètres.
