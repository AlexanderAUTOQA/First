import allure  
import pytest
import requests  

base_url = "URL API"  

@allure.epic("API Testing")  
@allure.feature("HTTP Requests")  
class TestHttpRequests:  

    @allure.title("Test GET request")  
    def test_get_request(self):  
        with allure.step("Send GET request"):  
            response = requests.get(f"{base_url}/posts/1")  

        with allure.step("Verify response status code"):  
            assert response.status_code == 200  

        with allure.step("Verify response JSON structure"):  
            json_response = response.json()  
            assert json_response["id"] == 1  
            assert json_response["userId"] == 1  
            assert "title" in json_response  
            assert "body" in json_response  

    @allure.title("Test POST request")  
    def test_post_request(self):  
        payload = {  
            "title": "foo",  
            "body": "bar",  
            "userId": 1  
        }  

        with allure.step("Send POST request"):  
            response = requests.post(f"{base_url}/posts", json=payload)  

        with allure.step("Verify response status code"):  
            assert response.status_code == 201  

        with allure.step("Verify response JSON structure"):  
            json_response = response.json()  
            assert json_response["title"] == payload["title"]  
            assert json_response["body"] == payload["body"]  
            assert json_response["userId"] == payload["userId"]


    
    

    



