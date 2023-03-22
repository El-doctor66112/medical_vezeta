from django.db import models
from django.contrib.auth.models import User
# from django.utils.translation import ugettext_lazy as _


from django.db.models.signals import post_save
from django.utils.text import slugify


TYPE_OF_PERSON = (
    ('M', "Male"),
    ('F', "Female")
)


class Profile(models.Model):

    DOCTOR_IN = (
        ('عظام', "عظام"),
        ('جلدية', "جلدية"),
        ('جراحة عظام', "جراحة عظام"),
        ('اطفال', "اطفال"),
        ('نساء وتوليد', "نساء وتوليد"),
        ('باطنة', "باطنة"),
        ('جراحة عامة', "جراحة عامة"),
    )

    user = models.OneToOneField(
        User, verbose_name=("user"), on_delete=models.CASCADE)
    name = models.CharField("name", max_length=80)
    surname = models.CharField("sur name", max_length=50)
    subtitle = models.CharField("sub title", max_length=50)
    address = models.CharField("Address", max_length=50)
    address_detail = models.CharField("Address detail", max_length=50)
    number_phone = models.CharField("phone", max_length=50)
    working_hours = models.CharField("working hours", max_length=50)
    waiting_time = models.IntegerField(
        "waiting time", blank=True, null=True)
    who_i = models.TextField("who i", max_length=250)
    price = models.IntegerField("price", blank=True, null=True)
    facebook = models.CharField(max_length=100, blank=True, null=True)
    '''
    twitter = models.CharField(max_length=100, blank=True, null=True)
    google = models.CharField(max_length=100, blank=True, null=True)
    '''
    join_new = models.DateTimeField(
        "join us", auto_now_add=True, )
    type_of_person = models.CharField(
        "gender", choices=TYPE_OF_PERSON, max_length=50)
    doctor = models.CharField(
        "doctor", choices=DOCTOR_IN, max_length=50, blank=True, null=True)
    image = models.ImageField(
        "image", upload_to='profile', blank=True, null=True)
    specialist_doctor = models.CharField(
        "specialist at", max_length=50, blank=True, null=True)
    slug = models.SlugField("slug", blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.user.username)
        super(Profile, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return '%s' % (self.user.username)


def create_profile(sender, **kwargs):
    if kwargs['created']:
        Profile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
