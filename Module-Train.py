import cv2
import os
import numpy as np

# 資料集路徑
face_data_dir = 'Image_library2'

# 初始化人臉檢測器
face_cascade = cv2.CascadeClassifier('../source/face_detect.xml')

# 創建兩個列表，一個存儲圖像數據，另一個存儲對應的 ID
face = []
ids = []

# 瀏覽所有圖像
for image_name in os.listdir(face_data_dir):
    if image_name.endswith(".jpg"):
        # 從文件名中提取ID
        user_id = int(image_name.split('_')[0])
        
        # 加載圖像並轉換為灰階
        image_path = os.path.join(face_data_dir, image_name)
        gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

        # 檢測人臉
        faces = face_cascade.detectMultiScale(gray_image)
        for (x, y, w, h) in faces:
            face.append(gray_image[y:y+h, x:x+w])
            ids.append(user_id)

# 將ID轉換為 NumPy 數組
ids = np.array(ids)

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.train(face, ids)
recognizer.save('recognizer.yml') #儲存模型