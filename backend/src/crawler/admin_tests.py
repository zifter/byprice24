from unittest.mock import Mock
from unittest.mock import patch

from crawler.admin import ScrapingStateAdmin
from crawler.models import ScrapingState
from django.contrib.admin import AdminSite
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from django.test.client import RequestFactory
from django.urls import reverse


class ScrapingStateAdminTestCase(TestCase):
    fixtures = [
        'prod/markets.yaml'
    ]

    def setUp(self) -> None:
        User.objects.create_superuser(
            username='admin', password='admin', email='admin@example.com'
        )
        self.client = Client()
        self.client.login(username='admin', password='admin')

    def test_scraping_state_admin_loads_correctly(self):
        resp = self.client.get(reverse(
            'admin:crawler_scrapingstate_change',
            args=(1,)
        ))
        self.assertTrue('Force Scrape' in str(resp.content))

    @patch('django.contrib.admin.ModelAdmin.message_user', (lambda: Mock())())
    def test_click_on_force_scrape(self):
        request = RequestFactory().post('/')
        request.POST = {'force-scrape': True}

        admin_scraping_state = ScrapingStateAdmin(ScrapingState, AdminSite())
        resp = admin_scraping_state.response_change(request, ScrapingState.objects.first())
        self.assertEqual(302, resp.status_code)