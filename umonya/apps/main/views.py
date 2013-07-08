from django.core.mail import send_mail


def send_email_f(f):
    subject = 'User Registration'
    message = ''
    for item in f.cleaned_data:
        message = (
            message + item.upper() + '\n' + str(f.cleaned_data[item]) + '\n\n')
    sender = 'umonya@admin.com'
    recipients = ['umonya@admin.com']
    if send_mail(subject, message, sender, recipients):
        return True
