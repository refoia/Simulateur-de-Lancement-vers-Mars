import random
import math
import time
from typing import List, Dict, Any

# Constants
G = 6.67430e-11
M_terre = 5.97e24
R_terre = 6.371e6
M_fusee_initial = 1e6
dist_terre_mars = 225e9

# Nouvelles constantes
DUREE_JOUR = 24 * 60 * 60  # Durée d'un jour en secondes
DISTANCE_TERRE_MARS = 225e9  # Distance moyenne Terre-Mars en mètres

class Astronaute:
    def __init__(self, nom: str):
        self.nom = nom
        self.sante = 100
        self.competences = {
            "pilotage": random.randint(1, 10),
            "ingenierie": random.randint(1, 10),
            "science": random.randint(1, 10),
            "medical": random.randint(1, 10)
        }
        self.moral = 100

class Vaisseau:
    def __init__(self):
        self.integrite = 100
        self.boucliers = 100
        self.carburant = M_fusee_initial
        self.oxygene = 100
        self.nourriture = 100
        self.energie = 100

class Experience:
    def __init__(self, nom: str, difficulte: float):
        self.nom = nom
        self.progression = 0
        self.difficulte = difficulte
        self.valeur_scientifique = 1

class Plante:
    def __init__(self, nom: str, taille_max: float, rendement_base: float):
        self.nom = nom
        self.taille = 0
        self.taille_max = taille_max
        self.eau_besoin = random.uniform(1, 5)
        self.lumiere_besoin = random.uniform(1, 5)
        self.sante = 100
        self.rendement_base = rendement_base

