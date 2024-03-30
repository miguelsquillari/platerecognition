import cv2
import pytesseract


class CarPlateDetector:
    def __init__(self):
        pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        # Inicializa el clasificador preentrenado para detección de automóviles
        self.car_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')

    def detect_car_plate(self, image_path):
        try:
            # Carga la imagen
            image = cv2.imread(image_path)

            # Convierte la imagen a escala de grises
            gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

            # Detecta automóviles en el fotograma
            cars = self.car_cascade.detectMultiScale(gray_image, 1.1, 3)

            # Si se detecta un automóvil, procesa la matrícula
            if len(cars) > 0:
                x, y, w, h = cars[0]
                license_plate_image = gray_image[y:y + h, x:x + w]

                # Realiza OCR en la imagen de la matrícula
                license_plate_text = pytesseract.image_to_string(license_plate_image, config='--psm 7')

                return license_plate_text.strip()
            else:
                return "No se detectó ningún automóvil en la imagen."

        except Exception as e:
            return f"Error al procesar la imagen: {str(e)}"


# Ejemplo de uso
if __name__ == "__main__":
    image_path = "C:/Users/migue/Pictures/patente1.jpg"
    reader = CarPlateDetector()
    plate_number = reader.detect_car_plate(image_path)
    print(f"Matrícula detectada: {plate_number}")
