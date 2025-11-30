# dynamics.py
import numpy as np
from scipy.integrate import solve_ivp

RHO = 1.225  # densité air au niveau de la mer (kg/m^3)
G0 = 9.8 # g tel que (m/s²)

# calc de la force de traînée
def drag_force(rho, cd, area, vx, vy):
    v = np.hypot(vx, vy)  # v totale
    if v == 0:
        return 0.0, 0.0
    f = 0.5 * rho * v * v * cd * area
    # dir opposée a la vitesse
    return -f * (vx / v), -f * (vy / v)

# Sim de la traj
def simulate(rocket, angle_rad: float = 0.0, max_t: float = 300.0, dt: float = 0.1):
    # rocket : instance de Rocket
    # angle_rad : angle initial de poussée (0 = horizontal)
    # max_t : durée max de simulation (s)
    # dt : pas de temps max pour solve_ivp

    # Définition des équations du mouvement
    def rhs(t, y):
        x, z, vx, vz, prop = y
        # poussée instant
        T = rocket.thrust_profile.thrust(t)
        # plus de carb => plus de poussée
        if prop <= 0:
            T = 0.0
            mdot = 0.0
        else:
            mdot = min(rocket.mass_flow_rate(T), prop / 1e-6 if prop>0 else 0.0)

        # comp de la poussée
        Tx = T * np.cos(angle_rad)
        Tz = T * np.sin(angle_rad)

        # traînée
        Dx, Dz = drag_force(RHO, rocket.cd, rocket.area, vx, vz)

        # masse instantanée
        m = rocket.mass_at(prop)

        # accél
        ax = (Tx + Dx) / m
        az = (Tz + Dz) / m - G0

        return [vx, vz, ax, az, -mdot]

    # évènement : impact au sol
    def impact(t, y):
        return y[1]  # on s'arrête quand y=0
    impact.terminal = True
    impact.direction = -1

    # conditions initiales
    x0 = 0.0
    z0 = 0.0
    vx0 = 0.0
    vz0 = 0.0
    prop0 = rocket.prop_mass

    y0 = [x0, z0, vx0, vz0, prop0]

    # intégration
    sol = solve_ivp(rhs, (0.0, max_t), y0, max_step=dt, events=impact, dense_output=True)

    # récup des résultats
    t = sol.t
    states = []
    for ti in t:
        yi = sol.sol(ti)
        x, z, vx, vz, prop = yi
        T = rocket.thrust_profile.thrust(ti) if prop>0 else 0.0
        states.append([x, z, vx, vz, prop, T])

    import numpy as _np
    return _np.array(t), _np.array(states)