class MissionMars:
    def __init__(self):
        self.equipage: List[Astronaute] = [Astronaute(nom) for nom in ["Alice", "Bob", "Charlie"]]
        self.vaisseau = Vaisseau()
        self.experiences: List[Experience] = [
            Experience("Croissance des cristaux", 1.2),
            Experience("Étude des radiations cosmiques", 1.5)
        ]
        self.vegetaux: List[Plante] = [
            Plante("Tomate", 30, 5),
            Plante("Laitue", 20, 3)
        ]
        self.jour_actuel = 0
        self.distance_parcourue = 0
        self.log: List[str] = []

    def simuler_jour(self):
        self.jour_actuel += 1
        self.log.append(f"\n--- Jour {self.jour_actuel} ---")
        
        self.gerer_ressources()
        self.gerer_difficultes()
        self.gerer_plantation()
        self.gerer_experiences()
        self.gerer_moral_equipage()
        self.mettre_a_jour_position()

    def gerer_ressources(self):
        self.vaisseau.oxygene -= random.uniform(0.5, 1.5)
        self.vaisseau.nourriture -= random.uniform(0.5, 1)
        self.vaisseau.energie -= random.uniform(1, 2)
        
        if self.vaisseau.oxygene < 20 or self.vaisseau.nourriture < 20 or self.vaisseau.energie < 20:
            self.log.append("ALERTE: Niveaux critiques de ressources!")

    def gerer_difficultes(self):
        if random.random() < 0.2:
            evenements = [
                ("micro_astéroïde", "Collision avec un micro astéroïde!"),
                ("tempête_solaire", "Tempête solaire imminente!"),
                ("panne_système", "Panne d'un système critique!"),
                ("fuite_oxygène", "Fuite d'oxygène détectée!")
            ]
            evenement, description = random.choice(evenements)
            self.log.append(description)
            
            dommage = random.randint(5, 15)
            self.vaisseau.integrite -= dommage
            self.log.append(f"Le vaisseau a subi {dommage} points de dommages. Intégrité: {self.vaisseau.integrite}")
            
            if evenement == "tempête_solaire":
                impact_bouclier = random.randint(10, 20)
                self.vaisseau.boucliers -= impact_bouclier
                self.log.append(f"Boucliers réduits de {impact_bouclier}. Niveau: {self.vaisseau.boucliers}")
            
            self.reparer_vaisseau()

    def reparer_vaisseau(self):
        for astronaute in self.equipage:
            if self.vaisseau.integrite < 50:
                reparation = 5 + astronaute.competences["ingenierie"]
                self.vaisseau.integrite = min(100, self.vaisseau.integrite + reparation)
                self.log.append(f"{astronaute.nom} répare le vaisseau. Nouvelle intégrité: {self.vaisseau.integrite}")

    def gerer_plantation(self):
        for plante in self.vegetaux:
            croissance = random.uniform(0.1, 0.5) * (plante.sante / 100)
            plante.taille += croissance
            self.log.append(f"{plante.nom} a grandi de {croissance:.2f}cm. Taille: {plante.taille:.2f}cm")
            
            if plante.taille >= plante.taille_max:
                recolte = random.uniform(0.8, 1.2) * plante.rendement_base
                self.vaisseau.nourriture += recolte
                self.log.append(f"Récolte de {plante.nom}: {recolte:.2f} unités de nourriture")
                plante.taille = 0

    def gerer_experiences(self):
        for astronaute in self.equipage:
            if random.random() < 0.8:
                experience = random.choice(self.experiences)
                progression = (10 + astronaute.competences["science"]) / experience.difficulte
                experience.progression += progression
                self.log.append(f"{astronaute.nom} travaille sur {experience.nom}. Progression: {experience.progression:.2f}%")
                
                if experience.progression >= 100:
                    self.log.append(f"Expérience {experience.nom} terminée!")
                    self.experiences.remove(experience)
                    self.experiences.append(self.generer_nouvelle_experience())

    def gerer_moral_equipage(self):
        for astronaute in self.equipage:
            variation_moral = random.uniform(-5, 5)
            astronaute.moral = max(0, min(100, astronaute.moral + variation_moral))
            self.log.append(f"Moral de {astronaute.nom}: {astronaute.moral:.2f}%")

    def mettre_a_jour_position(self):
        vitesse_moyenne = 20000  # m/s (approximatif)
        distance_jour = vitesse_moyenne * DUREE_JOUR
        self.distance_parcourue += distance_jour
        progression = (self.distance_parcourue / DISTANCE_TERRE_MARS) * 100
        self.log.append(f"Distance parcourue: {self.distance_parcourue/1e6:.2f} millions km ({progression:.2f}% du trajet)")

    def generer_nouvelle_experience(self) -> Experience:
        noms_experiences = [
            "Étude de la croissance bactérienne en microgravité",
            "Analyse de l'impact des radiations sur les matériaux",
            "Observation des changements physiologiques de l'équipage",
            "Test de nouveaux alliages pour la construction spatiale",
            "Étude du comportement des fluides en apesanteur"
        ]
        return Experience(random.choice(noms_experiences), random.uniform(0.8, 1.5))

    def verifier_fin_mission(self) -> bool:
        if self.vaisseau.integrite <= 0:
            self.log.append("Mission échouée: Le vaisseau est trop endommagé.")
            return True
        if all(a.moral <= 20 for a in self.equipage):
            self.log.append("Mission échouée: Le moral de l'équipage est critique.")
            return True
        if self.distance_parcourue >= DISTANCE_TERRE_MARS:
            self.log.append("Mission réussie: Arrivée sur Mars!")
            return True
        return False

def simuler_mission_mars(duree_mission: int):
    mission = MissionMars()
    for _ in range(duree_mission):
        mission.simuler_jour()
        if mission.verifier_fin_mission():
            break
    
    print("\n".join(mission.log))
    print("\nRésumé de la mission:")
    print(f"Durée totale: {mission.jour_actuel} jours")
    print(f"Distance parcourue: {mission.distance_parcourue/1e9:.2f} milliards km")
    print(f"État final du vaisseau: Intégrité {mission.vaisseau.integrite}%, Boucliers {mission.vaisseau.boucliers}%")
    print("État final de l'équipage:")
    for astronaute in mission.equipage:
        print(f"  {astronaute.nom}: Santé {astronaute.sante}%, Moral {astronaute.moral:.2f}%")

if __name__ == "__main__":
    simuler_mission_mars(365)  # Simuler une mission d'un an