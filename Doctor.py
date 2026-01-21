class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    def full_name(self):
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self):
        return self.__first_name

    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def get_surname(self):
        return self.__surname

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def get_speciality(self):
        return self.__speciality

    def set_speciality(self, new_speciality):
        self.__speciality = new_speciality

    def remove_patient(self, patient_name):
        if patient_name in self.__patients:
            self.__patients.remove(patient_name)

    def add_patient(self, patient_name):
        self.__patients.append(patient_name)

    def patients(self):
        return self.__patients

    def add_appointment(self, appointment):
        self.__appointments.append(appointment)

    def appointments(self):
        return self.__appointments

    def __str__(self):
        return f'{self.full_name():^30}|{self.__speciality:^15}'


