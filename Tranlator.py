import os
from bs4 import BeautifulSoup, Comment
from googletrans import Translator
import time
import sys

# HTML tag list
tags = ['h1', 'h2', 'h3', 'p', 'ol', 'ul', 'li', 'title', 'span', 'button', 'body', 'a', 'div', 'main', 'footer', 'form', 'strong', 'em', 'small', 'dl', 'dt', 'dd', 'figure', 'figcaption', 'input', 'i']

# root dir of the HTML file
root = './Copia'

def process_file(archive, file):
    # Open and read file
    with open(archive, 'r', encoding='utf-8') as f:
        content_html = f.read()

    # Create an object BeautifulSoup with the content HTML
    soup = BeautifulSoup(content_html, 'html.parser')

    # Create a translator object
    translator = Translator(service_urls=['translate.google.com'])

    # Find all the HTML text tags you want to translate and translate their content
    for tag in soup.find_all(string=True):
        if tag.parent.name in tags:
            if not isinstance(tag, Comment) and tag != "\n":
                try:
                    translated_text = translator.translate(tag, dest='hi')
                    time.sleep(1)
                    tag.string.replace_with(translated_text.text)
                except Exception as e:
                    print(f"Error translate file {file} in {archive}: {e}")
    
    # Remove the file
    os.remove(archive)

    # Save the translated content to a new file with the same name
    with open(archive, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"The file {file} in {archive} has been translate")

root_dir = []
files = []

# Loop through all HTML files in the root directory and its subdirectories
for dirpath, _, filenames in os.walk(root):
    for file in filenames:
        if file.endswith('.html'):
            root_dir.append(dirpath)
            files.append(file)

i = 0
for file in files:
    # Process each file
    archive = os.path.join(root_dir[i], file)
    process_file(archive, file)
    i = i + 1
print("Finished")
end = True

if  end == True:
    sys.exit()