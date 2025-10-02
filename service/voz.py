
def reconhecer_voz(dados_audio):
  
    if dados_audio: #usar biblioteca para retornar o texto transcrito
          texto_transcrito = "Olá, meu nome é Bruna."
          return texto_transcrito
    return None

def traduzir_texto_para_libras(texto):
    
    if not texto or texto.lower() in ["sinal não detectado", "nenhum texto."]:
        return []

    videos_libras = []  #gerar videos os links
    
    return videos_libras