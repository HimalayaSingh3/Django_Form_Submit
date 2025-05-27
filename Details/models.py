from django.db import models

# Gender choices
GENDER_CHOICES = [
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

class FormDetails(models.Model):
    form_name = models.CharField(max_length=255, unique=True)
    form_gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='Other')
    form_age = models.PositiveIntegerField()
    form_email = models.EmailField(blank=True, null=True)
    form_phone = models.CharField(max_length=15, blank=True, null=True)
    form_address = models.TextField(blank=True, null=True)
    form_city = models.CharField(max_length=100, blank=True, null=True)
    form_state = models.CharField(max_length=100, blank=True, null=True)
    form_zip_code = models.CharField(max_length=20, blank=True, null=True)
    form_country = models.CharField(max_length=100, blank=True, null=True)
    form_experience = models.CharField(max_length=100, blank=True, null=True)
    form_skills = models.TextField(blank=True, null=True)
    form_education = models.CharField(max_length=255, blank=True, null=True)
    form_message = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.form_name
    class Meta:
        verbose_name = 'Form Detail'
        verbose_name_plural = 'Form Details'
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['form_name']),
            models.Index(fields=['form_email']),
        ]
