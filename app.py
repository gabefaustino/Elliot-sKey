import secrets  # Biblioteca para geração de números aleatórios seguros
import string   # Biblioteca para trabalhar com strings de caracteres

# Função para gerar uma senha segura
def gerar_senha(tamanho=12):
    # Verifica se o tamanho está dentro do intervalo permitido (entre 8 e 16)
    if tamanho < 8 or tamanho > 16:
        raise ValueError("O tamanho da senha deve ser entre 8 e 16 caracteres.")
    
    # Garante que a senha tenha pelo menos 1 número, 1 letra maiúscula, 1 letra minúscula e 1 caractere especial
    numeros = secrets.choice(string.digits)  # Escolhe um número aleatório de '0' a '9'
    maiusculas = secrets.choice(string.ascii_uppercase)  # Escolhe uma letra maiúscula de 'A' a 'Z'
    minusculas = secrets.choice(string.ascii_lowercase)  # Escolhe uma letra minúscula de 'a' a 'z'
    especiais = secrets.choice(string.punctuation)  # Escolhe um caractere especial, como '!@#$%^&*'
    
    # Combina os caracteres obrigatórios
    senha_inicial = [numeros, maiusculas, minusculas, especiais]
    
    # Calcula quantos caracteres restantes são necessários para atingir o tamanho total da senha
    restantes = tamanho - len(senha_inicial)  # Subtrai os 4 caracteres obrigatórios
    
    # Gera os caracteres restantes aleatoriamente usando secrets.choice para manter a segurança
    todos_caracteres = string.ascii_letters + string.digits + string.punctuation
    senha_restante = [secrets.choice(todos_caracteres) for _ in range(restantes)]
    
    # Junta os caracteres obrigatórios com os restantes
    senha_completa = senha_inicial + senha_restante
    
    # Embaralha todos os caracteres para garantir que os obrigatórios não fiquem sempre nas mesmas posições
    secrets.SystemRandom().shuffle(senha_completa)
    
    # Converte a lista de caracteres em uma string e a retorna
    return ''.join(senha_completa)

# Função para garantir que o input do usuário seja um número válido
def pegar_tamanho_senha():
    while True:  # Loop para continuar pedindo input até receber um valor válido
        try:
            # Solicita ao usuário o tamanho da senha e converte para inteiro
            tamanho = int(input("Escolha o tamanho da senha (entre 8 e 16): "))
            
            # Verifica se o número está dentro do intervalo permitido
            if (tamanho < 8) or (tamanho > 16):
                print("Por favor, escolha um número entre 8 e 16.")
            else:
                return tamanho  # Retorna o tamanho válido
        except ValueError:
            # Exibe mensagem de erro se o valor inserido não for um número
            print("Entrada inválida. Digite um número entre 8 e 16.")


tamanho_senha = pegar_tamanho_senha()  # Obtém o tamanho da senha do usuário
senha_gerada = gerar_senha(tamanho=tamanho_senha)  # Gera a senha com o tamanho especificado
print(f"Senha gerada: {senha_gerada}")  # Exibe a senha gerada