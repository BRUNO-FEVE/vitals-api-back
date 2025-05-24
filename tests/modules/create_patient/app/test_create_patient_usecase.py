from datetime import datetime
from src.modules.create_patient.app.create_patient_usecase import CreatePatientUseCase
from src.shared.domain.entities.patient import Patient
from src.shared.infra.repositories.users_repository_mock import UsersRepositoryMock


class Test_CreatePatientUsecase:
    
    def test_create_patient(self):
        repo = UsersRepositoryMock()
        usecase = CreatePatientUseCase(repo)

        patient = usecase(
            name="Vitor Choueri",
            cpf="123.456.989-00",
            date_of_birth=datetime(1990, 1, 1)
        )
        
        assert repo.patients[4] == patient