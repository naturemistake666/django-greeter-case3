from django.test import Client, TestCase
from django.urls import reverse

from .forms import VisitorForm
from .models import Visitor


class VisitorModelTests(TestCase):
    def test_valid_name_saves(self):
        visitor = Visitor.objects.create(name="Виктор")
        self.assertEqual(Visitor.objects.count(), 1)
        self.assertEqual(str(visitor), "Виктор")

    def test_blank_name_is_invalid(self):
        visitor = Visitor(name="")
        with self.assertRaises(Exception):
            visitor.full_clean()

    def test_whitespace_only_name_is_invalid(self):
        visitor = Visitor(name="   ")
        with self.assertRaises(Exception):
            visitor.full_clean()


class VisitorFormTests(TestCase):
    def test_form_valid_with_name(self):
        form = VisitorForm(data={"name": "Мария"})
        self.assertTrue(form.is_valid())

    def test_form_invalid_when_empty(self):
        form = VisitorForm(data={"name": ""})
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_form_invalid_when_whitespace_only(self):
        form = VisitorForm(data={"name": "   "})
        self.assertFalse(form.is_valid())


class HomeViewTests(TestCase):
    def test_get_renders_empty_form(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Ваше имя")
        self.assertNotContains(response, "Здравствуйте")

    def test_post_valid_name_saves_and_greets(self):
        response = self.client.post(reverse("home"), {"name": "Алексей"}, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Здравствуйте, Алексей!")
        self.assertEqual(Visitor.objects.count(), 1)
        self.assertEqual(Visitor.objects.first().name, "Алексей")

    def test_post_empty_name_shows_error_and_does_not_save(self):
        response = self.client.post(reverse("home"), {"name": ""})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Пожалуйста, введите имя")
        self.assertEqual(Visitor.objects.count(), 0)

    def test_post_whitespace_name_shows_error_and_does_not_save(self):
        response = self.client.post(reverse("home"), {"name": "   "})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Visitor.objects.count(), 0)

    def test_post_is_redirect_after_success(self):
        """Post/Redirect/Get: успешная отправка формы должна быть редиректом,
        а не прямым рендерингом -- это защищает от повторной отправки формы
        при обновлении страницы."""
        response = self.client.post(reverse("home"), {"name": "Ольга"})
        self.assertEqual(response.status_code, 302)

    def test_csrf_protection_is_enforced(self):
        """Без CSRF-токена запрос от "чужого" клиента должен быть отклонён."""
        strict_client = Client(enforce_csrf_checks=True)
        response = strict_client.post(reverse("home"), {"name": "Игорь"})
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Visitor.objects.count(), 0)

    def test_csrf_token_present_in_rendered_form(self):
        response = self.client.get(reverse("home"))
        self.assertContains(response, "csrfmiddlewaretoken")
