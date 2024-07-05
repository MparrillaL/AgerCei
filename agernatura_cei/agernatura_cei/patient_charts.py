from .patient import Patient, ScalePatient
import matplotlib.pyplot as plt

class ChartGenerator:
    """
    Generador de gráficos relacionados con la información de pacientes.

    Parameters
    ----------
    patient : Patient
        El objeto de paciente para el cual se generarán los gráficos.
    """
    def __init__(self, patient):
        """
        Inicializa el generador de gráficos.

        Parameters
        ----------
        patient : Patient
            El objeto de paciente para el cual se generarán los gráficos.
        """

        self.patient = patient

    def get_imc_graf(self):
        """
        Genera un gráfico de barras horizontal para el Índice de Masa Corporal (IMC).

        Returns
        -------
        matplotlib.figure.Figure
            La figura del gráfico generado.
        """
        limites_imc = [0, 18.5, 25, 30, 35, 50, 60]
        colores_imc = ['#E0E0E0', '#7FFF7F', 'yellow', 'orange', '#FF9999', 'red']
        etiquetas_imc = ['Bajo peso', 'Peso normal', 'Sobrepeso', 'Obesidad I', 'Obesidad II',
                         'Obesidad III']

        imc_paciente = self.patient.imc

        fig, ax = plt.subplots(figsize=(4.5, 1.65))

        for i in range(len(limites_imc) - 1):
            ax.barh(0, limites_imc[i + 1] - limites_imc[i], left=limites_imc[i], height=0.5,
                    color=colores_imc[i], edgecolor='black', label=etiquetas_imc[i])

        ax.scatter(imc_paciente, 0, color='white', marker='.', s=50, edgecolor='black')
        ax.text(imc_paciente, 0.50, f'{self.patient.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(0, 60)
        ax.set_ylim(-1, 1)
        ax.set_xticks([10, 20, 30, 40, 50, 60])
        ax.set_yticks([])
        ax.set_xlabel('IMC')
        ax.set_title(f"")

        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        plt.tight_layout()
        return fig

    def get_gc_graf(self):
        """
        Genera un gráfico de barras horizontal para el porcentaje de grasa corporal (%GC).

        Returns
        -------
        matplotlib.figure.Figure
            La figura del gráfico generado.
        """

        limites_gc = [0, 23, 35, 41, 50]
        colores_gc = ["#E0E0E0", "#7FFF7F", "yellow", "#FF9999"]
        etiquetas_gc = ["Bajo grasa", "saludable", "alto grasa", "obeso"]
        gc_paciente = self.patient.grass_percent
        fig, ax = plt.subplots(figsize=(4.5, 1.5))

        for i in range(len(limites_gc) - 1):
            ax.barh(0, limites_gc[i + 1] - limites_gc[i], left=limites_gc[i], height=0.5,
                    color=colores_gc[i], edgecolor='black', label=etiquetas_gc[i])

        ax.scatter(gc_paciente, 0, color='white', marker='.', s=50, edgecolor='black')
        ax.text(gc_paciente, 0.50, f'{self.patient.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(0, 50)
        ax.set_ylim(-1, 1)
        ax.set_xticks([10, 20, 30, 40, 50])
        ax.set_yticks([])
        ax.set_xlabel(f"% Grasa Corporal")


        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        plt.tight_layout()
        return fig

    def get_wl_graf(self):
        """
        Genera un gráfico de barras horizontal para el porcentaje de agua corporal (%AC).

        Returns
        -------
        matplotlib.figure.Figure
            La figura del gráfico generado.
        """
        limites_wl = [0, 44, 66, 80]
        colores_wl = ["#E0E0E0", "#7FFF7F", "#E0E0E0"]
        etiquetas_wl = ["Inferior", "saludable", "Superior"]
        wl_paciente = self.patient.water_percent
        fig, ax = plt.subplots(figsize=(4.5, 1.5))

        for i in range(len(limites_wl) - 1):
            ax.barh(0, limites_wl[i + 1] - limites_wl[i], left=limites_wl[i], height=0.5,
                    color=colores_wl[i], edgecolor='black', label=etiquetas_wl[i])

        ax.scatter(wl_paciente, 0, color='white', marker='.', s=50, edgecolor='black')
        ax.text(wl_paciente, 0.50, f'{self.patient.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(30, 80)
        ax.set_ylim(-1, 1)
        ax.set_xticks([30, 45, 50, 60, 65, 80])
        ax.set_yticks([])
        ax.set_xlabel(f"% Agua Corporal")


        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        plt.tight_layout()
        return fig

    def get_cvrisk_graf(self):
        """
        Genera un gráfico de barras horizontal para el riesgo cardiovascular (CV Risk).

        Returns
        -------
        matplotlib.figure.Figure
            La figura del gráfico generado.
        """
        limites_cv = [0, 5, 9, 13, 17, 21]
        colores_cv = ["#7FFF7F", "yellow", "orange", "#FF9999", "red"]
        etiquetas_cv = ["Saludable", "Normal", "Aumentado", "Muy alto", "Extremo"]
        cv_paciente = self.patient.visceral_grass
        fig, ax = plt.subplots(figsize=(4.5, 1.5))

        for i in range(len(limites_cv) - 1):
            ax.barh(0, limites_cv[i + 1] - limites_cv[i], left=limites_cv[i], height=0.5,
                    color=colores_cv[i], edgecolor='black', label=etiquetas_cv[i])

        ax.scatter(cv_paciente, 0, color='white', marker='.', s=50, edgecolor='black')
        ax.text(cv_paciente, 0.50, f'{self.patient.name}', ha='center', va='center', color='black', fontsize=10,
                bbox=dict(facecolor='white', edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xlim(0, 21)
        ax.set_ylim(-1, 1)
        ax.set_xticks([0, 5, 9, 13, 17, 21])
        ax.set_yticks([])
        ax.set_xlabel(f"Grasa Visceral")


        ax.legend(loc='upper left', bbox_to_anchor=(1, 1))

        plt.tight_layout()
        return fig

    def generate_all_graphs(self):

        self.get_imc_graf()
        self.get_gc_graf()
        self.get_wl_graf()
        self.get_cvrisk_graf()
        plt.show()




paciente1 = Patient("Maria", "Gonzalez", 30, "m", 169, 82, "sedentario", 142)
paciente1_bascula = ScalePatient.add_patient(paciente1
                                             , 142
                                             , 35.2
                                             , 2.4
                                             , 38
                                             , 29.5
                                             , 52
                                             , 12
                                             , 42
                                             )

# quitar el comentario '#' para obtener una demostración del codigo:
# ChartGenerator(paciente1_bascula).generate_all_graphs()