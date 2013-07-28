from django.core.mail import send_mail
from time import time


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


def get_image_path(instance, filename):
    '''
        Returns the file path to store the images which is passed to the
        database
    '''
    return 'img/pic/bios/%s_%s' % (str(time()).replace('.', '_'), filename)


def get_total_pages(total_items):
    if total_items > 5:
        # get page numbers, and total pages
        total_pages = total_items // 5
        total_pages += total_items % 5 and 1 or 0
    else:
        total_pages = 1
    return total_pages
