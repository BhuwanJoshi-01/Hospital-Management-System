import tkinter as tk
from tkinter import ttk, messagebox
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

class HospitalManagementSystem:
    def __init__(self, root, main_loop, admin):
        self.root = root
        self.main_loop = main_loop
        self.admin = admin
        self.root.title("Hospital Management System")
        self.root.geometry("800x600")

        self.doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'), Doctor('Jone', 'Carlos', 'Cardiology')]
        self.patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['Symptom1', 'Symptom2', 'Symptom3']), Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['Symptom1', 'Symptom2', 'Symptom3']), Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['Symptom1', 'Symptom2', 'Symptom3'])]

        self.discharge_patients = []

        self.create_widgets()

    def create_widgets(self):
        # Navigation panel
        nav_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        nav_frame.pack(side=tk.LEFT, fill=tk.Y)

        tk.Button(nav_frame, text="Doctor Management", command=self.doctor_management).pack(fill=tk.X)
        tk.Button(nav_frame, text="Patient Management", command=self.patient_management).pack(fill=tk.X)
        tk.Button(nav_frame, text="Discharge Patient", command=self.discharge_patient).pack(fill=tk.X)
        tk.Button(nav_frame, text="View Discharged Patients", command=self.view_discharged_patients).pack(fill=tk.X)
        tk.Button(nav_frame, text="Assign Doctor", command=self.assign_doctor).pack(fill=tk.X)
        tk.Button(nav_frame, text="Reallocate Patient", command=self.reallocate_patient).pack(fill=tk.X)
        tk.Button(nav_frame, text="Save Data", command=self.save_data).pack(fill=tk.X)
        tk.Button(nav_frame, text="Load Data", command=self.load_data).pack(fill=tk.X)
        tk.Button(nav_frame, text="Management Report", command=self.management_report).pack(fill=tk.X)
        tk.Button(nav_frame, text="Show Graphs", command=self.show_graphs).pack(fill=tk.X)
        tk.Button(nav_frame, text="Update Admin Details", command=self.update_admin_details).pack(fill=tk.X)
        tk.Button(nav_frame, text="Quit", command=self.quit_application).pack(fill=tk.X)

        # Main working area
        self.main_frame = tk.Frame(self.root, bd=2, relief=tk.RIDGE)
        self.main_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Welcome to Hospital Management System")
        status_bar = tk.Label(self.root, textvariable=self.status_var, bd=1, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)

    def doctor_management(self):
        self.clear_main_frame()
        # Create GUI components for doctor management
        tk.Label(self.main_frame, text="Doctor Management", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Register Doctor", command=self.register_doctor).pack(pady=5)
        tk.Button(self.main_frame, text="View Doctors", command=self.view_doctors).pack(pady=5)
        tk.Button(self.main_frame, text="Update Doctor", command=self.update_doctor).pack(pady=5)
        tk.Button(self.main_frame, text="Delete Doctor", command=self.delete_doctor).pack(pady=5)

    def patient_management(self):
        self.clear_main_frame()
        # Create GUI components for patient management
        tk.Label(self.main_frame, text="Patient Management", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Add Patient", command=self.add_patient).pack(pady=5)
        tk.Button(self.main_frame, text="View Patients", command=self.view_patients).pack(pady=5)
        tk.Button(self.main_frame, text="View Symptoms", command=self.view_symptoms).pack(pady=5)
        tk.Button(self.main_frame, text="View Grouped Patients", command=self.view_grouped_patients).pack(pady=5)

    def discharge_patient(self):
        self.clear_main_frame()
        # Step 1: Display the patient list
        tk.Label(self.main_frame, text="Discharge Patient", font=("Arial", 16)).pack(pady=10)
        self.view_patients()
        tk.Label(self.main_frame, text="Patient ID").pack(pady=5)
        patient_id_entry = tk.Entry(self.main_frame)
        patient_id_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Discharge", command=lambda: self.discharge(patient_id_entry.get())).pack(pady=10)

    def view_discharged_patients(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="View Discharged Patients", font=("Arial", 16)).pack(pady=10)
        tree = ttk.Treeview(self.main_frame, columns=("ID", "Full Name", "Doctor", "Age", "Mobile", "Postcode", "Symptoms"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Full Name", text="Full Name")
        tree.heading("Doctor", text="Doctor")
        tree.heading("Age", text="Age")
        tree.heading("Mobile", text="Mobile")
        tree.heading("Postcode", text="Postcode")
        tree.heading("Symptoms", text="Symptoms")
        for idx, patient in enumerate(self.discharge_patients, start=1):
            symptoms = patient.get_symptoms()
            symptoms_display = f"{symptoms[0]}..." if symptoms else ""
            tree.insert("", "end", values=(idx, patient.full_name(), patient.get_doctor(), patient.get_age(), patient.get_mobile(), patient.get_postcode(), symptoms_display))
        tree.pack(fill=tk.BOTH, expand=True)

    def assign_doctor(self):
        self.clear_main_frame()
        # Step 1: Display the patient list
        tk.Label(self.main_frame, text="Assign Doctor", font=("Arial", 16)).pack(pady=10)
        self.view_patients()
        tk.Label(self.main_frame, text="Patient ID").pack(pady=5)
        patient_id_entry = tk.Entry(self.main_frame)
        patient_id_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Next", command=lambda: self.show_patient_symptoms(patient_id_entry.get())).pack(pady=10)

    def show_patient_symptoms(self, patient_id):
        try:
            patient_id = int(patient_id) - 1
            if patient_id not in range(len(self.patients)):
                messagebox.showerror("Error", "Invalid Patient ID")
                return
            self.clear_main_frame()
            tk.Label(self.main_frame, text="Patient Symptoms", font=("Arial", 16)).pack(pady=10)
            symptoms = self.patients[patient_id].get_symptoms()
            tk.Label(self.main_frame, text="\n".join(symptoms)).pack(pady=10)
            tk.Button(self.main_frame, text="OK", command=lambda: self.show_doctor_list(patient_id)).pack(pady=10)
        except ValueError:
            messagebox.showerror("Error", "Invalid Patient ID")

    def show_doctor_list(self, patient_id):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Assign Doctor", font=("Arial", 16)).pack(pady=10)
        self.view_doctors()
        tk.Label(self.main_frame, text="Doctor ID").pack(pady=5)
        doctor_id_entry = tk.Entry(self.main_frame)
        doctor_id_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Next", command=lambda: self.show_appointment_months(patient_id, doctor_id_entry.get())).pack(pady=10)

    def show_appointment_months(self, patient_id, doctor_id):
        try:
            doctor_id = int(doctor_id) - 1
            if doctor_id not in range(len(self.doctors)):
                messagebox.showerror("Error", "Invalid Doctor ID")
                return
            self.clear_main_frame()
            tk.Label(self.main_frame, text="Select Appointment Month", font=("Arial", 16)).pack(pady=10)
            months = ["January", "February", "March", "April", "May", "June",
                      "July", "August", "September", "October", "November", "December"]
            for idx, month in enumerate(months, start=1):
                tk.Label(self.main_frame, text=f"{idx}. {month}").pack()
            tk.Label(self.main_frame, text="Month Number").pack(pady=5)
            month_entry = tk.Entry(self.main_frame)
            month_entry.pack(pady=5)
            tk.Button(self.main_frame, text="Assign", command=lambda: self.assign(patient_id, doctor_id, month_entry.get())).pack(pady=10)
        except ValueError:
            messagebox.showerror("Error", "Invalid Doctor ID")

    def save_data(self):
        self.admin.save_data(self.patients, self.discharge_patients)

    def load_data(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Loaded Patient Data", font=("Arial", 16)).pack(pady=10)
        tree = ttk.Treeview(self.main_frame, columns=("Name", "Age", "Mobile No", "Address", "Symptoms", "Is_Discharged"), show='headings')
        tree.heading("Name", text="Name")
        tree.heading("Age", text="Age")
        tree.heading("Mobile No", text="Mobile No")
        tree.heading("Address", text="Address")
        tree.heading("Symptoms", text="Symptoms")
        tree.heading("Is_Discharged", text="Is_Discharged")
        try:
            with open('patient_data.yml', 'r') as f:
                patient_data = {}
                for line in f:
                    if line.strip() == "":
                        if patient_data:
                            tree.insert("", "end", values=(patient_data.get('Name', 'N/A'), patient_data.get('Age', 'N/A'), patient_data.get('Mobile No', 'N/A'), patient_data.get('Address', 'N/A'), patient_data.get('Symptoms', 'N/A'), patient_data.get('Is_Discharged', 'N/A')))
                            patient_data = {}
                    else:
                        key, value = line.strip().split(": ", 1)
                        if key == "Symptoms":
                            patient_data[key] = value.split(", ")
                        else:
                            patient_data[key] = value
                if patient_data:
                    tree.insert("", "end", values=(patient_data.get('Name', 'N/A'), patient_data.get('Age', 'N/A'), patient_data.get('Mobile No', 'N/A'), patient_data.get('Address', 'N/A'), patient_data.get('Symptoms', 'N/A'), patient_data.get('Is_Discharged', 'N/A')))
            tree.pack(fill=tk.BOTH, expand=True)
        except FileNotFoundError:
            messagebox.showerror("Error", "The file patient_data.yml does not exist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def management_report(self):
        self.clear_main_frame()
        report_text = tk.Text(self.main_frame)
        report_text.pack(fill=tk.BOTH, expand=True)
        report_text.insert(tk.END, 'Management Report\n')
        report_text.insert(tk.END, '==================================================\n')
        report_text.insert(tk.END, f'Number of doctors: {len(self.doctors)}\n')
        report_text.insert(tk.END, '--------------------------------------------------\n')
        for doctor in self.doctors:
            report_text.insert(tk.END, f'Doctor: {doctor.full_name()}\n')
            report_text.insert(tk.END, f'Speciality: {doctor.get_speciality()}\n')
            report_text.insert(tk.END, f'Number of Patients: {len(doctor.patients())}\n')
            report_text.insert(tk.END, '--------------------------------------------------\n')
        report_text.insert(tk.END, '==================================================\n')
        report_text.insert(tk.END, 'Appointment Report\n')
        report_text.insert(tk.END, '==================================================\n')
        for doctor in self.doctors:
            report_text.insert(tk.END, f'Doctor: {doctor.full_name()}\n')
            appointments_by_month = self.admin.appointments_per_month(doctor)
            for month, appointments in appointments_by_month.items():
                if appointments:
                    report_text.insert(tk.END, f'{month}:\n')
                    for count, patient in enumerate(appointments, start=1):
                        report_text.insert(tk.END, f'  {count}. {patient}\n')
            report_text.insert(tk.END, '--------------------------------------------------\n')
        report_text.insert(tk.END, '==================================================\n')
        report_text.insert(tk.END, 'Patient Report\n')
        report_text.insert(tk.END, '==================================================\n')
        illness_count = self.admin.count_patients_by_illness(self.patients)
        for illness, count in illness_count.items():
            report_text.insert(tk.END, f'Illness: {illness}, Number of Patients: {count}\n')
        report_text.insert(tk.END, '==================================================\n')
        print(report_text.get("1.0", tk.END))

    def show_graphs(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Show Graphs", font=("Arial", 16)).pack(pady=10)
        tk.Button(self.main_frame, text="Total number of doctors in the system", command=lambda: self.admin.show_graphs(self.doctors, self.patients, 'a')).pack(pady=5)
        tk.Button(self.main_frame, text="Total number of patients per doctor", command=lambda: self.admin.show_graphs(self.doctors, self.patients, 'b')).pack(pady=5)
        tk.Button(self.main_frame, text="Total number of appointments per month per doctor", command=lambda: self.admin.show_graphs(self.doctors, self.patients, 'c')).pack(pady=5)
        tk.Button(self.main_frame, text="Total number of patients based on the illness type", command=lambda: self.admin.show_graphs(self.doctors, self.patients, 'd')).pack(pady=5)

    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    def register_doctor(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Register Doctor", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="First Name").pack(pady=5)
        first_name_entry = tk.Entry(self.main_frame)
        first_name_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Surname").pack(pady=5)
        surname_entry = tk.Entry(self.main_frame)
        surname_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Speciality").pack(pady=5)
        speciality_entry = tk.Entry(self.main_frame)
        speciality_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Register", command=lambda: self.add_doctor(first_name_entry.get(), surname_entry.get(), speciality_entry.get())).pack(pady=10)

    def add_doctor(self, first_name, surname, speciality):
        new_doctor = Doctor(first_name, surname, speciality)
        self.doctors.append(new_doctor)
        messagebox.showinfo("Success", "Doctor registered successfully")

    def view_doctors(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="View Doctors", font=("Arial", 16)).pack(pady=10)
        tree = ttk.Treeview(self.main_frame, columns=("ID", "Full Name", "Speciality"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Full Name", text="Full Name")
        tree.heading("Speciality", text="Speciality")
        for idx, doctor in enumerate(self.doctors, start=1):
            tree.insert("", "end", values=(idx, doctor.full_name(), doctor.get_speciality()))
        tree.pack(fill=tk.BOTH, expand=True)

    def update_doctor(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Update Doctor", font=("Arial", 16)).pack(pady=10)
        self.view_doctors()
        tk.Label(self.main_frame, text="Doctor ID").pack(pady=5)
        doctor_id_entry = tk.Entry(self.main_frame)
        doctor_id_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Field to Update").pack(pady=5)
        field_combobox = ttk.Combobox(self.main_frame, values=["First Name", "Surname", "Speciality"])
        field_combobox.pack(pady=5)
        tk.Label(self.main_frame, text="New Value").pack(pady=5)
        new_value_entry = tk.Entry(self.main_frame)
        new_value_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Update", command=lambda: self.update_doctor_details(doctor_id_entry.get(), field_combobox.get(), new_value_entry.get())).pack(pady=10)

    def update_doctor_details(self, doctor_id, field, new_value):
        try:
            doctor_id = int(doctor_id) - 1
            if doctor_id in range(len(self.doctors)):
                if field.lower() == "first name":
                    self.doctors[doctor_id].set_first_name(new_value)
                elif field.lower() == "surname":
                    self.doctors[doctor_id].set_surname(new_value)
                elif field.lower() == "speciality":
                    self.doctors[doctor_id].set_speciality(new_value)
                else:
                    messagebox.showerror("Error", "Invalid field")
                    return
                messagebox.showinfo("Success", "Doctor details updated successfully")
            else:
                messagebox.showerror("Error", "Doctor ID not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid Doctor ID")

    def delete_doctor(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Delete Doctor", font=("Arial", 16)).pack(pady=10)
        self.view_doctors()
        tk.Label(self.main_frame, text="Doctor ID").pack(pady=5)
        doctor_id_entry = tk.Entry(self.main_frame)
        doctor_id_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Delete", command=lambda: self.remove_doctor(doctor_id_entry.get())).pack(pady=10)

    def remove_doctor(self, doctor_id):
        try:
            doctor_id = int(doctor_id) - 1
            if doctor_id in range(len(self.doctors)):
                del self.doctors[doctor_id]
                messagebox.showinfo("Success", "Doctor deleted successfully")
            else:
                messagebox.showerror("Error", "Doctor ID not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid Doctor ID")

    def add_patient(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Add Patient", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="First Name").pack(pady=5)
        first_name_entry = tk.Entry(self.main_frame)
        first_name_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Surname").pack(pady=5)
        surname_entry = tk.Entry(self.main_frame)
        surname_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Age").pack(pady=5)
        age_entry = tk.Entry(self.main_frame)
        age_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Mobile").pack(pady=5)
        mobile_entry = tk.Entry(self.main_frame)
        mobile_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Postcode").pack(pady=5)
        postcode_entry = tk.Entry(self.main_frame)
        postcode_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Symptoms").pack(pady=5)
        symptoms_entry = tk.Entry(self.main_frame)
        symptoms_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Add", command=lambda: self.add_new_patient(first_name_entry.get(), surname_entry.get(), age_entry.get(), mobile_entry.get(), postcode_entry.get(), symptoms_entry.get())).pack(pady=10)

    def add_new_patient(self, first_name, surname, age, mobile, postcode, symptoms):
        new_patient = Patient(first_name, surname, int(age), mobile, postcode, symptoms.split(','))
        self.patients.append(new_patient)
        messagebox.showinfo("Success", "Patient added successfully")

    def view_patients(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="View Patients", font=("Arial", 16)).pack(pady=10)
        tree = ttk.Treeview(self.main_frame, columns=("ID", "Full Name", "Doctor", "Age", "Mobile", "Postcode", "Symptoms"), show='headings')
        tree.heading("ID", text="ID")
        tree.heading("Full Name", text="Full Name")
        tree.heading("Doctor", text="Doctor")
        tree.heading("Age", text="Age")
        tree.heading("Mobile", text="Mobile")
        tree.heading("Postcode", text="Postcode")
        tree.heading("Symptoms", text="Symptoms")
        for idx, patient in enumerate(self.patients, start=1):
            symptoms = patient.get_symptoms()
            symptoms_display = f"{symptoms[0]}..." if symptoms else ""
            tree.insert("", "end", values=(idx, patient.full_name(), patient.get_doctor(), patient.get_age(), patient.get_mobile(), patient.get_postcode(), symptoms_display))
        tree.pack(fill=tk.BOTH, expand=True)

    def view_symptoms(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="View Symptoms", font=("Arial", 16)).pack(pady=10)
        self.view_patients()
        tk.Label(self.main_frame, text="Patient ID").pack(pady=5)
        patient_id_entry = tk.Entry(self.main_frame)
        patient_id_entry.pack(pady=5)
        tk.Button(self.main_frame, text="View", command=lambda: self.show_symptoms(patient_id_entry.get())).pack(pady=10)

    def show_symptoms(self, patient_id):
        try:
            patient_id = int(patient_id) - 1
            if patient_id in range(len(self.patients)):
                symptoms = self.patients[patient_id].get_symptoms()
                messagebox.showinfo("Symptoms", "\n".join(symptoms))
            else:
                messagebox.showerror("Error", "Patient ID not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid Patient ID")

    def view_grouped_patients(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="View Grouped Patients", font=("Arial", 16)).pack(pady=10)
        text_widget = tk.Text(self.main_frame)
        text_widget.pack(fill=tk.BOTH, expand=True)
        grouped_patients = {}
        for patient in self.patients:
            surname = patient.get_surname()
            if surname not in grouped_patients:
                grouped_patients[surname] = []
            grouped_patients[surname].append(patient)
        for surname, patients in grouped_patients.items():
            text_widget.insert(tk.END, f"Family Name: {surname}\n")
            for patient in patients:
                text_widget.insert(tk.END, f"  Full Name: {patient.full_name()}\n")
                text_widget.insert(tk.END, f"  Doctor: {patient.get_doctor()}\n")
                text_widget.insert(tk.END, f"  Age: {patient.get_age()}\n")
                text_widget.insert(tk.END, f"  Mobile: {patient.get_mobile()}\n")
                text_widget.insert(tk.END, f"  Postcode: {patient.get_postcode()}\n")
                text_widget.insert(tk.END, "----------------------------------------\n")

    def discharge(self, patient_id):
        try:
            patient_id = int(patient_id) - 1
            if patient_id in range(len(self.patients)):
                self.admin.discharge(self.patients, self.discharge_patients, patient_id)
                messagebox.showinfo("Success", "Patient discharged successfully")
            else:
                messagebox.showerror("Error", "Patient ID not found")
        except ValueError:
            messagebox.showerror("Error", "Invalid Patient ID")

    def assign(self, patient_id, doctor_id, month):
        patient_id1 = int(patient_id)
        doctor_id1 = int(doctor_id) 
        try:
            if patient_id1 in range(len(self.patients)) and doctor_id1 in range(len(self.doctors)):
                self.patients[patient_id1].link(self.doctors[doctor_id1].full_name())
                self.doctors[doctor_id1].add_patient(self.patients[patient_id1].full_name())
                self.admin.set_appointment(self.doctors[doctor_id1], self.patients[patient_id1], month)
                messagebox.showinfo("Success", "Doctor assigned to patient successfully")
            else:
                messagebox.showerror("Error", "Invalid Patient ID or Doctor ID")
        except ValueError:
            messagebox.showerror("Error", "Invalid Patient ID or Doctor ID")

    def reallocate_patient(self):
        self.clear_main_frame()
        # Step 1: Display the patient list
        tk.Label(self.main_frame, text="Reallocate Patient", font=("Arial", 16)).pack(pady=10)
        self.view_patients()
        tk.Label(self.main_frame, text="Patient ID").pack(pady=5)
        patient_id_entry = tk.Entry(self.main_frame)
        patient_id_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Next", command=lambda: self.show_reallocate_doctor_list(patient_id_entry.get())).pack(pady=10)

    def show_reallocate_doctor_list(self, patient_id):
        try:
            patient_id = int(patient_id) - 1
            if patient_id not in range(len(self.patients)):
                messagebox.showerror("Error", "Invalid Patient ID")
                return
            self.clear_main_frame()
            # Step 2: Display the doctor list
            tk.Label(self.main_frame, text="Reallocate Doctor", font=("Arial", 16)).pack(pady=10)
            self.view_doctors()
            tk.Label(self.main_frame, text="New Doctor ID").pack(pady=5)
            doctor_id_entry = tk.Entry(self.main_frame)
            doctor_id_entry.pack(pady=5)
            tk.Button(self.main_frame, text="Reallocate", command=lambda: self.reallocate(patient_id, doctor_id_entry.get())).pack(pady=10)
        except ValueError:
            messagebox.showerror("Error", "Invalid Patient ID")

    def reallocate(self, patient_id, doctor_id):
        patient_id1 = int(patient_id)
        doctor_id1 = int(doctor_id) - 1
        try:
            if patient_id1 in range(len(self.patients)) and doctor_id1 in range(len(self.doctors)):
                old_doctor_name = self.patients[patient_id1].get_doctor()
                self.patients[patient_id1].link(self.doctors[doctor_id1].full_name())
                self.doctors[doctor_id1].add_patient(self.patients[patient_id1].full_name())
                for doctor in self.doctors:
                    if doctor.full_name() == old_doctor_name:
                        doctor.remove_patient(self.patients[patient_id1].full_name())
                        break
                messagebox.showinfo("Success", "Patient reallocated to new doctor successfully")
            else:
                messagebox.showerror("Error", "Invalid Patient ID or Doctor ID")
        except ValueError:
            messagebox.showerror("Error", "Invalid Patient ID or Doctor ID")



    def update_admin_details(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Update Admin Details", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.main_frame, text="Select Option").pack(pady=5)
        options = ["Username", "Password", "Address"]
        self.selected_option = tk.StringVar(value=options[0])
        option_menu = tk.OptionMenu(self.main_frame, self.selected_option, *options)
        option_menu.pack(pady=5)
        
        tk.Button(self.main_frame, text="Proceed", command=self.proceed_update).pack(pady=10)
    
    def proceed_update(self):
        choice = self.selected_option.get()
        if choice == "Username":
            self.update_username()
        elif choice == "Password":
            self.update_password()
        elif choice == "Address":
            self.update_address()
    
    def update_username(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Update Username", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="New Username").pack(pady=5)
        self.username_entry = tk.Entry(self.main_frame)
        self.username_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Update", command=self.submit_username).pack(pady=10)
    
    def submit_username(self):
        new_username = self.username_entry.get()
        self.admin.update_username(new_username)
        messagebox.showinfo("Success", "Username updated successfully")
        self.update_admin_details()
    
    def update_password(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Update Password", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="New Password").pack(pady=5)
        self.password_entry = tk.Entry(self.main_frame, show="*")
        self.password_entry.pack(pady=5)
        tk.Label(self.main_frame, text="Confirm Password").pack(pady=5)
        self.confirm_entry = tk.Entry(self.main_frame, show="*")
        self.confirm_entry.pack(pady=5)
        
        tk.Button(self.main_frame, text="Update", command=self.submit_password).pack(pady=10)
    
    def submit_password(self):
        new_password = self.password_entry.get()
        confirm_password = self.confirm_entry.get()

        if new_password != confirm_password:
            messagebox.showerror("Error", "Passwords do not match")
            return

        if self.admin.update_password(new_password):
            messagebox.showinfo("Success", "Password updated successfully. Please log in again.")
            self.root.destroy()
            self.root.quit()
        else:
            messagebox.showerror("Error", "Failed to update password")
    
    def update_address(self):
        self.clear_main_frame()
        tk.Label(self.main_frame, text="Update Address", font=("Arial", 16)).pack(pady=10)
        tk.Label(self.main_frame, text="New Address").pack(pady=5)
        self.address_entry = tk.Entry(self.main_frame)
        self.address_entry.pack(pady=5)
        tk.Button(self.main_frame, text="Update", command=self.submit_address).pack(pady=10)
    
    def submit_address(self):
        new_address = self.address_entry.get()
        self.admin.update_address(new_address)
        messagebox.showinfo("Success", "Address updated successfully")
        self.update_admin_details()

    def quit_application(self):
        self.main_loop[0] = False
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    main_loop = [True]
    admin = Admin('admin', '123', 'B1 1AB')
    app = HospitalManagementSystem(root, main_loop, admin)
    root.mainloop()
