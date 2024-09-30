import math
import random
import time
from utilitaires import *

# Constantes
G = 6.67430e-11
M_terre = 5.97e24
R_terre = 6.371e6
M_fusee_initial = 1e6
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
        }
    ]
    incident = random.choice(incidents)
    return f"{incident['description']} - Impact: {incident['impact']}"

def generer_solution(incident):
    solutions = {
        "Légère fluctuation dans les moteurs": [
            "Ajustement automatique de la poussée",
            "Recalibrage des injecteurs de carburant",
            "Activation du système de compensation des vibrations"
        ],
        "Petite variation de trajectoire détectée": [
            "Correction de trajectoire par les propulseurs secondaires",
            "Mise à jour des paramètres de navigation",
            "Réalignement des gyroscopes de précision"
        ],
        "Pic de température dans le système de refroidissement": [
            "Augmentation temporaire du débit du liquide de refroidissement",
            "Réduction momentanée de la puissance des moteurs",
            "Activation des systèmes de refroidissement auxiliaires"
        ],
        "Brève perturbation dans les communications": [
            "Basculement sur l'antenne de secours",
            "Réinitialisation du système de communication",
            "Amplification du signal par relais satellite"
        ],
        "Microfissure détectée dans un réservoir secondaire": [
            "Application automatique d'un agent d'étanchéité",
            "Isolation du réservoir concerné et redistribution du carburant",
            "Activation du système de pressurisation de secours"
        ],
        "Dysfonctionnement mineur dans le système de navigation": [
            "Passage au système de navigation redondant",
            "Recalibrage des gyroscopes",
            "Initialisation du système de navigation stellaire"
        ],
        "Défaillance partielle des panneaux solaires": [
            "Réorientation des panneaux pour maximiser l'exposition",
            "Activation des panneaux solaires de secours",
            "Réduction de la consommation d'énergie non essentielle"
        ],
        "Problème dans le système de recyclage de l'air": [
            "Activation des filtres de secours",
            "Augmentation de la ventilation",
            "Réparation des composants défectueux"
        ],
        "Dysfonctionnement du système de contrôle thermique": [
            "Augmentation de la ventilation pour dissiper la chaleur",
            "Activation du système de refroidissement d'urgence",
            "Réparation des composants défectueux"
        ],
        "Interférence électromagnétique": [
            "Recalibration des instruments affectés",
            "Activation des systèmes de secours",
            "Détection et isolation de la source d'interférence"
        ]
    }
    return random.choice(solutions.get(incident, ["Analyse de la situation en cours", "Consultation immédiate avec le contrôle au sol", "Activation des protocoles d'urgence généraux"]))

def simuler_lancement():
    M_fusee = M_fusee_initial
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
    carburant = M_fusee
    poussée = 1.5 * M_fusee * 9.81

    while elapsed_time < 300:
        time.sleep(0.1)  # Pause de 0.1 seconde pour une simulation plus rapide
        elapsed_time = time.time() - start_time
        altitude += vitesse * 0.1
        acceleration = (poussée - (M_fusee * 9.81)) / M_fusee
        vitesse += acceleration * 0.1
        carburant -= poussée * 0.1 / (isp * 9.81)
        M_fusee -= poussée * 0.1 / (isp * 9.81)

        if random.random() < 0.05:  # 5% de chance d'incident par 0.1 seconde
            incident = generer_incident()
            print(f"T+{elapsed_time:.1f}s - INCIDENT: {incident}")

            time.sleep(0.5)  # Pause pour simuler le temps de réaction

            solution = generer_solution(incident)
            print(f"T+{elapsed_time:.1f}s - SOLUTION: {solution}")

        if int(elapsed_time) % 10 == 0 and elapsed_time % 1 < 0.1:
            print(f"T+{elapsed_time:.0f}s - Altitude: {altitude/1000:.2f} km, Vitesse: {vitesse:.2f} m/s, Carburant: {carburant:.2e} kg")

        if carburant <= 0:
            print("Carburant épuisé ! La mission a échoué.")
            break

    if carburant > 0:
        print("\nFin de la simulation de lancement")
        print(f"Altitude finale: {altitude/1000:.2f} km")
        print(f"Vitesse finale: {vitesse:.2f} m/s")
        print(f"Carburant restant: {carburant:.2e} kg")

        # Simulation de la communication après le lancement
        print(envoyer_message_terre("Lancement réussi, en route vers l'orbite."))
        print(recevoir_message_terre())
        print(envoyer_message_fusee("Navigation stable, tous les systèmes sont nominal."))
        print(recevoir_message_fusee())
        print(f"Temps de communication Terre-Mars : {simuler_delai_communication(dist_terre_mars):.2f} secondes")

def envoyer_message_terre(message):
    return f"Message envoyé à la Terre: {message}"

def recevoir_message_terre():
    return "Message reçu de la Terre: Confirmation de la réussite du lancement."

def envoyer_message_fusee(message):
    return f"Message envoyé à la fusée: {message}"

def recevoir_message_fusee():
    return "Message reçu de la fusée: Tous les systèmes sont nominal."

def simuler_delai_communication(distance):
    c = 299792458  # Vitesse de la lumière en m/s
    return distance / c

if __name__ == "__main__":
    simuler_lancement()
