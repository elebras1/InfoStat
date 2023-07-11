from django.core.management.base import BaseCommand
from ...utils.data_utils import (
    generate_secteurs,
    generate_theme,
    generate_infographie,
    generate_article,
    generate_region,
    generate_link,
)


class Command(BaseCommand):
    help = "generate fake data"

    def handle(self, *args, **kwargs):
        generate_secteurs(20)
        generate_theme(200)
        generate_infographie(2000)
        generate_article(2000)
        generate_region(197)
        generate_link()
        print("completed")
