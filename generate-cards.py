#!/usr/bin/env python
# encoding: utf-8

# Imports #####################################################################

import codecs, StringIO, sys, urllib, cStringIO

from pyPdf import PdfFileWriter, PdfFileReader
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics import renderPDF
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.lib.utils import ImageReader


# Functions ###################################################################

def main():
    if len(sys.argv) != 2:
        print u'Usage: {file} <qr_file.csv>'.format(file=__file__)
        return 1

    cards_list_file = sys.argv[1]

    output = PdfFileWriter()

    for card in get_cards_list(cards_list_file):

        # Draw qr
        pdf = StringIO.StringIO()
        c = canvas.Canvas(pdf, pagesize=letter)
        image = ImageReader(card['url'])
        iw, ih = image.getSize()
        width = 41.5
        aspect = ih / float(iw)
        c.drawImage(image, 177, 63 - ((width * aspect)/2), width=width, height=(width * aspect), mask='auto')
        c.setFont("Helvetica", 7)
        string = card['firstname'] + " " + card['lastname']
        c.drawString(22, 69.5, string)
        string = card['birthdate']
        c.drawString(22, 40, string)
        c.showPage()
        c.save()
        pdf.seek(0)
        new_pdf = PdfFileReader(pdf)

        # Read card file
        existing_pdf = PdfFileReader(file("card.pdf", "rb"))

        # Merge pdf's
        page = existing_pdf.getPage(0)
        page.mergePage(new_pdf.getPage(0))
        output.addPage(page)

        print u'\U0001F37A  Generating {0}'.format(card['firstname'])

    # Write output to file
    outputStream = file(u'cards.pdf'.format(card['firstname']), "wb")
    output.write(outputStream)
    outputStream.close()

def get_cards_list(cards_list_file):
    cards = []
    with codecs.open(cards_list_file, encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            card_row = line.split(';')
            cards.append({
                'firstname': card_row[0],
                'lastname': card_row[1],
                'birthdate': card_row[2],
                'url': card_row[3]
            })
    return cards

# Main ########################################################################

if __name__ == '__main__':
    return_code = main()
    sys.exit(return_code)
