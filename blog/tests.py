import datetime

from django.utils import timezone
from django.test import TestCase

from models import Blog


class BlogMethodTests(TestCase):

    def test_was_posted_recently_with_upcoming_blog(self):

        time = timezone.now() + datetime.timedelta(days=30)
        up_blog = Blog(posted=time)
        self.assertIs(up_blog.was_posted_recently(), False)

    def test_was_posted_recently(self):

        time = timezone.now()
        b = Blog(posted=time)
        self.assertIs(b.was_posted_recently(), True)
