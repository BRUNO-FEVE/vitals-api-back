from src.shared.domain.entities.patient import Patient
from src.shared.domain.repositories.users_repository_interface import IUsersRepository
from src.shared.helpers.errors.domain_errors import EntityError


class CreatePatientUseCase:
    def __init__(self, repo: IUsersRepository):
        self.repo = repo
        
    def __call__(self, name: str, cpf: str, date_of_birth: str) -> None:
        
        if not Patient.validate_name(name):
            raise EntityError("name")
        
        if not Patient.validate_cpf(cpf):
            raise EntityError("cpf")
        
        new_patient = Patient(
            cpf=cpf,
            name=name,
            date_of_birth=date_of_birth
        )
        
        return self.repo.create_patient(new_patient)