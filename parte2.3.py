from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

ruta_dir = 'parte-2-b/'
pdfs = os.listdir(ruta_dir)

text = ''

for pdf in pdfs:

	print '\n \n'+pdf
	pages = convert_from_path(ruta_dir+pdf, 500, None, None, None)
	#f = open(pdf+'.txt', "a")

	i = 1
	
	for page in pages:
		page.save('out_'+str(i)+'.jpg', 'JPEG')
		text = text + pytesseract.image_to_string(Image.open('out_'+str(i)+'.jpg'))
		#f.write(text)
		os.remove('out_'+str(i)+'.jpg')
		i = i + 1

	#f.close()
	print text


