from django.core.management.base import BaseCommand
from listings.models import Listing, User
from faker import Faker
import random

class Command(BaseCommand):
    def add_arguments(self, parser):

        # Named (optional) arguments
        parser.add_argument(
            "--no_of_listing",
            type=int,
            default=10,
            nargs=1,
            help="Number of listing to seed database with",
        )

    def handle(self, *args, **options):
        users = User.objects.all()  # Ensure you have users to link as hosts

        if not users.exists():
            users = [
                User.objects.create(
                    first_name = Faker.first_name(),
                    last_name = Faker.last_name(),
                    email = Faker.email(),
                    password = Faker.password(),
                    username = Faker.user_name()
            )]

        no_of_listing = options["no_of_listing"]
        for _ in range(no_of_listing):
            host = random.choice(users)  # Randomly assign a user as the host
            listing = Listing(
                listing_id=Faker.uuid4(),
                host=host,
                name=Faker.catch_phrase(),
                description=Faker.text(max_nb_chars=400),
                location=Faker.city(),
                pricepernight=round(random.uniform(50, 500), 2),
            )
            listing.save()
