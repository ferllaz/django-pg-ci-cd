from rest_framework.test import APITestCase
from rest_framework import status


class HealthAPITest(APITestCase):
    def test_health_endpoint(self):
        response = self.client.get("/api/health/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "ok")