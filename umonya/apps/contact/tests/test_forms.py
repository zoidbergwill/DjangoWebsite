from apps.contact.forms import ContactForm
from django.test import TestCase
from apps.utils.functions import send_email_f


class TestForms(TestCase):
    def test_contactform_good_fields(self):
        form_data = {"name": "Mark Gituma", "email": "Email@mail.com", "text": "Hello World"}
        form = ContactForm(data=form_data)
        self.assertIn("name", form.data)
        self.assertIn("email", form.data)
        self.assertIn("text", form.data)
        if form.is_valid():
            self.assertEqual(send_email_f(form), True)

    def test_contactform_empty_fields(self):
        form_data = {"name": "", "email": "", "text": ""}
        form = ContactForm(data=form_data)
        self.assertEqual(form["name"].errors, [u'This field is required.'])
        self.assertEqual(form["email"].errors, [u'This field is required.'])

    def test_contactform_bad_fields(self):
        form_data = {"name": "", "email": "umonya", "text": ""}
        form = ContactForm(data=form_data)
        self.assertEqual(form["email"].errors, [u'Enter a valid email address.'])

    def test_contact_form_post(self):
        form_data = {"name": "Mark Gituma", "email": "Email@mail.com", "text": "Hello World"}
        response = self.client.post("/contact/", form_data)
        self.assertIn("success", response.context)
