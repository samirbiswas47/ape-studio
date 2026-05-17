# =====================================================
# api/signals.py
# =====================================================

from django.db.models.signals import post_save
from django.dispatch import receiver

from api.models import Enquiry

from api.services.email_service import (
    send_enquiry_acknowledgement
)


@receiver(post_save, sender=Enquiry)
def enquiry_created(
    sender,
    instance,
    created,
    **kwargs
):

    print("SIGNAL RUNNING")

    if created:

        print("NEW ENQUIRY CREATED")

        send_enquiry_acknowledgement(
            instance
        )