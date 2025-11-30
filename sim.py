# sim.py
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from rocket import Rocket
from dynamics import simulate
from utils import constant_thrust

# Fonction prim
def main():
    # args en ligne de commande
    parser = argparse.ArgumentParser(description="Simulateur de trajectoire fusée 2D")
    parser.add_argument("--angle", type=float, default=85.0, help="Angle de poussée initial (deg)")
    parser.add_argument("--output", type=str, default=None, help="Fichier CSV de sortie")
    parser.add_argument("--plot", action="store_true", help="Afficher le graphe")
    args = parser.parse_args()

    # Exemple de fusée
    thrust_n = 500000.0  # N
    burn_time = 60.0      # s
    isp = 300.0           # s

    # Profil de poussée const
    thrust_profile = constant_thrust(thrust_n, burn_time)

    # Création de la fusée
    rocket = Rocket(
        dry_mass=10000.0,
        prop_mass=15000.0,
        area=10.0,
        cd=0.5,
        isp=isp,
        thrust_profile=thrust_profile,
    )

    # Conversion ang en rad
    angle_rad = np.deg2rad(args.angle)

    # sim
    t, states = simulate(rocket, angle_rad=angle_rad, max_t=600.0, dt=0.05)

    # svgrd des results ds un DataFrame
    df = pd.DataFrame(states, columns=["x", "y", "vx", "vy", "prop_remaining", "thrust"])
    df.insert(0, "t", t)

    # svgrd CSV si demandé
    if args.output:
        df.to_csv(args.output, index=False)
        print(f"# Résultats sauvegardés dans {args.output}")

    # Affichage graph si demandé
    if args.plot:
        fig, ax = plt.subplots(figsize=(8,6))
        ax.plot(df['x'], df['y'])
        ax.set_xlabel('x (m)')
        ax.set_ylabel('y (m)')
        ax.set_title('Trajectoire fusée')
        ax.grid(True)
        plt.show()

# Point d'entrée
if __name__ == '__main__':
    main()
