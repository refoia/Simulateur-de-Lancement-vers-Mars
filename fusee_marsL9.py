import random
import math
import random
import time

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
            "Activation du système de compensation des vibrations",
            "Vérification des paramètres de combustion",
            "Analyse des données de télémétrie pour identifier la cause"
        ],
        "Petite variation de trajectoire détectée": [
            "Correction de trajectoire par les propulseurs secondaires",
            "Mise à jour des paramètres de navigation",
            "Réalignement des gyroscopes de précision",
            "Recalcul des vecteurs de poussée",
            "Vérification des capteurs de position"
        ],
        "Pic de température dans le système de refroidissement": [
            "Augmentation temporaire du débit du liquide de refroidissement",
            "Réduction momentanée de la puissance des moteurs",
            "Activation des systèmes de refroidissement auxiliaires",
            "Surveillance continue des températures critiques",
            "Diagnostic des composants du système de refroidissement"
        ],
        "Brève perturbation dans les communications": [
            "Basculement sur l'antenne de secours",
            "Réinitialisation du système de communication",
            "Amplification du signal par relais satellite",
            "Vérification des antennes principales",
            "Analyse des interférences potentielles"
        ],
        "Microfissure détectée dans un réservoir secondaire": [
            "Application automatique d'un agent d'étanchéité",
            "Isolation du réservoir concerné et redistribution du carburant",
            "Activation du système de pressurisation de secours",
            "Inspection visuelle des réservoirs",
            "Surveillance des niveaux de carburant"
        ],
        "Dysfonctionnement mineur dans le système de navigation": [
            "Passage au système de navigation redondant",
            "Recalibrage des gyroscopes",
            "Initialisation du système de navigation stellaire",
            "Vérification des capteurs de position",
            "Analyse des données de navigation"
        ],
        "Défaillance partielle des panneaux solaires": [
            "Réorientation des panneaux pour maximiser l'exposition",
            "Activation des panneaux solaires de secours",
            "Réduction de la consommation d'énergie non essentielle",
            "Diagnostic des panneaux défectueux",
            "Surveillance de la production d'énergie"
        ],
        "Problème dans le système de recyclage de l'air": [
            "Activation des filtres de secours",
            "Augmentation de la ventilation",
            "Réparation des composants défectueux",
            "Surveillance de la qualité de l'air",
            "Analyse des données de recyclage de l'air"
        ],
        "Dysfonctionnement du système de contrôle thermique": [
            "Augmentation de la ventilation pour dissiper la chaleur",
            "Activation du système de refroidissement d'urgence",
            "Réparation des composants défectueux",
            "Surveillance des températures critiques",
            "Diagnostic des composants du système de contrôle thermique"
        ],
        "Interférence électromagnétique": [
            "Recalibration des instruments affectés",
            "Activation des systèmes de secours",
            "Détection et isolation de la source d'interférence",
            "Analyse des données de communication",
            "Surveillance des systèmes électroniques"
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
        time.sleep(0.1)
        elapsed_time = time.time() - start_time
        altitude += vitesse * 0.1
        acceleration = (poussée - (M_fusee * 9.81)) / M_fusee
        vitesse += acceleration * 0.1
        carburant -= poussée * 0.1 / (isp * 9.81)
        M_fusee -= poussée * 0.1 / (isp * 9.81)

        if random.random() < 0.05:
            incident_description = generer_incident()
            print(f"T+{elapsed_time:.1f}s - INCIDENT: {incident_description}")
            time.sleep(0.5)
            solution = generer_solution(incident_description)
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

        print(envoyer_message_terre("Lancement réussi, en route vers l'orbite."))
        print(recevoir_message_terre())
        print(envoyer_message_fusee("Navigation stable, tous les systèmes sont nominal."))
        print(recevoir_message_fusee())
        print(f"Temps de communication Terre-Mars : {simuler_delai_communication(dist_terre_mars):.2f} secondes")

        # Initialisation des variables pour le voyage
        equipage = ["Alice", "Bob", "Charlie"]
        vaisseau = {"integrité": 100}
        niveau_bouclier = 100

        experiences = [
            {"nom": "Expérience sur la croissance des cristaux", "progression": 0},
            {"nom": "Étude des radiations cosmiques", "progression": 0}
        ]

        vegetaux = [
            {"nom": "Tomate", "taille": 0, "taille_max": 30, "eau_besoin": 3, "lumiere_besoin": 5},
            {"nom": "Laitue", "taille": 0, "taille_max": 20, "eau_besoin": 2, "lumiere_besoin": 4}
        ]

        # Simulation du voyage vers Mars
        print("\nDébut du voyage vers Mars.")

        temps_voyage_jours = int(temps_voyage / 86400)
        for jour in range(1, temps_voyage_jours + 1):
            gestion_experiences(equipage, jour, experiences)
            gestion_plantation(vegetaux, jour)

            if random.random() < 0.1:
                evenement = random.choice(["micro_astéroïde", "tempête_solaire"])
                gerer_difficultes(equipage, evenement, vaisseau, niveau_bouclier)

            if vaisseau["integrité"] <= 0:
                print("Le vaisseau est trop endommagé pour continuer la mission.")
                break

            time.sleep(0.1)  # Pour ralentir la simulation

def gerer_difficultes(equipage, evenement, vaisseau, niveau_bouclier):
    evenements = {
        "micro_astéroïde": {
            "description": "Collision avec un micro astéroïde détectée!",
            "dommage": lambda: random.randint(5, 15),
            "impact_bouclier": lambda: random.randint(5, 10)
        },
        "tempête_solaire": {
            "description": "Tempête solaire imminente!",
            "dommage": lambda: random.randint(0, 5),
            "impact_bouclier": lambda: random.randint(15, 25)
        },
        "panne_système": {
            "description": "Panne d'un système critique détectée!",
            "dommage": lambda: random.randint(10, 20),
            "impact_bouclier": lambda: 0
        },
        "fuite_oxygène": {
            "description": "Fuite d'oxygène détectée dans un compartiment!",
            "dommage": lambda: random.randint(5, 10),
            "impact_bouclier": lambda: 0
        }
    }

    if evenement in evenements:
        event = evenements[evenement]
        print(event["description"])
        dommage = event["dommage"]()
        impact_bouclier = event["impact_bouclier"]()

        vaisseau["integrité"] -= dommage
        niveau_bouclier -= impact_bouclier

        print(f"Le vaisseau a subi {dommage} points de dommages. Intégrité actuelle : {vaisseau['integrité']}")
        print(f"Les boucliers ont diminué de {impact_bouclier} points. Niveau actuel des boucliers : {niveau_bouclier}")

        if vaisseau["integrité"] <= 50:
            print("Alerte : Le vaisseau est en mauvais état. Réparations nécessaires!")
            for membre in equipage:
                competence = random.randint(1, 10)
                reparation = 5 + competence
                vaisseau["integrité"] += reparation
                print(f"{membre} répare le vaisseau. Intégrité restaurée de {reparation} points.")

        if niveau_bouclier <= 20:
            print("Alerte : Niveau des boucliers critique. Régénération d'urgence activée.")
            regeneration = random.randint(10, 20)
            niveau_bouclier += regeneration
            print(f"Boucliers régénérés de {regeneration} points. Nouveau niveau : {niveau_bouclier}")

    return vaisseau["integrité"], niveau_bouclier

def gestion_plantation(vegetaux, jours):
    print(f"Jour {jours}: Surveillance de l'évolution des plantes.")
    for plante in vegetaux:
        print(f"Plante {plante['nom']} :")
        
        # Facteurs environnementaux aléatoires
        qualite_lumiere = random.uniform(0.8, 1.2)
        qualite_eau = random.uniform(0.8, 1.2)
        temperature = random.uniform(18, 28)

        # Calcul de la croissance en fonction des facteurs
        croissance_base = random.uniform(0.1, 0.5)
        croissance = croissance_base * qualite_lumiere * qualite_eau * (1 - abs(temperature - 23) / 20)
        plante['taille'] += croissance
        
        print(f" - Croissance de {croissance:.2f} cm. Taille actuelle : {plante['taille']:.2f} cm.")
        
        # Gestion des besoins en eau et lumière
        plante['eau_besoin'] -= random.uniform(0.5, 1.5)
        plante['lumiere_besoin'] -= random.uniform(0.5, 1.5)
        
        if plante['eau_besoin'] <= 0:
            print(f" - La plante a besoin d'eau!")
            reapprovisionnement_eau = random.uniform(1, 3)
            plante['eau_besoin'] = reapprovisionnement_eau
            print(f" - La plante a reçu {reapprovisionnement_eau:.2f} unités d'eau.")
        
        if plante['lumiere_besoin'] <= 0:
            print(f" - La plante a besoin de lumière!")
            reapprovisionnement_lumiere = random.uniform(2, 4)
            plante['lumiere_besoin'] = reapprovisionnement_lumiere
            print(f" - La plante a été exposée à la lumière pendant {reapprovisionnement_lumiere:.2f} heures.")
        
        # Gestion des maladies
        if random.random() < 0.05:  # 5% de chance de maladie
            print(f" - Attention! La plante {plante['nom']} montre des signes de maladie.")
            plante['sante'] = max(0, plante['sante'] - random.uniform(5, 15))
        else:
            plante['sante'] = min(100, plante['sante'] + random.uniform(0, 5))
        
        print(f" - Santé de la plante : {plante['sante']:.2f}%")
        
        if plante['taille'] >= plante['taille_max']:
            print(f" - La plante {plante['nom']} est prête pour la récolte!")
            recolte = random.uniform(0.8, 1.2) * plante['rendement_base']
            print(f" - Récolte : {recolte:.2f} unités")
            plante['taille'] = 0  # Réinitialisation après la récolte

def gestion_experiences(equipage, jour, experiences):
    print(f"Jour {jour}: Activités scientifiques.")
    for membre in equipage:
        if random.random() < 0.8:  # 80% de chance de travailler sur une expérience
            experience = random.choice(experiences)
            print(f"{membre} travaille sur l'expérience : {experience['nom']}.")
            
            competence = random.randint(1, 10)
            motivation = random.uniform(0.8, 1.2)
            difficulte = experience.get('difficulte', 1)
            
            progression = (10 + competence) * motivation / difficulte
            experience['progression'] += progression
            
            if experience['progression'] >= 100:
                experience['progression'] = 100
                print(f"L'expérience {experience['nom']} est terminée!")
                analyser_resultats(experience)
                
                # Générer une nouvelle expérience
                nouvelle_experience = generer_nouvelle_experience()
                experiences.append(nouvelle_experience)
                print(f"Nouvelle expérience ajoutée : {nouvelle_experience['nom']}")
            else:
                print(f"L'expérience {experience['nom']} progresse à {experience['progression']:.2f}%.")
                
            # Chance de découverte inattendue
            if random.random() < 0.05:  # 5% de chance
                print(f"Découverte inattendue lors de l'expérience {experience['nom']}!")
                gerer_decouverte(experience)
        else:
            print(f"{membre} effectue des tâches de maintenance du vaisseau.")

def generer_nouvelle_experience():
    noms_experiences = [
        "Étude de la croissance bactérienne en microgravité",
        "Analyse de l'impact des radiations sur les matériaux",
        "Observation des changements physiologiques de l'équipage",
        "Test de nouveaux alliages pour la construction spatiale",
        "Étude du comportement des fluides en apesanteur"
    ]
    return {
        "nom": random.choice(noms_experiences),
        "progression": 0,
        "difficulte": random.uniform(0.8, 1.5)
    }

def gerer_decouverte(experience):
    decouvertes = [
        "Un nouveau phénomène physique observé",
        "Une réaction chimique inattendue",
        "Un comportement cellulaire anormal détecté",
        "Une propriété inconnue d'un matériau révélée",
        "Une adaptation physiologique surprenante constatée"
    ]
    decouverte = random.choice(decouvertes)
    print(f"  - {decouverte}")
    experience['valeur_scientifique'] = experience.get('valeur_scientifique', 1) * 1.5

def simuler_voyage_mars(jours_total):
    equipage = ["Alice", "Bob", "Charlie"]
    vaisseau = {"integrité": 100}
    niveau_bouclier = 100
    moral_equipage = 100

    experiences = [
        {"nom": "Expérience sur la croissance des cristaux", "progression": 0, "difficulte": 1.2},
        {"nom": "Étude des radiations cosmiques", "progression": 0, "difficulte": 1.5}
    ]

    vegetaux = [
        {"nom": "Tomate", "taille": 0, "taille_max": 30, "eau_besoin": 3, "lumiere_besoin": 5, "sante": 100, "rendement_base": 5},
        {"nom": "Laitue", "taille": 0, "taille_max": 20, "eau_besoin": 2, "lumiere_besoin": 4, "sante": 100, "rendement_base": 3}
    ]

    for jour in range(1, jours_total + 1):
        print(f"\n--- Jour {jour} ---")
        
        # Gestion des difficultés
        if random.random() < 0.2:  # 20% de chance d'un événement par jour
            evenement = random.choice(["micro_astéroïde", "tempête_solaire", "panne_système", "fuite_oxygène"])
            vaisseau["integrité"], niveau_bouclier = gerer_difficultes(equipage, evenement, vaisseau, niveau_bouclier)

        # Gestion des plantations
        gestion_plantation(vegetaux, jour)

        # Gestion des expériences
        gestion_experiences(equipage, jour, experiences)

        # Gestion du moral de l'équipage
        variation_moral = random.uniform(-5, 5)
        moral_equipage = max(0, min(100, moral_equipage + variation_moral))
        print(f"Moral de l'équipage : {moral_equipage:.2f}%")

        if vaisseau["integrité"] <= 0:
            print("Le vaisseau est trop endommagé. Fin de la mission.")
            break

        if moral_equipage <= 20:
            print("Le moral de l'équipage est critique. La mission est compromise.")
            break

    print("\nFin de la simulation du voyage vers Mars.")
    print(f"Intégrité finale du vaisseau : {vaisseau['integrité']}%")
    print(f"Niveau final des boucliers : {niveau_bouclier}")
    print(f"Moral final de l'équipage : {moral_equipage:.2f}%")

 
if __name__ == "__main__":
    simuler_lancement()
    print("\nDébut de la simulation du voyage vers Mars")
    simuler_voyage_mars(100)  # Simule un voyage de 100 jours    
