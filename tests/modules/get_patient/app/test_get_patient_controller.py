from src.modules.get_patient.app.get_patient_controller import GetPatientController
from src.modules.get_patient.app.get_patient_usecase import GetPatientUsecase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.users_repository_mock import UsersRepositoryMock


class TestGetPatientController:
    def test_get_patient_controller(self):
        
        repo = UsersRepositoryMock()
        usecase = GetPatientUsecase(repo)
        controller = GetPatientController(usecase)
        request = HttpRequest(body={
            'patient_id': 'aa33de2e-d4ae-4aba-b066-a917ccdbfe07'
        })
        response = controller(request)
        assert response.status_code == 200
        assert response.body['patient']['patient_id'] == 'aa33de2e-d4ae-4aba-b066-a917ccdbfe07'
        assert response.body['patient']['name'] == 'Gabriel Bianconi'
        assert response.body['patient']['cpf'] == '123.456.789-00'
        assert response.body['patient']['date_of_birth'] == '1990-01-01T00:00:00'
        assert response.body['message'] == 'Patient retrieved successfully'