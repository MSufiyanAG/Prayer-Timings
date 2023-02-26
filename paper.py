import requests
from bs4 import BeautifulSoup
import cv2
import fitz


response = requests.get('https://munsifdaily.in/epapers/')
soup = BeautifulSoup(response.text, 'html.parser')
links = soup.find_all('a')

i = 0

# From all links check for pdf link and
# if present download file
for link in links:
    if ('.pdf' in link.get('href', [])):
        i += 1
        #print("Downloading file: ", i)

        # Get response object for link
        response = requests.get(link.get('href'))

        # Write content in pdf file
        pdf = open("pdf"+str(i)+".pdf", 'wb')
        pdf.write(response.content)
        pdf.close()
        break
        #print("File ", i, " downloaded")

#print("All PDF files downloaded")


pdffile = "pdf1.pdf"
doc = fitz.open(pdffile)
page = doc.load_page(1)  # number of page

zoom = 5    # zoom factor
mat = fitz.Matrix(zoom, zoom)
pix = page.get_pixmap(matrix = mat)
pix.save('op.jpeg')
doc.close()


img = cv2.imread("op.jpeg")
crop = img[450:600, 1275:1800] 
cv2.imwrite('cropped.jpeg', crop)