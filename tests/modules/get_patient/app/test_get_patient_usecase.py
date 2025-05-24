from datetime import datetime
from src.modules.get_patient.app.get_patient_usecase import GetPatientUsecase
from src.shared.infra.repositories.users_repository_mock import UsersRepositoryMock


class Test_GetPatientUsecase:
    def test_get_patient_usecase(self):
        users_repository = UsersRepositoryMock()
        usecase = GetPatientUsecase(users_repository)
        
        patient = usecase("aa33de2e-d4ae-4aba-b066-a917ccdbfe07")
        assert patient is not None
        assert patient.patient_id == "aa33de2e-d4ae-4aba-b066-a917ccdbfe07"
        assert patient.cpf == "123.456.789-00"
        assert patient.name == "Gabriel Bianconi"
        assert patient.date_of_birth == datetime(1990, 1, 1, 0, 0)
    
    def test_no_items_found(self):
        users_repository = UsersRepositoryMock()
        usecase = GetPatientUsecase(users_repository)
        
        try:
            usecase("non-existent-id")
        except Exception as e:
            assert str(e) == "No items found for patient_id"