import json
import os
from pathlib import Path

# Data directory is relative to the root of the project (one level up from src)
DATA_DIR = Path(__file__).resolve().parent.parent.parent / "data"
CONFIG_FILE = DATA_DIR / "language.json"

_current_lang = "en"
_translations = {}

def get_current_lang():
    return _current_lang

def load_language():
    global _current_lang, _translations
    if CONFIG_FILE.exists():
        try:
            with open(CONFIG_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                _current_lang = data.get("lang", "en")
        except:
            _current_lang = "en"
    else:
        _current_lang = "en"

    locale_file = Path(__file__).parent / f"locales_{_current_lang}.json"
    if locale_file.exists():
        with open(locale_file, "r", encoding="utf-8") as f:
            _translations = json.load(f)
    else:
        _translations = {}

def set_language(lang):
    global _current_lang
    _current_lang = lang
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump({"lang": lang}, f)
    load_language()

def _(text):
    return _translations.get(text, text)

# Initialize on module import
load_language()
