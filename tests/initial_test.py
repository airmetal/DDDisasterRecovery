import unittest
import vcr
from libcloud.compute.drivers.dimensiondata import DimensionDataNodeDriver
import libcloud.httplib_ssl
from libcloud.common.dimensiondata import DEFAULT_REGION
from vcr.stubs import VCRHTTPSConnection, VCRHTTPConnection
from libcloud.utils.py3 import httplib

class DDInitialTestCase(unittest.TestCase):
    def test_i_will_always_pass(self):
        pass

