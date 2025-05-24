import uuid


class Vitals:
    def __init__(self,
                 patient_id: str,
                 temperature: float,
                 heart_rate: int,
                 oxygen_saturation: int,
                 systolic_pressure: int,
                 diastolic_pressure: int,
                 weight: float,
                 vitals_id: str = None):

        if not self.validate_uuid(patient_id):
            raise ValueError("Invalid patient_id")

        if not self.validate_float(temperature):
            raise ValueError("Invalid temperature")

        if not self.validate_int(heart_rate):
            raise ValueError("Invalid heart_rate")

        if not self.validate_int(oxygen_saturation):
            raise ValueError("Invalid oxygen_saturation")

        if not self.validate_int(systolic_pressure):
            raise ValueError("Invalid systolic_pressure")

        if not self.validate_int(diastolic_pressure):
            raise ValueError("Invalid diastolic_pressure")

        if not self.validate_float(weight):
            raise ValueError("Invalid weight")

        self.vitals_id = vitals_id if vitals_id is not None else str(uuid.uuid4())
        if not self.validate_uuid(self.vitals_id):
            raise ValueError("Invalid vitals_id")

        self.patient_id = patient_id
        self.temperature = temperature
        self.heart_rate = heart_rate
        self.oxygen_saturation = oxygen_saturation
        self.systolic_pressure = systolic_pressure
        self.diastolic_pressure = diastolic_pressure
        self.weight = weight

    @staticmethod
    def validate_uuid(val: str) -> bool:
        if val is None or not isinstance(val, str):
            return False
        try:
            uuid.UUID(val)
            return True
        except ValueError:
            return False

    @staticmethod
    def validate_float(val) -> bool:
        return isinstance(val, (float, int)) 

    @staticmethod
    def validate_int(val) -> bool:
        return isinstance(val, int)

    def __repr__(self):
        return (f"Vitals(vitals_id={self.vitals_id}, patient_id={self.patient_id}, temperature={self.temperature}, "
                f"heart_rate={self.heart_rate}, oxygen_saturation={self.oxygen_saturation}, "
                f"systolic_pressure={self.systolic_pressure}, diastolic_pressure={self.diastolic_pressure}, "
                f"weight={self.weight})")
