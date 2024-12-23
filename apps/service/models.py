from django.db import models

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # icon = models.ImageField(upload_to='service/icons/%Y/%m/%d')

    def __str__(self):
        return self.title
    

class FeedbackClient(models.Model):
    full_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='services/feedback_client/%Y/%m/%d')
    feedback_text = models.TextField()
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.full_name


