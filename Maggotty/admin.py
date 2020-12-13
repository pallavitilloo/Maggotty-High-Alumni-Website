from django.contrib import admin
from Maggotty.models import UserProfileInfo, User
from Maggotty.models import Event, Contribute, Poll, UserOpinions

# Register your models here.
admin.site.register(UserProfileInfo)

# register the contribute model
admin.site.register(Contribute)

# register the poll model
admin.site.register(Poll)

# resgister the UserOpionions model
admin.site.register(UserOpinions)

# register the Event model
admin.site.register(Event)