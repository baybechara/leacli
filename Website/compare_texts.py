import re
import sys
from html.parser import HTMLParser

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.texts = []
        self.in_script_or_style = False
        
    def handle_starttag(self, tag, attrs):
        if tag in ('script', 'style'):
            self.in_script_or_style = True
            
    def handle_endtag(self, tag):
        if tag in ('script', 'style'):
            self.in_script_or_style = False
            
    def handle_data(self, data):
        if not self.in_script_or_style:
            text = data.strip()
            if text:
                text = re.sub(r'\s+', ' ', text)
                self.texts.append(text)

def get_text_nodes(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    parser = TextExtractor()
    parser.feed(html)
    return parser.texts

file_current = r"c:\Users\User\Desktop\LEACLI\LeaCLI new\Website\promotion\google-ads-contextual-ads.html"
file_user = r"c:\Users\User\Desktop\LEACLI\LeaCLI new\Страница контекст\Страница контекст\ai.leacli.com\promotion\google-ads-contextual-ads.html"

texts_current = get_text_nodes(file_current)
texts_user = get_text_nodes(file_user)

from difflib import ndiff

diff = list(ndiff(texts_current, texts_user))
diff_filtered = [line for line in diff if line.startswith('+ ') or line.startswith('- ')]

with open("compare_results.txt", "w", encoding="utf-8") as out:
    out.write(f"Current texts count: {len(texts_current)}\n")
    out.write(f"User texts count: {len(texts_user)}\n\n")
    out.write("--- Differences found ---\n")
    for line in diff_filtered:
        out.write(line + "\n")
print("Done writing compare_results.txt")
