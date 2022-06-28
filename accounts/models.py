from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have email address')
        if not username:
            raise ValueError('User must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, first_name, last_name, username, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )
        user.is_admin=True
        user.is_active=True
        user.is_satff=True
        user.is_superadmin=True
        user.save()
        return user
        
SECTOR = (
    ('West', 'West'),
    ('East', 'East'),
)

ROLE = (
    ('Doctor', 'Doctor'),
)


class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    username = models.CharField(max_length=60, unique=True)
    email = models.EmailField(max_length=160, unique=True)
    phone = models.CharField(max_length=50)

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'username',
        'first_name',
        'last_name',
    ]
    
    objects = MyAccountManager()

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.email}'

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True


class Employee(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    ssn = models.IntegerField(unique=True, verbose_name='Social security number')
    home_address = models.CharField(max_length=65, verbose_name='Home address')
    office_address = models.CharField(max_length=150, verbose_name='Office address')
    role = models.CharField(max_length=20, choices=ROLE)
    sector = models.CharField(max_length=20, choices=SECTOR)

    def __str__(self):
        return f'{self.account.full_name()} {self.role} '


