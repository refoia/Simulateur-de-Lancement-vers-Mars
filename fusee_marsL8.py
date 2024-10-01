import math
import random
import time

# Constantes
G = 6.67430e-11
M_terre = 5.97e24
R_terre = 6.371e6
dist_terre_mars = 225e9

# Masse des structures de la fusée (par exemple, 200 000 kg)
M_structures = 2e5

# Masse de carburant variable entre 800 000 kg et 1 000 000 kg
M_carburant_initial = random.uniform(8e5, 1e6)

# Masse totale initiale de la fusée
M_fusee_initial = M_structures + M_carburant_initial

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

import random

def generer_solution(incident):
    solutions = {
        "Légère fluctuation dans les moteurs": [
            "Ajustement automatique de la poussée",
            "Recalibrage des injecteurs de carburant",
            "Activation du système de compensation des vibrations",
            "Vérification des paramètres de combustion",
            "Analyse des données de télémétrie pour identifier la cause",
            "Inspection visuelle des moteurs",
            "Réduction temporaire de la charge de travail des moteurs",
            "Vérification des systèmes de lubrification",
            "Analyse des données de vibration",
            "Consultation avec les experts en propulsion"
        ],
        "Petite variation de trajectoire détectée": [
            "Correction de trajectoire par les propulseurs secondaires",
            "Mise à jour des paramètres de navigation",
            "Réalignement des gyroscopes de précision",
            "Recalcul des vecteurs de poussée",
            "Vérification des capteurs de position",
            "Utilisation des données GPS pour recalibrer la trajectoire",
            "Analyse des données de vent solaire",
            "Vérification des systèmes de guidage inertiel",
            "Consultation avec les experts en navigation",
            "Activation des systèmes de navigation de secours"
        ],
        "Pic de température dans le système de refroidissement": [
            "Augmentation temporaire du débit du liquide de refroidissement",
            "Réduction momentanée de la puissance des moteurs",
            "Activation des systèmes de refroidissement auxiliaires",
            "Surveillance continue des températures critiques",
            "Diagnostic des composants du système de refroidissement",
            "Inspection des conduits de refroidissement",
            "Vérification des pompes de refroidissement",
            "Analyse des données de température historiques",
            "Consultation avec les experts en thermodynamique",
            "Activation des systèmes de refroidissement d'urgence"
        ],
        "Brève perturbation dans les communications": [
            "Basculement sur l'antenne de secours",
            "Réinitialisation du système de communication",
            "Amplification du signal par relais satellite",
            "Vérification des antennes principales",
            "Analyse des interférences potentielles",
            "Inspection des câbles de communication",
            "Vérification des systèmes de transmission",
            "Analyse des données de communication historiques",
            "Consultation avec les experts en télécommunications",
            "Activation des systèmes de communication de secours"
        ],
        "Microfissure détectée dans un réservoir secondaire": [
            "Application automatique d'un agent d'étanchéité",
            "Isolation du réservoir concerné et redistribution du carburant",
            "Activation du système de pressurisation de secours",
            "Inspection visuelle des réservoirs",
            "Surveillance des niveaux de carburant",
            "Vérification des systèmes de pressurisation",
            "Analyse des données de pression historiques",
            "Consultation avec les experts en ingénierie des matériaux",
            "Activation des systèmes de surveillance des réservoirs",
            "Réparation temporaire des fissures"
        ],
        "Dysfonctionnement mineur dans le système de navigation": [
            "Passage au système de navigation redondant",
            "Recalibrage des gyroscopes",
            "Initialisation du système de navigation stellaire",
            "Vérification des capteurs de position",
            "Analyse des données de navigation",
            "Inspection des systèmes de navigation",
            "Vérification des systèmes de guidage inertiel",
            "Analyse des données de navigation historiques",
            "Consultation avec les experts en navigation",
            "Activation des systèmes de navigation de secours"
        ],
        "Défaillance partielle des panneaux solaires": [
            "Réorientation des panneaux pour maximiser l'exposition",
            "Activation des panneaux solaires de secours",
            "Réduction de la consommation d'énergie non essentielle",
            "Diagnostic des panneaux défectueux",
            "Surveillance de la production d'énergie",
            "Inspection des systèmes de conversion d'énergie",
            "Vérification des systèmes de stockage d'énergie",
            "Analyse des données de production d'énergie historiques",
            "Consultation avec les experts en énergie solaire",
            "Activation des systèmes de production d'énergie de secours"
        ],
        "Problème dans le système de recyclage de l'air": [
            "Activation des filtres de secours",
            "Augmentation de la ventilation",
            "Réparation des composants défectueux",
            "Surveillance de la qualité de l'air",
            "Analyse des données de recyclage de l'air",
            "Inspection des systèmes de filtration",
            "Vérification des systèmes de ventilation",
            "Analyse des données de qualité de l'air historiques",
            "Consultation avec les experts en systèmes de support de vie",
            "Activation des systèmes de recyclage de l'air de secours"
        ],
        "Dysfonctionnement du système de contrôle thermique": [
            "Augmentation de la ventilation pour dissiper la chaleur",
            "Activation du système de refroidissement d'urgence",
            "Réparation des composants défectueux",
            "Surveillance des températures critiques",
            "Diagnostic des composants du système de contrôle thermique",
            "Inspection des systèmes de refroidissement",
            "Vérification des systèmes de chauffage",
            "Analyse des données de température historiques",
            "Consultation avec les experts en thermodynamique",
            "Activation des systèmes de contrôle thermique de secours"
        ],
        "Interférence électromagnétique": [
            "Recalibration des instruments affectés",
            "Activation des systèmes de secours",
            "Détection et isolation de la source d'interférence",
            "Analyse des données de communication",
            "Surveillance des systèmes électroniques",
            "Inspection des systèmes de communication",
            "Vérification des systèmes de transmission",
            "Analyse des données de communication historiques",
            "Consultation avec les experts en télécommunications",
            "Activation des systèmes de communication de secours"
        ]
    }
    return random.choice(solutions.get(incident, ["Analyse de la situation en cours", "Consultation immédiate avec le contrôle au sol", "Activation des protocoles d'urgence généraux"]))

