from datetime import datetime
from src.shared.domain.entities.patient import Patient


class PatientViewmodel:
    patient_id: str
    name: str
    cpf: str
    date_of_birth: datetime
    
    def __init__(self, patient: Patient):
        self.patient_id = patient.patient_id
        self.name = patient.name
        self.cpf = patient.cpf
        self.date_of_birth = patient.date_of_birth
        
    def to_dict(self) -> dict:
        return {
            "patient_id": self.patient_id,
            "name": self.name,
            "cpf": self.cpf,
            "date_of_birth": self.date_of_birth.isoformat() if isinstance(self.date_of_birth, datetime) else self.date_of_birth
        }
        
class CreatePatientViewmodel:
    def __init__(self, patient: Patient):
        self.patient = patient
        
    def to_dict(self) -> dict:
        return {
            'patient': PatientViewmodel(self.patient).to_dict(),
            'message': 'Patient created successfully'
        }
