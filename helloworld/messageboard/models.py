# messageboard/models.py
from django.db import models

class Message(models.Model):
    sender_name = models.CharField(max_length=100)  # User submitting's name
    receiver_name = models.CharField(max_length=100)  # User Receiving's name
    message_text = models.TextField()  # Content 
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"Message from {self.sender_name} to {self.receiver_name} at {self.timestamp}"
