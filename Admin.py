from Doctor import Doctor
from Patient import Patient


class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self):
        """
        A method that deals with the login
        Returns:
            bool: True if login is successful, False otherwise
        """
        print("-----Login-----")
        # Get the details of the admin
        username = input('Enter the username: ')
        password = input('Enter the password: ')

        # Check if the username and password match the registered ones
        return username == self.__username and password == self.__password

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        first_name = input("Enter the first name of the doctor: ")
        surname = input("Enter the surname of the doctor: ")
        speciality_of_doctor = input("Enter the speciality of the doctor: ")
        return Doctor(first_name, surname, speciality_of_doctor)

    def doctor_management(self, doctors):
        
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """
     
        print("-----Doctor Management-----")

        # menu
        print('Choose the operation:')
        print(' 1 - Register')
        print(' 2 - View')
        print(' 3 - Update')
        print(' 4 - Delete')

        op = input("Please choose an operation: ")


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            print('Enter the doctor\'s details:')

            new_doctor = self.get_doctor_details()
            first_name = new_doctor.get_first_name()
            surname = new_doctor.get_surname()
       
            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    name_exists = True
                    break # save time and end the loop
               

            # add the doctor ...
                                                         # ... to the list of doctors
            if name_exists == False:
                doctors.append(new_doctor)
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Enter the ID of the doctor: ')) - 1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index != False:
                        
                        break
                        
                    else:
                        print("Doctor not found")

                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            op = int(input('Input: '))   # make the user input lowercase

            if op == 1:
                first_name = input("Enter new first name: ")
                doctors[index].set_first_name(first_name)
            elif op == 2:
                surname = input("Enter new surname: ")
                doctors[index].set_surname(surname)
            elif op == 3:
                speciality = input("Enter new speciality: ")
                doctors[index].set_speciality(speciality)
            else: 
                print("Invalid choice. Please try again.")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)
    
            doctor_index = input('Enter the ID of the doctor to be deleted: ')
            doctor_index_int = int(doctor_index) - 1
            if doctor_index_int in range(len(doctors)):
                del doctors[doctor_index_int]

            else:
                print('The id entered is incorrect')

        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')


    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) - 1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:
                    
                # link the patients to the doctor and vice versa
                months = ["January", "February", "March", "April", "May", "June","July", "August", "September", "October", "November", "December"]


                if patients[patient_index].get_doctor() != 'None':
                    print('The doctor is already assigned to this patient')
                else:
                    for index, month in enumerate(months):
                        print(f"{index+1}. {month}") 
                    month = int(input("Enter the month for appointment: ")) - 1
                    doctors[doctor_index].add_appointment(f"{patients[patient_index].full_name()} - {months[month]}")
                    patients[patient_index].link(doctors[doctor_index].full_name())
                    doctors[doctor_index].add_patient(patients[patient_index].full_name())
                    print('The patient is now assign to the doctor.')

                

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients, patient_id):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
            patient_id (int): the ID of the patient to be discharged
        """
        print("-----Discharge Patient-----")

        patient_index = patient_id
        patient_index_check = self.find_index(patient_index, patients)
        if patient_index_check != False:
            discharge_patients.append(patients[patient_index])
            del patients[patient_index]
            print("Patient discharged successfully")
        else:
            print("Patient not found")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharge_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(discharged_patients)

    def update_details_terminal(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            #ToDo14 
            username = input("Enter your New Username: ")
            self.__username = username
            print(f"Your Username has been changed to {self.__username}")

        elif op == 2:
            password = input('Enter the new password: ')
            # validate the password
            if password == input('Enter the new password again: '):
                self.__password = password
                print("Your Password has been changed")
                return True

        elif op == 3:
            address = input('Enter the new address: ')
            self.__address = address
            print(f"Your address has been changed to {self.__address}")

        else:
            print("Please enter the valid feild to be updated!")
        

    def update_details(self):
        """
        Allows the user to update and change username, password, and address
        Returns:
            bool: True if password is changed, False otherwise
        """
        print('Choose the field to be updated:')
        print(' 1 Username')
        print(' 2 Password')
        print(' 3 Address')
        op = int(input('Input: '))

        if op == 1:
            self.update_username()
        elif op == 2:
            return self.update_password()
        elif op == 3:
            self.update_address()
        else:
            print("Please enter a valid field to be updated!")
        
        return False

    def view_symptoms(self,patient):
        """
        Prints the list of all symptoms
        """
        self.view_patient(patient)
        op = int(input(' Please select the ID of the patient you want to view the symptoms of: ')) - 1
        try:
            print()
            print("-----Symptoms-----")
            if op in range(len(patient)):
                patient[op].print_symptoms()
            print()
        except:
            print("Invalid choice")


    def add_patient(self,patient):
        """
        Adds a new patient to the system
        """
        first_name = input("Enter Patient first name: ")
        last_name = input("Enter Patient last name: ")
        age = int(input("Enter Patient age: "))
        mobile = input("Enter Patient mobile number: ")
        address = input("Enter Patient address: ")
        symptoms = []
        while True:
            symptom = input("Enter symptoms one by one (press q or Q when you're done!): ")
            if symptom == "q" or symptom == "Q":
                break
            symptoms.append(symptom)
            print(symptoms)

        return Patient(first_name,last_name,age,mobile,address,symptoms)
    
    def view_grouped_patient(self,patient , grouped_patients):
        """
        Prints the grouped patients by surname
        """

     
        # Step 1: Sort patients by surname
        patients_sorted = sorted(patient, key=lambda p: p.get_surname())
        

        # Step 2: Print grouped patients
        current_surname = None

        for p in patients_sorted:
            if p.get_surname() != current_surname: 
                print(f"\n--- Family: {p.get_surname()} ---")  
                current_surname = p.get_surname()

            print(p)  
            grouped_patients.append(p)

        

    
    def patient_management(self, patient,  grouped_patients):
        """
        This function is used to manage the patient data
        """
        info = """
        1- add patient
        2- view patient 
        3- view symptoms
        4- view grouped patients

        """
        print(info)
        try:
            op = int(input("Please select operation: "))

            if op == 1:
                patient.append(self.add_patient(patient))

            elif op == 2:
                self.view_patient(patient)

            elif op == 3:
                self.view_symptoms(patient)

            elif op == 4:
                self.view_grouped_patient(patient , grouped_patients)
                # self.view(grouped_patient_by_surname)

            else:
                print("Invalid choice")

        except ValueError:
            print("Please choose Numeric value only")




    def save_data(self,patient, discharged_patients):
        """
        This function is used to save the patient data to a file
        """
        with open('patient_data.yml', 'w') as f:
            for p in patient:
                f.write(f"Name: {p.full_name()}\n")
                f.write(f"Age: {p.get_age()}\n")
                f.write(f"Mobile No: {p.get_mobile()}\n")
                f.write(f"Address: {p.get_postcode()}\n")
                f.write(f"Symptoms: {p.write_symptoms()}\n")
                f.write(f"Is_Discharged: NO\n")
                f.write("\n")

            for d in discharged_patients:
                f.write(f"Name: {d.full_name()}\n")
                f.write(f"Age: {d.get_age()}\n")
                f.write(f"Mobile No: {p.get_mobile()}\n")
                f.write(f"Address: {p.get_postcode()}\n")
                f.write(f"Symptoms: {d.print_symptoms()}\n")
                f.write(f"Is_Discharged: YES\n")
                f.write("\n")
            


    def reallocation(self, patients, doctors):
        """
        This function is used to reallocate the patient to a doctor
        """
        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode ')
        self.view(patients)

        patient_index = input('Please enter the patient ID you want to reallocate: ')

        try:
            patient_index = int(patient_index) -1

            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return 

        except ValueError:
            print('The id entered is incorrect')
            return 

        print("-----Doctors Select-----")
        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            doctor_index = int(doctor_index) - 1

            if self.find_index(doctor_index,doctors)!=False:
                    
                patients[patient_index].link(doctors[doctor_index].full_name())
                doctors[doctor_index].add_patient(patients[patient_index])
                
                print('The patient is now reallocated to new doctor.')

            else:
                print('The id entered was not found.')

        except ValueError: 
            print('The id entered is incorrect')


    
    def load_data(self):
        """
        This function is used to load the patient data from a file and display it in the terminal
        """
        try:
            with open('patient_data.yml', 'r') as f:
                print("-----Loaded Patient Data-----")
                patient_data = {}
                for line in f:
                    if line.strip() == "":
                        if patient_data:
                            print(f"Name: {patient_data.get('Name', 'N/A')}")
                            print(f"Age: {patient_data.get('Age', 'N/A')}")
                            print(f"Mobile No: {patient_data.get('Mobile No', 'N/A')}")
                            print(f"Address: {patient_data.get('Address', 'N/A')}")
                            print(f"Symptoms: {patient_data.get('Symptoms', 'N/A')}")
                            print(f"Is_Discharged: {patient_data.get('Is_Discharged', 'N/A')}")
                            print("\n")
                            patient_data = {}
                    else:
                        key, value = line.strip().split(": ", 1)
                        if key == "Symptoms":
                            patient_data[key] = value.split(", ")
                        else:
                            patient_data[key] = value
                if patient_data:
                    print(f"Name: {patient_data.get('Name', 'N/A')}")
                    print(f"Age: {patient_data.get('Age', 'N/A')}")
                    print(f"Mobile No: {patient_data.get('Mobile No', 'N/A')}")
                    print(f"Address: {patient_data.get('Address', 'N/A')}")
                    print(f"Symptoms: {patient_data.get('Symptoms', 'N/A')}")
                    print(f"Is_Discharged: {patient_data.get('Is_Discharged', 'N/A')}")
                    print("\n")
        except FileNotFoundError:
            print("The file patient_data.yml does not exist.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def count_patients_by_illness(self, patients):
        """
        Count the number of patients based on illness type.
        Args:
            patients (list<Patient>): list of all the active patients
        Returns:
            dict: a dictionary with illness type as keys and count as values
        """
        illness_count = {}
        for patient in patients:
            for symptom in patient.get_symptoms():
                if symptom in illness_count:
                    illness_count[symptom] += 1
                else:
                    illness_count[symptom] = 1
        return illness_count

    def appointments_per_month(self, doctor):
        """
        Organize appointments per month for a given doctor.
        Args:
            doctor (Doctor): the doctor object
        Returns:
            dict: a dictionary with months as keys and list of appointments as values
        """
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        appointments_by_month = {month: [] for month in months}
        for appointment in doctor.appointments():
            patient_name, month = appointment.split(" - ")
            appointments_by_month[month].append(patient_name)
        return appointments_by_month

    def management_report(self, doctors, patients):
        """
        This function is used to generate a report of the system's management
        """
        print('Management Report')
        print('==================================================')
        print(f'Number of doctors: {len(doctors)}')
        print('--------------------------------------------------')
        for doctor in doctors:
            print(f'Doctor: {doctor.full_name()}')
            print(f'Speciality: {doctor.get_speciality()}')
            print(f'Number of Patients: {len(doctor.patients())}')
            print('--------------------------------------------------')
        print('==================================================')
        print('Appointment Report')
        print('==================================================')
        for doctor in doctors:
            print(f'Doctor: {doctor.full_name()}')
            appointments_by_month = self.appointments_per_month(doctor)
            for month, appointments in appointments_by_month.items():
                if appointments:
                    print(f'{month}:')
                    for count, patient in enumerate(appointments, start=1):
                        print(f'  {count}. {patient}')
            print('--------------------------------------------------')
        print('==================================================')
        print('Patient Report')
        print('==================================================')
        illness_count = self.count_patients_by_illness(patients)
        for illness, count in illness_count.items():
            print(f'Illness: {illness}, Number of Patients: {count}')
        print('==================================================')

    def set_appointment(self, doctor, patient, month):
        """
        Set an appointment for a patient with a doctor in a specific month.
        Args:
            doctor (Doctor): the doctor object
            patient (Patient): the patient object
            month (int): the month number (1-12)
        """
        months = ["January", "February", "March", "April", "May", "June",
                  "July", "August", "September", "October", "November", "December"]
        if 1 <= len(month) <= 12:
            month_name = months[len(month) - 1]
            appointment = f"{patient.full_name()} - {month_name}"
            doctor.add_appointment(appointment)
            print(f"Appointment set for {patient.full_name()} with Dr. {doctor.full_name()} in {month_name}")
        else:
            print("Invalid month. Please enter a number between 1 and 12.")

    def show_graphs(self, doctors, patients, graph_type):
        """
        This function is used to show the graphs of the system's management
        """
        import matplotlib.pyplot as plt

        if graph_type == 'a':
            # Total number of doctors in the system
            plt.figure(figsize=(6, 4))
            plt.bar(['Doctors'], [len(doctors)], color='blue')
            plt.title('Total Number of Doctors')
            plt.ylabel('Count')
            plt.show()

        elif graph_type == 'b':
            # Total number of patients per doctor
            doctor_names = [doctor.full_name() for doctor in doctors]
            patient_counts = [len(doctor.patients()) for doctor in doctors]
            plt.figure(figsize=(10, 6))
            plt.bar(doctor_names, patient_counts, color='green')
            plt.title('Total Number of Patients per Doctor')
            plt.xlabel('Doctors')
            plt.ylabel('Number of Patients')
            plt.xticks(rotation=45)
            plt.show()

        elif graph_type == 'c':
            # Total number of appointments per month per doctor
            months = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
            for doctor in doctors:
                appointments_by_month = self.appointments_per_month(doctor)
                month_counts = [len(appointments_by_month[month]) for month in months]
                plt.figure(figsize=(12, 6))
                plt.bar(months, month_counts, color='purple')
                plt.title(f'Total Number of Appointments per Month for Dr. {doctor.full_name()}')
                plt.xlabel('Months')
                plt.ylabel('Number of Appointments')
                plt.xticks(rotation=45)
                plt.show()

        elif graph_type == 'd':
            # Total number of patients based on the illness type
            illness_count = self.count_patients_by_illness(patients)
            illnesses = list(illness_count.keys())
            counts = list(illness_count.values())
            plt.figure(figsize=(12, 6))
            plt.bar(illnesses, counts, color='red')
            plt.title('Total Number of Patients Based on Illness Type')
            plt.xlabel('Illness Type')
            plt.ylabel('Number of Patients')
            plt.xticks(rotation=45)
            plt.show()

        else:
            print("Invalid option selected.")

   



    def update_username(self, new_username):
        """
        Update the admin's username
        """
        self.__username = new_username
        print(f"Your Username has been changed to {self.__username}")

    def update_password(self, new_password):
        """
        Update the admin's password and logout
        """
        self.__password = new_password
        print("Your Password has been changed. You need to log in again.")
        return True

    def update_address(self, new_address):
        """
        Update the admin's address
        """
        self.__address = new_address
        print(f"Your address has been changed to {self.__address}")



    def show_graphs_terminal(self, doctors, patients):
        """
        This function is used to show the graphs of the system's management
        """
        import matplotlib.pyplot as plt

        print("a- Total number of doctors in the system")
        print("b- Total number of patients per doctor")
        print("c- Total number of appointments per month per doctor")
        print("d- Total number of patients based on the illness type")
        op = input("Please select the operation: ")

        if op == 'a':
            # Total number of doctors in the system
            plt.figure(figsize=(6, 4))
            plt.bar(['Doctors'], [len(doctors)], color='blue')
            plt.title('Total Number of Doctors')
            plt.ylabel('Count')
            plt.show()

        elif op == 'b':
            # Total number of patients per doctor
            doctor_names = [doctor.full_name() for doctor in doctors]
            patient_counts = [len(doctor.patients()) for doctor in doctors]
            plt.figure(figsize=(10, 6))
            plt.bar(doctor_names, patient_counts, color='green')
            plt.title('Total Number of Patients per Doctor')
            plt.xlabel('Doctors')
            plt.ylabel('Number of Patients')
            plt.xticks(rotation=45)
            plt.show()

        elif op == 'c':
            # Total number of appointments per month per doctor
            months = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
            for doctor in doctors:
                appointments_by_month = self.appointments_per_month(doctor)
                month_counts = [len(appointments_by_month[month]) for month in months]
                plt.figure(figsize=(12, 6))
                plt.bar(months, month_counts, color='purple')
                plt.title(f'Total Number of Appointments per Month for Dr. {doctor.full_name()}')
                plt.xlabel('Months')
                plt.ylabel('Number of Appointments')
                plt.xticks(rotation=45)
                plt.show()

        elif op == 'd':
            # Total number of patients based on the illness type
            illness_count = self.count_patients_by_illness(patients)
            illnesses = list(illness_count.keys())
            counts = list(illness_count.values())
            plt.figure(figsize=(12, 6))
            plt.bar(illnesses, counts, color='red')
            plt.title('Total Number of Patients Based on Illness Type')
            plt.xlabel('Illness Type')
            plt.ylabel('Number of Patients')
            plt.xticks(rotation=45)
            plt.show()

        else:
            print("Invalid option selected.")
