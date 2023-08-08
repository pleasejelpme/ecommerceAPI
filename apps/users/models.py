from django.db import models
from django.contrib.auth.models import UserManager, AbstractBaseUser, PermissionsMixin
from simple_history.models import HistoricalRecords
from phonenumber_field.modelfields import PhoneNumberField

class UserManager(UserManager):
    def _create_user(self, email, password, **kwargs):
        if not email:
            raise ValueError('User must have an email address')
        
        if not password:
            raise ValueError('User must have a password') 
        
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email=None, password=None, **kwargs):
        kwargs.setdefault('is_staff', False)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email=None, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', True)
        return self._create_user(email, password, **kwargs)

    def create_staff_user(self, email=None, password=None, **kwargs):
        kwargs.setdefault('is_staff', True)
        kwargs.setdefault('is_superuser', False)
        return self._create_user(email, password, **kwargs)
    

    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField('Name', max_length=255, blank=True, null=True)
    last_name = models.CharField('Last name', max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    historical = HistoricalRecords()
    objects = UserManager()

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'
    
    def __str__(self):
        return self.email