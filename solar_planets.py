import cv2

# Leia a imagem
img = cv2.imread("solar-system.jpg")

# Adicione texto para cada planeta
cv2.putText(img, "Mercurio", (120, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Venus", (200, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Terra", (290, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Marte", (380, 150), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
cv2.putText(img, "Jupiter", (500, 300), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv2.putText(img, "Saturno", (720, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv2.putText(img, "Urano", (950, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
cv2.putText(img, "Netuno", (1080, 200), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

# Exiba a imagem
cv2.imshow("resultado", img)

# Aguarde até que uma tecla seja pressionada
cv2.waitKey(0)

# Salve a imagem com os textos
cv2.imwrite("Solar_system_with_names.jpg", img)

# Feche todas as janelas
cv2.destroyAllWindows()
