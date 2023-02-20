from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin
from django.utils import timezone
from django.contrib import auth
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.core.validators import RegexValidator

class UserManager(UserManager):

    def _create_user(self, email, password, **extra_fields):

        email = self.normalize_email(email)
        user = self.model( email=email, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

    def with_perm(self, perm, is_active=True, include_superusers=True, backend=None, obj=None):
        if backend is None:
            backends = auth._get_backends(return_tuples=True)
            if len(backends) == 1:
                backend, _ = backends[0]
            else:
                raise ValueError(
                    'You have multiple authentication backends configured and '
                    'therefore must provide the `backend` argument.'
                )
        elif not isinstance(backend, str):
            raise TypeError(
                'backend must be a dotted import path string (got %r).'
                % backend
            )
        else:
            backend = auth.load_backend(backend)
        if hasattr(backend, 'with_perm'):
            return backend.with_perm(
                perm,
                is_active=is_active,
                include_superusers=include_superusers,
                obj=obj,
            )
        return self.none()

class SexChoices(models.TextChoices):
    MEN = '男性'
    WOMEN = '女性'
    Other = 'その他'

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField("メールアドレス",unique=True)

    name = models.CharField("名前", max_length=150, blank=True)
    address = models.CharField("住所", max_length=150, blank=True)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    tel = models.CharField("電話番号",validators = [phoneNumberRegex], max_length = 16,null=True,blank=True)

    gender = models.CharField(
        '性別',
        choices=SexChoices.choices,
        max_length=3,
        null=True,blank=True
    )



    is_staff = models.BooleanField(
        _('staff status'),
        default=False,
        help_text=_('管理者ならTrue.'),
    )
    is_active = models.BooleanField(
        _('active'),
        default=True,
        help_text=_('在籍者ならTrue'),
    )


    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')


    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)
