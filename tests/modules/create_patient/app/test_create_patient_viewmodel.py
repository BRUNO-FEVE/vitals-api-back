from datetime import datetime
from src.modules.create_patient.app.create_patient_viewmodel import CreatePatientViewmodel
from src.shared.domain.entities.patient import Patient



class TestCreatePatientViewmodel:

    def test_patient_viewmodel(self):
        patient = Patient(
            name="Ana Clara",
            cpf="123.456.789-00",
            date_of_birth=datetime(1990, 5, 20)
        )

        viewmodel = CreatePatientViewmodel(patient)
        result = viewmodel.to_dict()

        assert "patient" in result
        assert result["message"] == "Patient created successfully"
        assert result["patient"]["name"] == "Ana Clara"
        assert result["patient"]["cpf"] == "123.456.789-00"
        assert result["patient"]["date_of_birth"] == "1990-05-20T00:00:00"
        assert isinstance(result["patient"]["patient_id"], str)
