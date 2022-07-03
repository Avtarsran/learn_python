import PyPDF2
a = PyPDF2.PdfFileReader('pdf.pdf')
# print(a.documentInfo)
# print(a.getNumPages())
print(a.getPage(2).extractText())
str = ""
for i in range(1,11):
    str += a.getPage(2).extractText()
    
with open('Texttext.txt',"w",encoding="utf-8") as f:
    f.write(str)
