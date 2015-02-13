from Products.CMFCore.utils import getToolByName
from biel.schule.testing import BIEL_POLICY_INTEGRATION_TESTING
from unittest2 import TestCase


class TestBielSchuleInstallation(TestCase):

    layer = BIEL_POLICY_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']

    def test_biel_schulen_policy_installed(self):
        portal_setup = getToolByName(self.portal, 'portal_setup')

        version = portal_setup.getLastVersionForProfile(
            'biel.schule:default')
        self.assertNotEqual(version, None)
        self.assertNotEqual(version, 'unknown')
