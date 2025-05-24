from src.shared.domain.repositories.users_repository_interface import IUsersRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class GetPatientUsecase:
    def __init__(self, repo = IUsersRepository):
        self.repo = repo
        
    def __call__(self, patient_id: str) -> dict:
        patient = self.repo.get_patient(patient_id)
        
        if not patient:
            raise NoItemsFound("patient_id")
        
        return patient