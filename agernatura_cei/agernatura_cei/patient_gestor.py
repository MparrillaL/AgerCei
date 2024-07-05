import pandas as pd
from patient import ScalePatient

class PatientGestor:
    def __init__(self):
        """
        Initializes a PatientGestor object.

        The PatientGestor manages patient data using a pandas DataFrame.
        """
        self.patients_df = pd.DataFrame(columns=[
            "id", "date", "name", "surname", "age", "gender", "height", "weight", "activity",
            "waist_measure", "grass_percent", "bone_mass", "muscular_mass", "imc",
            "metabolic_age", "visceral_fat", "water_percent"
        ])
        self.next_id = 1

    @property
    def get_dataframe(self):
        """
        Gets the DataFrame containing patient information.

        Returns
        -------
        pd.DataFrame
            DataFrame with patient information.
        """
        return self.patients_df







    def add_patient(self, patient_data):
        """
        Adds a patient to the database.

        Parameters
        ----------
        patient_data : dict
            Patient data.

        Returns
        -------
        None
        """
        same_name_surname = self.patients_df[
            (self.patients_df['name'] == patient_data['name']) &
            (self.patients_df['surname'] == patient_data['surname'])
        ]

        if not same_name_surname.empty:
            existing_id = same_name_surname.iloc[0]['id']
            print(f"New data for user ID: {existing_id}")
            patient_data["id"] = existing_id
        else:
            patient_data["id"] = self.next_id
            self.next_id += 1

        self.patients_df = self.patients_df.append(patient_data, ignore_index=True)


    def remove_patient_by_id(self, patient_id):
        """
        Removes a patient from the database by ID.

        Parameters
        ----------
        patient_id : int
            ID of the patient to remove.

        Returns
        -------
        None
        """
        self.patients_df = self.patients_df[self.patients_df['id'] != patient_id]

    def edit_patient_data(self, patient_id, column_name, new_value):
        """
        Edits a specific data column for a patient.

        Parameters
        ----------
        patient_id : int
            ID of the patient.
        column_name : str
            Name of the column to edit.
        new_value : any
            New value to set for the specified column.

        Returns
        -------
        None
        """
        self.patients_df.loc[self.patients_df['id'] == patient_id, column_name] = new_value


    def create_patient_objects(self):
        """
        Creates patient objects based on the data in the DataFrame.

        Returns
        -------
        dict
            Dictionary of patient objects with names as keys.
        """
        patient_objects = {}
        for index, row in self.patients_df.iterrows():
            patient_data = row.drop(['id', 'date'])
            patient_obj = ScalePatient(**patient_data)

            patient_id = row['id']
            patient_name = f"patient_{patient_id}"

            patient_objects[patient_name] = patient_obj
        return patient_objects