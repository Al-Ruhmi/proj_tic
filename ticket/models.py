import uuid
from django.db import models
from users.models import User
# Create your models here.


class Ticket(models.Model):

    TASK = (
        ('Opening','Opening'),
        ('Processing','Processing'),
        ('Completed','Completed'),
        ('Rejected','Rejected'),
        )
            
    
    ticket_number = models.UUIDField(default=uuid.uuid4)

    title = models.CharField(max_length=100)
    content = models.TextField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_by')
    assigned_to = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    accepted_date = models.DateTimeField(null=True, blank=True)
    closed_date = models.DateTimeField(null=True , blank=True)
    ticket_status = models.CharField(max_length=15, choices=TASK)
    is_resolved = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title


