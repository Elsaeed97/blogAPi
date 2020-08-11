from django.test import TestCase
from .models import Post
from django.contrib.auth.models import User
# Create your tests here.

class BlogTests(TestCase):
	@classmethod
	def setUpTestData(cls):
		testuser = User.objects.create_user(username='admin',password='abc123')
		testuser.save()

		test_post = Post.objects.create(author=testuser, title='This is title', body='post body')
		test_post.save()

	def test_blog_content(self):
		post = Post.objects.get(id=1)
		author = f'{post.author}'
		title = f'{post.title}'
		body = f'{post.body}'
		self.assertEqual(author, 'admin')
		self.assertEqual(title, 'This is title')
		self.assertEqual(body, 'post body')

