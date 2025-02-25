import json
from pathlib import Path
import boto3
from botocore.exceptions import BotoCoreError, ClientError
from mypy_boto3_textract.type_defs import DetectDocumentTextResponseTypeDef


def obter_caminho_imagem(nome_arquivo: str) -> Path:
    """Retorna o caminho completo do arquivo de imagem."""
    return Path(__file__).parent / "images" / nome_arquivo


def extrair_texto_imagem(caminho_imagem: Path) -> dict:
    """Utiliza AWS Textract para detectar texto na imagem."""
    cliente_textract = boto3.client("textract")

    try:
        with caminho_imagem.open("rb") as arquivo_imagem:
            imagem_bytes = arquivo_imagem.read()

        resposta_textract = cliente_textract.detect_document_text(Document={"Bytes": imagem_bytes})

        # Salvar resposta como JSON formatado
        with open("resposta_textract.json", "w") as arquivo_resposta:
            json.dump(resposta_textract, arquivo_resposta, indent=4)

        return resposta_textract

    except (ClientError, BotoCoreError) as erro:
        print(f"Erro ao processar o documento: {erro}")
        return {}


def obter_linhas_texto(resposta: dict) -> list[str]:
    """Extrai e retorna as linhas de texto detectadas na resposta do Textract."""
    try:
        blocos = resposta.get("Blocks", [])
        return [bloco["Text"] for bloco in blocos if bloco.get("BlockType") == "LINE"]
    except KeyError:
        print("Erro ao extrair as linhas de texto.")
        return []


if __name__ == "__main__":
    nome_imagem = "lista-material-escolar.jpeg"
    caminho_imagem = obter_caminho_imagem(nome_imagem)

    if not caminho_imagem.exists():
        print(f"Erro: O arquivo {nome_imagem} não foi encontrado.")
    else:
        resposta_textract = extrair_texto_imagem(caminho_imagem)
        for linha in obter_linhas_texto(resposta_textract):
            print(linha)
