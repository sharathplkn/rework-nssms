from django.contrib.auth.models import User

def group_processor(request):
    if request.user.is_authenticated:
        is_po_group = request.user.groups.filter(name='po').exists()
        is_admin_group = request.user.groups.filter(name='admin').exists()
        is_vs_group = request.user.groups.filter(name='vs').exists()  # Adjust as needed
    else:
        is_po_group = False
        is_admin_group = False
        is_vs_group = False

    return {
        'is_po_group': is_po_group,
        'is_admin_group': is_admin_group,
        'is_vs_group': is_vs_group,
    }
