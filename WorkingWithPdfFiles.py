import PyPDF2
# rb means reading in binary method.
myfile = open('covid-safe-australia-roadmap.pdf', mode='rb')
pdf_reader = PyPDF2.PdfFileReader(myfile)
page_count = pdf_reader.numPages
page_one = pdf_reader.getPage(0)
data_from_page_one = page_one.extractText()
print(data_from_page_one)
myfile.close()

my_file = open('covid-safe-australia-roadmap.pdf', 'rb')
pdf_reader = PyPDF2.PdfFileReader(my_file)
first_page = pdf_reader.getPage(0)
pdf_writer = PyPDF2.PdfFileWriter()
pdf_writer.addPage(first_page)
pdf_output = open('MyNewPdfFile.pdf', 'wb')
pdf_writer.write(pdf_output)
pdf_output.close()
my_file.close()


my_new_pdf = open("MyNewPdfFile.pdf", 'rb')
pdf_reader = PyPDF2.PdfFileReader(my_new_pdf)
page_count = pdf_reader.numPages
print(f"\n\npage_count of new pdf is {page_count} \n\n")
my_new_pdf.close()

pdf_file = open("MyNewPdfFile.pdf", 'rb')
pdf_text = [0]
pdf_reader = PyPDF2.PdfFileReader(pdf_file)
for p in range(pdf_reader.numPages):
    page = pdf_reader.getPage(p)
    pdf_text.append(page.extractText())

pdf_file.close()

for page in pdf_text:
    print(page)
    print('\n \n \n \n')
