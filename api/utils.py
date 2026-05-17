# =====================================================
# api/utils.py
# =====================================================

from threading import Thread
import traceback


def replace_email_keywords(content, data):

    for key, value in data.items():

        content = content.replace(
            key,
            str(value)
        )

    return content


class EmailThread(Thread):

    def __init__(self, email):

        super().__init__()

        self.email = email

        self.daemon = True

    def run(self):

        try:

            self.email.send(
                fail_silently=False
            )

            print(
                "ASYNC EMAIL SENT"
            )

        except Exception as e:

            print(
                "ASYNC EMAIL ERROR:",
                str(e)
            )

            traceback.print_exc()


def send_async_email(email):

    thread = EmailThread(email)

    thread.start()

    return thread