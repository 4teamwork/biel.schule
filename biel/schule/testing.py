from egov.core.testing import TeamraumInstallationLayer
from ftw.builder.testing import functional_session_factory
from ftw.builder.testing import set_builder_session_factory
from ftw.testing.quickinstaller import snapshots
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting


snapshots.disable()


class BielPolicyLayer(TeamraumInstallationLayer):

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'biel.schule:default')


BIEL_POLICY_FIXTURE = BielPolicyLayer()
BIEL_POLICY_INTEGRATION_TESTING = IntegrationTesting(
    bases=(BIEL_POLICY_FIXTURE, ), name="BielSchule:Integration")
BIEL_POLICY_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(BIEL_POLICY_FIXTURE,
           set_builder_session_factory(functional_session_factory)),
    name="BielSchule:Functional")
