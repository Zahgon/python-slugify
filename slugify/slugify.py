from __future__ import annotations

import re
import unicodedata
from collections.abc import Iterable
from html.entities import name2codepoint

try:
    import unidecode
except ImportError:
    import text_unidecode as unidecode  # type: ignore[import-untyped, no-redef]

__all__ = ['slugify', 'smart_truncate']


CHAR_ENTITY_PATTERN = re.compile(r'&(%s);' % '|'.join(name2codepoint))
DECIMAL_PATTERN = re.compile(r'&#(\d+);')
HEX_PATTERN = re.compile(r'&#x([\da-fA-F]+);')
QUOTE_PATTERN = re.compile(r'[\']+')
DISALLOWED_CHARS_PATTERN = re.compile(r'[^-a-zA-Z0-9]+')
DISALLOWED_UNICODE_CHARS_PATTERN = re.compile(r'[\W_]+')
DUPLICATE_DASH_PATTERN = re.compile(r'-{2,}')
NUMBERS_PATTERN = re.compile(r'(?<=\d),(?=\d)')
DEFAULT_SEPARATOR = '-'


def smart_truncate(
    string: str,
    max_length: int = 0,
    word_boundary: bool = False,
    separator: str = " ",
    save_order: bool = False,
) -> str:
    """
    Truncate a string.
    :param string (str): string for modification
    :param max_length (int): output string length
    :param word_boundary (bool):
    :param save_order (bool): if True then word order of output string is like input string
    :param separator (str): separator between words
    :return:
    """
    pass


def slugify(
    text: str,
    entities: bool = True,
    decimal: bool = True,
    hexadecimal: bool = True,
    max_length: int = 0,
    word_boundary: bool = False,
    separator: str = DEFAULT_SEPARATOR,
    save_order: bool = False,
    stopwords: Iterable[str] = (),
    regex_pattern: re.Pattern[str] | str | None = None,
    lowercase: bool = True,
    replacements: Iterable[Iterable[str]] = (),
    allow_unicode: bool = False,
) -> str:
    """
    Make a slug from the given text.
    :param text (str): initial text
    :param entities (bool): converts html entities to unicode
    :param decimal (bool): converts html decimal to unicode
    :param hexadecimal (bool): converts html hexadecimal to unicode
    :param max_length (int): output string length
    :param word_boundary (bool): truncates to complete word even if length ends up shorter than max_length
    :param save_order (bool): when set, does not include shorter subsequent words even if they fit
    :param separator (str): separator between words
    :param stopwords (iterable): words to discount
    :param regex_pattern (str): regex pattern for disallowed characters
    :param lowercase (bool): activate case sensitivity by setting it to False
    :param replacements (iterable): list of replacement rules e.g. [['|', 'or'], ['%', 'percent']]
    :param allow_unicode (bool): allow unicode characters
    :return (str):
    """
    pass
