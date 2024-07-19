from django.contrib.auth.base_user import BaseUserManager

from django.utils.translation import gettext_lazy


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        kwargs.setdefault('is_active', True)

        if kwargs.get('is_staff') is not True or kwargs.get('is_superuser') is not True:
            raise ValueError(
                'is_staff and is_superuser must be True for a superuser.')

        return self.create_user(email, password, **kwargs)
