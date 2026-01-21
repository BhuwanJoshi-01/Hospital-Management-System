# Imports
from gui import HospitalManagementSystem
from tkinter import Tk
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def terminal_mode(admin, doctors, patients, grouped_patients, discharged_patients):
    """
    The function to run the terminal mode.
    """
    while True:
        if admin.login():
            running = True
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Choose the operation:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Discharge patients')
        print(' 3- View discharged patient')
        print(' 4- Assign doctor to a patient')
        print(' 5- Update admin details')
        print(" 6- Add patient/view patient/print symptoms/ view grouped patients")
        print(" 7- Store patient data to file")
        print(" 8- Load patient data from file")
        print(" 9- Reallocate patients to another doctor")
        print(" 10- Request Management Report")
        print(" 11- Show graphs")
        print(' 12- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            admin.doctor_management(doctors)
        elif op == '2':
            admin.view_patient(patients)
            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()
                if op == 'yes' or op == 'y':
                    patient_id = int(input('Enter the patient ID to discharge:  ')) - 1
                    admin.discharge(patients, discharged_patients, patient_id)
                elif op == 'no' or op == 'n':
                    break
                else:
                    print('Please answer by yes or no.')
        elif op == '3':
            admin.view_discharge(discharged_patients)
            
        elif op == '4':
            admin.assign_doctor_to_patient(patients, doctors)
        elif op == '5':
            if admin.update_details_terminal() == True:
                admin.login()
        elif op == '6':
            admin.patient_management(patients, grouped_patients)
        elif op == '7':
            admin.save_data(patients, discharged_patients)
        elif op == '8':
            admin.load_data()
        elif op == '9':
            admin.reallocation(patients, doctors)
        elif op == '10':
            admin.management_report(doctors, patients)
        elif op == '11':
            admin.show_graphs_terminal(doctors, patients)
        elif op == '12':
            break
        else:
            print('Invalid option. Try again')

def main():
    """
    The main function to be run when the program starts.
    """
    admin = Admin('admin', '123', 'B1 1AB')
    doctors = [Doctor('John', 'Smith', 'Internal Med.'), Doctor('Jone', 'Smith', 'Pediatrics'), Doctor('Jone', 'Carlos', 'Cardiology')]
    patients = [Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['Symptom1', 'Symptom2', 'Symptom3']),
                Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['Symptom1', 'Symptom2', 'Symptom3']),
                Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['Symptom1', 'Symptom2', 'Symptom3'])]
    grouped_patients = []
    discharged_patients = []

    print("Choose the mode of operation:")
    print("1. GUI")
    print("2. Terminal")
    mode = input("Enter your choice (1 or 2): ")

    if mode == '1':
        main_loop = [True]
        while main_loop[0]:
            if admin.login():
                root = Tk()
                app = HospitalManagementSystem(root, main_loop, admin)
                root.mainloop()
            else:
                print('Incorrect username or password.')
    elif mode == '2':
        terminal_mode(admin, doctors, patients, grouped_patients, discharged_patients)
    else:
        print("Invalid choice. Please restart the program and choose a valid option.")

if __name__ == '__main__':
    main()
