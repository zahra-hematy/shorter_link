from django.db import models

# Create your models here.



from django.contrib.auth.models import User

# User = get_current_user()



class Link(models.Model):
    url_long = models.URLField()
    url_short = models.CharField(max_length=20, blank=True, null=True)
    create = models.DateTimeField(auto_now_add=True, verbose_name='تاریخ')   
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="linkup", verbose_name='ارسال کننده', null=True, blank=True)
    def __str__(self):
        return self.url_short
