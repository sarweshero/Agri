from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("The Phone Number field must be set")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(phone_number, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    phone_number = models.CharField(max_length=15, unique=True)
    name = models.CharField(max_length=30, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    email = models.EmailField(unique=True, blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone_number

class landprep(models.Model):
    farmer_name = models.CharField(max_length=100)
    cultivation_area = models.CharField(max_length=100)
    date = models.DateField()
    fertilizer = models.CharField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='landprep_photos/')
    belongs_to = models.IntegerField()
    def __str__(self):
        return f"Land Preparation on {self.date} with {self.fertilizer}"
class transplanting(models.Model):
    date = models.DateField()
    seed_variety = models.CharField(max_length=100)
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='transportation_photos/')
    belongs_to = models.IntegerField()
    def __str__(self):
        return f"Transplanting on {self.date} with {self.seed_variety}"
    
class fertilizer(models.Model):
    date = models.DateField()
    application_type = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='fertilizer_photos/')
    belongs_to = models.IntegerField()
    def __str__(self):
        return f"Fertilizer Application on {self.date} with {self.application_type}"
class harverst(models.Model):
    seed_variety = models.CharField(max_length=100)
    date = models.DateField()
    photo = models.ImageField(upload_to='harvest_photos/')
    belongs_to = models.IntegerField()
    def __str__(self):
        return f"Harvest on {self.date} with {self.seed_variety}"
class packaging(models.Model):
    seed_variety = models.CharField(max_length=100)
    date = models.DateField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='packaging_photos/')
    belongs_to = models.IntegerField()
    def __str__(self):
        return f"Packaging on {self.date} with quantity {self.quantity}"
    
class Procurement(models.Model):
    procurer_name = models.CharField(max_length=100)
    farmer_name = models.CharField(max_length=100)
    seed_variety = models.CharField(max_length=100)
    lot_id = models.CharField(max_length=100)
    date = models.DateField()
    quantity = models.IntegerField()
    avg_price = models.IntegerField()
    photo = models.ImageField(upload_to='procurement_photos/')
    belongs_to = models.IntegerField()
    def __str__(self):
        return f"Procurement of {self.seed_variety} from {self.farmer_name} on {self.date}"
class packing(models.Model):
    lot_id = models.CharField(max_length=100)
    date = models.DateField()
    avg_sale_price = models.IntegerField()
    quantity = models.IntegerField()
    photo = models.ImageField(upload_to='packing_photos/')
    belongs_to = models.IntegerField()
    def __str__(self):
        return f"Packing on {self.date} with quantity {self.quantity}"