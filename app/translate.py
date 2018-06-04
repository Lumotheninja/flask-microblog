import json
import requests
from flask import current_app
from flask_babel import _


def translate(text, source_language, dest_language):
    if 'YANDEX_KEY' not in current_app.config or \
            not current_app.config['YANDEX_KEY']:
        return _('Error: the translation service is not configured.')
    auth = current_app.config['YANDEX_KEY']
    print (auth)
    print (1211)
    r = requests.get('https://translate.yandex.net/api/v1.5/tr.json/translate?key={}&text={}&lang={}-{}'.format(
        auth, text, source_language, dest_language))
    if r.status_code != 200:
        return _('Error: the translation service failed.')
    return json.loads(r.content.decode('utf-8-sig')).get('text')[0]