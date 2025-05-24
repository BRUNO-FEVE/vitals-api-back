import pytest
from src.shared.infra.repositories.quiz_vitals_repository_mock import QuizVitalsRepositoryMock
from src.shared.helpers.errors.usecase_errors import NoItemsFound


class TestQuizVitalsRepositoryMock:

    def test_get_vitals(self):
        repo = QuizVitalsRepositoryMock()
        first_vitals = repo.vitals_list[0]
        result = repo.get_vitals(first_vitals.vitals_id)

        assert result.vitals_id == first_vitals.vitals_id
        assert result.heart_rate == 75
        assert result.temperature == 36.7

    def test_create_vitals(self):
        repo = QuizVitalsRepositoryMock()
        initial_len = len(repo.vitals_list)

        new = repo.create_vitals(
            patient_id="12345678-aaaa-bbbb-cccc-123456789000",
            temperature=37.8,
            heart_rate=78,
            oxygen_saturation=96,
            systolic_pressure=122,
            diastolic_pressure=82,
            weight=74.5
        )

        assert len(repo.vitals_list) == initial_len + 1
        assert new.patient_id == "12345678-aaaa-bbbb-cccc-123456789000"
        assert new.vitals_id is not None
        assert new.temperature == 37.8

    def test_update_vitals(self):
        repo = QuizVitalsRepositoryMock()
        vitals_to_update = repo.vitals_list[1]

        updated = repo.update_vitals(
            vitals_id=vitals_to_update.vitals_id,
            temperature=39.0,
            heart_rate=100,
            oxygen_saturation=89,
            systolic_pressure=150,
            diastolic_pressure=95,
            weight=85.0
        )

        assert updated.temperature == 39.0
        assert updated.heart_rate == 100
        assert updated.oxygen_saturation == 89
        assert updated.systolic_pressure == 150
        assert updated.weight == 85.0
