from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Comment


class CommenListTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='adam', password='pass')

    def test_can_list_comments(self):
        adam = User.objects.get(username='adam')
        response = self.client.get('/comments/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_logged_in_user_can_create_comment(self):
        self.client.login(username='adam', password='pass')
        data = {'content': 'Another test comment.'}
        response = self.client.post('/comments/', data, format='json')

    def test_user_not_logged_in_cant_create_comment(self):
        response = self.client.post('/comment/', {'title': 'a title'})


class CommentDetailViewTests(APITestCase):
    def setUp(self):
        adam = User.objects.create_user(username='adam', password='pass')
        brian = User.objects.create_user(username='brian', password='pass')
        Comment.objects.create(
            owner=adam, content='adams content'
        )
        Comment.objects.create(
            owner=brian, content='brians content'
        )