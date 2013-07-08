from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from forms import ContactForm
from apps.main.views import send_email_f


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_email_f(form)
            success = {'success': 'success'}
            return render_to_response(
                'contact.html',
                success,
                context_instance=RequestContext(request))
    else:
        form = ContactForm
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response(
        'contact.html',
        args,
        context_instance=RequestContext(request))
