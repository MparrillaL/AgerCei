import re


class Patient:
    """
    Clase que representa a un paciente.

    Atributos
    ----------
    name : str
        Nombre del paciente.
    surname : str
        Apellido del paciente.
    age : int
        Edad del paciente.
    gender : str
        Género del paciente ('H' para hombres, 'W' para mujeres).
    height : float
        Altura del paciente en centímetros.
    weight : float
        Peso del paciente en kilogramos.
    activity : str
        Nivel de actividad del paciente.
    waist_measure : float
        Medida de la cintura del paciente en centímetros.

    Métodos
    -------
    __init__(name, surname, age, gender, height, weight, activity, waist_measure)
        Inicializa un objeto Patient con la información del paciente.
    get_basal_metabolic_rate()
        Calcula la tasa metabólica basal (BMR) del paciente.
    Raises
    ------
    ValueError
        Cuando height o weight son valores negativos.
    TypeError
        Cuando alguno de los atributos no tiene el tipo de dato correcto.

    Excepciones personalizadas
    --------------------------
    GenderError
        Se lanza cuando el género proporcionado no es 'H' para hombres o 'W' para mujeres,
        sin distinción entre mayúsculas y minúsculas.
     InvalidNameError
        Se lanza cuando el nombre o apellido contiene caracteres no permitidos.
    """

    def __init__(self, name, surname, age, gender, height, weight, activity, waist_measure):
        """
        Inicializa un objeto Patient con la información del paciente.

        Parámetros
        ----------
        name : str
            Nombre del paciente.
        surname : str
            Apellido del paciente.
        age : int
            Edad del paciente.
        gender : str
            Género del paciente ('H' para hombres, 'W' para mujeres).
        height : float
            Altura del paciente en centímetros.
        weight : float
            Peso del paciente en kilogramos.
        activity : str
            Nivel de actividad del paciente.
        waist_measure : float
            Medida de la cintura del paciente en centímetros.

        Raises
        ------
        ValueError
            Cuando height o weight son valores negativos.
        TypeError
            Cuando alguno de los atributos no tiene el tipo de dato correcto.
        GenderError
            Se lanza cuando el género proporcionado no es 'H' para hombres o 'W' para mujeres,
            sin distinción entre mayúsculas y minúsculas.
        """
        self._validate_name(name)
        self._validate_name(surname)
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender.lower()
        if height < 0:
            raise ValueError(f"{height} must be a positive value")
        else:
            self.height = height
        if weight < 0:
            raise ValueError(f"{weight} must be a positive value")
        else:
            self.weight = weight
        self.activity = activity.lower()
        self.waist_measure = waist_measure


        if not isinstance(waist_measure, (int, float)):
            raise TypeError(f"{waist_measure} must be a float or integer")

        if not isinstance(name, str):
            raise TypeError(f"{name} must be a string.")

        if not isinstance(surname, str):
            raise TypeError(f"{surname} must be a string.")

        if not isinstance(age, int):
            raise TypeError(f"{age} must be an integer.")

        if gender not in ["h", "m"]:
            raise ValueError(f"{gender} is invalid, must be 'H' for men or 'W' for women.")

        if not isinstance(height, (int, float)):
            raise TypeError(f"{height} must be a float or integer")

        if not isinstance(weight, (int, float)):
            raise TypeError(f"{weight} must be a float or integer")

    def _validate_name(self, name):
        """Valida que el nombre o apellido contenga solo letras y permita un espacio entre dos strings."""
        if not re.match(r'^[A-Za-z]+( [A-Za-z]+)*$', name):
            raise ValueError(
                f"{name} contiene caracteres no permitidos. Debe contener solo letras y permitir un espacio entre dos strings.")

    def get_basal_metabolic_rate(self):
        """
        Calcula la tasa metabólica basal (BMR) del paciente.

        Returns
        -------
        float
            Tasa metabólica basal calculada equivalente al numero de calorias diarias necesarias.
        """
        if self.gender == 'm':
            bmr = 655 + (9.6 * self.weight) + (1.8 * self.height) - (4.7 * self.age)
        else:
            bmr = 66 + (13.7 * self.weight) + (5 * self.height) - (6.8 * self.age)

        activity_factors = {
            "sedentario": 1.2,
            "poco activo": 1.375,
            "activo con moderacion": 1.55,
            "activo con moderación": 1.55,
            "activo": 1.725,
            "muy activo": 1.9
        }

        if self.activity in activity_factors:
            bmr *= activity_factors[self.activity]
        print(f"{self.name} {self.surname} necesita {round(bmr, 2)} calorias al día")
        return bmr


