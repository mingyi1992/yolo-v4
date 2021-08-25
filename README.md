# yolo-v4
### requirements
scipy==1.2.1</br>
numpy==1.17.0</br>
matplotlib==3.1.2</br>
opencv_python==4.1.2.30</br>
torch==1.2.0</br>
torchvision==0.4.0</br>
tqdm==4.60.0</br>
Pillow==8.2.0</br>
h5py==2.10.0</br>
tensorflow==2.2.0</br>
註 : 不知為何，gpu一直無法順利啟動...所以這邊選擇安裝一般的tensorflow而不是tensorflow-gpu</br>

### How to use</br>
(1)將圖片檔至於 VOCdevkit -> VOC2007 -> JPEGImages 下，yolo的boundin-box檔(xml)則至於同一路徑的Annotations資料夾下</br>
(2)將voc2yolo4.py的trainval_percent參數改為1</br>
(3)依次執行跟目錄底下的voc_annotation.py跟kmeans_for_anchors.py為模組設定要認識的class及依照bounding-box的大小作k-means分群</br>
(4)進入model-data修改my_classes，把你要認的東西也都寫上去</br>
(5)執行train.py開始訓練模組，如果要用tensorboard觀察也可以在這邊開啟，參數分為train_loss及total_loss，分別表示訓練損失函數及測試損失函數</br>
如果兩個都穩定下降表示模組仍在學習當中</br>
若total_loss下降而train_loss停滯表示你的數據及有問題</br>
若total_loss停滯而train_loss持續下降則表示模組產生過擬合</br>
若兩者皆停滯則表示你的學習率太大了，模組目前處在學習瓶頸<>

(6)訓練完成之後將將voc2yolo4.py的trainval_percent參數改為0讓圖片全部參與測驗</br>
(7)依次執行get_dr_txt.py，get_gt_txt.py，get_map.py，如果出現缺少model，則請直接安裝新版的pytorch及torchvision即可解決，</br>
若是出現out-of-range，則表示你的xml裡面有label用到空白符號或是錯位，請進行修正。</br>
input資料夾內的資料是測試mAP用的，如果報錯則是因為這邊的資料，也修要修正</br>
(8)把圖片放進img資料夾後，執行predict.py即可測驗yolo模組成效</br>
