from django.test import TestCase

from crud.models import Article


# Create your tests here.
class ArticleTestCase(TestCase):
    def setUp(self):
        return Article.objects.create(title="cat", author="meow", email="cat@gmail.com")

    def test_create_article(self):
        a, b = Article.objects.get_or_create(title="cat", author="meow", email="cat@gmail.com")
        print(121, a, 54, b)
        self.assertNotEqual(a, 200)
        self.assertTrue(isinstance(a, Article))
