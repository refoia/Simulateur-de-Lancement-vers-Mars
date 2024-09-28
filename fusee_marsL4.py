import math
import random
import time

# Constantes
G = 6.67430e-11
M_terre = 5.97e24
R_terre = 6.371e6
M_fusee = 1e6
dist_terre_mars = 225e9

def calculer_vitesse_echappement():
    return math.sqrt(2 * G * M_terre / R_terre)

def calculer_energie_cinetique(masse, vitesse):
    return 0.5 * masse * vitesse**2

def calculer_delta_v_hohmann():
    r1 = R_terre + 200000
    r2 = dist_terre_mars
    mu = G * M_terre
    return math.sqrt(mu/r1) * (math.sqrt(2*r2/(r1+r2)) - 1) + \
           math.sqrt(mu/r2) * (1 - math.sqrt(2*r1/(r1+r2)))

def calculer_temps_voyage():
    return math.pi * math.sqrt((dist_terre_mars**3) / (8 * G * M_terre))

def generer_incident():
    incidents = [
        {
            "description": "Légère fluctuation dans les moteurs",
            "impact": "Les moteurs connaissent une légère perte de puissance, ce qui peut affecter la vitesse et la trajectoire."
        },
        {
            "description": "Petite variation de trajectoire détectée",
            "impact": "La trajectoire de la fusée dévie légèrement de sa route prévue, nécessitant des corrections de navigation."
        },
        {
            "description": "Pic de température dans le système de refroidissement",
            "impact": "Un pic de température est détecté, ce qui pourrait endommager les composants critiques si non résolu rapidement."
        },
        {
            "description": "Brève perturbation dans les communications",
            "impact": "Les communications avec le centre de contrôle sont momentanément interrompues, entraînant une perte de télémétrie."
        },
        {
            "description": "Microfissure détectée dans un réservoir secondaire",
            "impact": "Une microfissure est détectée, ce qui pourrait entraîner une fuite de carburant si non réparée."
        },
        {
            "description": "Dysfonctionnement mineur dans le système de navigation",
            "impact": "Le système de navigation montre des anomalies, nécessitant une recalibration pour maintenir la trajectoire."
        },
        {
            "description": "Défaillance partielle des panneaux solaires",
            "impact": "Un des panneaux solaires ne fonctionne pas correctement, réduisant l'efficacité de la production d'énergie."
        },
        {
            "description": "Problème dans le système de recyclage de l'air",
            "impact": "Le système de recyclage de l'air rencontre des difficultés, ce qui pourrait affecter la qualité de l'air à bord."
        },
        {
            "description": "Dysfonctionnement du système de contrôle thermique",
            "impact": "Le système de contrôle thermique ne régule pas correctement la température interne, risquant une surchauffe des équipements."
        },
        {
            "description": "Interférence électromagnétique",
            "impact": "Une interférence électromagnétique affecte les systèmes électroniques, causant des erreurs de communication et de navigation."
        },
        {
            "description": "Impact de météorite détecté",
            "impact": "Un impact de météorite a été détecté, entraînant une déviation de la trajectoire et une possible perte de vitesse."
        }
    ]
    incident = random.choice(incidents)
    return f"{incident['description']} - Impact: {incident['impact']}"

def generer_solution(incident):
    solutions = {
        "Légère fluctuation dans les moteurs": [
            "Ajustement automatique de la poussée",
            "Recalibrage des injecteurs de carburant",
            "Inspection et ajustement des moteurs en vol"
        ],
        "Petite variation de trajectoire détectée": [
            "Correction de trajectoire par les propulseurs secondaires",
            "Mise à jour des paramètres de navigation",
            "Utilisation des étoiles pour recalibrer la trajectoire"
        ],
        "Pic de température dans le système de refroidissement": [
            "Augmentation temporaire du débit du liquide de refroidissement",
            "Réduction momentanée de la puissance des moteurs",
            "Activation du système de refroidissement d'urgence"
        ],
        "Brève perturbation dans les communications": [
            "Basculement sur l'antenne de secours",
            "Réinitialisation du système de communication",
            "Utilisation du mode de communication redondant"
        ],
        "Microfissure détectée dans un réservoir secondaire": [
            "Application automatique d'un agent d'étanchéité",
            "Isolation du réservoir concerné et redistribution du carburant",
            "Activation du système de protection des réservoirs"
        ],
        "Dysfonctionnement mineur dans le système de navigation": [
            "Passage au système de navigation redondant",
            "Recalibrage des gyroscopes",
            "Utilisation du système de navigation inertielle"
        ],
        "Défaillance partielle des panneaux solaires": [
            "Réorientation des panneaux fonctionnels pour maximiser l'exposition",
            "Réparation en vol des panneaux endommagés",
            "Activation des batteries de secours"
        ],
        "Problème dans le système de recyclage de l'air": [
            "Passage au système de filtration secondaire",
            "Réparation du système principal en vol",
            "Activation des réserves d'air"
        ],
        "Dysfonctionnement du système de contrôle thermique": [
            "Activation du système de contrôle thermique secondaire",
            "Réparation des composants défaillants",
            "Réduction de la charge thermique en diminuant la puissance des systèmes non essentiels"
        ],
        "Interférence électromagnétique": [
            "Passage aux fréquences de communication de secours",
            "Utilisation des boucliers anti-interférence",
            "Augmentation de la puissance du signal"
        ],
        "Impact de météorite détecté": [
            "Correction de trajectoire par les propulseurs principaux",
            "Réparation des dommages structurels en vol",
            "Redistribution du carburant pour compenser la perte de masse"
        ]
    }
    return random.choice(solutions[incident])

