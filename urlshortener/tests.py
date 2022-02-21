from django.test import TestCase
from http import HTTPStatus

# Create your tests here.


'''
Test of load app
'''
class ViewsTestCase(TestCase):
    def test_index_loads_properly(self):
        """The index page loads properly"""
        print("Testing root path ")
        response = self.client.get('http://172.17.0.2:8000')
        self.assertEqual(response.status_code, 200)

    def test_access_urlshortener(self):
        """The urlshortnet test without login"""
        print("Testing urlshortner method")
        response = self.client.get('http://127.0.0.1:8000/urlshortener/')
        self.assertEqual(response.status_code, 200)


    def test_access_dashboard_login(self):
        """The login test"""
        print("Testando dashboard ")
        response = self.client.get('http://127.0.0.1:8000/dashboard/')

        '''
        302 FOUND - The target resource resides temporarily under a different URI. LOGIN
        '''
        self.assertEqual(response.status_code, 302)

    def test_url_shortener_simple(self):
        response = self.client.post("/", data={"long_url": "http://globo.com", "name_short_url": "", "duration_expire": ""})
        self.assertEqual(response.status_code, HTTPStatus.OK)
