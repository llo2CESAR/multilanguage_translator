from flask import Flask
from flask_cors import CORS
from src.infrastructure.persistence.in_memory_libras_repository import InMemoryLibrasRepository
from src.domain.use_cases.translate_text_to_libras import TranslateTextToLibrasUseCase
from src.infrastructure.web.controllers.translation_controller import translation_bp, TranslationController
import os
import sys

app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), '..', 'templates'), static_folder=os.path.join(os.path.dirname(__file__), '..', 'static'))
CORS(app)

repository = InMemoryLibrasRepository()
translate_use_case = TranslateTextToLibrasUseCase(repository)  
TranslationController(translate_use_case)

app.register_blueprint(translation_bp)

if __name__ == '__main__':
    app.run(debug=True)