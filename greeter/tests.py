from django.test import Client, TestCase
from django.urls import reverse

from .models import Visitor


class VisitorModelTests(TestCase):
    def test_create_visitor(self):
        visitor = Visitor.objects.create(name='Виктор')
        self.assertEqual(Visitor.objects.count(), 1)
        self.assertEqual(str(visitor), 'Виктор')


class HomeViewTests(TestCase):
    def test_get_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, 'Здравствуйте')

    def test_post_valid_name_saves_and_greets(self):
        response = self.client.post(reverse('home'), {'name': 'Алексей'}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Здравствуйте, Алексей!')
        self.assertEqual(Visitor.objects.count(), 1)

    def test_post_empty_name_shows_error(self):
        response = self.client.post(reverse('home'), {'name': ''})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Имя не может быть пустым')
        self.assertEqual(Visitor.objects.count(), 0)

    def test_post_whitespace_name_shows_error(self):
        response = self.client.post(reverse('home'), {'name': '   '})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Visitor.objects.count(), 0)

    def test_post_redirects_after_success(self):
        response = self.client.post(reverse('home'), {'name': 'Ольга'})
        self.assertEqual(response.status_code, 302)

    def test_csrf_protection_is_enforced(self):
        strict_client = Client(enforce_csrf_checks=True)
        response = strict_client.post(reverse('home'), {'name': 'Игорь'})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Visitor.objects.count(), 0)
