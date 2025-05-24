from abc import ABC, abstractmethod
from src.shared.domain.entities.vitals import Vitals


class IQuizVitalsRepository(ABC):

    @abstractmethod
    def create_vitals(self, vitals: Vitals) -> Vitals:
        """
        Create a new Vitals entry in the repository.
        """
        pass

    @abstractmethod
    def get_vitals(self, vitals_id: str) -> Vitals:
        """
        Retrieve a Vitals entry by its ID.
        """
        pass

    @abstractmethod
    def update_vitals(self, vitals_id: str, updated_data: dict) -> Vitals:
        """
        Update an existing Vitals entry with new data.
        """
        pass
