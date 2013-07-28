from apps.utils.models import Dynamic_Section


def dynamic_menu(request):
    # Adds Dynamic Menu Template Context
    try:
        return{"registration": Dynamic_Section.objects.get(section="registration")}
    except:
        return {"registration": False}
