# SafeFileCrypt 🔐

**SafeFileCrypt** é um utilitário Python seguro para criptografar e descriptografar arquivos individuais usando **senha** e **salt**, baseado na biblioteca `cryptography`.

Este projeto é **educacional e legal**, projetado para proteger **apenas arquivos do próprio usuário**, com consentimento explícito.

> ⚠️ **Aviso Importante:** Este software **não é ransomware**. Ele não criptografa diretórios inteiros automaticamente nem exige pagamento. O uso é manual e controlado.

---

## 📦 Funcionalidades

- ✅ Criptografia de **um arquivo por vez** com senha definida pelo usuário.
- ✅ Descriptografia **segura** do mesmo arquivo para restaurar o original.
- ✅ Geração de **salt aleatório** para proteger contra ataques de força bruta.
- ✅ Uso de **PBKDF2HMAC** para transformar a senha em uma chave criptográfica forte.
- ✅ Mensagens claras de confirmação antes de qualquer operação crítica.
- ✅ Compatível com **Python 3.8+**.

---

## 🔐 Conceitos de Segurança

O projeto utiliza práticas modernas de criptografia:

1.  **Senha:** Definida pelo usuário no momento da execução (nunca é armazenada no código).
2.  **Salt:** Um valor aleatório que "tempera" a senha antes de gerar a chave.
    * *Função:* Impede ataques de dicionário e *rainbow tables*.
    * *Armazenamento:* Salvo automaticamente no arquivo `salt.bin`.
3.  **Derivação de Chave:** A senha + salt são processados via **PBKDF2HMAC** para criar uma chave Fernet válida.
4.  **Fernet:** O sistema de criptografia simétrica que garante confidencialidade, integridade e autenticação dos dados.

---

## ⚙️ Instalação

Certifique-se de ter o Python instalado.
Instale as dependências:
```python
pip install cryptography
```

📝 Como Usar

1. Criptografar um arquivo
Execute o script de criptografia:

```python
python encrypt.py
Informe o nome do arquivo (ex: documento.txt).

Confirme a ação.

Digite e confirme uma senha segura.

Resultado: O arquivo será criptografado no mesmo local e um arquivo salt.bin será criado.

2. Descriptografar um arquivo
Execute o script de descriptografia:
```

python decrypt.py
Informe o nome do arquivo criptografado.

Digite a mesma senha usada na criptografia.

Resultado: O conteúdo original do arquivo é restaurado.

⚠️ Atenção: Se a senha estiver incorreta ou o arquivo salt.bin for perdido/deletado, a descriptografia falhará permanentemente.
