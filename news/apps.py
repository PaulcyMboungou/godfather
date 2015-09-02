from django.apps import AppConfig
from actstream import registry

class MyAppConfig(AppConfig):
    name = 'news'

    def ready(self):
        registry.register(self.get_model('MyUser'), self.get_model('Article'))