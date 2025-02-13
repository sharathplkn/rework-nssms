from django.contrib.auth.decorators import user_passes_test

def group_required(*group_names, login_url=None):
    def in_group(user):
        if user.is_authenticated:
            return user.groups.filter(name__in=group_names).exists()
        return False
    return user_passes_test(in_group, login_url=login_url)
