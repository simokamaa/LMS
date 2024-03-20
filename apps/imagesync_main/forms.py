from django import forms
from .models import (
    UserProfile, Image, BrandGuidelines, Feedback, Subscription, Payment, ProcessedImages, Language,
    ImageLanguage, AnalyticsData, SystemUpdate, ErrorLog, HelpResource,
    FAQ, Notification, ThirdPartyService, Backup, LoadBalancer, EmailTemplate, RegulatoryRequirement
)

class FAQForm(forms.ModelForm):
    class Meta:
        model = FAQ
        fields = "__all__"

class RegulatoryRequirementForm(forms.ModelForm):
    class Meta:
        model = RegulatoryRequirement
        fields = "__all__"

class EmailTemplateForm(forms.ModelForm):
    class Meta:
        model = EmailTemplate
        fields = "__all__"

class LoadBalancerForm(forms.ModelForm):
    class Meta:
        model = LoadBalancer
        fields = "__all__"

class BackupForm(forms.ModelForm):
    class Meta:
        model = Backup
        fields = "__all__"

class ThirdPartyServiceForm(forms.ModelForm):
    class Meta:
        model = ThirdPartyService
        fields = "__all__"

class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = "__all__"


class HelpResourceForm(forms.ModelForm):
    class Meta:
        model = HelpResource
        fields = "__all__"

class SystemUpdateForm(forms.ModelForm):
    class Meta:
        model = SystemUpdate
        fields = '__all__'

class ErrorLogForm(forms.ModelForm):
    class Meta:
        model = ErrorLog
        fields = '__all__'

class  AnalyticsDataForm(forms.ModelForm):
    class Meta:
        model =  AnalyticsData
        fields = '__all__'
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['bio', 'profile_picture']  # Add fields as needed

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']  # Add fields as needed

class BrandGuidelinesForm(forms.ModelForm):
    class Meta:
        model = BrandGuidelines
        fields = ['company_name', 'guidelines_file']  # Add fields as needed

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ['feedback_text']  # Add fields as needed

class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ['plan_type']  # Add fields as needed

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount']  # Add fields as needed

class ProcessedImagesForm(forms.ModelForm):
    class Meta:
        model = ProcessedImages
        fields = ['processed_image']  # Add fields as needed

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name']  # Add fields as needed

class ImageLanguageForm(forms.ModelForm):
    class Meta:
        model = ImageLanguage
        fields = ['language']  # Add fields as needed

# Repeat the above pattern for other models...

# Add more form models as needed for additional functionalities
