from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.template import RequestContext
from forms import RegistrationForm
from apps.utils.functions import send_email_f
from apps.utils.models import Dynamic_Section


def registration(request):
    if request.method == 'POST':
        f = RegistrationForm(request.POST)
        if f.is_valid():
            send_email_f(f)
            success = {'success': 'success'}
            return render_to_response(
                'registration.html', success,
                context_instance=RequestContext(request))
    else:
        f = RegistrationForm()

    try:
        # queryset only evaluated in second line, and only one record stored,
        # so this is more efficient, as count is done at db level.
        dyn_sections = Dynamic_Section.objects.filter(section='registration')
        section = dyn_sections[dyn_sections.count() - 1]
    except Dynamic_Section.DoesNotExist:
        section = False

    args = {}
    args.update(csrf(request))
    args['section'] = section
    args['form'] = f

    return render_to_response(
        'registration.html',
        args,
        context_instance=RequestContext(request))
