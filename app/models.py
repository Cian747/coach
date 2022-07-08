from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse

# Create your models here.

class Sport(models.Model):
    sport_image = CloudinaryField('image',blank=True, null=True)
    name = models.CharField(max_length=150,null=True, blank=True)
    description = models.TextField()

    def __str__(self) -> str:
       return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    coach_name = models.CharField(max_length=50,null=True,blank=True)
    profile_photo = CloudinaryField('image',blank=True,null=True)
    sport = models.ForeignKey(Sport, on_delete=models.DO_NOTHING,null=True)
    coach_email = models.EmailField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

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

class Enquiry(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    question = models.TextField()
    sent_on = models.DateTimeField(auto_now_add=True)

class Services(models.Model):
    sport_punchline = models.CharField(max_length=50)
    service_image = CloudinaryField('image',blank=True,null=True)
    related_sport = models.ForeignKey(Sport, on_delete=models.CASCADE)
    description = models.TextField()
    created_at =  models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(Profile, on_delete=models.CASCADE)


    def __str__(self) -> str:
       return self.sport_punchline


class Wishlist(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_name = models.ForeignKey(Services,on_delete=models.CASCADE)
    saved_on = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
       return self.service_name


