from src.shared.domain.entities.patient import Patient
from src.shared.helpers.errors.controller_errors import MissingParameters
from src.shared.helpers.errors.domain_errors import EntityError
from src.shared.helpers.errors.usecase_errors import DuplicatedItem
from src.shared.helpers.external_interfaces.http_codes import BadRequest, Created, InternalServerError
from src.shared.helpers.external_interfaces.external_interface import IRequest, IResponse
from .create_patient_usecase import CreatePatientUseCase
from .create_patient_viewmodel import CreatePatientViewmodel
from datetime import datetime


class CreatePatientController:
    def __init__(self, usecase: CreatePatientUseCase):
        self.usecase = usecase

    def __call__(self, request: IRequest) -> IResponse:
        try:
            name = request.data.get('name')
            cpf = request.data.get('cpf')
            date_of_birth = request.data.get('date_of_birth')

            if name is None:
                raise MissingParameters('name')
            if cpf is None:
                raise MissingParameters('cpf')
            if date_of_birth is None:
                raise MissingParameters('date_of_birth')

            try:
                date_of_birth = datetime.fromisoformat(date_of_birth)
            except ValueError:
                raise EntityError('date_of_birth')

            patient = self.usecase(
                name=name,
                cpf=cpf,
                date_of_birth=date_of_birth
            )

            viewmodel = CreatePatientViewmodel(patient)
            return Created(viewmodel.to_dict())

        except MissingParameters as err:
            return BadRequest(body=err.message)

        except EntityError as err:
            return BadRequest(body=err.message)

        except DuplicatedItem as err:
            return BadRequest(body=err.message)

        except Exception as err:
            return InternalServerError(body=err.args[0])
