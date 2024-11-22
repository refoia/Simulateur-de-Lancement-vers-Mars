import math
import random
import time
import matplotlib.pyplot as plt
import csv
 

# Constantes existantes
G = 6.67430e-11
M_terre = 5.97e24
R_terre = 6.371e6
M_fusee_initiale = 1e6
M_charge_utile = 2e5
dist_terre_mars = 225e9
isp = 300
debit_massique = 2500

# Nouvelles constantes
M_mars = 6.39e23
R_mars = 3.3895e6
altitude_orbite_terrestre = 400000  # 400 km
altitude_orbite_mars = 300000  # 300 km


 


def phase_atterrissage_mars(masse_initiale, altitude_initiale, vitesse_initiale):
    altitude = altitude_initiale
    vitesse = vitesse_initiale
    masse = masse_initiale
    temps = 0
    dt = 0.1  # Pas de temps en secondes

    while altitude > 0:
        g_mars = G * M_mars / (R_mars + altitude)**2
        poussee = calculer_poussee(isp, debit_massique)
        acceleration = (poussee / masse) - g_mars

        vitesse -= acceleration * dt
        altitude -= vitesse * dt

        masse -= debit_massique * dt
        if masse < M_charge_utile:
            masse = M_charge_utile

        temps += dt

        if random.random() < 0.01:
            incident_info = generer_incident()
            print(f"T+{temps:.1f}s - INCIDENT: {incident_info['description']} - Impact: {incident_info['impact']}")
            solution = generer_solution(incident_info['description'])
            print(f"T+{temps:.1f}s - SOLUTION: {solution}")

        if altitude < 0:
            altitude = 0

        if int(temps) % 10 == 0:
            print(f"T+{temps:.0f}s - Altitude: {altitude:.2f} m, Vitesse: {vitesse:.2f} m/s, Masse: {masse:.2f} kg")

    print("\nAtterrissage réussi sur Mars!")
    print(f"Temps total: {temps:.2f} s")
    print(f"Vitesse finale: {vitesse:.2f} m/s")
    print(f"Masse finale: {masse:.2f} kg")
    return temps, masse

def simuler_delai_communication():
    vitesse_lumiere = 3e8  # m/s
    delai = dist_terre_mars / vitesse_lumiere
    print(f"Temps de communication aller-simple: {delai:.2f} secondes")
    return delai
import json

def enregistrer_rapport(rapport):
    with open('rapport_mission.json', 'w') as fichier:
        json.dump(rapport, fichier, indent=4)

# Exemple de rapport
rapport_mission = {
    "phase": "mise_en_orbite",
    "temps_total": 540.2,
    "vitesse_finale": 7800,
    "masse_finale": 850000
}
enregistrer_rapport(rapport_mission)

from mpl_toolkits.mplot3d import Axes3D

def tracer_trajectoire_3d(positions):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = zip(*positions)
    ax.plot(x, y, z, label="Trajectoire de la mission")
    ax.legend()
    plt.show()


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
    return incident

def generer_solution(incident_description):
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
    return random.choice(solutions.get(incident_description, ["Aucune solution disponible"]))

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

def calculer_poussée(isp, debit_massique):
    # Poussée = Isp * débit_massique * g0
    g0 = 9.81  # Accélération gravitationnelle à la surface de la Terre
    return isp * debit_massique * g0

def calculer_poussee(isp, debit_massique):
    g0 = 9.81
    return isp * debit_massique * g0

