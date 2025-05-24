import pytest
from datetime import datetime
from src.shared.domain.entities.patient import Patient
from src.shared.helpers.errors.domain_errors import EntityError


class Test_Patient:
    def test_patient(self):
        Patient(
            patient_id="123e4567-e89b-12d3-a456-426614174000",
            cpf="123.456.789-00",
            name="João Silva",
            date_of_birth=datetime(1990, 5, 10)
        )

    def test_patient_id_is_none(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id=None,
                cpf="123.456.789-00",
                name="João Silva",
                date_of_birth=datetime(1990, 5, 10)
            )

    def test_patient_id_is_not_str(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id=123,
                cpf="123.456.789-00",
                name="João Silva",
                date_of_birth=datetime(1990, 5, 10)
            )

    def test_patient_cpf_is_invalid_format(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id="123",
                cpf="12345678900",
                name="João Silva",
                date_of_birth=datetime(1990, 5, 10)
            )

    def test_patient_cpf_is_not_str(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id="123",
                cpf=12345678900,
                name="João Silva",
                date_of_birth=datetime(1990, 5, 10)
            )

    def test_patient_name_is_none(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id="123",
                cpf="123.456.789-00",
                name=None,
                date_of_birth=datetime(1990, 5, 10)
            )

    def test_patient_name_is_too_short(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id="123",
                cpf="123.456.789-00",
                name="A",
                date_of_birth=datetime(1990, 5, 10)
            )

    def test_patient_name_is_not_str(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id="123",
                cpf="123.456.789-00",
                name=123,
                date_of_birth=datetime(1990, 5, 10)
            )

    def test_patient_date_of_birth_is_none(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id="123",
                cpf="123.456.789-00",
                name="João Silva",
                date_of_birth=None
            )

    def test_patient_date_of_birth_is_not_datetime(self):
        with pytest.raises(EntityError):
            Patient(
                patient_id="123",
                cpf="123.456.789-00",
                name="João Silva",
                date_of_birth="1990-05-10"
            )
