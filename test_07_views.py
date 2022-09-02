from django.test import Client

from django.urls import reverse
client = Client()

print("#############################################")
print("Testando views:")
print("#############################################")

response = client.get(reverse('index'))
print(response.status_code)
assert response.status_code == 200
