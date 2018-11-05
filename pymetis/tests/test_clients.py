import unittest
from pymetis.clients import charts, dashboards, datasources, response


class TestCharts(unittest.TestCase):
    def test_get(self):
        print 'TestCharts.test_get method called'
        dataset = charts.get("localhost", "4200", "3146e029-8035-49f2-b881-38c8c0f5dfe3")
        print dataset


class TestDashboards(unittest.TestCase):
    def test_get(self):
        print 'TestDashboards.test_get method called'
        dataset = dashboards.get("localhost", "4200", "3146e029-8035-49f2-b881-38c8c0f5dfe3")
        print dataset


class TesDatasources(unittest.TestCase):
    def test_get(self):
        print 'TesDatasources.test_get method called'
        dataset = datasources.get("localhost", "4200", "3146e029-8035-49f2-b881-38c8c0f5dfe3")
        print dataset


class TestResponse(unittest.TestCase):
    def test_write(self):
        coefficient = 2
        intercept = 0
        model = {'coefficient': coefficient, 'intercept': intercept}
        response.write(model)


if __name__ == '__main__':
    unittest.main()
