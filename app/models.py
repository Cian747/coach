from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


# Create your models here.

class Sport(models.Model):
    '''
    Use this to pick the sport you would like to view categorically
    '''
    sport_image = CloudinaryField('image',blank=True, null=True)
    name = models.CharField(max_length=150,null=True, blank=True)
    description = models.TextField(null=True,blank=True)
# Add the profile relation key here
    def __str__(self) -> str:
       return self.name #type:ignore
    
    def save_sport(self):
        return self.save()


class Location(models.Model):
    name = models.CharField(max_length=255, unique=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    sport = models.ForeignKey(Sport, on_delete=models.CASCADE, null=True, blank=True)

    def save_location(self):
        return self.save()

    def __str__(self):
        return self.name

class Profile(models.Model):
    ADMIN = 1
    STUDENT = 2

    USER_ROLE_CHOICES = (
        (ADMIN, 'Coach'),
        (STUDENT, 'Client'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=False)
    sport = models.ForeignKey(Sport, on_delete=models.SET_NULL, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True, blank=True)
    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES, blank=True, null=True, default=2)
    profile_photo = CloudinaryField('profile_image',null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    specialization = models.CharField(max_length=255, blank=True, null=True)
    certifications = models.TextField(blank=True, null=True)
    experience_years = models.PositiveIntegerField(default=0)
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='supporters')

    def __str__(self) -> str:
        return f"{self.user.username} - {self.sport.name if self.sport else 'No Sport'}"

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        return self.save()

    def delete_profile(self):
        return self.delete()

    @classmethod
    def update_profile_photo(cls, id,coach_email):
        return cls.objects.filter(id = id).update(coach_email=coach_email)

    
    @classmethod
    def search_username(cls,search_term):
        return cls.objects.filter(user__username__icontains = search_term)


    def get_absolute_url(self):
        return reverse('profile',args=[str(self.id)])

        # return reverse('home')
    
    def __str__(self) -> str:
       return self.user.username

# class Enquiry(models.Model):
#     profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
#     question = models.TextField()
#     sent_on = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.profile.user.username

#     def save_enquiry(self):
#         return self.save()

class SportAdvert(models.Model):
    sport_punchline = models.CharField(max_length=50)
    service_image = CloudinaryField('image',blank=True,null=True)
    related_sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    description = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE,null=True,blank=True)


    def __str__(self) -> str:
       return self.sport_punchline
    
    def save_service(self):
        return self.save()


class Wishlist(models.Model):
    '''
    A user can add services they are interested in following or trying out
    '''
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_name = models.ForeignKey(SportAdvert,on_delete=models.CASCADE)
    sport = models.ForeignKey(Sport,on_delete=models.CASCADE)
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
       return self.service_name
    
    def save_wishlist(self):
        return self.save()

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.IntegerField(default=0,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
       return self.profile.coach_name

    def save_comment(self):
        return self.save()


