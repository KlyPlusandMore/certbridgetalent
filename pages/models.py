from django.db import models

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('security', 'Information Security'),
        ('quality', 'Quality & Risk'),
        ('resilience', 'Continuity & Resilience'),
        ('technical', 'Technical & HSE'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']

class Registration(models.Model):
    FORMAT_CHOICES = [
        ('physical', 'Physical (Classroom)'),
        ('virtual', 'Virtual (Online)'),
    ]
    
    STATUS_CHOICES = [
        ('pending', 'Pending Approval'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='registrations')
    training_format = models.CharField(max_length=20, choices=FORMAT_CHOICES, default='physical')
    message = models.TextField(blank=True, null=True, help_text="Additional requests or information")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.course.title}"

    class Meta:
        ordering = ['-created_at']
