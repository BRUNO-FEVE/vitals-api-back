import pytest
from src.shared.domain.entities.vitals import Vitals
import uuid


class TestVitals:

    def test_create_valid_vitals(self):
        vitals = Vitals(
            patient_id=str(uuid.uuid4()),
            temperature=36.7,
            heart_rate=72,
            oxygen_saturation=98,
            systolic_pressure=120,
            diastolic_pressure=80,
            weight=70.0
        )
        assert isinstance(vitals.vitals_id, str)
        assert vitals.temperature == 36.7

    def test_invalid_patient_id(self):
        with pytest.raises(ValueError, match="Invalid patient_id"):
            Vitals(
                patient_id="not-a-uuid",
                temperature=36.7,
                heart_rate=72,
                oxygen_saturation=98,
                systolic_pressure=120,
                diastolic_pressure=80,
                weight=70.0
            )

    def test_invalid_temperature(self):
        with pytest.raises(ValueError, match="Invalid temperature"):
            Vitals(
                patient_id=str(uuid.uuid4()),
                temperature="hot",
                heart_rate=72,
                oxygen_saturation=98,
                systolic_pressure=120,
                diastolic_pressure=80,
                weight=70.0
            )

    def test_invalid_heart_rate(self):
        with pytest.raises(ValueError, match="Invalid heart_rate"):
            Vitals(
                patient_id=str(uuid.uuid4()),
                temperature=36.7,
                heart_rate="fast",
                oxygen_saturation=98,
                systolic_pressure=120,
                diastolic_pressure=80,
                weight=70.0
            )

    def test_invalid_oxygen_saturation(self):
        with pytest.raises(ValueError, match="Invalid oxygen_saturation"):
            Vitals(
                patient_id=str(uuid.uuid4()),
                temperature=36.7,
                heart_rate=72,
                oxygen_saturation=None,
                systolic_pressure=120,
                diastolic_pressure=80,
                weight=70.0
            )

    def test_invalid_systolic_pressure(self):
        with pytest.raises(ValueError, match="Invalid systolic_pressure"):
            Vitals(
                patient_id=str(uuid.uuid4()),
                temperature=36.7,
                heart_rate=72,
                oxygen_saturation=98,
                systolic_pressure="high",
                diastolic_pressure=80,
                weight=70.0
            )

    def test_invalid_diastolic_pressure(self):
        with pytest.raises(ValueError, match="Invalid diastolic_pressure"):
            Vitals(
                patient_id=str(uuid.uuid4()),
                temperature=36.7,
                heart_rate=72,
                oxygen_saturation=98,
                systolic_pressure=120,
                diastolic_pressure=None,
                weight=70.0
            )

    def test_invalid_weight(self):
        with pytest.raises(ValueError, match="Invalid weight"):
            Vitals(
                patient_id=str(uuid.uuid4()),
                temperature=36.7,
                heart_rate=72,
                oxygen_saturation=98,
                systolic_pressure=120,
                diastolic_pressure=80,
                weight="heavy"
            )

    def test_invalid_vitals_id(self):
        with pytest.raises(ValueError, match="Invalid vitals_id"):
            Vitals(
                patient_id=str(uuid.uuid4()),
                temperature=36.7,
                heart_rate=72,
                oxygen_saturation=98,
                systolic_pressure=120,
                diastolic_pressure=80,
                weight=70.0,
                vitals_id="invalid-uuid"
            )
