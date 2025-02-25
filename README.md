# 📝 Extração de Texto com AWS Textract

Este projeto utiliza o **AWS Textract** para realizar a extração de texto de imagens. O código permite detectar o texto presente em um arquivo de imagem e salvar os resultados em um arquivo JSON.

---

## 🚀 Funcionalidades

- 📂 **Carregamento de Imagens**: Obtém o caminho da imagem a ser processada.
- 🔍 **Detecção de Texto**: Utiliza **AWS Textract** para extrair o texto da imagem.
- 💾 **Armazenamento da Resposta**: Salva a saída do Textract em um arquivo `resposta_textract.json`.
- 📜 **Exibição do Texto**: Exibe no terminal todas as linhas de texto extraídas da imagem.
- listaEscolar.py"

** 📜 Lista de Material Escolar**

| Qtd | Descrição |
| - | ------ |
| 3 | rolos de fita crepe |
| 1 | bloco de canson A4 |
| 1 | fita adesiva |
| 5 | folhas de cartolina |
| 3 | placas de EVA |
| 1 | EVA com glitter |
| 5 | papéis colorset |
| 1 | caneta permanente |
| 1 | pacote de palito de sorvete |
| 4 | papéis cartão |
| 1 | kit Leoni n. 1 |
| 1 | dicionário |
| 1 | pincel n. 14 |
| 1 | pasta 20mm |

---

## 📦 Dependências

Antes de executar o código, certifique-se de ter o **Python 3.9+** instalado e as seguintes bibliotecas instaladas:

```
pip install boto3 mypy-boto3-textract
```
### ▶️ Como Executar

1. Clone este repositório:
    ```
    git clone https://github.com/seu-usuario/nome-do-repositorio.git
    cd nome-do-repositorio
    ```
2. Adicione a imagem que deseja processar na pasta images/.
3. Execute o script:
    ```
   python main.py
    ```
Se a execução for bem-sucedida, o texto extraído será impresso no terminal e salvo no arquivo resposta_textract.json.

### ⚠️ Configuração da AWS
Para utilizar o AWS Textract, é necessário configurar suas credenciais da AWS. Você pode fazer isso via AWS CLI:

```
aws configure
```

Informe suas chaves de acesso da AWS e selecione a região apropriada.

