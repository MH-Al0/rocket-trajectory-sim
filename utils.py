# utils.py
import numpy as np
from rocket import ThrustProfile

# Poussée const pendant burn_time s
def constant_thrust(thrust_n: float, burn_time: float) -> ThrustProfile:
    def f(t): 
        return thrust_n if 0.0 <= t <= burn_time else 0.0
    return ThrustProfile(f)

# Poussée qui var linéairement entre thrust0 et thrust_end pendant burn_time
def linear_burn(thrust0: float, thrust_end: float, burn_time: float) -> ThrustProfile:
    def f(t):
        if t < 0 or t > burn_time:
            return 0.0
        return thrust0 + (thrust_end - thrust0) * (t / burn_time)
    return ThrustProfile(f)
