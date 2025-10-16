from django.test import SimpleTestCase
from django.urls import reverse

class HomeTest(SimpleTestCase):
    def test_home_ok(self):
        resp = self.client.get(reverse("home"))
        assert resp.status_code == 200
        assert b"Bienvenido" in resp.content or b"hola" in resp.content
