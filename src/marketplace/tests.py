from django.test import Client
from django.test import TestCase


class MarketplaceViewTestCase(TestCase):
    def setUp(self):
        # Every test needs a client.
        self.client = Client()

    def test_env_empty_list(self):
        response = self.client.get('/api/v1/marketplaces/')
        self.assertEqual(len(response.data['EnvironmentsList']), 0)

    def test_api_empty_list(self):
        response = self.client.get('/api/v1/marketplaces/')
        self.assertEqual(len(response.data), 0)
    #
    # def test_put_and_get(self):
    #     data = {
    #     	"Name": "Production",
    #         "NetOptimism": True,
    #         "InactivityKickTimeout": 120,
    #         "UseTLS": True,
    #         "Language": "RU",
    #         "MainServiceUri": "wapi.projectx.vizor-games.com",
    #         "SiteURL": "https://bloodofheroes.online",
    #         "HasRegion": True
    #     }
    #
    #     response = self.client.post('/api/v1/env/', data=data)
    #     self.assertEqual(response.status_code, 201)
    #
    #     response = self.client.get('/api/v1/env/')
    #     self.assertEqual(len(response.data), 1)
    #
    #     response = self.client.get('/env/')
    #     self.assertEqual(len(response.data['EnvironmentsList']), 1)
    #     cfg = response.data['EnvironmentsList'][0]
    #     self.assertEqual(cfg['Name'], 'Production')
    #     self.assertNotIn('PSNEnv', cfg)
    #
    # def test_put_json_without_url(self):
    #     data = {
    #         "Name": "Production",
    #     }
    #
    #     response = self.client.post('/api/v1/env/', data=data)
    #     self.assertEqual(response.status_code, 400)
    #
    # def test_put_json_with_psn_env(self):
    #     data = {
    #         "Name": "Production",
    #         "MainServiceUri": "wapi.projectx.vizor-games.com",
    #         "PSNEnv": "np",
    #     }
    #
    #     response = self.client.post('/api/v1/env/', data=data)
    #     self.assertEqual(response.status_code, 201)
    #
    #     response = self.client.get('/env/')
    #     cfg = response.data['EnvironmentsList'][0]
    #     self.assertEqual(cfg['PSNEnv'], "np")
