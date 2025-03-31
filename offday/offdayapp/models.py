from django.db import models

class TeamMember(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class OffDay(models.Model):
    OFFDAY_CHOICES = [
        ('off', 'Off'),
        ('leave', 'Leave')
    ]
    
    team_member = models.ForeignKey(TeamMember, on_delete=models.CASCADE)
    day = models.CharField(max_length=10)  # Example: "Monday"
    type = models.CharField(max_length=10, choices=OFFDAY_CHOICES, default='off')

    def __str__(self):
        return f"{self.team_member.name} - {self.day} ({self.get_type_display()})"
