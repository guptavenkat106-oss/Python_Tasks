class Staff:
    def __init__(self, name, staff_id):
        self.name = name
        self.staff_id = staff_id

    def display_info(self):
        print("Name:", self.name)
        print("Staff ID:", self.staff_id)


class Professor(Staff):
    def __init__(self, name, staff_id, subject):
        super().__init__(name, staff_id)
        self.subject = subject

    def display_info(self):
        super().display_info()
        print("Subject:", self.subject)


class LabAssistant(Staff):
    def __init__(self, name, staff_id, lab):
        super().__init__(name, staff_id)
        self.lab = lab

    def display_info(self):
        super().display_info()
        print("Lab:", self.lab)


class Administrator(Staff):
    def __init__(self, name, staff_id, department):
        super().__init__(name, staff_id)
        self.department = department

    def display_info(self):
        super().display_info()
        print("Department:", self.department)


prof = Professor("Rao", 101, "Mathematics")
lab_asst = LabAssistant("Ram", 102, "Physics Lab")
admin = Administrator("Rakesh", 103, "Accounts")

print("Professor Details:")
prof.display_info()

print("\nLab Assistant Details:")
lab_asst.display_info()

print("\nAdministrator Details:")
admin.display_info()
