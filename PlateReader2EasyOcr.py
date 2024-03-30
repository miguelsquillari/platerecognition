import cv2
import easyocr


class LicensePlateDetector:
    def __init__(self):
        # Inicializa EasyOCR con el idioma deseado (por ejemplo, español)
        self.reader = easyocr.Reader(['en'])

    def detect_license_plate(self, image_path):
        try:
            # Carga la imagen
            image = cv2.imread(image_path)

            # Realiza OCR en la imagen
            results = self.reader.readtext(image)

            # Filtra los resultados para obtener solo las matrículas
            license_plates = [result[1] for result in results if 'license' in result[1].lower()]

            return license_plates

        except Exception as e:
            return f"Error al procesar la imagen: {str(e)}"

# Ejemplo de uso
if __name__ == "__main__":
    image_path = "C:/Users/migue/Pictures/patente1.jpg"
    detector = LicensePlateDetector()
    detected_plates = detector.detect_license_plate(image_path)

    if detected_plates:
        print(f"Matrículas detectadas: {', '.join(detected_plates)}")
    else:
        print("No se encontraron matrículas en la imagen.")
