from src.modules.get_patient.app.get_patient_usecase import GetPatientUsecase
from src.modules.get_patient.app.get_patient_viewmodel import GetPatientViewmodel
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.external_interfaces.external_interface import IRequest
from src.shared.helpers.external_interfaces.http_codes import OK, BadRequest, InternalServerError


class GetPatientController:
    
    def __init__(self, usecase: GetPatientUsecase):
        self.usecase = usecase
        
    def __call__(self, request: IRequest):
        try:
            patient_id = request.data.get('patient_id')
            
            if patient_id is None:
                raise MissingParameters('patient_id')
            
            usecase = self.usecase(patient_id)
            viewmodel = GetPatientViewmodel(usecase)
            
            return OK(viewmodel.to_dict())
            
        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])     