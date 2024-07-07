
from django.db import models
from django.contrib.auth.models import User
from reviews.models import Review

class LikeReview(models.Model):
    """
    LikeReview model, related to 'owner' and 'review'. The 'unique_together'
    attribute ensures Users can't like the same comment twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(
        Review,
        related_name='likes',
        on_delete=models.CASCADE
    )
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']
        unique_together = ['owner', 'review']

    def __str__(self):
        return f'{self.owner} {self.review}'