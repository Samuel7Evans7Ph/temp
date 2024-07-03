import cv2
import os
# import matplotlib.pyplot as plt

def bounding_box(img,face_classifier):
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    face=face_classifier.detectMultiScale(grey_img,scaleFactor=1.1,minNeighbors=4,minSize=(40,40))

    print("The number of faces are",len(face),)
    os.makedirs("Image_Files")
    count=0
    for (x,y,w,h) in face:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,4),1)
        file_name=str(count)+'.jpg'
        save_path=os.path.join("Image_Files",file_name)
        image=face[y,y+h:x,x+w]

        cv2.imwrite(save_path,image)



    return




def start_verification(img):


    img_path='/home/opentrends/Downloads/5.jpg'
    # print("here")
    #video_capture=cv2.VideoCapture('/home/opentrends/Downloads/3.mp4')
    face_classifier=cv2.CascadeClassifier(cv2.data.haarcascades +"haarcascade_frontalface_default.xml")
    # while True:

        # result,vid_frame=video_capture.read()
        # if not result:
        #     break

    bounding_box(img,face_classifier)
    cv2.imshow("loading",img)
    cv2.waitKey(0)

    cv2.destroyAllWindows()

        # gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        

    
        # print("Number of faces detected:", len(face))


        # for (x, y, w, h) in face:
        #     cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 4)

    img_rgb = cv2.cvtColor(vid_frame, cv2.COLOR_BGR2RGB)
    return


    # video_capture.release()
    # cv2.destroyAllWindows()


