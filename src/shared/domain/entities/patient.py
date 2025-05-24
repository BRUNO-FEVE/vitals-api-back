import uuid
from datetime import datetime

from src.shared.helpers.errors.domain_errors import EntityError


class Patient:
    MIN_NAME_LENGTH = 2

    def __init__(self, cpf: str, name: str, date_of_birth: datetime, patient_id: str = None):
        if patient_id is None:
            self.patient_id = str(uuid.uuid4())
        elif not isinstance(patient_id, str):
            raise EntityError("patient_id")
        else:
            self.patient_id = patient_id

        if not self.validate_cpf(cpf):
            raise EntityError("cpf")
        self.cpf = cpf

        if not self.validate_name(name):
            raise EntityError("name")
        self.name = name

        if not isinstance(date_of_birth, datetime):
            raise EntityError("date_of_birth")
        self.date_of_birth = date_of_birth

    @staticmethod
    def validate_cpf(cpf: str) -> bool:
        if not isinstance(cpf, str):
            return False
        return bool(len(cpf) == 14 and cpf.count(".") == 2 and cpf.count("-") == 1)

    @staticmethod
    def validate_name(name: str) -> bool:
        return isinstance(name, str) and len(name) >= Patient.MIN_NAME_LENGTH

    def __repr__(self):
        return f"Patient(patient_id={self.patient_id}, name={self.name}, cpf={self.cpf}, date_of_birth={self.date_of_birth})"
