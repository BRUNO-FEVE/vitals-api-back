from src.modules.get_patient.app.get_patient_controller import GetPatientController
from src.modules.get_patient.app.get_patient_usecase import GetPatientUsecase
from src.shared.environments import Environments
from src.shared.helpers.external_interfaces.http_lambda_requests import LambdaHttpRequest, LambdaHttpResponse


repo = Environments.get_users_repository()()
usecase = GetPatientUsecase(repo=repo)
controller = GetPatientController(usecase=usecase)

def get_patient_presenter(event, context):
    httpRequest = LambdaHttpRequest(data=event)
    response = controller(httpRequest)
    httpResponse = LambdaHttpResponse(status_code=response.status_code, body=response.body, headers=response.headers)

    return httpResponse.toDict()
def lambda_handler(event, context):
    response = get_patient_presenter(event, context)

    return response