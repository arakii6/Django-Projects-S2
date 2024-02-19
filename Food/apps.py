from django.apps import AppConfig


class FoodConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Food'

    def ready(self) -> None:
        import Food.signals
        return super().ready()
