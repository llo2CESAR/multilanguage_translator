from bd import Dicionario_libras
from typing import Dict, List

def traduzir_texto_para_libras_service(texto: str, dicionario: dict = Dicionario_libras) -> list:
    # Traduzir texto para uma lista de videos, chamando o dicionario de tradução e retornando uma lista 
        
    if not texto:
        return []

    try:
        
        palavras_texto = texto.lower().strip().split() #vai deixa tudo padronizado, dividindo o texto
       
        chaves_ordenadas = sorted(
            dicionario.keys(), 
            key=lambda k: -len(k.split())
        ) #ordenar e verificar expressoes

        urls_videos = []
        i = 0
        while i < len(palavras_texto):
            encontrado = False
            
            for chave in chaves_ordenadas: #combinação de texto com frases longas
                chave_palavras = chave.split()
                tamanho_chave = len(chave_palavras)
                                
                if (i + tamanho_chave) <= len(palavras_texto) and \
                   palavras_texto[i : i + tamanho_chave] == chave_palavras:
                    
                    url = dicionario.get(chave)
                    if url:
                        urls_videos.append(url)
                    
                    i += tamanho_chave 
                    encontrado = True
                    break 
            
        
            if not encontrado: #caso nenhuma fase seja encontrada, tentar uma palavra única
                palavra_unica = palavras_texto[i]
                url = dicionario.get(palavra_unica)
                
                if url:
                    urls_videos.append(url)
                else:
                    pass 
                
                i += 1 # Avançar para próxima palavra

        return urls_videos
    
    except Exception as e:
        print(f"Erro no serviço de tradução: {e}")
        return []

