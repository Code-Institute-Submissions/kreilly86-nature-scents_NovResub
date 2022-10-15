from django.db import models


class NewsletterInput(models.Model):
    """
    Creates a newsletter model for users
    to sign-up for updates
    """
    email = models.EmailField(max_length=254, null=False, blank=False)

    def __str__(self):
        return self.email



