#Source: https://stackoverflow.com/questions/60038366/attributeerror-settings-object-has-no-attribute
urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),