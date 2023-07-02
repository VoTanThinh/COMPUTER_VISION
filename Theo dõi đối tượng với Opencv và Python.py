import cv2

# Đọc hình ảnh
image = cv2.imread("hoahong.jpg")

# Chuyển đổi sang ảnh đen trắng
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Áp dụng phương pháp tách biên Canny
edges = cv2.Canny(gray, threshold1=255, threshold2=255)
filtered_image = cv2.GaussianBlur(image, (255, 255), 0)
# Tìm kiếm và vẽ khung bao xung quanh các đối tượng đã tách biên
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Hiển thị hình ảnh với khung bao xung quanh các đối tượng
cv2.imshow("Image with Bounding Boxes", image)
cv2.waitKey(0)
cv2.destroyAllWindows()