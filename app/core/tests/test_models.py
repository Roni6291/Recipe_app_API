from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTests(TestCase):

    def test_create_user_with_email_successful(self):
        """test creating a new user as successful"""
        email = 'test@email.com'
        password = 'Test1234'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        """test the email for new user normalised"""
        email = 'test@EMAIL.COM'
        user = get_user_model().objects.create_user(
            email, 'test1234')
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'Test1234')

    def test_create_new_superuser(self):
        """test for creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@email.com", 'test1234'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
