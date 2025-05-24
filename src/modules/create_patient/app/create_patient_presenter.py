from src.modules.create_patient.app.create_patient_controller import CreatePatientController
from src.modules.create_patient.app.create_patient_usecase import CreatePatientUseCase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_users_repository()()
usecase = CreatePatientUseCase(repo=repo)
controller = CreatePatientController(usecase=usecase)

def create_patient_presenter(event, context):
    
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()

def lambda_handler(event, context):
    
    response = create_patient_presenter(event, context)
   
    return response