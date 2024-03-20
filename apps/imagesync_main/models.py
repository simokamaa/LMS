from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add fields for personal and professional details as required
    # Example:
    # bio = models.TextField(blank=True)
    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True)

class Image(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='user_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed for image metadata or processing status

class BrandGuidelines(models.Model):
    company_name = models.CharField(max_length=100)
    guidelines_file = models.FileField(upload_to='brand_guidelines/')

class Feedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedback_text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Subscription(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Add fields for subscription details (e.g., plan type, renewal date)

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    # Add fields for payment details (e.g., transaction ID, payment status)

class ProcessedImages(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    original_image = models.ForeignKey(Image, on_delete=models.CASCADE)
    processed_image = models.ImageField(upload_to='processed_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed for processed image metadata

class Language(models.Model):
    name = models.CharField(max_length=50)

class ImageLanguage(models.Model):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

class AnalyticsData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed for tracking analytics data

class SystemUpdate(models.Model):
    description = models.TextField()
    update_date = models.DateField()
    # Add fields for tracking system updates

class ErrorLog(models.Model):
    error_message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed for logging errors

class HelpResource(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Add more fields as needed for help resources

class FAQ(models.Model):
    question = models.CharField(max_length=200)
    answer = models.TextField()
    # Add more fields as needed for frequently asked questions

class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Add more fields as needed for notifications

class ThirdPartyService(models.Model):
    name = models.CharField(max_length=100)
    api_key = models.CharField(max_length=200)
    # Add more fields as needed for third-party service integration

class Backup(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    # Add fields for backup details (e.g., backup location, status)

class LoadBalancer(models.Model):
    name = models.CharField(max_length=100)
    ip_address = models.CharField(max_length=15)
    # Add fields for load balancer details (e.g., status, capacity)

class EmailTemplate(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    # Add more fields as needed for email templates

class RegulatoryRequirement(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Add more fields as needed for regulatory requirements

# Add more models as needed for additional functionalities
