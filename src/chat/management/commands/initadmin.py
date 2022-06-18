from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

ADMINS = ('test_1', 'test_2', 'test_3')


class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for username in ADMINS:
                password = 'admin'
                self.stdout.write('Creating account for %s' % username)
                admin = User.objects.create_superuser(username=username, password=password, first_name='Ivan',
                                                      last_name='Ivanov')
                admin.is_active = True
                admin.is_admin = True
                admin.save()
        else:
            self.stdout.write('Admin accounts can only be initialized if no Accounts exist')
