import math

# Constantes
G = 6.67430e-11  # Constante gravitationnelle (m^3 kg^-1 s^-2)
M_terre = 5.97e24  # Masse de la Terre (kg)
R_terre = 6.371e6  # Rayon de la Terre (m)
M_fusee = 1e6  # Masse de la fusée (kg)
dist_terre_mars = 225e9  # Distance moyenne Terre-Mars (m)

def calculer_vitesse_echappement():
    return math.sqrt(2 * G * M_terre / R_terre)

def calculer_energie_cinetique(masse, vitesse):
    return 0.5 * masse * vitesse**2

def calculer_delta_v_hohmann():
    # Calcul simplifié du delta-v pour une orbite de transfert de Hohmann
    r1 = R_terre + 200000  # Orbite basse terrestre (m)
    r2 = dist_terre_mars
    mu = G * M_terre
    return math.sqrt(mu/r1) * (math.sqrt(2*r2/(r1+r2)) - 1) + \
           math.sqrt(mu/r2) * (1 - math.sqrt(2*r1/(r1+r2)))

def calculer_temps_voyage():
    # Temps de voyage pour une orbite de transfert de Hohmann
    return math.pi * math.sqrt((dist_terre_mars**3) / (8 * G * M_terre))

def simuler_lancement():
    v_echappement = calculer_vitesse_echappement()
    e_cinetique = calculer_energie_cinetique(M_fusee, v_echappement)
    delta_v = calculer_delta_v_hohmann()
    temps_voyage = calculer_temps_voyage()

    print(f"Vitesse d'échappement: {v_echappement:.2f} m/s")
    print(f"Énergie cinétique nécessaire: {e_cinetique:.2e} J")
    print(f"Delta-v pour le transfert vers Mars: {delta_v:.2f} m/s")
    print(f"Temps de voyage estimé: {temps_voyage/86400:.2f} jours")

    # Calcul simplifié de la consommation de carburant
    isp = 300  # Impulsion spécifique (s)
    m_prop = M_fusee * (1 - math.exp(-delta_v / (isp * 9.81)))
    print(f"Masse de propergol estimée: {m_prop:.2e} kg")

if __name__ == "__main__":
    simuler_lancement()