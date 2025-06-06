from django.contrib.admin import AdminSite
from django.shortcuts import redirect


class MyAdminSite(AdminSite):
    site_header = 'My Admin'

    def has_permission(self, request):
        """
        Return True if the given HttpRequest has permission to view
        the admin site. Override to redirect to custom login if not authenticated.
        """
        if request.user.is_active and request.user.is_staff:
            return True
        return False

    def login(self, request, extra_context=None):
        """
        Redirect to custom login if unauthenticated or unauthorized.
        """
        return redirect('/accounts/login/')


# instantiate it
custom_admin_site = MyAdminSite(name='myadmin')
