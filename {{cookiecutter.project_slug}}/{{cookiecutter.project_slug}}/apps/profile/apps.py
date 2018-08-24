from django.apps import AppConfig


class ProfileConfig(AppConfig):
    name = "{{ cookiecutter.project_slug }}.apps.profile"

    def ready(self):
        import {{ cookiecutter.project_slug }}.apps.profile.signals.handlers