paciente1 = Patient("Maria", "Gonzalez", 30, "m", 169, 82, "sedentario", 142)


# paciente1.get_basal_metabolic_rate()

class ScalePatient(Patient):
    """
            Clase que representa a un paciente con información adicional de escala.

            Atributos
            ----------
            name : str
                Nombre del paciente.
            surname : str
                Apellido del paciente.
            age : int
                Edad del paciente.
            gender : str
                Género del paciente ('H' para hombres, 'W' para mujeres).
            height : float
                Altura del paciente en centímetros.
            weight : float
                Peso del paciente en kilogramos.
            activity : str
                Nivel de actividad del paciente.
            waist_measure : float
                Medida de la cintura del paciente en centímetros.
            grass_percent : float
                Porcentaje de grasa corporal del paciente.
            bone_mass : float
                Masa ósea del paciente en kilogramos.
            muscular_mass : float
                Masa muscular del paciente en kilogramos.
            imc : float
                Índice de masa corporal (IMC) del paciente.
            metabolic_age : float
                Edad metabólica del paciente.
            visceral_grass : float
                Grasa visceral del paciente.
            water_percent : float
                Porcentaje de agua corporal del paciente.

            Métodos
            -------
            __init__(name, surname, age, gender, height, weight, activity, waist_measure, grass_percent,
                     bone_mass, muscular_mass, imc, metabolic_age, visceral_grass, water_percent)
                Inicializa un objeto ScalePatient con la información del paciente y atributos adicionales.
            get_cardiovascular_risk()
                Calcula el riesgo cardiovascular del paciente.
            get_complexion()
                Determina la complexión del paciente.
            get_imc_standard()
                Obtiene el estándar de IMC del paciente.
            get_grass_percent()
                Devuelve la categoría del porcentaje de grasa corporal del paciente.
            get_w_level()
                Determina los niveles de agua corporal del paciente.
            get_im_muscular()
                Clasifica el índice de masa muscular del paciente.
            get_ev_gv()
                Evalúa el nivel de grasa visceral del paciente.
            add_patient(patient_obj, waist_measure, grass_percent, bone_mass, muscular_mass, imc,
                        metabolic_age, visceral_grass, water_percent)
                Agrega un nuevo paciente con información adicional de escala.
    """

    def __init__(self, name, surname, age, gender, height, weight, activity, waist_measure, grass_percent,
                 bone_mass, muscular_mass, imc, metabolic_age, visceral_grass, water_percent):
        """
        Inicializa un objeto ScalePatient con la información del paciente y atributos adicionales.

        Parámetros
        ----------
        name : str
            Nombre del paciente.
        surname : str
            Apellido del paciente.
        age : int
            Edad del paciente.
        gender : str
            Género del paciente ('H' para hombres, 'W' para mujeres).
        height : float
            Altura del paciente en centímetros.
        weight : float
            Peso del paciente en kilogramos.
        activity : str
            Nivel de actividad del paciente.
        waist_measure : float
            Medida de la cintura del paciente en centímetros.
        grass_percent : float
            Porcentaje de grasa corporal del paciente.
        bone_mass : float
            Masa ósea del paciente en kilogramos.
        muscular_mass : float
            Masa muscular del paciente en kilogramos.
        imc : float
            Índice de masa corporal (IMC) del paciente.
        metabolic_age : float
            Edad metabólica del paciente.
        visceral_grass : float
            Grasa visceral del paciente.
        water_percent : float
            Porcentaje de agua corporal del paciente.

        Raises
        ------
        ValueError
            Cuando alguno de los atributos tiene un valor negativo.
        TypeError
            Cuando alguno de los atributos no tiene el tipo de dato correcto.
        GenderError
            Se lanza cuando el género proporcionado no es 'H' para hombres o 'W' para mujeres,
            sin distinción entre mayúsculas y minúsculas.
        """
        super().__init__(name, surname, age, gender, height, weight, activity, waist_measure)
        self.grass_percent = grass_percent
        self.bone_mass = bone_mass
        self.muscular_mass = muscular_mass
        self.imc = imc
        self.metabolic_age = metabolic_age
        self.visceral_grass = visceral_grass
        self.water_percent = water_percent

        if not isinstance(waist_measure, (int, float)):
            raise TypeError(f"{waist_measure} must be a float or integer")
        if waist_measure < 0:
            raise ValueError(f"{waist_measure} must be a positive value")

        if not isinstance(grass_percent, (int, float)):
            raise TypeError(f"{grass_percent} must be a float or integer")
        if grass_percent < 0:
            raise ValueError(f"{grass_percent} must be a positive value")

        if not isinstance(bone_mass, (int, float)):
            raise TypeError(f"{bone_mass} must be a float or integer")
        if bone_mass < 0:
            raise ValueError(f"{bone_mass} must be a positive value")

        if not isinstance(muscular_mass, (int, float)):
            raise TypeError(f"{muscular_mass} must be a float or integer")
        if muscular_mass < 0:
            raise ValueError(f"{muscular_mass} must be a positive value")

        if not isinstance(imc, (int, float)):
            raise TypeError(f"{imc} must be a float or integer")
        if imc < 0:
            raise ValueError(f"{imc} must be a positive value")

        if not isinstance(metabolic_age, (int, float)):
            raise TypeError(f"{metabolic_age} must be a float or integer")
        if metabolic_age < 0:
            raise ValueError(f"{metabolic_age} must be a positive value")

        if not isinstance(visceral_grass, (int, float)):
            raise TypeError(f"{visceral_grass} must be a float or integer")
        if visceral_grass < 0:
            raise ValueError(f"{visceral_grass} must be a positive value")

    def get_cardiovascular_risk(self):
        """
        Calcula y devuelve el riesgo cardiovascular del paciente.

        Returns
        -------
        str
            Riesgo cardiovascular del paciente (Normal, Elevado, Muy elevado).
        """
        if self.gender == 'm':

            if self.waist_measure < 82:
                cardiovascular_risk = "Normal"
            elif self.waist_measure >= 82 and self.waist_measure <= 87:
                cardiovascular_risk = "Elevado"
            else:
                cardiovascular_risk = "Muy elevado"

        else:

            if self.waist_measure < 95:
                cardiovascular_risk = "Normal"
            elif self.waist_measure >= 95 and self.waist_measure <= 101:
                cardiovascular_risk = "Elevado"
            else:
                cardiovascular_risk = "Muy elevado"

        return cardiovascular_risk

    def get_complexion(self):
        """
        Determina y devuelve la complexión del paciente.

        Returns
        -------
        str
            Complexión del paciente (pequeña, mediana, grande)
        """
        if self.gender == 'm':
            if self.height >= 155 and self.height < 159:
                if self.weight < 54:
                    complexion = "pequeña"
                elif self.weight < 59:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 160 and self.height < 164:
                if self.weight < 56:
                    complexion = "pequeña"
                elif self.weight < 61:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 165 and self.height < 169:
                if self.weight < 59:
                    complexion = "pequeña"
                elif self.weight < 64:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 170 and self.height <= 175:
                if self.weight < 65:
                    complexion = "pequeña"
                elif self.weight < 69:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            else:
                complexion = "grande"

        else:
            if self.height >= 170 and self.height < 174:
                if self.weight < 66:
                    complexion = "pequeña"
                elif self.weight < 70:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 175 and self.height < 179:
                if self.weight < 69:
                    complexion = "pequeña"
                elif self.weight < 73:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 180 and self.height < 184:
                if self.weight < 71:
                    complexion = "pequeña"
                elif self.weight < 76:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            elif self.height >= 185 and self.height <= 190:
                if self.weight < 76:
                    complexion = "pequeña"
                elif self.weight < 85:
                    complexion = "mediana"
                else:
                    complexion = "grande"
            else:
                complexion = "grande"

        return f"su complexion es: '{complexion}'."

    def get_imc_standard(self):
        """
        Obtiene y devuelve el estándar de IMC del paciente.

        Returns
        -------
        str
            Estándar de IMC del paciente.
        """
        if self.imc < 18.5:
            imc_standard = "Peso insuficiente"
        elif self.imc >= 18.5 and self.imc < 25:
            imc_standard = "Normopeso"
        elif self.imc >= 25 and self.imc < 27:
            imc_standard = "Sobrepeso grado I"
        elif self.imc >= 27 and self.imc < 30:
            imc_standard = "Sobrepeso grado II (preobesidad)"
        elif self.imc >= 30 and self.imc < 35:
            imc_standard = "Obesidad de tipo I"
        elif self.imc >= 35 and self.imc < 40:
            imc_standard = "Obesidad de tipo II"
        elif self.imc >= 40 and self.imc < 50:
            imc_standard = "Obesidad de tipo III (mórbida)"
        else:
            imc_standard = "Obesidad de tipo IV (extrema)"

        return imc_standard

    def get_grass_percent(self):
        """
        Devuelve la categoría del porcentaje de grasa corporal del paciente.

        Returns
        -------
        str
            Categoría del porcentaje de grasa corporal del paciente.
        """
        if self.gender == 'm':
            if self.age <= 20:
                if self.grass_percent < 16:
                    return "Delgado"
                elif self.grass_percent < 22:
                    bodyfat = "Ideal"
                elif self.grass_percent < 30:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 25:
                if self.grass_percent < 18.5:
                    bodyfat = "Delgado"
                elif self.grass_percent < 25:
                    bodyfat = "Ideal"
                elif self.grass_percent < 31:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 30:
                if self.grass_percent < 19:
                    bodyfat = "Delgado"
                elif self.grass_percent < 25:
                    bodyfat = "Ideal"
                elif self.grass_percent < 32:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 35:
                if self.grass_percent < 19:
                    bodyfat = "Delgado"
                elif self.grass_percent < 25:
                    bodyfat = "Ideal"
                elif self.grass_percent < 33:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 40:
                if self.grass_percent < 22:
                    bodyfat = "Delgado"
                elif self.grass_percent < 28:
                    bodyfat = "Ideal"
                elif self.grass_percent < 33:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 45:
                if self.grass_percent < 23:
                    bodyfat = "Delgado"
                elif self.grass_percent < 28:
                    bodyfat = "Ideal"
                elif self.grass_percent < 35:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 50:
                if self.grass_percent < 23:
                    bodyfat = "Delgado"
                elif self.grass_percent < 29:
                    bodyfat = "Ideal"
                elif self.grass_percent < 35:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 55:
                if self.grass_percent < 24:
                    bodyfat = "Delgado"
                elif self.grass_percent < 30:
                    bodyfat = "Ideal"
                elif self.grass_percent < 36:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            else:
                if self.grass_percent < 25:
                    bodyfat = "Delgado"
                elif self.grass_percent < 31:
                    bodyfat = "Ideal"
                elif self.grass_percent < 38:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
        else:
            if self.age <= 20:
                if self.grass_percent < 4:
                    bodyfat = "Delgado"
                elif self.grass_percent < 14:
                    bodyfat = "Ideal"
                elif self.grass_percent < 19:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 25:
                if self.grass_percent < 5:
                    bodyfat = "Delgado"
                elif self.grass_percent < 14.5:
                    bodyfat = "Ideal"
                elif self.grass_percent < 22:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 30:
                if self.grass_percent < 8.5:
                    bodyfat = "Delgado"
                elif self.grass_percent < 17:
                    bodyfat = "Ideal"
                elif self.grass_percent < 23:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 35:
                if self.grass_percent < 9.5:
                    bodyfat = "Delgado"
                elif self.grass_percent < 18:
                    bodyfat = "Ideal"
                elif self.grass_percent < 24:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 40:
                if self.grass_percent < 10.5:
                    bodyfat = "Delgado"
                elif self.grass_percent < 19:
                    bodyfat = "Ideal"
                elif self.grass_percent < 25:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 45:
                if self.grass_percent < 14:
                    bodyfat = "Delgado"
                elif self.grass_percent < 22:
                    bodyfat = "Ideal"
                elif self.grass_percent < 27:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 50:
                if self.grass_percent < 15:
                    bodyfat = "Delgado"
                elif self.grass_percent < 23:
                    bodyfat = "Ideal"
                elif self.grass_percent < 28:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            elif self.age <= 55:
                if self.grass_percent < 16:
                    bodyfat = "Delgado"
                elif self.grass_percent < 24:
                    bodyfat = "Ideal"
                elif self.grass_percent < 29:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"
            else:
                if self.grass_percent < 17:
                    bodyfat = "Delgado"
                elif self.grass_percent < 25:
                    bodyfat = "Ideal"
                elif self.grass_percent < 31:
                    bodyfat = "Promedio"
                else:
                    bodyfat = "Superior al promedio"

        return bodyfat

    def get_w_level(self):
        """
        Determina y devuelve los niveles de agua corporal del paciente.

        Returns
        -------
        str
            Niveles de agua corporal del paciente.
        """
        if self.gender == 'm':
            if 44 <= self.water_percent <= 61:
                w_level = "saludables"
            elif self.water_percent < 44:
                w_level = "inferiores al promedio"
            else:
                w_level = "superiores al promedio"
        else:
            if 49 <= self.water_percent <= 66:
                w_level = "saludables"
            elif self.water_percent < 49:
                w_level = "inferiores al promedio"
            else:
                w_level = "superiores al promedio"

        return w_level

    def get_im_muscular(self):
        """
        Clasifica y devuelve el índice de masa muscular del paciente.

        Returns
        -------
        str
            Clasificación del índice de masa muscular del paciente.
        """
        if self.gender == 'm':
            if self.age <= 30:
                if self.muscular_mass < 35:
                    return "Baja"
                elif 35 <= self.muscular_mass <= 41:
                    return "Normal"
                else:
                    return "Excesiva"
            elif 30 < self.age <= 60:
                if self.muscular_mass < 33:
                    return "Baja"
                elif 33 <= self.muscular_mass <= 38:
                    return "Normal"
                else:
                    return "Excesiva"
            else:
                if self.muscular_mass < 28:
                    return "Baja"
                elif 28 <= self.muscular_mass <= 33:
                    return "Normal"
                else:
                    return "Excesiva"
        else:
            if self.age <= 30:
                if self.muscular_mass < 43:
                    return "Baja"
                elif 43 <= self.muscular_mass <= 56:
                    return "Normal"
                else:
                    return "Excesiva"
            elif 30 < self.age <= 60:
                if self.muscular_mass < 40:
                    return "Baja"
                elif 40 <= self.muscular_mass <= 50:
                    return "Normal"
                else:
                    return "Excesiva"
            else:
                if self.muscular_mass < 38:
                    return "Baja"
                elif 38 <= self.muscular_mass <= 57:
                    return "Normal"
                else:
                    return "Excesiva"

    def get_ev_gv(self):
        """
        Evalúa y devuelve el nivel de grasa visceral del paciente.

        Returns
        -------
        str
            Nivel de grasa visceral del paciente.
        """
        if self.visceral_grass < 5:
            ev_gv = "Bien"
        elif self.visceral_grass < 9:
            ev_gv = "Medio"
        elif self.visceral_grass < 13:
            ev_gv = "Exceso"
        else:
            ev_gv = "Alarmante"

        return ev_gv

    @classmethod
    def add_patient(cls, patient_obj, waist_measure, grass_percent, bone_mass, muscular_mass, imc,
                    metabolic_age, visceral_grass, water_percent):
        """
        Agrega un nuevo paciente con información adicional de escala.

        Parámetros
        ----------
        patient_obj : Patient
            Objeto paciente existente.
        waist_measure : float
            Medida de la cintura del paciente en centímetros.
        grass_percent : float
            Porcentaje de grasa corporal del paciente.
        bone_mass : float
            Masa ósea del paciente en kilogramos.
        muscular_mass : float
            Masa muscular del paciente en kilogramos.
        imc : float
            Índice de masa corporal (IMC) del paciente.
        metabolic_age : float
            Edad metabólica del paciente.
        visceral_grass : float
            Grasa visceral del paciente.
        water_percent : float
            Porcentaje de agua corporal del paciente.

        Returns
        -------
        ScalePatient
            Nuevo paciente con información adicional de escala.
        """
        name = patient_obj.name
        surname = patient_obj.surname
        age = patient_obj.age
        gender = patient_obj.gender
        height = patient_obj.height
        weight = patient_obj.weight
        activity = patient_obj.activity

        new_patient = cls(name,
                          surname,
                          age,
                          gender,
                          height,
                          weight,
                          activity,
                          waist_measure,
                          grass_percent,
                          bone_mass,
                          muscular_mass,
                          imc,
                          metabolic_age,
                          visceral_grass,
                          water_percent
                          )

        return new_patient


def run_health_checks(patient):
    """
    Ejecuta diversas verificaciones de salud para un paciente y muestra los resultados.

    Parámetros
    ----------
    patient : ScalePatient
        Paciente con información adicional de escala.
    """
    try:
        patient.get_basal_metabolic_rate()
        print("----------------------------------------")
        print(f"Riesgo cardiovascular: {patient.get_cardiovascular_risk()}.")
        print("----------------------------------------")
        print(f"Complexion: {patient.get_complexion()}")
        print("----------------------------------------")
        print(f"IMC: {patient.get_imc_standard()}.")
        print("----------------------------------------")
        print(f"Porcentaje graso: {patient.get_grass_percent()}.")
        print("----------------------------------------")
        print(f"Niveles de agua corporal: {patient.get_w_level()}.")
        print("----------------------------------------")
        print(f"Indice de masa muscular: {patient.get_im_muscular()}.")
        print("----------------------------------------")
        print(f"Grasa visceral: {patient.get_ev_gv()}.")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

paciente1_bascula = ScalePatient.add_patient(
    paciente1, 142, 35.2, 2.4, 38, 29.5, 52, 12, 42
)

# quitar el comentario '#' para obtener una demostración del codigo:
# run_health_checks(paciente1_bascula)
