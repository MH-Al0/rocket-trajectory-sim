# rocket.py
from typing import Callable

G0 = 9.8  # gravité standard (m/s)

# Classe qui déf la poussée en fonction du temps
class ThrustProfile:
    def __init__(self, func: Callable[[float], float]):
        # func : fonction t -> poussée (N)
        self.func = func

    def thrust(self, t: float) -> float:
        # Retourne thrust à l'inst t
        return float(self.func(t))


# Classe qui rep la fusée
class Rocket:
    def __init__(self, dry_mass: float, prop_mass: float, area: float, cd: float, isp: float, thrust_profile: ThrustProfile):
        self.dry_mass = dry_mass      # masse à vide (kg)
        self.prop_mass = prop_mass    # masse carburant (kg)
        self.area = area              # surface projetée (m²)
        self.cd = cd                  # coef de traînée
        self.isp = isp                # impulsion spécifique (s)
        self.thrust_profile = thrust_profile

    @property
    def initial_mass(self) -> float:
        # Masse tot au départ
        return self.dry_mass + self.prop_mass

    def mass_at(self, prop_remaining: float) -> float:
        # Masse tot  à un instant donné en fonc du carb 
        return self.dry_mass + max(0.0, prop_remaining)

    def mass_flow_rate(self, thrust: float) -> float:
        # Déb massique corresp à une poussée et un Isp
        # mdot = T / (g0 * Isp)
        if self.isp <= 0:
            return 0.0
        return thrust / (G0 * self.isp)
