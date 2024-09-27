from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        import blog.signals


from django.apps import AppConfig
from django.db.models.signals import post_save
