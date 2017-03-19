from django.contrib import admin

# Import Album and Song class model
from .models import Album
from .models import Song

# Register Album model in admin
admin.site.register(Album)
# Register Song model in admin
admin.site.register(Song)
