from abc import ABC, abstractmethod

from src.shared.domain.entities.patient import Patient


class IUsersRepository(ABC):
    
    @abstractmethod
    def get_patient(self, patient_id:str) -> Patient:
        """
        If patient not found raise NoItemsFound
        """
        pass
    
    @abstractmethod
    def create_patient(self, patient: Patient) -> Patient:
        """
        Create Patient
        """
        pass