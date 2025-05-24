import abc
import re
from datetime import datetime
from src.shared.helpers.errors.domain_errors import EntityError


class Patient(abc.ABC):
    patient_id: str
    cpf: str
    name: str
    date_of_birth: datetime

    MIN_NAME_LENGTH = 2
    CPF_REGEX = r"^\d{3}\.\d{3}\.\d{3}-\d{2}$"

    def __init__(self, patient_id: str, cpf: str, name: str, date_of_birth: datetime):
        if not Patient.validate_patient_id(patient_id):
            raise EntityError("patient_id")
        self.patient_id = patient_id

        if not Patient.validate_cpf(cpf):
            raise EntityError("cpf")
        self.cpf = cpf

        if not Patient.validate_name(name):
            raise EntityError("name")
        self.name = name

        if not Patient.validate_date_of_birth(date_of_birth):
            raise EntityError("date_of_birth")
        self.date_of_birth = date_of_birth

    @staticmethod
    def validate_patient_id(patient_id: str) -> bool:
        return isinstance(patient_id, str) and len(patient_id.strip()) > 0

    @staticmethod
    def validate_cpf(cpf: str) -> bool:
        if not isinstance(cpf, str):
            return False
        return bool(re.fullmatch(Patient.CPF_REGEX, cpf))

    @staticmethod
    def validate_name(name: str) -> bool:
        return isinstance(name, str) and len(name.strip()) >= Patient.MIN_NAME_LENGTH

    @staticmethod
    def validate_date_of_birth(date_of_birth: datetime) -> bool:
        return isinstance(date_of_birth, datetime)

    def __repr__(self):
        return (
            f"Patient(patient_id={self.id}, cpf={self.cpf}, name={self.name}, "
            f"date_of_birth={self.date_of_birth.isoformat()})"
        )