# Nouvelles fonctions pour les phases de mission
def phase_mise_en_orbite(altitude_initiale, vitesse_initiale, masse_initiale):
    altitude = altitude_initiale
    vitesse = vitesse_initiale
    masse = masse_initiale
    temps = 0
    dt = 0.1  # Pas de temps en secondes

    while altitude < altitude_orbite_terrestre:
        # Calcul de l'accélération
        r = R_terre + altitude
        g = G * M_terre / r**2
        poussee = calculer_poussee(isp, debit_massique)
        acceleration = (poussee / masse) - g

        # Mise à jour de la vitesse et de l'altitude
        vitesse += acceleration * dt
        altitude += vitesse * dt

        # Mise à jour de la masse
        masse -= debit_massique * dt
        if masse < M_charge_utile:
            masse = M_charge_utile

        temps += dt

        # Gérer les incidents aléatoires
        if random.random() < 0.01:
            incident_info = generer_incident()
            print(f"T+{temps:.1f}s - INCIDENT: {incident_info['description']} - Impact: {incident_info['impact']}")
            solution = generer_solution(incident_info['description'])
            print(f"T+{temps:.1f}s - SOLUTION: {solution}")

        if int(temps) % 10 == 0:
            print(f"T+{temps:.0f}s - Altitude: {altitude/1000:.2f} km, Vitesse: {vitesse:.2f} m/s, Masse: {masse:.2f} kg")

    vitesse_orbitale = math.sqrt(G * M_terre / (R_terre + altitude_orbite_terrestre))
    delta_v = vitesse_orbitale - vitesse
    masse_finale = masse * math.exp(-delta_v / (isp * 9.81))

    print(f"\nMise en orbite terrestre terminée")
    print(f"Temps total: {temps:.2f} s")
    print(f"Vitesse orbitale: {vitesse_orbitale:.2f} m/s")
    print(f"Masse finale: {masse_finale:.2f} kg")

    return temps, altitude_orbite_terrestre, vitesse_orbitale, masse_finale

def phase_transfert_hohmann(masse_initiale):
    delta_v = calculer_delta_v_hohmann()
    temps_transfert = calculer_temps_voyage()
    masse_finale = masse_initiale * math.exp(-delta_v / (isp * 9.81))

    print(f"\nDébut du transfert de Hohmann vers Mars")
    print(f"Delta-v pour le transfert: {delta_v:.2f} m/s")
    print(f"Temps de transfert estimé: {temps_transfert/86400:.2f} jours")
    print(f"Masse au début du transfert: {masse_initiale:.2f} kg")
    print(f"Masse à la fin du transfert: {masse_finale:.2f} kg")

    return temps_transfert, masse_finale

def phase_insertion_orbite_mars(masse_initiale):
    v_arrivee = math.sqrt(G * M_mars / (R_mars + altitude_orbite_mars))
    v_hyperbole = math.sqrt(v_arrivee**2 + 2*G*M_mars/(R_mars + altitude_orbite_mars))
    delta_v = v_hyperbole - v_arrivee
    masse_finale = masse_initiale * math.exp(-delta_v / (isp * 9.81))

    print(f"\nInsertion en orbite martienne")
    print(f"Delta-v pour l'insertion: {delta_v:.2f} m/s")
    print(f"Vitesse orbitale autour de Mars: {v_arrivee:.2f} m/s")
    print(f"Masse finale en orbite martienne: {masse_finale:.2f} kg")

    return delta_v, masse_finale

def simuler_mission_complete():
    print("Début de la simulation de la mission complète vers Mars")

    # Phase de lancement
    altitude_finale_lancement, vitesse_finale_lancement, masse_finale_lancement = simuler_lancement()

    # Phase de mise en orbite terrestre
    temps_mise_en_orbite, altitude_orbite, vitesse_orbitale, masse_orbitale = phase_mise_en_orbite(
        altitude_finale_lancement, vitesse_finale_lancement, masse_finale_lancement)

    # Phase de transfert de Hohmann
    temps_transfert, masse_arrivee_mars = phase_transfert_hohmann(masse_orbitale)

    # Phase d'insertion en orbite martienne
    delta_v_insertion, masse_finale_orbite_mars = phase_insertion_orbite_mars(masse_arrivee_mars)

    print("\nRésumé de la mission:")
    print(f"Masse initiale de la fusée: {M_fusee_initiale:.2f} kg")
    print(f"Masse finale en orbite terrestre: {masse_orbitale:.2f} kg")
    print(f"Masse à l'arrivée à Mars: {masse_arrivee_mars:.2f} kg")
    print(f"Masse finale en orbite martienne: {masse_finale_orbite_mars:.2f} kg")
    print(f"Temps total de la mission: {(temps_mise_en_orbite + temps_transfert)/86400:.2f} jours")

