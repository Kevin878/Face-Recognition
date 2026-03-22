# 家庭成員人臉辨識系統

這是一個使用 Python 與 OpenCV 製作的人臉辨識專案，主要用途是透過攝影機擷取人臉影像、訓練 LBPH 人臉辨識模型，最後進行即時辨識。

## 專案功能

- 使用電腦攝影機擷取人臉影像
- 將影像儲存為訓練資料集
- 使用 Haar Cascade 進行人臉偵測
- 使用 OpenCV 的 `LBPHFaceRecognizer` 訓練辨識模型
- 透過即時攝影機畫面進行人臉辨識

## 專案結構

```text
Project_2-Family-Identify/
├── Create-image.py      # 建立影像資料集
├── Module-Train.py      # 訓練人臉辨識模型
├── main.py              # 即時人臉辨識
├── Image_library2/      # 儲存訓練影像
└── recognizer.yml       # 訓練完成後產生的模型檔
```

另外，本專案使用外部的人臉偵測模型：

```text
../source/face_detect.xml
```

請確認此檔案存在，否則訓練與辨識都無法執行。

## 執行環境

- Python 3.x
- OpenCV
- NumPy
- 可正常使用的電腦攝影機

建議安裝套件：

```bash
pip install opencv-contrib-python numpy
```

注意：本專案使用 `cv2.face.LBPHFaceRecognizer_create()`，因此必須安裝 `opencv-contrib-python`，不能只裝 `opencv-python`。

## 使用流程

### 1. 建立人臉影像資料集

執行：

```bash
python Create-image.py
```

程式會：

- 開啟預設攝影機
- 建立 `Image_library2` 資料夾（若尚未存在）
- 自動擷取影像並儲存前 100 張畫面
- 檔名格式為 `2_0000.jpg`、`2_0001.jpg` ...

按下 `q` 可以提前結束。

### 2. 訓練人臉辨識模型

執行：

```bash
python Module-Train.py
```

程式會：

- 讀取 `Image_library2` 內的 `.jpg` 檔案
- 從檔名的前半段擷取使用者 ID
- 偵測影像中的人臉區域
- 使用 LBPH 演算法訓練模型
- 產生 `recognizer.yml`

## 檔名規則

訓練程式會從檔名中解析 ID：

```text
人物ID_流水號.jpg
```

例如：

```text
2_0001.jpg
```

其中：

- `2` 代表人物 ID
- `0001` 代表該人物的第幾張影像

如果要加入其他家庭成員，可以依照相同格式建立影像，例如：

```text
1_0000.jpg
3_0000.jpg
4_0000.jpg
```

### 3. 開始即時辨識

執行：

```bash
python main.py
```

程式會：

- 開啟攝影機
- 使用 `face_detect.xml` 偵測畫面中的人臉
- 載入 `recognizer.yml` 進行辨識
- 在畫面上顯示辨識結果與信心值

按下 `q` 可離開程式。

## 辨識結果說明

`main.py` 目前的邏輯如下：

- 當 `confidence < 40` 時，畫面顯示：

```text
This guy is {label} confidence {confidence}
```

- 否則顯示：

```text
NO!!!!
```

其中：

- `label` 是模型預測的人物 ID
- `confidence` 數值越低，通常代表越接近訓練資料中的人臉

## 注意事項

- `Create-image.py` 目前寫死輸出到 `Image_library2`
- 影像檔名目前預設使用人物 ID `2`
- `main.py` 顯示的是數字 ID，尚未建立「ID 對應姓名」功能
- 若 `recognizer.yml` 尚未產生，`main.py` 將無法正常辨識
- 若 `../source/face_detect.xml` 路徑錯誤，程式會無法偵測人臉

## 可改進方向

- 加入多位家庭成員的姓名對照表
- 在擷取資料時只儲存偵測到的人臉區域，而非整張畫面
- 將人物 ID、輸出資料夾、擷取張數改為可設定參數
- 顯示更友善的辨識訊息，例如姓名而不是數字 ID
- 加入錯誤處理與訓練資料檢查機制

## 作者說明

本專案適合用來練習：

- OpenCV 基本影像處理
- Haar Cascade 人臉偵測
- LBPH 人臉辨識流程
- 攝影機即時影像擷取與模型應用
