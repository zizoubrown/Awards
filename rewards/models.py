from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from cloudinary.models import CloudinaryField
from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Profile(models.Model):
    profilePic = models.ImageField(upload_to='profile/',null=True)
    bio = models.CharField(max_length=60,blank=True)
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.user.username} Profile'

    
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        try:
            instance.profile.save()
        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()
    
    def create_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Image(models.Model):
    image = models.ForeignKey(Image, on_delete = models.CASCADE)
    name = models.CharField(max_length=30)
    caption = models.CharField(max_length = 60)
    upload_date = models.DateTimeField(default=timezone.now)
    # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes = models.PositiveIntegerField(default=0)
    link = models.CharField(max_length=100)

    @classmethod
    def search_by_name(cls,search_term):
        jake = cls.objects.filter(name__icontains=search_term)
        return jake

    def no_of_ratings(self):
        ratings = Rating.objects.filter(image=self)
        return len(ratings)

    def avg_rating(self):
        sum = 0
        ratings = Rating.objects.filter(image=self)
        for rating in ratings:
            sum += rating.stars
        if len(ratings) > 0:
            return ' '.join(['Average rating',str(sum / len(ratings))])
        else:
            return 'No ratings yet'

    def __str__(self):
        return self.caption
    class Meta:
        ordering = ['-upload_date']

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()

    @classmethod
    def update_caption(cls,id,caption):
        captioned = Image.objects.filter(id=id).update(caption = caption)
        return captioned

    @classmethod
    def get_all(cls):
        imgs = Image.objects.all()
        return imgs

    @classmethod
    def get_image_by_id(cls,id):
        image = Image.objects.filter(id=Image.id)
        return image

class Rating(models.Model):
  image = models.ForeignKey(Image, on_delete = models.CASCADE)
  user = models.ForeignKey(User, on_delete = models.CASCADE)
  stars = models.IntegerField(validators = [MinValueValidator(1),MaxValueValidator(5)])