# Elliot's Key
Elliot's Key é um gerador de senhas seguras inspirado em boas práticas de cibersegurança, projetado para criar senhas aleatórias e criptograficamente seguras. O gerador utiliza a biblioteca secrets do Python, garantindo que suas senhas atendam aos padrões de segurança necessários para proteção em sistemas modernos.

## Funcionalidades
- Gera senhas com comprimento definido pelo usuário (entre 8 e 16 caracteres).
- Garante a presença de pelo menos:
  - 1 número.
  - 1 letra maiúscula.
  - 1 letra minúscula.
  - 1 caractere especial.
- Segurança através da biblioteca _secrets_ do Python.

## Uso da Biblioteca `secrets`

O projeto "Elliot's Key" utiliza a biblioteca `secrets` do Python para garantir a geração de senhas seguras. A `secrets` é projetada para gerar números aleatórios criptograficamente seguros, tornando-a ideal para a criação de senhas, tokens de autenticação e outras aplicações que requerem aleatoriedade forte.

### Vantagens do uso da biblioteca `secrets`:

- **Aleatoriedade Segura:** Gera números aleatórios difíceis de prever, protegendo informações sensíveis contra ataques.
- **Simplicidade:** API fácil de usar para gerar valores aleatórios sem complicações adicionais.
- **Substituição para `random`:** Oferece uma alternativa segura em comparação com a biblioteca `random`, que não deve ser usada para aplicações de segurança.
- **Parte da Biblioteca Padrão:** Disponível a partir do Python 3.6, não é necessário instalar pacotes adicionais.


## Como usar
Clone este repositório:

> git clone https://github.com/seu-usuario/elliots-key.git

Navegue até o diretório do projeto:
> cd elliots-key

Execute o script Python:
> python gerador_de_senhas.py

Informe o tamanho desejado da senha (entre 8 e 16 caracteres).

## Exemplo de uso
Após rodar o script, você verá algo assim:

> Escolha o tamanho da senha (entre 8 e 16): 12
> Senha gerada: A4ds&!p@JwT2

## Requisitos
Python 3.x

Nenhuma dependência externa necessária além das bibliotecas padrão do Python (secrets, string).
