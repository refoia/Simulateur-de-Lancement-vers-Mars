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
        }
    ]
    incident = random.choice(incidents)
    return f"{incident['description']} - Impact: {incident['impact']}"

# Exemple d'utilisation
for _ in range(3):
    print(generer_incident())

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
        "Panne d'un moteur principal": [
            "Reconfiguration de la poussée des moteurs restants",
            "Ajustement de la trajectoire pour compenser la perte de poussée",
            "Activation des moteurs de secours"
        ],
        "Défaillance critique du système électrique": [
            "Basculement sur les batteries de secours",
            "Redémarrage séquentiel des systèmes essentiels",
            "Activation du mode de conservation d'énergie d'urgence"
        ],
        "Dépressurisation partielle d'un compartiment": [
            "Isolation immédiate du compartiment affecté",
            "Activation des systèmes de repressurisation d'urgence",
            "Réorientation de l'équipage vers les zones sécurisées"
        ],
        "Dysfonctionnement majeur du système de support de vie": [
            "Passage aux systèmes de support de vie de secours",
            "Activation des purificateurs d'air d'urgence",
            "Mise en place des protocoles de conservation des ressources vitales"
        ],
        "Détection d'un objet spatial sur la trajectoire": [
            "Calcul rapide d'une trajectoire d'évitement",
            "Activation des propulseurs d'urgence pour manœuvre d'évitement",
            "Déploiement du bouclier anti-débris"
        ],
        "Surchauffe critique d'un composant électronique essentiel": [
            "Activation du système de refroidissement cryogénique d'urgence",
            "Basculement sur les systèmes redondants",
            "Isolation thermique immédiate du composant affecté"
        ]
    }
    return random.choice(solutions.get(incident, ["Analyse de la situation en cours", "Consultation immédiate avec le contrôle au sol", "Activation des protocoles d'urgence généraux"]))

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
        
        if int(elapsed_time) % 10 == 0 and elapsed_time % 1 < 0.1:
            print(f"T+{elapsed_time:.0f}s - Altitude: {altitude/1000:.2f} km, Vitesse: {vitesse:.2f} m/s")

    print("\nFin de la simulation de lancement")
    print(f"Altitude finale: {altitude/1000:.2f} km")
    print(f"Vitesse finale: {vitesse:.2f} m/s")

if __name__ == "__main__":
    simuler_lancement()