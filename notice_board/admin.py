from django.contrib import admin
from .models import UserProfile, University, Thread, Post

admin.site.register(UserProfile)
admin.site.register(University)
admin.site.register(Thread)
admin.site.register(Post)
