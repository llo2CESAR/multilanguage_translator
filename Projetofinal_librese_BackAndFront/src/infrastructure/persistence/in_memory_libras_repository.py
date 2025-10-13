from typing import Dict
from src.domain.repositories.libras_repository import ILibrasRepository

class InMemoryLibrasRepository(ILibrasRepository):
    def __init__(self):
        # Use keys normalized (lowercase, sem acento, sem pontuação)
        # e filenames padronizados em lowercase com underscores (recomendado)
        self._mappings: Dict[str, str] = {
            "oi": "/static/Gifs/oi.gif",
            "ok": "/static/Gifs/ok.gif",
            "boa noite": "/static/Gifs/boa_noite.gif",
            "boa_noite": "/static/Gifs/boa_noite.gif",
            "boanoite": "/static/Gifs/boa_noite.gif",
            "boa-tarde": "/static/Gifs/boa_tarde.gif",
            "bom dia": "/static/Gifs/bom_dia.gif",
            "bom_dia": "/static/Gifs/bom_dia.gif",
            "de nada": "/static/Gifs/de_nada.gif",
            "de_nada": "/static/Gifs/de_nada.gif",
            "legal": "/static/Gifs/legal.gif",
            "meu nome e": "/static/Gifs/meu_nome_e.gif",
            "meu_nome_e": "/static/Gifs/meu_nome_e.gif",
            "obrigado": "/static/Gifs/obrigado.gif",
            "por favor": "/static/Gifs/por_favor.gif",
            "por_favor": "/static/Gifs/por_favor.gif",
            "tchau": "/static/Gifs/tchau.gif",
            "prazer em te conhecer": "/static/Gifs/prazer_em_te_conhecer.gif",
            "qual e o seu nome": "/static/Gifs/qual_e_o_seu_nome.gif"
        }

    def get_all_mappings(self) -> Dict[str, str]:
        return self._mappings.copy()
