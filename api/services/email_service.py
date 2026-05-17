# =====================================================
# api/services/email_service.py
# =====================================================

from django.conf import settings
from django.core.mail import EmailMultiAlternatives

from api.models import EmailTemplate
from api.email import email_body
from api.utils import (
    replace_email_keywords,
    send_async_email
)


def send_enquiry_acknowledgement(instance):

    try:

        print("STEP 1")

        template = EmailTemplate.objects.filter(
            template_identifier=(
                'Acknowledgment email for enquiry form submission'
            ),
            is_active=True
        ).first()

        print("STEP 2")

        # =================================================
        # VALIDATIONS
        # =================================================

        if not template:

            print(
                "EMAIL ERROR: Template not found"
            )

            return False

        if not template.template_content:

            print(
                "EMAIL ERROR: Template content empty"
            )

            return False

        if not template.template_subject:

            print(
                "EMAIL ERROR: Template subject empty"
            )

            return False

        if not instance.email:

            print(
                "EMAIL ERROR: User email empty"
            )

            return False

        print("STEP 3")

        # =================================================
        # KEYWORDS
        # =================================================

        keywords = {

            '###NAME###': (
                instance.name
            ),

            '###SERVICE_INTEREST###': (
                str(
                    instance.service_interest
                ).title()
            ),
        }

        print("STEP 4")

        # =================================================
        # REPLACE TEMPLATE KEYWORDS
        # =================================================

        content = replace_email_keywords(
            template.template_content,
            keywords
        )

        print("STEP 5")

        # =================================================
        # FINAL HTML
        # =================================================

        final_html = email_body(content)

        print("STEP 6")

        # =================================================
        # EMAIL OBJECT
        # =================================================

        email = EmailMultiAlternatives(

            subject=template.template_subject,

            body='Acknowledgement Email',

            from_email=(
                settings.DEFAULT_FROM_EMAIL
            ),

            to=[instance.email]
        )

        email.attach_alternative(
            final_html,
            "text/html"
        )

        print("STEP 7")

        # =================================================
        # SEND EMAIL
        # =================================================

        if settings.DEBUG:

            email.send(
                fail_silently=False
            )

            print(
                "SYNC EMAIL SENT"
            )

        else:

            send_async_email(email)

            print(
                "ASYNC EMAIL STARTED"
            )

        return True

    except Exception as e:

        import traceback

        print(
            "ENQUIRY EMAIL ERROR:",
            str(e)
        )

        traceback.print_exc()

        return False