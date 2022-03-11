import xml.etree.ElementTree as ET

from lxml import etree
from io import StringIO, BytesIO

from xml.dom.minidom import parse, parseString
from inspect import getmembers, isclass, isfunction


parser = etree.HTMLParser()
tree = etree.parse("transANC13trk1-PO.html", parser)
root = tree.getroot()
transcriptions = []
for element in root.iter("td"):
    if element.get('class') == 'transcription':
        transcriptions.append(element.text)

with open('aleut_trans.txt', 'w', encoding='utf-8') as file:
    for trans in transcriptions:
        file.write(trans + '\n')

