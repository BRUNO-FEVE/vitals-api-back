from datetime import datetime
from src.shared.domain.entities.patient import Patient
from src.shared.infra.repositories.users_repository_mock import UsersRepositoryMock


class Test_UsersRepositoryMock:
    def test_get_patient(self):
        
        repo = UsersRepositoryMock()
        user = repo.get_patient("a9456609-211b-451b-a88a-84735e0ab0f8")

        assert user.name == "Bruno Fevereiro"
        assert user.patient_id == "a9456609-211b-451b-a88a-84735e0ab0f8"
        assert user.cpf == "987.654.321-00"
        assert user.date_of_birth == datetime(1985, 2, 2)
        
    def test_create_patient(self):
        repo = UsersRepositoryMock()
        new_patient = Patient(
            cpf="123.456.789-00",
            name="New Patient",
            date_of_birth=datetime(2000, 1, 1)
        )
        new_user = repo.create_patient(new_patient)

        assert new_user.name == "New Patient"
        assert new_user.cpf == "123.456.789-00"
        assert new_user.date_of_birth == datetime(2000, 1, 1)
        print(new_user.patient_id)
        assert new_user.patient_id is not None