def envoyer_message_terre(message):
    print(f"Envoi du message : {message}")
    return f"Message envoyé à la Terre: {message}"

def recevoir_message_terre():
    message = "Confirmation de la réussite du lancement."
    print(f"Réception du message de la Terre : {message}")
    return f"Message reçu de la Terre: {message}"

def envoyer_message_fusee(message):
    print(f"Envoi du message : {message}")
    return f"Message envoyé à la fusée: {message}"

def recevoir_message_fusee():
    message = "Tous les systèmes sont nominal."
    print(f"Réception du message de la fusée : {message}")
    return f"Message reçu de la fusée: {message}"

def simuler_delai_communication(distance):
    c = 299792458  # Vitesse de la lumière en m/s
    return distance / c

def analyser_resultats(experience):
    print(f"Analyse des résultats de l'expérience {experience['nom']}.")
    # Ajoutez ici la logique d'analyse des résultats

def gerer_difficultes(equipage, evenement, vaisseau, niveau_bouclier):
    if evenement == "micro_astéroïde":
        print("Collision avec un micro astéroïde détectée!")
        dommage = 10
        vaisseau["integrité"] -= dommage
        print(f"Le vaisseau a subi {dommage} points de dommages. Intégrité actuelle : {vaisseau['integrité']}")
        if vaisseau["integrité"] <= 50:
            print("Alerte : Le vaisseau est en mauvais état. Réparations nécessaires!")
            for membre in equipage:
                reparation = 5
                vaisseau["integrité"] += reparation
                print(f"{membre} répare le vaisseau. Intégrité restaurée de {reparation} points.")

    elif evenement == "tempête_solaire":
        print("Tempête solaire imminente!")
        reduction_bouclier = 20
        niveau_bouclier -= reduction_bouclier
        print(f"Les boucliers du vaisseau ont diminué de {reduction_bouclier} points. Niveau actuel des boucliers : {niveau_bouclier}")
        if niveau_bouclier <= 0:
            print("Protection des radiations endommagée.")

