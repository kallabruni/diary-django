from django.db import models

class Card(models.Model):
    STATUS_CARD = (
        ('visible', 'Visible'),
        ('not_visible', 'Not_visible'),
    )
    card_date_long = models.DateTimeField(auto_now_add=True)
    card_date_short = models.DateField(auto_now_add=True)
    card_date_hapend = models.DateTimeField(auto_now_add=False)
    card_images = models.ImageField(upload_to="card_images", null=True, blank=True)
    card_title = models.CharField(max_length=64, blank=False, unique=True)
    card_description = models.TextField(default="")
    status = models.CharField(max_length=12, choices=STATUS_CARD, default='visible')


    class Meta:
        verbose_name="card"

    def __str__(self):
        return self.title_date()

    def title_date(self):
        return "{} ({})".format(self.card_title, self.card_date_long)
