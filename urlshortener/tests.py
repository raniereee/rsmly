from django.test import TestCase

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



