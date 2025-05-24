import json
from src.modules.get_patient.app.get_patient_presenter import lambda_handler


class Test_Get_Patient_Presenter:
    def test_get_patient_presenter(self):
        event = {
            "version": "2.0",
            "routeKey": "$default",
            "rawPath": "/my/path",
            "rawQueryString": "parameter1=value1&parameter1=value2&parameter2=value",
            "cookies": [
                "cookie1",
                "cookie2"
            ],
            "headers": {
                "header1": "value1",
                "header2": "value1,value2"
            },
            "queryStringParameters": {
                "parameter1": "1"
            },
            "requestContext": {
                "accountId": "123456789012",
                "apiId": "<urlid>",
                "authentication": None,
                "authorizer": {
                     "claims":{
                "sub": "13bc6ada-c0d1-7054-66ab-e17414c48ae3",
                "name": "Vitor Guirão Mpntm",
                "email": "vsoller@airubio.com",
                "custom:isMaua": True
                    }
                },
                "domainName": "<url-id>.lambda-url.us-west-2.on.aws",
                "domainPrefix": "<url-id>",
                "external_interfaces": {
                    "method": "POST",
                    "path": "/my/path",
                    "protocol": "HTTP/1.1",
                    "sourceIp": "123.123.123.123",
                    "userAgent": "agent"
                },
                "requestId": "id",
                "routeKey": "$default",
                "stage": "$default",
                "time": "12/Mar/2020:19:03:58 +0000",
                "timeEpoch": 1583348638390
            },
            "body": '{"patient_id": "aa33de2e-d4ae-4aba-b066-a917ccdbfe07"}',
            "pathParameters": None,
            "isBase64Encoded": None,
            "stageVariables": None
        }
        
        response = lambda_handler(event, None)
        assert response['statusCode'] == 200
        assert json.loads(response['body'])['patient']['name'] == 'Gabriel Bianconi'
        assert json.loads(response['body'])['patient']['cpf'] == '123.456.789-00'
        assert json.loads(response['body'])['patient']['date_of_birth'] == '1990-01-01T00:00:00'
        assert json.loads(response['body'])['patient']['patient_id'] == 'aa33de2e-d4ae-4aba-b066-a917ccdbfe07'
        assert json.loads(response['body'])['message'] == 'Patient retrieved successfully'