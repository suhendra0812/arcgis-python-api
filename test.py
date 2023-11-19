import unittest

from auth import Auth
from features import FeatureLayer


class Test(unittest.TestCase):
    username: str = "arcgis.ji"
    password: str = "Jababeka1234"
    portal_url: str = "https://tmaps.jababeka.com/arcgis"
    auth: Auth = Auth(portal_url, username, password)
    service_url: str = (
        f"{portal_url}/rest/services/Hosted/JSmart_Report/FeatureServer/0"
    )

    def test_token(self):
        token = self.auth.get_token()
        self.assertIsInstance(token, str)

    def test_query(self):
        layer: FeatureLayer = FeatureLayer(self.service_url, self.auth)
        feats = layer.query(order_by_fields="waktu_awal DESC", result_record_count=1)
        print(feats)
        self.assertIn("features", feats.keys())
