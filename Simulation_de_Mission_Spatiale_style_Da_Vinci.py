import numpy as np
import matplotlib.pyplot as plt
from dataclasses import dataclass

@dataclass
class ParamètresFusée:
    """Paramètres principaux de la fusée et de sa mission."""
    masse_totale: float  # kg
    masse_combustible: float  # kg
    efficacité_moteur: float  # rapport poussée/masse combustible
    altitude_cible: float  # m

class SimulateurMissionSpatiale:
    """Simulateur principal de la mission spatiale."""
    
    def __init__(self, params: ParamètresFusée):
        self.params = params
        self.g = 9.81  # m/s²
        self.coefficient_trainée = 0.2  # coefficient de résistance de l'air
        
    def calculer_poussée(self, masse_combustible_restante: float) -> float:
        """Calcule la poussée instantanée du moteur."""
        return (self.params.efficacité_moteur * 
                masse_combustible_restante * self.g)

    def calculer_résistance_air(self, vitesse: float, masse_actuelle: float) -> float:
        """Calcule la résistance de l'air."""
        return self.coefficient_trainée * masse_actuelle * (vitesse ** 2)

    def simuler(self, durée_simulation: int = 300, pas_temps: float = 1.0):
        """Simule la mission spatiale complète."""
        nombre_pas = int(durée_simulation / pas_temps)
        temps = np.linspace(0, durée_simulation, nombre_pas)
        
        # Initialisation des tableaux de données
        altitude = np.zeros(nombre_pas)
        vitesse = np.zeros(nombre_pas)
        accélération = np.zeros(nombre_pas)
        masse_combustible = np.zeros(nombre_pas)
        masse_combustible[0] = self.params.masse_combustible
        
        for i in range(1, nombre_pas):
            # Calcul de la masse actuelle
            masse_actuelle = (self.params.masse_totale - 
                            (self.params.masse_combustible - masse_combustible[i-1]))
            
            # Calcul des forces
            poussée = self.calculer_poussée(masse_combustible[i-1])
            résistance = self.calculer_résistance_air(vitesse[i-1], masse_actuelle)
            
            # Équations du mouvement
            force_nette = poussée - résistance - (masse_actuelle * self.g)
            accélération[i] = force_nette / masse_actuelle
            vitesse[i] = vitesse[i-1] + accélération[i] * pas_temps
            altitude[i] = altitude[i-1] + vitesse[i] * pas_temps
            
            # Mise à jour du combustible
            if masse_combustible[i-1] > 0:
                masse_combustible[i] = (masse_combustible[i-1] - 
                                      self.params.efficacité_moteur * pas_temps)
                masse_combustible[i] = max(0, masse_combustible[i])
            else:
                masse_combustible[i] = 0
                
        return temps, altitude, vitesse, accélération, masse_combustible

    def visualiser_résultats(self, temps, altitude, vitesse, accélération, masse_combustible):
        """Crée une visualisation artistique des résultats."""
        fig, axes = plt.subplots(2, 2, figsize=(15, 10))
        fig.suptitle("Étude du Vol Spatial\n- Dans l'esprit de Léonard de Vinci -", 
                    fontsize=16, fontfamily='serif')

        # Style inspiré des croquis de Da Vinci
        style = {
            'color': 'brown',
            'alpha': 0.7,
            'linewidth': 1.5,
            'linestyle': '-'
        }

        # Graphique 1: Altitude
        axes[0, 0].plot(temps, altitude, **style)
        axes[0, 0].set_title("Altitude en fonction du temps")
        axes[0, 0].set_xlabel("Temps (s)")
        axes[0, 0].set_ylabel("Altitude (m)")
        axes[0, 0].grid(True, alpha=0.3)

        # Graphique 2: Vitesse
        axes[0, 1].plot(temps, vitesse, **style)
        axes[0, 1].set_title("Vitesse en fonction du temps")
        axes[0, 1].set_xlabel("Temps (s)")
        axes[0, 1].set_ylabel("Vitesse (m/s)")
        axes[0, 1].grid(True, alpha=0.3)

        # Graphique 3: Accélération
        axes[1, 0].plot(temps, accélération, **style)
        axes[1, 0].set_title("Accélération en fonction du temps")
        axes[1, 0].set_xlabel("Temps (s)")
        axes[1, 0].set_ylabel("Accélération (m/s²)")
        axes[1, 0].grid(True, alpha=0.3)

        # Graphique 4: Masse de combustible
        axes[1, 1].plot(temps, masse_combustible, **style)
        axes[1, 1].set_title("Masse de combustible restante")
        axes[1, 1].set_xlabel("Temps (s)")
        axes[1, 1].set_ylabel("Masse (kg)")
        axes[1, 1].grid(True, alpha=0.3)

        plt.tight_layout()
        return fig

def main():
    # Paramètres de la mission
    params = ParamètresFusée(
        masse_totale=10000,  # kg
        masse_combustible=8000,  # kg
        efficacité_moteur=0.3,  # ratio
        altitude_cible=100000  # m
    )
    
    # Création et exécution de la simulation
    simulateur = SimulateurMissionSpatiale(params)
    résultats = simulateur.simuler()
    
    # Visualisation des résultats
    figure = simulateur.visualiser_résultats(*résultats)
    plt.show()

if __name__ == "__main__":
    main()