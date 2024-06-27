# coding: utf-8

"""
    Barte Api

    Documentação para integração com a API da Barte <h3>Segurança</h3> Utilizamos um token de autorização cadastrado dentro da plataforma da Barte no menu  <b>Configurações -> Integração -> Chaves API</b> para autenticar as operações executadas.</br> Adicione o token a requisição utilizando o header <b>X-Token-Api</b>, na documentação utilize  o botão <b>Authorize</b> para os testes. <h3>Ambientes</h3> Disponibilizamos dois ambientes <b>(sandbox e produção)</b>. Utilize o primeiro para seus  testes de desenvolvimento.</br> Você pode selecionar o ambiente que quer utilizar na nossa documentação através com combo  <b>servers</b></br> <b>Observação: </b> Entre contato com nossa equipe de operações para lhe auxiliar na criação  de uma conta em nosso ambiente de sandbox.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bartesdk.models.subscription_additional_value_response import SubscriptionAdditionalValueResponse

class TestSubscriptionAdditionalValueResponse(unittest.TestCase):
    """SubscriptionAdditionalValueResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SubscriptionAdditionalValueResponse:
        """Test SubscriptionAdditionalValueResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SubscriptionAdditionalValueResponse`
        """
        model = SubscriptionAdditionalValueResponse()
        if include_optional:
            return SubscriptionAdditionalValueResponse(
                value = 750,
                installments = 3
            )
        else:
            return SubscriptionAdditionalValueResponse(
                value = 750,
                installments = 3,
        )
        """

    def testSubscriptionAdditionalValueResponse(self):
        """Test SubscriptionAdditionalValueResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
