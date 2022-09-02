import pytest
from django.test import Client
from django.urls import reverse

@pytest.mark.django_db
def test_view(client):
   url = reverse('index')
   response = client.get(url)
   print(response.status_code)
   assert response.status_code == 200


