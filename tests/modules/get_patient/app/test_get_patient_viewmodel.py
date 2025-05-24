from datetime import datetime
from src.modules.get_patient.app.get_patient_viewmodel import GetPatientViewmodel
from src.shared.domain.entities.patient import Patient


class TestGetPatientViewModel:
    def test_get_patient_viewmodel(self):
        patient = Patient(
            name="Ana Clara",
            cpf="123.456.789-00",
            date_of_birth=datetime(1990, 5, 20)
        )
        
        viewmodel = GetPatientViewmodel(patient)
        result = viewmodel.to_dict()
        
        assert "patient" in result
        assert result["message"] == "Patient retrieved successfully"
        assert result["patient"]["name"] == "Ana Clara"
        assert result["patient"]["cpf"] == "123.456.789-00"
        assert result["patient"]["date_of_birth"] == "1990-05-20T00:00:00"