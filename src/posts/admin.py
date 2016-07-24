from django.contrib import admin

# Register your models here.
from .models import Post

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["id","domain","url","content_type","timestamp","request_count"]
	list_display_links = ["id"]
	list_filter = ["domain","content_type","url"]	
	search_fields = ["url","domain","content_type","timestamp"]
	
	class Meta:
		model = Post


admin.site.register(Post, PostModelAdmin)
