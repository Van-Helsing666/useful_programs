
import math
import matplotlib.pyplot as plt
from pathlib import Path

# ==========================================
# 1. PARAMETRY FIZYCZNE
# ==========================================

v0 = 20.0          # Predkosc poczatkowa [m/s]
alpha = 45.0       # Kat wyrzutu [stopnie]
g = 9.81           # Przyspieszenie ziemskie [m/s^2]

m = 0.20           # Masa ciala [kg]
rho = 1.225        # Gestosc powietrza [kg/m^3]
Cd = 0.47          # Wspolczynnik oporu
A = 0.01           # Powierzchnia przekroju [m^2]

dt = 0.01          # Krok czasowy [s]

alpha_rad = math.radians(alpha)
k = 0.5 * rho * Cd * A

vx0 = v0 * math.cos(alpha_rad)
vy0 = v0 * math.sin(alpha_rad)

# Folder na wykresy
output_dir = Path("wykresy")
output_dir.mkdir(exist_ok=True)


# ==========================================
# 2. RZUT BEZ OPORU POWIETRZA
# ==========================================

def simulate_without_drag():
    t = 0.0
    x = 0.0
    y = 0.0

    times = []
    xs = []
    ys = []
    vxs = []
    vys = []

    while True:
        times.append(t)
        xs.append(x)
        ys.append(y)
        vxs.append(vx0)
        vys.append(vy0 - g * t)

        next_t = t + dt
        next_y = vy0 * next_t - 0.5 * g * next_t**2

        if next_y <= 0:
            fraction = y / (y - next_y)
            landing_t = t + fraction * dt
            times.append(landing_t)
            xs.append(vx0 * landing_t)
            ys.append(0.0)
            vxs.append(vx0)
            vys.append(vy0 - g * landing_t)
            break

        t = next_t
        x = vx0 * t
        y = next_y

    return times, xs, ys, vxs, vys


# ==========================================
# 3. ROWNANIA ROZNICZKOWE Z OPOREM
# ==========================================

def derivatives(state):
    x, y, vx, vy = state

    speed = math.sqrt(vx**2 + vy**2)

    ax = -(k / m) * speed * vx
    ay = -g - (k / m) * speed * vy

    return [vx, vy, ax, ay]


# ==========================================
# 4. METODA RUNGEGO-KUTTY RK4
# ==========================================

def rk4_step(state, dt):
    k1 = derivatives(state)

    s2 = [
        state[i] + 0.5 * dt * k1[i]
        for i in range(4)
    ]
    k2 = derivatives(s2)

    s3 = [
        state[i] + 0.5 * dt * k2[i]
        for i in range(4)
    ]
    k3 = derivatives(s3)

    s4 = [
        state[i] + dt * k3[i]
        for i in range(4)
    ]
    k4 = derivatives(s4)

    return [
        state[i] + (dt / 6) *
        (k1[i] + 2*k2[i] + 2*k3[i] + k4[i])
        for i in range(4)
    ]


# ==========================================
# 5. SYMULACJA Z OPOREM POWIETRZA
# ==========================================

def simulate_with_drag():
    t = 0.0
    state = [0.0, 0.0, vx0, vy0]

    times = [t]
    xs = [0.0]
    ys = [0.0]
    vxs = [vx0]
    vys = [vy0]

    while True:
        next_state = rk4_step(state, dt)

        if next_state[1] <= 0:
            fraction = state[1] / (
                state[1] - next_state[1]
            )

            landing_state = [
                state[i] + fraction *
                (next_state[i] - state[i])
                for i in range(4)
            ]

            t += fraction * dt

            times.append(t)
            xs.append(landing_state[0])
            ys.append(0.0)
            vxs.append(landing_state[2])
            vys.append(landing_state[3])
            break

        state = next_state
        t += dt

        times.append(t)
        xs.append(state[0])
        ys.append(state[1])
        vxs.append(state[2])
        vys.append(state[3])

    return times, xs, ys, vxs, vys


# ==========================================
# 6. WYKONANIE SYMULACJI
# ==========================================

t1, x1, y1, vx1, vy1 = simulate_without_drag()
t2, x2, y2, vx2, vy2 = simulate_with_drag()


# ==========================================
# 7. WYKRES TORU RUCHU
# ==========================================

plt.figure(figsize=(9, 6))

plt.plot(x1, y1, label="Bez oporu powietrza")
plt.plot(x2, y2, label="Z oporem powietrza")

plt.title("Porownanie torow ruchu")
plt.xlabel("Odleglosc pozioma x [m]")
plt.ylabel("Wysokosc y [m]")
plt.legend()
plt.grid()

plt.savefig(output_dir / "tor_ruchu.png", dpi=300)
plt.close()


# ==========================================
# 8. WYKRES WYSOKOSCI W CZASIE
# ==========================================

plt.figure(figsize=(9, 6))

plt.plot(t1, y1, label="Bez oporu")
plt.plot(t2, y2, label="Z oporem")

plt.title("Wysokosc ciala w czasie")
plt.xlabel("Czas t [s]")
plt.ylabel("Wysokosc y [m]")
plt.legend()
plt.grid()

plt.savefig(output_dir / "wysokosc_czas.png", dpi=300)
plt.close()


# ==========================================
# 9. WYKRES SKLADOWYCH PREDKOSCI
# ==========================================

plt.figure(figsize=(9, 6))

plt.plot(t1, vx1, label="vx bez oporu")
plt.plot(t1, vy1, label="vy bez oporu")

plt.plot(t2, vx2, "--", label="vx z oporem")
plt.plot(t2, vy2, "--", label="vy z oporem")

plt.title("Skladowe predkosci w czasie")
plt.xlabel("Czas t [s]")
plt.ylabel("Predkosc [m/s]")
plt.legend()
plt.grid()

plt.savefig(output_dir / "predkosc_czas.png", dpi=300)
plt.close()


# ==========================================
# 10. WYNIKI SYMULACJI
# ==========================================

print("WYNIKI SYMULACJI")
print("-----------------------------")

print("BEZ OPORU POWIETRZA")
print(f"Czas lotu: {t1[-1]:.2f} s")
print(f"Zasieg: {x1[-1]:.2f} m")
print(f"Maksymalna wysokosc: {max(y1):.2f} m")

print("\nZ OPOREM POWIETRZA")
print(f"Czas lotu: {t2[-1]:.2f} s")
print(f"Zasieg: {x2[-1]:.2f} m")
print(f"Maksymalna wysokosc: {max(y2):.2f} m")

print("\nWykresy zapisano w folderze:", output_dir)
