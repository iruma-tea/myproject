from django.test import TestCase
from django.urls import reverse
from .models import Post


# Create your tests here.
class PostModelTest(TestCase):
    def setUp(self):
        self.post = Post.objects.create(
            title="Test Title",
            content="This is a test content that is more than 100 characters. This part will be cut off in the summary.",
        )

    def test_get_summary(self):
        summary = self.post.get_summary()
        self.assertEqual(summary, "This is a test content that is more than 100 characters. This part will be cut off in the summary.")


class PostViewTest(TestCase):
    def setUp(self):
        Post.objects.create(title="Test Title 1", content="Test content 1.")
        Post.objects.create(title="Test Title 2", content="Test content 2.")

    def test_post_list_view(self):
        response = self.client.get(reverse('post_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Title 1")
        self.assertContains(response, "Test Title 2")
