from django.core.management.base import BaseCommand
import random

from crud.models import Article

# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")
        parser.add_argument('--clear', type=str, help="Mode")

    def handle(self, *args, **options):
        print(options)
        if options["clear"]:
            options = "clear"
        if options["mode"]:
            options = "mode"
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data(self):
    """Deletes all the table data"""
    self.stdout.write("Delete Article instances")


def create_article(self):
    """Creates an address object combining different elements from the list"""
    title = ["#221 B", "#101 A", "#550I", "#420G", "#A13"]
    author = ["Bakers Street", "Rajori Gardens", "Park Street", "MG Road", "Indiranagar"]
    email = ["101234@gamil.com", "101232@gamil.com", "101231@gamil.com", "101236@gamil.com", "101239@gamil.com"]

    article = Article(
        title=random.choice(title),
        author=random.choice(author),
        email=random.choice(email),
    )
    article.save()
    self.stdout.write("{} article created.".format(article))
    return article


def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear
    :return:
    """
    # Clear data from tables
    clear_data(self)
    if mode == MODE_CLEAR:
        print("exit")
        return
    self.stdout.write("start")
    # Creating 15 addresses
    for i in range(15):
        create_article(self)
