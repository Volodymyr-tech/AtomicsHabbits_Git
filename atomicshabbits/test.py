from rest_framework import status
from rest_framework.status import HTTP_403_FORBIDDEN
from rest_framework.test import APITestCase

from atomicshabbits.models import Habbits
from users.models import CustomUser


class HabbitsViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            "testuser@gmail.com", password="testpassword", username="testuser"
        )
        self.unregistered_user = CustomUser.objects.create_user(
            "thief@gmail.com", password="thiefpassword", username="thiefuser"
        )
        self.habbit = Habbits.objects.create(
            user=self.user,
            place="Park",
            time="2025-04-14T10:00:00Z",
            action="Morning jog",
            is_pleasant_habit=True,
            periodicity=3,
            award="Coffee after jogging",
            time_to_do=30,
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_get_list(self):
        # Testing GET-request API
        url = r"http://127.0.0.1:8002/api/habbits/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_object(self):
        # Testing GET-request API
        url = f"http://127.0.0.1:8002/api/habbits/{self.habbit.id}/"
        response = self.client.get(url)
        dict_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict_data.get("place"), "Park")
        self.assertEqual(dict_data.get("time"), "2025-04-14T10:00:00Z")
        self.assertEqual(dict_data.get("action"), "Morning jog")
        self.assertEqual(dict_data.get("is_pleasant_habit"), True)
        self.assertEqual(dict_data.get("periodicity"), 3)
        self.assertEqual(dict_data.get("award"), "Coffee after jogging")
        self.assertEqual(dict_data.get("time_to_do"), 30)
        self.assertEqual(dict_data.get("is_public"), True)

    def test_patch(self):
        # Testing POST-request API
        url = f"http://127.0.0.1:8002/api/habbits/{self.habbit.id}/"
        data = {"place": "Office", "action": "Write blog for web"}
        response = self.client.patch(url, data, format="json")
        dict_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict_data.get("place"), "Office")
        self.assertEqual(dict_data.get("time"), "2025-04-14T10:00:00Z")
        self.assertEqual(dict_data.get("action"), "Write blog for web")
        self.assertEqual(dict_data.get("is_pleasant_habit"), True)
        self.assertEqual(dict_data.get("periodicity"), 3)
        self.assertEqual(dict_data.get("award"), "Coffee after jogging")
        self.assertEqual(dict_data.get("time_to_do"), 30)
        self.assertEqual(dict_data.get("is_public"), True)

    def test_get_object_permission_denied(self):
        # Testing GET-request API
        self.client.logout()
        self.client.force_authenticate(self.unregistered_user)
        url = f"http://127.0.0.1:8002/api/habbits/{self.habbit.id}/"
        response = self.client.get(url)
        self.assertTrue(response.status_code, HTTP_403_FORBIDDEN)

    def test_create_habbit(self):
        url = r"http://127.0.0.1:8002/api/habbits/"
        data = {"place": "Barcelona Los Bunckers", "action": "Walk around"}
        response = self.client.post(url, data, format="json")
        dict_data = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(dict_data.get("place"), "Barcelona Los Bunckers")
        self.assertEqual(dict_data.get("time"), None)
        self.assertEqual(dict_data.get("action"), "Walk around")
        self.assertEqual(dict_data.get("is_pleasant_habit"), None)
        self.assertEqual(dict_data.get("periodicity"), None)
        self.assertEqual(dict_data.get("award"), None)
        self.assertEqual(dict_data.get("time_to_do"), 120)
        self.assertEqual(dict_data.get("is_public"), None)

    def test_update_permission_denied(self):
        self.client.logout()
        self.client.force_authenticate(self.unregistered_user)
        url = f"http://127.0.0.1:8002/api/habbits/{self.habbit.id}/"
        data = {"place": "Office", "is_public": False}
        response = self.client.patch(url, data, format="json")
        self.assertTrue(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_permission_denied(self):
        self.client.logout()
        self.client.force_authenticate(self.unregistered_user)
        url = f"http://127.0.0.1:8002/api/habbits/{self.habbit.id}/"
        response = self.client.delete(url)
        self.assertTrue(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete(self):
        url = f"http://127.0.0.1:8002/api/habbits/{self.habbit.id}/"
        response = self.client.delete(url)
        self.assertTrue(response.status_code, status.HTTP_204_NO_CONTENT)


class PublicHabbitsListAPIViewTestCase(APITestCase):
    def setUp(self):
        self.user = CustomUser.objects.create_user(
            "testuser@gmail.com", password="testpassword", username="testuser"
        )
        self.unregistered_user = CustomUser.objects.create_user(
            "thief@gmail.com", password="thiefpassword", username="thiefuser"
        )
        self.habbit = Habbits.objects.create(
            user=self.user,
            place="Park",
            time="2025-04-14T10:00:00Z",
            action="Morning jog",
            is_pleasant_habit=True,
            periodicity=3,
            award="Coffee after jogging",
            time_to_do=30,
            is_public=False,
        )
        self.habbit_2 = Habbits.objects.create(
            user=self.user,
            place="Barcelona Los Bunckers",
            time="2025-04-14T10:00:00Z",
            action="Walk around",
            is_pleasant_habit=True,
            periodicity=3,
            award="Coffee after walking",
            time_to_do=30,
            is_public=True,
        )
        self.client.force_authenticate(user=self.user)

    def test_get_list(self):
        # Testing GET-request API
        url = r"http://127.0.0.1:8002/api/public-habbits/"
        response = self.client.get(url)
        dict_data = response.json()
        lst = dict_data["results"][0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(lst.get("place"), "Barcelona Los Bunckers")
        self.assertEqual(lst.get("time"), "2025-04-14T10:00:00Z")
        self.assertEqual(lst.get("action"), "Walk around")
        self.assertEqual(lst.get("is_pleasant_habit"), True)
        self.assertEqual(lst.get("periodicity"), 3)
        self.assertEqual(lst.get("award"), "Coffee after walking")
        self.assertEqual(lst.get("time_to_do"), 30)
        self.assertEqual(lst.get("is_public"), True)
        self.assertIsNot(lst.get("place"), "Park")
