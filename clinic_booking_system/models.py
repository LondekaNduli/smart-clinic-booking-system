class Doctor:
    def __init__(self, name, specialty):
        self.name = name
        self.specialty = specialty


class Patient:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Appointment:
    def __init__(self, patient, doctor, date, time, status="Confirmed"):
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.time = time
        self.status = status

    def confirm_booking(self):
        return f"{self.patient} booked Dr {self.doctor} on {self.date} at {self.time}"