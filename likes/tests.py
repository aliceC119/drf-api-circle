from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Like


class LikeListTests(APITestCase):
    def setup(self):
        self.user = User.objects.create_user(username='adam', password='pass')

    def test_can_list_likes(self):

        response = self.client.get('/likes/')

    def test_logged_in_user_can_create_like(self):
        self.client.login(username='adam', password='pass')
        data = {'content': 'Another test like.'}
        response = self.client.post('/likes/', data, format='json')

    def test_user_not_logged_in_cant_create_like(self):
        data = {'content': 'Another test like.'}
        response = self.client.post('/likes/', data, format='json')


class LikeDetailViewTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adam', password='pass')
        self.otheruser = User.objects.create_user(
            username='brian',
            password='pass')

    def test_retrieve_like(self):
        self.client.login(username='user', password='password')
        response = self.client.get('/likes/')

    def test_delete_like(self):
        self.client.login(username='user', password='password')
        response = self.client.delete('/likes/')

    def test_use_not_logged_in_cant_like(self):
        self.client.login(username='otheruser', password='password')
        response = self.client.delete('/likes/')
