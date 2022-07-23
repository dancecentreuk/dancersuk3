from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from pages.choices import location_choices, gender_choices, hair_color_choices, eye_color_choices, build_choices, \
    primary_job_choices, cm_choices, kg_choices, ethnicity_choices, skin_choices, height_choices, dress_choices
from PIL import Image
from django.core.files.storage import default_storage
from io import BytesIO
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify
from datetime import datetime






# Create your models here.



class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('Your email is not correct')

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self._create_user(email, password, **extra_fields)

class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=200, blank=False)
    last_name = models.CharField(_('last name'), max_length=200, blank=False)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('is staff'), default=False)
    is_dancer = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

    # def get_absolute_url(self):
    #     return reverse('users:profile', kwargs={'pk': self.id})




    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def has_company_profile(self):
        return hasattr(self, 'company_profile')


    def has_dancers_profile(self):
        return hasattr(self, 'dancers_profile')

    def has_customer_membership(self):
        return hasattr(self, 'customer_membership')










class Profile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='profile')
    profile_image = models.ImageField(upload_to='media/users', default='media/users/person_1.jpg')
    date_of_birth = models.DateField(default=None, blank=True, null=True)
    location = models.CharField(max_length=100,
                                blank=False,
                                default=None,
                                choices=location_choices,
                                null=True)
    mobile = models.CharField(max_length=20)
    gender = models.CharField(choices=gender_choices,
                              default=None,
                              blank=True,
                              max_length=1,
                              null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    stripeid = models.CharField(max_length=255, null=True, blank=True)
    stripesubscription = models.CharField(max_length=255, null=True, blank=True)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
    paid_until = models.DateField(null=True, blank=True)




    def __str__(self):
        return self.user.first_name + ' '+self.user.last_name +' '+self.user.email

    # def calculate_age(self):
    #     return (date.today() - self.date_of_birth) // timedelta(days=365.2425)

    def calculate_age(self):
        if self.date_of_birth is None:
            pass
        else:
            return int((datetime.now().date() - self.date_of_birth).days / 365.25)

    def membership_status(self):
        if self.membership == True:
            return ('Valid membership')
        else:
            return ('no membership')



    # def save(self, *args, **kwargs):
    #     super(Profile, self).save(*args, **kwargs)
    #     memfile = BytesIO()
    #     img = Image.open(self.profile_image)
    #     if img.height > 200 or img.width > 200:
    #         new_size = (200, 200)
    #         img.thumbnail(new_size, Image.ANTIALIAS)
    #         img.save(memfile, 'PNG', quality=95)
    #         default_storage.save(self.profile_image.name, memfile)
    #         memfile.close()
    #         img.close()
    #         img.thumbnail(new_size)
    #         img.save(self.profile_image.path)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        memfile = BytesIO()

        img = Image.open(self.profile_image)
        if img.height > 500 or img.width > 500:
            output_size = (500, 500)
            img.thumbnail(output_size, Image.ANTIALIAS)
            img.save(memfile, 'PNG', quality=95)
            default_storage.save(self.profile_image.name, memfile)
            memfile.close()
            img.close()






@receiver(models.signals.post_save, sender=Account)
def post_save_user_signal(sender, instance, created, **kwargs):
    if created:
        instance.save()


def create_user_profile(sender, instance, created,  **kwargs,):
    location = getattr(instance, '_location', None)
    gender = getattr(instance, '_gender', None)
    date_of_birth = getattr(instance, '_date_of_birth', None)
    print(location)
    if created:
        Profile.objects.create(user=instance, location=location, gender=gender, date_of_birth=date_of_birth)


post_save.connect(create_user_profile, sender=Account)


class Customer(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='customer_membership')
    stripeid = models.CharField(max_length=255)
    stripe_subscription_id = models.CharField(max_length=255)
    cancel_at_period_end = models.BooleanField(default=False)
    membership = models.BooleanField(default=False)
    paid_until = models.DateField(null=True, blank=True)



class CompanyProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='company_profile')
    company_image = models.ImageField(upload_to='media/company_images', default='media/users/person_1.jpg')
    company_name = models.CharField(max_length=200)
    company_email = models.CharField(max_length=250)
    company_mobile = models.CharField(max_length=20, blank=True)
    company_bio = RichTextField(blank=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.first_name + ' '+self.user.email +' '+self.company_name


class DancersProfile(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='dancers_profile')
    location = models.CharField(max_length=100,
                                blank=False,
                                default='no-option',
                                choices=location_choices)
    dancers_image = models.ImageField(upload_to='media/dancers_images', default='media/users/person_1.jpg')
    bio = RichTextField(blank=True)
    experience = RichTextField(blank=True)
    credits = RichTextField(blank=True)
    primary_job = models.CharField(max_length=20,
                                   blank=True,
                                   default='0',
                                   choices=primary_job_choices)
    waist = models.IntegerField(blank=True,
                                   default='0',
                                   choices=cm_choices)
    build = models.CharField(max_length=30,
                             blank=True,
                             null=True,
                             choices=build_choices)
    bust = models.IntegerField(blank=True,
                             default='0',
                             choices=cm_choices)
    hip = models.IntegerField(blank=True,
                               default='0',
                               choices=cm_choices)
    height = models.IntegerField(blank=True,
                              default='0',
                              choices=height_choices)
    weight = models.IntegerField(blank=True,
                              choices=kg_choices)
    dress = models.CharField(max_length=20,
                            blank=True,
                            default='Not Applicable',
                            choices=dress_choices)
    # weight = models.IntegerField(choices=list(zip(range(10, 140), range(10, 140))), unique=True, blank=True, null=True)
    hair = models.CharField(max_length=20,
                            blank=True,
                            default='no-option',
                            choices=hair_color_choices)
    eye = models.CharField(max_length=20,
                           blank=True,
                           default='no-option',
                           choices=eye_color_choices)
    ethnicity = models.CharField(max_length=30,
                                 blank=True,
                                 default='no-option',
                                 choices=ethnicity_choices)

    skin = models.CharField(max_length=30,
                                 blank=True,
                                 default='no-option',
                                 choices=skin_choices)




    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default=None, editable=False)

    def __str__(self):
        return self.user.first_name + ' '+self.user.last_name +' '+self.user.email

    def save(self, *args, **kwargs):
        self.slug = slugify(self.user.first_name)
        super(DancersProfile, self).save(*args, **kwargs)

    def calculate_feet(self):
        if self.height is None:
            pass
        else:
            return self.height * 0.03281


class DancerImage(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/dancers_image_collection/%Y/%m/%d')
    owner = models.ForeignKey(DancersProfile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.owner)










