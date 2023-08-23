from django.core.management.base import BaseCommand
from ...utils.data_utils import (
    generate_secteurs,
    generate_theme,
    generate_infographie,
    generate_article,
    generate_region,
    generate_favori,
    generate_user,
)


class Command(BaseCommand):
    help = "generate fake data"

    def handle(self, *args, **kwargs):
        generate_secteurs(20)
        generate_theme(200)
        generate_region()
        generate_user(20)
        generate_infographie(2000)
        generate_article(2000)
        generate_favori()
        print("completed")