def gestion_experiences(equipage, jour, experiences):
    print(f"Jour {jour}: Début des expériences scientifiques.")
    for membre in equipage:
        experience = random.choice(experiences)
        print(f"{membre} participe à l'expérience : {experience['nom']}.")
        progression = random.randint(10, 30)
        experience['progression'] += progression
        if experience['progression'] >= 100:
            experience['progression'] = 100
            print(f"L'expérience {experience['nom']} est terminée!")
            analyser_resultats(experience)
        else:
            print(f"L'expérience {experience['nom']} progresse à {experience['progression']}%.")

def gestion_plantation(vegetaux, jours):
    print(f"Jour {jours}: Surveillance de l'évolution des plantes.")
    for plante in vegetaux:
        print(f"Plante {plante['nom']} :")
        croissance = random.uniform(0.1, 0.5)
        plante['taille'] += croissance
        print(f" - Croissance de {croissance:.2f} cm. Taille actuelle : {plante['taille']:.2f} cm.")
        plante['eau_besoin'] -= 1
        if plante['eau_besoin'] <= 0:
            print(f" - La plante a besoin d'eau!")
            reapprovisionnement_eau = random.randint(1, 5)
            plante['eau_besoin'] = reapprovisionnement_eau
            print(f" - La plante a reçu {reapprovisionnement_eau} unités d'eau.")
        plante['lumiere_besoin'] -= 1
        if plante['lumiere_besoin'] <= 0:
            print(f" - La plante a besoin de lumière!")
            reapprovisionnement_lumiere = random.randint(2, 6)
            plante['lumiere_besoin'] = reapprovisionnement_lumiere
            print(f" - La plante a été exposée à la lumière pendant {reapprovisionnement_lumiere} heures.")
        if plante['taille'] >= plante['taille_max']:
            print(f" - La plante {plante['nom']} est prête pour la récolte!")


def simuler_lancement():
    M_fusee = M_fusee_initial
    v_echappement = calculer_vitesse_echappement()
    e_cinetique = calculer_energie_cinetique(M_fusee, v_echappement)
    delta_v = calculer_delta_v_hohmann()
    temps_voyage = calculer_temps_voyage()

    print(f"Masse initiale de la fusée: {M_fusee_initial:.2e} kg")
    print(f"Masse initiale de carburant: {M_carburant_initial:.2e} kg")
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
    carburant = M_carburant_initial
    poussée = 1.5 * M_fusee_initial * 9.81

    while elapsed_time < 300:
        time.sleep(0.1)
        elapsed_time = time.time() - start_time
        altitude += vitesse * 0.1
        acceleration = (poussée - (M_fusee * 9.81)) / M_fusee
        vitesse += acceleration * 0.1
        masse_consomme = poussée * 0.1 / (isp * 9.81)
        carburant -= masse_consomme
        M_fusee -= masse_consomme

        if random.random() < 0.05:
            incident_description = generer_incident()
            print(f"T+{elapsed_time:.1f}s - INCIDENT: {incident_description}")
            time.sleep(0.5)
            solution = generer_solution(incident_description)
            print(f"T+{elapsed_time:.1f}s - SOLUTION: {solution}")

        if int(elapsed_time) % 10 == 0 and elapsed_time % 1 < 0.1:
            print(f"T+{elapsed_time:.0f}s - Altitude: {altitude/1000:.2f} km, Vitesse: {vitesse:.2f} m/s, Carburant: {carburant:.2e} kg")

        if carburant <= 0 or M_fusee <= M_structures:
            print("Carburant épuisé ! La mission a échoué.")
            break

    if carburant > 0 and M_fusee > M_structures:
        print("\nFin de la simulation de lancement")
        print(f"Altitude finale: {altitude/1000:.2f} km")
        print(f"Vitesse finale: {vitesse:.2f} m/s")
        print(f"Carburant restant: {carburant:.2e} kg")
        # ... [Le reste de la fonction continue normalement] ...


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


if __name__ == "__main__":
    simuler_lancement()
