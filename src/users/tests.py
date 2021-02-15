from django.test import TestCase
from django.contrib.auth import get_user_model


class CustomUserTest(TestCase):

    def test_new_user(self):
        db = get_user_model()
        user = db.objects.create_user(
            'testuser@email.com', 'testuser', 'first_name',
            'last_name', 'password1234'
        )

        self.assertEqual(str(user), user.email)
        self.assertEqual(user.email, 'testuser@email.com')
        self.assertEqual(user.username, 'testuser')
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.last_name, 'last_name')

        self.assertTrue(user.is_active)

        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(ValueError):
            db.objects.create_user(
                email='', username='testuser', first_name='first_name',
                last_name='last_name', password='password1234'
            )

    def test_new_superuser(self):
        db = get_user_model()
        user = db.objects.create_superuser(
            'testsuperuser@email.com', 'testsuperuser',
            'first_name', 'last_name', 'password1234'
        )

        self.assertEqual(str(user), user.email)
        self.assertEqual(user.email, 'testsuperuser@email.com')
        self.assertEqual(user.username, 'testsuperuser')
        self.assertEqual(user.first_name, 'first_name')
        self.assertEqual(user.last_name, 'last_name')

        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testsuperuser@email', username='testsuperuser',
                first_name='first_name', last_name='last_name', is_active=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testsuperuser@email.com', username='testsuperuser',
                first_name='first_name', last_name='last_name', is_staff=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='testsuperuser@email', username='testsuperuser',
                first_name='first_name', last_name='last_name', is_superuser=False
            )

        with self.assertRaises(ValueError):
            db.objects.create_superuser(
                email='', username='testsuperuser', first_name='first_name',
                last_name='last_name'
            )
