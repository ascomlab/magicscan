import os
import cv2

dir_data = 'D:/GitHub/magicscan/data/'
dir_datatemp = 'D:/GitHub/magicscan/datatemp/'
dimImg = 50
path1, dirs1, files1 = next(os.walk(dir_data)) #Get folders

for i in range(len(dirs1)):
    print("processing "+dirs1[i]+".....")
    path, dirs, files = next(os.walk(dir_data+dirs1[i])) #Get files
    keep_temp_path = dir_datatemp+dirs1[i]+'/'
    if not os.path.exists(keep_temp_path):
        os.makedirs(keep_temp_path)

    for j in range(len(files)):
        file_path = dir_data+files[j]
        if file_path.lower().endswith(('.png', '.jpg', '.jpeg', 'tif', 'tiff')):
            frame = cv2.imread(file_path, cv2.IMREAD_COLOR)
            img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            resizeimg = cv2.resize(img_gray, (dimImg, dimImg))
            cv2.imwrite(keep_temp_path + dirs1[i]+'_'+str(j)+'.png' , resizeimg)

        elif file_path.lower().endswith(('.mp4')):

            cap = cv2.VideoCapture(file_path)
            video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            print("Number of frames: ", video_length)
            count = 0
            print("Converting video..\n")

            while cap.isOpened():

                ret, frame = cap.read()
                img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                resize = cv2.resize(img_gray, (dimImg, dimImg))
                cv2.imwrite(keep_temp_path + dirs1[i]+'_'+str(j)+'_%d.png' %count , resizeimg)
                count = count + 1
                if (count > (video_length-1)):
                    cap.release()
                    break