# Fonctions supplémentaires pour simuler les perturbations des trajectoires

def calculer_perturbation_meteorite():
    # Générer une perturbation aléatoire en termes de vitesse et de direction
    changement_vitesse = random.uniform(-50, 50)  # en m/s
    angle_perturbation = random.uniform(0, 360)  # en degrés
    return changement_vitesse, angle_perturbation

def appliquer_perturbation(vitesse, angle, changement_vitesse, angle_perturbation):
    # Convertir les angles en radians
    angle_rad = math.radians(angle)
    angle_perturbation_rad = math.radians(angle_perturbation)
    
    # Calculer les nouvelles composantes de la vitesse
    vitesse_x = vitesse * math.cos(angle_rad) + changement_vitesse * math.cos(angle_perturbation_rad)
    vitesse_y = vitesse * math.sin(angle_rad) + changement_vitesse * math.sin(angle_perturbation_rad)
    
    # Calculer la nouvelle vitesse et son angle
    nouvelle_vitesse = math.sqrt(vitesse_x**2 + vitesse_y**2)
    nouvel_angle = math.degrees(math.atan2(vitesse_y, vitesse_x))
    
    return nouvelle_vitesse, nouvel_angle

def simuler_lancement():
    v_echappement = calculer_vitesse_echappement()
    e_cinetique = calculer_energie_cinetique(M_fusee, v_echappement)
    delta_v = calculer_delta_v_hohmann()
    temps_voyage = calculer_temps_voyage()

    print(f"Vitesse d'échappement: {v_echappement:.2f} m/s")
    print(f"Énergie cinétique nécessaire: {e_cinetique:.2e} J")
    print(f"Delta-v pour le transfert vers Mars: {delta_v:.2f} m/s")
    print(f"Temps de voyage estimé: {temps_voyage/86400:.2f} jours")

    isp = 300
    m_prop = M_fusee * (1 - math.exp(-delta_v / (isp * 9.81)))
    print(f"Masse de propergol estimée: {m_prop:.2e} kg")

    print("\nDébut de la simulation de lancement (5 minutes):")
    start_time = time.time()
    elapsed_time = 0
    altitude = 0
    vitesse = 0
    angle = 90  # angle initial de la trajectoire en degrés

    while elapsed_time < 300:
        time.sleep(0.1)  # Pause de 0.1 seconde pour une simulation plus rapide
        elapsed_time = time.time() - start_time
        altitude += vitesse * 0.1
        vitesse += (v_echappement / 300) * 0.1

        if random.random() < 0.05:  # 5% de chance d'incident par 0.1 seconde
            incident = generer_incident()
            print(f"T+{elapsed_time:.1f}s - INCIDENT: {incident}")
            
            time.sleep(0.5)  # Pause pour simuler le temps de réaction
            
            solution = generer_solution(incident)
            print(f"T+{elapsed_time:.1f}s - SOLUTION: {solution}")

            if "Impact de météorite" in incident:
                # Calculer et appliquer la perturbation
                changement_vitesse, angle_perturbation = calculer_perturbation_meteorite()
                vitesse, angle = appliquer_perturbation(vitesse, angle, changement_vitesse, angle_perturbation)
                print(f"T+{elapsed_time:.1f}s - Vitesse après perturbation: {vitesse:.2f} m/s, Angle: {angle:.2f}°")

        if int(elapsed_time) % 10 == 0 and elapsed_time % 1 < 0.1:
            print(f"T+{elapsed_time:.0f}s - Altitude: {altitude/1000:.2f} km, Vitesse: {vitesse:.2f} m/s")

    print("\nFin de la simulation de lancement")
    print(f"Altitude finale: {altitude/1000:.2f} km")
    print(f"Vitesse finale: {vitesse:.2f} m/s")

if __name__ == "__main__":
    simuler_lancement()
