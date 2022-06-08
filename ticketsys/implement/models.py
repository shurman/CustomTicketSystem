from django.db import models
from django.utils import timezone
from django.conf import settings

# Create your models here.

STATE_CHO = (
    ('0', "Open"),
    ('1', "Resolve"),
    ('2', "Close")
)

TICKET_TYPE = (
    ('0', "Bug"),
    ('1', "Feature Request"),
    ('2', "Test Case"),
)
SEVERITY_CHO = (
    ('0', "Low"),
    ('1', "Medium"),
    ('2', "High")
)

class Ticket(models.Model):
    title = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    status = models.CharField(max_length=2, choices=STATE_CHO, default='0')

    t_type = models.CharField("Type", max_length=2, choices=TICKET_TYPE, default='0')
    severity = models.CharField(max_length=2, choices=SEVERITY_CHO, default='0')

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    create_date = models.DateTimeField(default=timezone.now)
    last_date = models.DateTimeField(null=True)


