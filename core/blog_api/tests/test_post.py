from rest_framework.test import APITestCase


class PostTestCase(APITestCase):
    def test_get_post_list(self):
        response = self.client.post('/api/posts/')
        return response

