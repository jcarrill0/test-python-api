import unittest
import requests

# def test_get_uf_indicator_by_date():
    
#     date = '05-05-2023'
#     response = myapp.test_client().get(f'/api/indicator/{date}')
#     # res = json.loads(response.data.decode('utf-8')).get("valor")

#     # assert res == 35903.96
#     assert response.status_code == 200

class   TestApplication(unittest.TestCase):
    URL = 'http://127.0.0.1:8000/api/indicator/'

    def test_get_uf_indicator_by_date_success(self):
        search_date = '05-05-2023'
        response = requests.get(self.URL+search_date)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.json()['valor'], 35903.96)
        print("Test 1 completed")

    
    def test_get_uf_indicator_by_date_minor(self):
        search_date = '05-05-2012'
        response = requests.get(self.URL+search_date)
        self.assertEquals(response.status_code, 400)
        print("Test 2 completed")

    def test_get_uf_indicator_by_incorrect_date(self):
        search_date = '05-13-2022'
        response = requests.get(self.URL+search_date)
        self.assertEquals(response.status_code, 400)
        print("Test 3 completed")


if __name__ == '__main__':
    # tester = TestAPI()
    # tester.test_get_uf_indicator_by_date()
    unittest.main()