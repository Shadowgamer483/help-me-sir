import cv2
import dropbox
import time
import random
start_time=time.time()
def snap():
    number=random.randint(0,100)
    #HOW WE INITIALIZE MODULE CV2(cv2=camera)
    video_capture_object=cv2.VideoCapture(0)
    result=True
    while (result):
        ret,frame=video_capture_object.read()
        imagename="IMGG"+str(number)+".png"
        cv2.imwrite(imagename,frame)
        start_time=time.time()
        #result=false makes so only happen if we get image
        result=False
    return imagename
    print("snapshot taken")
    video_capture_object.release()
    cv2.destroyAllWindows()
def upload_file(imagename):
    access_token="fCSnMk2rVa8AAAAAAAAAAZfrCR_ahZLtVQ9lY0Iz_nVnA1n36lUfE6ck3MaXN89b"
    file=imagename
    file_from=file
    file_to="/testfolder/"+(imagename)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,"rb")as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print("upload it  :)")
def main():
    while(True):
        if ((time.time()-start_time)>=10):
            name=snap()
            upload_file(name)
main()

