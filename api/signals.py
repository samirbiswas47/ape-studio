from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Enquiry, EmailTemplate
from django.conf import settings
from .email import email_body
from .utils import replace_email_keywords


@receiver(post_save, sender=Enquiry)
def send_welcome_email(sender, instance, created, **kwargs):

    if not created:
        return

    try:

        template = EmailTemplate.objects.filter(
            template_identifier='Acknowledgment email for enquiry form submission',
            is_active=1
        ).first()

        # Validation: template not found
        if not template:
            print("EMAIL ERROR: Template not found")
            return

        # Validation: template content empty
        if not template.template_content:
            print("EMAIL ERROR: Template content is empty")
            return

        # Validation: subject empty
        if not template.template_subject:
            print("EMAIL ERROR: Template subject is empty")
            return

        # Validation: user email empty
        if not instance.email:
            print("EMAIL ERROR: User email is empty")
            return

        keywords = {
            '###NAME###': instance.name,
            '###SERVICE_INTEREST###': instance.service_interest.title
        }

        content = replace_email_keywords(
            template.template_content,
            keywords
        )

        final_html = email_body(content)

        email = EmailMultiAlternatives(
            subject=template.template_subject,
            body='Welcome Email',
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[instance.email]
        )

        email.attach_alternative(final_html, "text/html")

        email.send()

        print("EMAIL SENT")

    except Exception as e:
        print("EMAIL ERROR:", e)