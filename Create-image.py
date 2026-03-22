import cv2
import os

# 定義儲存影像的資料夾名稱
output_dir = 'Image_library2'

# 檢查資料夾是否存在，如果不存在則創建
if not os.path.exists(output_dir):
    os.makedirs(output_dir)
    print(f"已創建資料夾: {output_dir}")
else:
    print(f"資料夾已存在: {output_dir}")
    # if os.listdir(output_dir):
    #     for filename in os.listdir(output_dir):
    #         file_path = os.path.join(output_dir, filename)
    #         if os.path.isfile(file_path) or os.path.islink(file_path):
    #             os.unlink(file_path)  # 刪除文件
    #             print(f"已刪除文件: {file_path}")
    #         elif os.path.isdir(file_path):
    #             print(f"跳過資料夾: {file_path}")

# 初始化攝像頭，索引為0表示預設攝像頭
cap = cv2.VideoCapture(0)

# 檢查攝像頭是否成功打開
if not cap.isOpened():
    print("無法打開攝像頭")
    exit()

frame_count = 0  # 用於命名影像檔案

print("開始捕捉影像。按 'q' 鍵退出。")

while True:
    # 捕捉一幀影像
    ret, frame = cap.read()
    
    if not ret:
        print("無法接收影像（可能攝像頭已關閉）")
        break

    # 顯示影像在視窗中
    cv2.imshow('攝像頭', frame)

    # 增加幀計數
    frame_count += 1

    if frame_count <= 100:
        # 定義影像檔案名稱，使用四位數編號
        filename = os.path.join(output_dir, f"2_{frame_count-1:04d}.jpg")
    
        # 儲存影像到指定的檔案
        cv2.imwrite(filename, frame)
        print(f"儲存: {filename}")

    # 檢查是否按下 'q' 鍵以退出
    if cv2.waitKey(1) & 0xFF == ord('q') or frame_count >= 301:
        break

# 釋放攝像頭資源
cap.release()

# 關閉所有 OpenCV 視窗
cv2.destroyAllWindows()
