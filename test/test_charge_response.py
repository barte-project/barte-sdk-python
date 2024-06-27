# coding: utf-8

"""
    Barte Api

    Documentação para integração com a API da Barte <h3>Segurança</h3> Utilizamos um token de autorização cadastrado dentro da plataforma da Barte no menu  <b>Configurações -> Integração -> Chaves API</b> para autenticar as operações executadas.</br> Adicione o token a requisição utilizando o header <b>X-Token-Api</b>, na documentação utilize  o botão <b>Authorize</b> para os testes. <h3>Ambientes</h3> Disponibilizamos dois ambientes <b>(sandbox e produção)</b>. Utilize o primeiro para seus  testes de desenvolvimento.</br> Você pode selecionar o ambiente que quer utilizar na nossa documentação através com combo  <b>servers</b></br> <b>Observação: </b> Entre contato com nossa equipe de operações para lhe auxiliar na criação  de uma conta em nosso ambiente de sandbox.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from bartesdk.models.charge_response import ChargeResponse

class TestChargeResponse(unittest.TestCase):
    """ChargeResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ChargeResponse:
        """Test ChargeResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ChargeResponse`
        """
        model = ChargeResponse()
        if include_optional:
            return ChargeResponse(
                uuid = '67d44c8c-f2a9-4432-9ada-ac963780d49f',
                title = 'Titulo da Cobrança',
                expiration_date = '2022-04-14',
                paid_date = '2022-04-14',
                value = 153.33,
                payment_method = 'CREDIT_CARD',
                status = 'PAID',
                customer = bartesdk.models.customer_response.CustomerResponse(
                    document = '14105439000193', 
                    type = 'CNPJ', 
                    name = 'Nome do comprador', 
                    email = 'comprador@email.com', 
                    phone = '18999999999', 
                    alternative_email = 'alternativo@email.com', ),
                interest_amount = 3.5,
                bank_slip_barcode = '',
                bank_slip = '',
                pix_code = '',
                pix_qr_code_image = '',
                chargeback_deadline = datetime.datetime.strptime('1975-12-30', '%Y-%m-%d').date()
            )
        else:
            return ChargeResponse(
                uuid = '67d44c8c-f2a9-4432-9ada-ac963780d49f',
                title = 'Titulo da Cobrança',
                expiration_date = '2022-04-14',
                value = 153.33,
                payment_method = 'CREDIT_CARD',
                status = 'PAID',
                customer = bartesdk.models.customer_response.CustomerResponse(
                    document = '14105439000193', 
                    type = 'CNPJ', 
                    name = 'Nome do comprador', 
                    email = 'comprador@email.com', 
                    phone = '18999999999', 
                    alternative_email = 'alternativo@email.com', ),
        )
        """

    def testChargeResponse(self):
        """Test ChargeResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
