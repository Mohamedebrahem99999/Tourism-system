import os

MAX_ATTEMPTS = 3

EMAIL_REGEX = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
PHONE_REGEX = r"^01[0125]\d{8}$"
NATIONAL_ID_REGEX = r"^\d{14}$"
ISBN_PATTERN = r"^[\d-]{10,17}$"
URL_REGEX = r"^https?://[^\s/$.?#].[^\s]*/.+\.(PDF|DOCX|DOC|PPTX|TXT|EPUB|RTF)(\?[^\s]*)?$"

ALLOWED_FILE_FORMAT = ['PDF', 'DOCX', 'DOC', 'PPTX', 'TXT', 'EPUB', 'RTF']
USERS_FILE = "users.json"
ATTRACTIONS_FILE = "attractions.json"