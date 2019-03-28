from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, AbstractBaseUser, BaseUserManager


class CustomAccountManager(BaseUserManager):
    def create_user(self, email, first_name, last_name, password, user_type, date_of_birth=None,
                    middle_name=None, phone_number=None):

        user = self.model(first_name=first_name, last_name=last_name, middle_name=middle_name, email=email,
                          date_of_birth=date_of_birth, user_type=user_type, phone_number=phone_number, password=password)
        user.set_password(password)
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)

        return user

    def get_by_natural_key(self, email_):
        print(email_)
        return self.get(email=email_)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    u_types = (
        ('owner', 'Owner')
        , ('tenant', 'Tenant')
    )

    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    middle_name = models.CharField(verbose_name='middle name', max_length=150, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    date_of_birth = models.DateTimeField(null=True, blank=True)
    phone_number = models.DateField(null=True, blank=True)

    user_type = models.CharField(choices=u_types, max_length=25, blank=False, null=False)

    REQUIRED_FIELDS = ['first_name', 'last_name', 'user_type']
    USERNAME_FIELD = 'email'

    objects = CustomAccountManager()

    def get_short_name(self):
        return self.email

    def natural_key(self):
        return self.email

    def __str__(self):
        return self.email


class Listing(models.Model):
    title = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000)
    is_available = models.BooleanField(default=True)
    internal_review = models.BooleanField(default=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    rent = models.IntegerField(verbose_name='Listing rent')
    payable = models.IntegerField(verbose_name='Amount left pay')

    class Meta:
        unique_together = ('title', 'owner',)


class Applicants(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    # Tenant foreign key
    applicant = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('listing', 'applicant', )


class AcceptedApplicants(models.Model):
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)

    # Tenant foreign key
    applicant = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)

    class Meta:
        unique_together = ('listing', 'applicant', )
