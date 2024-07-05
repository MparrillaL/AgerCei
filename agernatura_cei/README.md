agernatura_cei
------------


![alt text](https://badgen.net/badge/python/3.10/cyan?icon=pypi)


## Description

"This project, developed as part of my course at CEI, stems from my desire to support my mother, a nutritionist. My goal was to create a comprehensive program that would streamline patient management from the moment they enter the consultation room until they receive their personalized treatment. This marks my first significant project in Python, where I aimed to merge my knowledge with a passion for programming to contribute to the field of nutrition. The program aims to streamline the care process by offering tools to record personal data, nutritional details, preferences, and food allergies, with the ability to provide personalized diets and advice tailored to individual needs. I aspire for this project to benefit not only my mother in her professional practice but also other nutrition professionals in optimizing their services."

## Packaging

As this is a project developed for academic purposes, the packaging of the project will be done manually running this command in the terminal.
Remember to replace 'output_path' with the path where the artifact will be stored.

```
python setup.py bdist_wheel --dist-dir=/output_path
```

## Distribution

As this is a project developed for academic purposes, the distribution of the project will be done manually uploading the generated '.whl' file to the Colab working environment.
Inside the working directory '/content' in Colab, we will create a 'packages' directory where we will upload the generated artefacts.

## Usage

To install our package on the Colab notebook, we need to tell pip not to look for the package in PyPI or any other artifact repository, but to look for it in the path '/content/packages' in the Colab framework.


```
pip install agernatura_cei --find-links=/content/packages
```

Once the package is installed, we can import it and start using it.

```
import agernatura_cei
```

### Usage Example

```
To use 'patient.py' in pycharm:
- simply uncomment the example at the end of the code.
To use 'patient.py' in collab:
- upload agernatura_cei package.
- use this code:
# load the module 'patient.py'
from agernatura_cei.patient import Patient, ScalePatient

# create patient
paciente1 = Patient("Maria", "Gonzalez", 30, "m", 169, 82, "sedentario", 142)

# add scale measures to patient
paciente1_bascula = ScalePatient.add_patient(
    paciente1, 142, 35.2, 2.4, 38, 29.5, 52, 12, 42
)

# demostration of all methods you can use with your patient:
paciente1_bascula.get_basal_metabolic_rate()
print("----------------------------------------")
print(f"Riesgo cardiovascular: {paciente1_bascula.get_cardiovascular_risk()}.")
print("----------------------------------------")
print(f"Complexion: {paciente1_bascula.get_complexion()}")
print("----------------------------------------")
print(f"IMC: {paciente1_bascula.get_imc_standard()}.")
print("----------------------------------------")
print(f"Porcentaje graso: {paciente1_bascula.get_grass_percent()}.")
print("----------------------------------------")
print(f"Niveles de agua corporal: {paciente1_bascula.get_w_level()}.")
print("----------------------------------------")
print(f"Indice de masa muscular: {paciente1_bascula.get_im_muscular()}.")
print("----------------------------------------")
print(f"Grasa visceral: {paciente1_bascula.get_ev_gv()}.")

To use 'patient_charts.py' in pycharm:
- simply uncomment the example at the end of the code.
To use 'patient_charts.py' in collab:
- upload agernatura_cei package.
- make sure you created your patient object previously.
- use this code:
# load the module 'patient_charts.py'
from agernatura_cei.patient_charts import ChartGenerator

#demostration:
ChartGenerator(paciente1_bascula).generate_all_graphs()

'patient_gestor' allows you to create a patient dataframe and easily add, delete, and edit patients 
in that dataframe.

In csv_analysis.py, we have edited a CSV file to align with our Patient object and created graphs 
illustrating the weight evolution of each patient.

In form.py, I have created the form that my mother needed to conduct an analysis of a new patient 
and be able to show their health status. To use this form from the terminal, make sure you are in
the same directory as the file and enter the command 'python form.py.' or simply execute form.py
in pycharm, using pyinstaller I made this file executable easilly for my mother to use it.
```

## Credits
I would like to express my sincere gratitude to:

- My mother, for her constant support and motivation.
- My professors, for their guidance and teachings.
- My classmates, for their collaboration and camaraderie.

Thank you all for making this project possible.

### Owner
- Manuel Parrilla <manuelparrillalahoz@alumnos.cei.es>
