from django.contrib import admin, auth, contenttypes, staticfiles
from django.contrib.auth.models import User, Group

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(admin)
admin.site.unregister(auth)
admin.site.unregister(contenttypes)
admin.site.unregister(staticfiles)
