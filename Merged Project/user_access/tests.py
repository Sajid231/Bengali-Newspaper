import unittest

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse


class UserModelTest(TestCase):

    def setUp(self):
        User.objects.create(username="abaa", password="hello", is_staff=True)
        User.objects.create(username="rrrr", password="hello", is_superuser=True)

    def test_username(self):
        u1 = User.objects.get(username="abaa")
        self.assertEqual(u1.username, "abaa")

    def test_superuser(self):
        u1 = User.objects.get(username="abaa")
        u2 = User.objects.get(username="rrrr")
        self.assertEqual(u1.is_superuser, False)
        self.assertEqual(u2.is_superuser, True)

    def test_staff(self):
        u1 = User.objects.get(username="abaa")
        u2 = User.objects.get(username="rrrr")
        self.assertEqual(u1.is_staff, True)
        self.assertEqual(u2.is_staff, False)

    def test_login_link(self):
        response = self.client.get(reverse('Login'))
        self.assertEqual(response.status_code, 200)

    def test_signup_link(self):
        response = self.client.get(reverse('Signup'))
        self.assertEqual(response.status_code, 200)

    def test_password_reset_link(self):
        response = self.client.get(reverse('Password Reset'))
        self.assertEqual(response.status_code, 200)
