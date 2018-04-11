from django.db import models
from hidegram.users import models as user_models

class TimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Image(TimeStampModel):
    file = models.ImageField()
    location = models.CharField(max_length=140)
    caption = models.TextField()

    def __str__(self):
        return '{} - {}'.format(self.location, self.caption)

class Comment(TimeStampModel):
    message = models.TextField()
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.message

class Like(TimeStampModel):
    creator = models.ForeignKey(user_models.User, on_delete=models.PROTECT, null=True)
    image = models.ForeignKey(Image, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return 'User :{} / Image Caption :{}'.format(self.creator.username, self.image.caption)