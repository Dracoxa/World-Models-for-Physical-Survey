from html.parser import HTMLParser
from pathlib import Path
class Site(HTMLParser):
    def __init__(self):
        super().__init__(); self.ids = set(); self.urls = []; self.images = 0
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if 'id' in attrs: self.ids.add(attrs['id'])
        if 'src' in attrs: self.urls.append(attrs['src'])
        if tag in ('a','link') and 'href' in attrs: self.urls.append(attrs['href'])
        self.images += tag == 'img'
root = Path(__file__).resolve().parent
site = Site(); site.feed((root/'index.html').read_text())
for url in site.urls:
    if url.startswith('#'): assert url[1:] in site.ids, url
    elif url.startswith('assets/'): assert (root/url.split('#')[0]).is_file(), url
assert site.images == 7
assert not (root/'.openai').exists()
print('Passed: seven figures, local assets, and section anchors.')
