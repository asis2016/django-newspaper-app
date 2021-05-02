from django.contrib.auth import get_user_model
from django.test import SimpleTestCase, TestCase
from django.urls import reverse


class HomePageTests(SimpleTestCase):
    """ Test for home page. """

    def test_home_page_status_code(self):
        """ Test if home url is okay. """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """ Test if home url NAME is okay. """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test if home template is correct. """
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')


class SignupPageTests(TestCase):
    """ Test for sign up. """
    username = 'newuser'
    email = 'newuser@email.com'

    def test_signup_page_status_code(self):
        """ Test if sign up page is working. """
        response = self.client.get('/users/signup/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_by_name(self):
        """ Test if sign up page NAME url is working. """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Test if signup is using signup.html """
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'signup.html')

    def test_signup_form(self):
        """ Test if newuser and newuser@gmail.com (NEW) user is working. """
        get_user_model().objects.create_user(self.username, self.email)
        self.assertEqual(get_user_model().objects.all().count(), 1)
        self.assertEqual(get_user_model().objects.all()[0].username, self.username)
        self.assertEqual(get_user_model().objects.all()[0].email, self.email)
