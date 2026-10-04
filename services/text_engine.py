import string
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
from rake_nltk import Rake
from langdetect import detect 

try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('tokenizers/punkt_tab')
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('punkt')
    nltk.download('punkt_tab')
    nltk.download('stopwords')

LANGUAGE_MAP = {
    'en': 'english',
    'id': 'indonesian',
    'es': 'spanish',
    'fr': 'french',
    'de': 'german',
    'it': 'italian',
    'nl': 'dutch'
}

def _get_language(text: str) -> str:
    """Mendeteksi bahasa dan mengambil nama bahasa untuk NLTK."""
    try:
        lang_code = detect(text)
        return LANGUAGE_MAP.get(lang_code, 'english')
    except:
        return 'english'

def generate_summary(text: str) -> tuple[str, str]:
    """Membuat ringkasan otomatis sesuai bahasa yang terdeteksi."""
    lang = _get_language(text)
    words = word_tokenize(text)
    sentences = sent_tokenize(text)

    if len(sentences) <= 2:
        return text, lang

    try:
        stop_words = set(stopwords.words(lang))
    except OSError:
        stop_words = set(stopwords.words("english"))
    
    freq_table = dict()
    for word in words:
        word = word.lower()
        if word in stop_words or word in string.punctuation:
            continue
        if word in freq_table:
            freq_table[word] += 1
        else:
            freq_table[word] = 1

    sentence_value = dict()
    for sentence in sentences:
        for word, freq in freq_table.items():
            if word in sentence.lower():
                if sentence in sentence_value:
                    sentence_value[sentence] += freq
                else:
                    sentence_value[sentence] = freq

    sum_values = sum(sentence_value.values())
    average = int(sum_values / len(sentence_value)) if len(sentence_value) > 0 else 0

    summary = ''
    for sentence in sentences:
        if (sentence in sentence_value) and (sentence_value[sentence] > (1.2 * average)):
            summary += " " + sentence

    if not summary.strip():
        return " ".join(sentence[:2]), lang

    return summary.strip(), lang

def extract_keywords(text: str) -> tuple[list[str], str]:
    """Mengekstrak Kata kunci otomatis sesuai bahasa yang terdeteksi."""
    lang = _get_language(text)

    try:
        r = Rake(language=lang)
    except Exception:
        r = Rake(language="english")

    r.extract_keywords_from_text(text)
    return r.get_ranked_phrases()[:5], lang