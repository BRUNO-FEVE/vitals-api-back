from typing import List
from src.shared.domain.entities.vitals import Vitals
from src.shared.domain.repositories.quiz_vitals_repository_interface import IQuizVitalsRepository
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class QuizVitalsRepositoryMock(IQuizVitalsRepository):
    def __init__(self):
        self.vitals_list: List[Vitals] = [
            Vitals(
                patient_id="f9d44b1e-b2cb-4e9c-b649-948b3d88c101",
                temperature=36.7,
                heart_rate=75,
                oxygen_saturation=98,
                systolic_pressure=120,
                diastolic_pressure=80,
                weight=70.0
            ),
            Vitals(
                patient_id="6de53c7a-bc0a-4b1e-a1d2-fdc92ceff777",
                temperature=37.2,
                heart_rate=85,
                oxygen_saturation=95,
                systolic_pressure=125,
                diastolic_pressure=85,
                weight=80.5
            ),
            Vitals(
                patient_id="dba52f20-48d7-4b9f-98ff-08f1b5de94aa",
                temperature=38.5,
                heart_rate=92,
                oxygen_saturation=90,
                systolic_pressure=135,
                diastolic_pressure=90,
                weight=90.0
            )
        ]

    def create_vitals(self, patient_id, temperature, heart_rate, oxygen_saturation,
                      systolic_pressure, diastolic_pressure, weight) -> Vitals:
        vitals = Vitals(
            patient_id=patient_id,
            temperature=temperature,
            heart_rate=heart_rate,
            oxygen_saturation=oxygen_saturation,
            systolic_pressure=systolic_pressure,
            diastolic_pressure=diastolic_pressure,
            weight=weight
        )
        self.vitals_list.append(vitals)
        return vitals

    def get_vitals(self, vitals_id: str) -> Vitals:
        for vitals in self.vitals_list:
            if vitals.vitals_id == vitals_id:
                return vitals
        raise NoItemsFound("vitals_id")

    def update_vitals(self, vitals_id: str, temperature: float, heart_rate: int,
                      oxygen_saturation: int, systolic_pressure: int,
                      diastolic_pressure: int, weight: float) -> Vitals:
        for vitals in self.vitals_list:
            if vitals.vitals_id == vitals_id:
                vitals.temperature = temperature
                vitals.heart_rate = heart_rate
                vitals.oxygen_saturation = oxygen_saturation
                vitals.systolic_pressure = systolic_pressure
                vitals.diastolic_pressure = diastolic_pressure
                vitals.weight = weight
                return vitals
        raise NoItemsFound("vitals_id")
