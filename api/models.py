import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import os
from django.core.validators import FileExtensionValidator, MaxValueValidator, MinValueValidator

class ActiveManager(models.Manager):

    def get_queryset(self):

        return (
            super()
            .get_queryset()
            .filter(is_deleted=False)
        )


# =====================================================
# BASE MODEL
# =====================================================

class BaseModel(models.Model):

    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(
        default=False,
        db_index=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    objects = ActiveManager()
    all_objects = models.Manager()

    class Meta:
        abstract = True

    def soft_delete(self):

        self.is_deleted = True
        self.is_active = False
        self.save(
            update_fields=[
                "is_deleted",
                "is_active"
            ]
        )

    def restore(self):
        self.is_deleted = False
        self.is_active = True
        self.save(
            update_fields=[
                "is_deleted",
                "is_active"
            ]
        )

    def delete(self, *args, **kwargs):
        self.soft_delete()

class User(AbstractUser):
    pass

# =========================
# Service Model
# =========================
class Service(BaseModel):
    title = models.CharField(max_length=200)
    description = models.TextField()
    icon = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.title


# =========================
# Portfolio Model
# =========================

def portfolio_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('portfolio', filename)

class Portfolio(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(
        upload_to=portfolio_image_upload_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpg', 'jpeg', 'webp']
            )
        ],
        null=True,
        blank=True
    )
    project_url = models.URLField(blank=True, null=True)
    technologies = models.CharField(
        max_length=255,
        help_text="Comma separated values"
    )
    featured = models.BooleanField(default=False)

    

    def __str__(self):
        return self.title


# =========================
# Testimonial Model
# =========================

def testimonial_image_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4().hex}.{ext}"
    return os.path.join('testimonial', filename)

class Testimonial(BaseModel):
    client_name = models.CharField(max_length=200)
    company = models.CharField(max_length=200, blank=True, null=True)
    feedback = models.TextField()
    rating = models.PositiveIntegerField(
        default=5,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    
    image = models.ImageField(
        upload_to=testimonial_image_upload_path,
        validators=[
            FileExtensionValidator(
                allowed_extensions=['png', 'jpg', 'jpeg', 'webp']
            )
        ],
        null=True,
        blank=True
    )
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return self.client_name

# =========================
# Contact / Enquiry Model
# =========================
class Enquiry(BaseModel):

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # ForeignKey to Service Model
    service_interest = models.ForeignKey(
        Service,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='enquiries'
    )
    message = models.TextField()
    #Is used to track whether the admin has viewed or handled an enquiry.
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# =========================
# Newsletter Subscriber Model
# =========================
class NewsletterSubscriber(BaseModel):

    email = models.EmailField(
        unique=True
    )
    subscribed_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.email

    class Meta:
        ordering = ['-subscribed_at']
        verbose_name = 'Newsletter Subscriber'
        verbose_name_plural = 'Newsletter Subscribers'

    
class EmailTemplate(BaseModel):
    type = models.CharField(max_length=12)

    template_identifier = models.CharField(
        max_length=100,
        null=True,
        blank=True
    )

    template_subject = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )

    template_content = models.TextField(
        null=True,
        blank=True
    )

    template_keyword = models.TextField(
        null=True,
        blank=True
    )

    body_font_style = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    footer_font_style = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )
   

    def __str__(self):
        return f"Template {self.template_identifier}"