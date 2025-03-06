'''

Securely protect and hide your PDFs from unwanted access.

Haris Khan

3/5/2025

'''

from PyPDF2 import PdfWriter, PdfReader
import getpass

pdfwriter=PdfWriter()
pdf=PdfReader("Your_Pdf_Name_Here.pdf")

for num_pg in range(len(pdf.pages)):
    pdfwriter.add_page(pdf.pages[num_pg])
pswd = getpass.getpass(prompt = 'Enter password: ')
pdfwriter.encrypt(pswd)
with open('Store_New_Pdf', 'wb') as f:
    pdfwriter.write(f)
