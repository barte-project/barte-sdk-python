# BarteSDK

Bem-vindo ao BarteSDK, a solução oficial para integração com as APIs de pagamento da Barte, projetada para simplificar e acelerar o desenvolvimento de aplicações fintech. Com nosso SDK, você pode facilmente integrar funcionalidades de pagamento, assinaturas, e gestão de compradores em sua aplicação.

## Recursos do SDK

O BarteSDK fornece métodos convenientes para interagir com as seguintes APIs:

- **API de Planos**: Facilita o gerenciamento dos planos cadastrados no seu checkout.
- **API de Pedidos**: Permite gerenciar os pedidos cadastrados no seu sistema.
- **API de Compradores**: Auxilia na gestão dos compradores cadastrados.
- **API de Cobranças**: Fornece ferramentas para o gerenciamento das cobranças.
- **API de Assinaturas**: Facilita a criação e gestão de assinaturas.
- **API de Criação de Link de Pagamento**: Permite a geração e gerenciamento de links de pagamento.

## Vantagens do BarteSDK

O BarteSDK foi desenvolvido pensando na eficiência e na otimização do tempo de desenvolvimento, oferecendo uma série de vantagens que vão além da simples integração com nossas APIs. Embora seu uso não seja obrigatório, recomendamos fortemente que você o adote para aproveitar os seguintes benefícios:

- **Mais Eficiência e Redução de Custos**: Implementar nosso SDK significa reduzir custos operacionais e de desenvolvimento. Ele já está pronto para uso e totalmente homologado pela Barte, garantindo que você esteja sempre alinhado com as melhores práticas e padrões do mercado.

- **Instalação Otimizada**: Facilitamos a instalação com nossa solução plug-and-play, que se integra perfeitamente a sistemas de gestão de pacotes como Composer, Gradle, Maven e NPM. Isso agiliza significativamente a integração do SDK ao seu projeto, economizando tempo valioso de desenvolvimento.

- **Construção de Requisições Simplificada**: Simplifique a construção de suas requisições com nossa interface intuitiva. O SDK foi projetado para minimizar a complexidade, otimizar o desenvolvimento e garantir uma implementação eficaz e livre de erros.

- **Segurança de Dados**: A segurança é uma prioridade absoluta no BarteSDK. Utilizamos as melhores práticas e padrões de segurança para proteger todas as informações transmitidas, garantindo a integridade e confidencialidade dos dados dos seus clientes.

Adotar o BarteSDK não é apenas uma questão de conveniência; é uma decisão estratégica que fortalece a segurança, reduz custos e aumenta a eficiência do desenvolvimento de software na sua organização.


## Como Começar

Para começar a usar o BarteSDK, siga os passos abaixo:

1. 📲**Instalação**

   Instale o SDK via pip:

   ```bash
   pip install bartesdk

2. 🌟**Uso**

Para usar o charges.listByUuid, que lista a cobrança passando como parâmetro o UUID, siga os passos abaixo:

### Código de Exemplo

```python
from bartesdk import BarteSDK

api_key = 'your-api-token'
api_client = BarteSDK(api_key, env="sandbox", api_version="v2")

response = api_client.charges.listByUuid(
    charge_uuid='fcb169c5-1238-45de-9d44-acdc858b021e'
)
print(response)
```
### Variáveis `api_client`
- `env`: prd ou sandbox.
- `api_version`: Versão da API ( v1 ou v2 ).
- `api_key`: API Token para autenticação.

3. 📚 **Documentação**

Acesso a página do OpenAPI/Swagger para saber com detalhes todos recursos e métodos:
 - [APIs](https://dev-bff.barte.com/v1/docs/swagger-ui/index.html?configUrl=/v1/api-docs/swagger-config#/)