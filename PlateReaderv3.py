import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
placa = []

print("Detection y lectura de patentes")
image = cv2.imread('C:/Users/migue/Pictures/patente1.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGRA2GRAY)
gray = cv2.blur(gray, (3,3))
canny = cv2.Canny(gray, 150,200)
#canny = cv2.dilate(canny, None, iterations=1)

# retorna 2 valores 1 son los contornos
cnts,_ = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(image, cnts,-1,(0,255,0),2)

# detectamos el rectangulo de la patente
# Patentes de ARG, Brasil, URU, PAR y VEN Dimensiones: 400 mm x 130 mm y un espesor de 1 mm.
# aspect ratio 400 / 130 = aspect ratio  3.076923076923077
for c in cnts:
    area = cv2.contourArea(c)
    x, y, w, h = cv2.boundingRect(c)
    ep = 0.09 * cv2.arcLength(c,True)
    ap = cv2.approxPolyDP(c, ep, True)
    #print("area:", area)
    if area > 1000 :
        #print("area 2", area)
        #print("aspect ratio ", 400/130)
        as_rat = float(w) / float(h)
        if as_rat > 3 and as_rat < 4.2:
            cv2.drawContours(image, [c], 0, (0,255,0), 2)
            patente = gray[y:y+h,x:x+w]
            #cv2.imshow("Patente", patente)
            patente_detectada = pytesseract.image_to_string(patente, config='--psm 11')
            print("Patente detectada ", patente_detectada)
            cv2.putText(image, patente_detectada, (20,30),cv2.FONT_HERSHEY_PLAIN,2.2,(255,0,0),3,cv2.LINE_AA)

cv2.imshow("Deteccion", image)
cv2.waitKey(0)


