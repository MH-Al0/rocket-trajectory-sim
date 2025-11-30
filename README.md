# Rocket Trajectory Simulator

Simulateur 2D simple de trajectoire de fusée en Python.  
Modélise la fusée avec : gravité, traînée aérodynamique, masse variable et poussée configurable.

## Structure du projet
rocket-trajectory-sim/

### rocket.py  
classes Rocket et ThrustProfile

### dynamics.py 
 équations du mouvement + intégration

### utils.py  
 profils de poussée et helpers
 
### sim.py  
 script principal pour exécuter la simulation


## Installation

```bash
python -m venv venv
source venv/bin/activate      # sur Linux/Mac
# ou venv\Scripts\activate    # sur Windows
pip install -r requirements.txt