def simuler_lancement():
    v_echappement = calculer_vitesse_echappement()
    e_cinetique = calculer_energie_cinetique(M_fusee_initiale, v_echappement)
    delta_v = calculer_delta_v_hohmann()
    temps_voyage = calculer_temps_voyage()
    
    print(f"Vitesse d'échappement: {v_echappement:.2f} m/s")
    print(f"Énergie cinétique nécessaire: {e_cinetique:.2e} J")
    print(f"Delta-v pour le transfert vers Mars: {delta_v:.2f} m/s")
    print(f"Temps de voyage estimé: {temps_voyage/86400:.2f} jours")
    
    m_prop = M_fusee_initiale * (1 - math.exp(-delta_v / (isp * 9.81)))
    print(f"Masse de propergol estimée: {m_prop:.2e} kg")
    
    print("\nDébut de la simulation de lancement (5 minutes):")
    start_time = time.time()
    elapsed_time = 0
    altitude = 0
    vitesse = 0
    angle = 90  # angle initial de la trajectoire en degrés
    M_fusee = M_fusee_initiale
    poussée = calculer_poussée(isp, debit_massique)
    g0 = 9.81  # Accélération gravitationnelle à la surface de la Terre
    
    # Préparation pour l'affichage graphique
    temps_list = []
    altitude_list = []
    vitesse_list = []
    masse_list = []
    
    # Ouvrir le fichier CSV pour l'enregistrement des données
    with open('donnees_lancement.csv', mode='w', newline='') as fichier_csv:
        writer = csv.writer(fichier_csv)
        writer.writerow(['Temps (s)', 'Altitude (m)', 'Vitesse (m/s)', 'Masse (kg)'])
    
        while elapsed_time < 300 and M_fusee > M_charge_utile:
            time.sleep(0.1)  # Pause de 0.1 seconde pour une simulation plus rapide
            elapsed_time = time.time() - start_time
            # Calcul de l'accélération (a = (poussée - poids) / masse)
            poids = M_fusee * G * M_terre / (R_terre + altitude)**2
            acceleration = (poussée - poids) / M_fusee
            vitesse += acceleration * 0.1
            altitude += vitesse * 0.1
            
            # Consommation de carburant
            M_fusee -= debit_massique * 0.1
            if M_fusee < M_charge_utile:
                M_fusee = M_charge_utile  # La masse ne peut pas être inférieure à la charge utile
            
            # Enregistrement des données
            temps_list.append(elapsed_time)
            altitude_list.append(altitude)
            vitesse_list.append(vitesse)
            masse_list.append(M_fusee)
            writer.writerow([elapsed_time, altitude, vitesse, M_fusee])
    
            if random.random() < 0.01:  # 1% de chance d'incident par 0.1 seconde
                incident_info = generer_incident()
                incident_description = incident_info['description']
                incident_impact = incident_info['impact']
                print(f"T+{elapsed_time:.1f}s - INCIDENT: {incident_description} - Impact: {incident_impact}")
                
                time.sleep(0.5)  # Pause pour simuler le temps de réaction
                
                solution = generer_solution(incident_description)
                print(f"T+{elapsed_time:.1f}s - SOLUTION: {solution}")
    
                if "Impact de météorite" in incident_description:
                    # Calculer et appliquer la perturbation
                    changement_vitesse, angle_perturbation = calculer_perturbation_meteorite()
                    vitesse, angle = appliquer_perturbation(vitesse, angle, changement_vitesse, angle_perturbation)
                    print(f"T+{elapsed_time:.1f}s - Vitesse après perturbation: {vitesse:.2f} m/s, Angle: {angle:.2f}°")
    
            if int(elapsed_time) % 10 == 0 and elapsed_time % 1 < 0.1:
                print(f"T+{elapsed_time:.0f}s - Altitude: {altitude/1000:.2f} km, Vitesse: {vitesse:.2f} m/s, Masse: {M_fusee:.2f} kg")
    
    print("\nFin de la simulation de lancement")
    print(f"Altitude finale: {altitude/1000:.2f} km")
    print(f"Vitesse finale: {vitesse:.2f} m/s")
    print(f"Masse finale de la fusée: {M_fusee:.2f} kg")
    
    # Affichage graphique des résultats
    plt.figure(figsize=(12, 6))
    
    plt.subplot(2, 1, 1)
    plt.plot(temps_list, [a/1000 for a in altitude_list], label='Altitude (km)')
    plt.xlabel('Temps (s)')
    plt.ylabel('Altitude (km)')
    plt.legend()
    
    plt.subplot(2, 1, 2)
    plt.plot(temps_list, vitesse_list, label='Vitesse (m/s)', color='orange')
    plt.xlabel('Temps (s)')
    plt.ylabel('Vitesse (m/s)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    simuler_lancement()
