from django.test import TestCase
from django.contrib.auth import get_user_model

# Create your tests here.

class CustomUserTests(TestCase):

    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(
            username = 'sojol',
            password = '0170680sj',
            email = 'sojol@gmail.com'
        )

        self.assertEqual(user.username,'sojol')
        self.assertEqual(user.email,'sojol@gmail.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)


    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(
            username = 'supersojol',
            password = '0170680sj',
            email = 'supersojol@gmail.com'
        )

        self.assertEqual(admin_user.email,'supersojol@gmail.com')
        self.assertEqual(admin_user.username,'supersojol')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

