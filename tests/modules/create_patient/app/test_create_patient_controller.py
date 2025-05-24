from src.modules.create_patient.app.create_patient_controller import CreatePatientController
from src.modules.create_patient.app.create_patient_usecase import CreatePatientUseCase
from src.shared.helpers.external_interfaces.http_models import HttpRequest
from src.shared.infra.repositories.users_repository_mock import UsersRepositoryMock


class TestCreatePatientController:
    def test_create_patient_controller(self):
        
        repo = UsersRepositoryMock()
        usecase = CreatePatientUseCase(repo)
        controller = CreatePatientController(usecase)
        request = HttpRequest(body={
            'name': 'John Doe',
            'cpf': '123.432.123-54',
            'date_of_birth': '2000-01-01'
        })
        
        response = controller(request)
        
        assert response.status_code == 201
        assert response.body['patient']['name'] == 'John Doe'
        assert response.body['patient']['cpf'] == '123.432.123-54'
        assert response.body['patient']['date_of_birth'] == '2000-01-01T00:00:00'
        assert response.body['message'] == 'Patient created successfully'