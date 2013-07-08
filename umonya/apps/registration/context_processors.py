def dynamic_menu(request):
    # Adds Dynamic Menu Template Context
    from apps.main.models import Dynamic_Section
    try:
        return{"registration": Dynamic_Section.objects.get(section="registration")}
    except:
        return {"registration": False}
