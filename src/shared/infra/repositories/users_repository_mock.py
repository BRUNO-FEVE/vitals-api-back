from typing import List
from datetime import datetime
import uuid

from src.shared.domain.entities.patient import Patient
from src.shared.domain.repositories.users_repository_interface import IUsersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class UsersRepositoryMock(IUsersRepository):
    patients: List[Patient]

    def __init__(self):
        self.patients = [
            Patient(
                patient_id="aa33de2e-d4ae-4aba-b066-a917ccdbfe07",
                cpf="123.456.789-00",
                name="Gabriel Bianconi",
                date_of_birth=datetime(1990, 1, 1)
            ),
            Patient(
                patient_id="a9456609-211b-451b-a88a-84735e0ab0f8",
                cpf="987.654.321-00",
                name="Bruno Fevereiro",
                date_of_birth=datetime(1985, 2, 2)
            ),
            Patient(
                patient_id="785c3612-5f94-472f-9eb4-1c5b21cf37ff",
                cpf="111.222.333-44",
                name="Carlos Alberto",
                date_of_birth=datetime(1970, 3, 3)
            ),
            Patient(
                patient_id="cb848316-ba67-44d6-945b-9a9a016e08c4",
                cpf="555.666.777-88",
                name="Marcio Maciel",
                date_of_birth=datetime(1995, 4, 4)
            )
        ]

    def get_patient(self, patient_id: str) -> Patient:
        for patient in self.patients:
            if patient.patient_id == patient_id:
                return patient
        raise NoItemsFound("patient_id")

    def create_patient(self, new_patient: Patient) -> Patient:
        if new_patient.patient_id is None:
            new_patient.patient_id = str(uuid.uuid4())
        self.patients.append(new_patient)
        return new_patient
