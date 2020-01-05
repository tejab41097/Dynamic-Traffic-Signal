import cv2
import numpy as np
import vehicles
import time

class Cameras:
    
    def __init__ (self, video_name):
        self.video_name=video_name
        
    def count_CARS(self):
        
        cnt_down=0
        
        cap=cv2.VideoCapture(self.video_name)

        #Get width and height of video

        w=cap.get(3)
        h=cap.get(4)
        frameArea=h*w
        areaTH=frameArea/400

        #Lines

        line_down=int(4*(h/5))
        up_limit=int(1*(h/5))
        down_limit=int(4.5*(h/5))

        line_down_color=(255,0,0)
        pt1 =  [0, line_down]
        pt2 =  [w, line_down]
        pts_L1 = np.array([pt1,pt2], np.int32)
        pts_L1 = pts_L1.reshape((-1,1,2))

        pt5 =  [0, up_limit]
        pt6 =  [w, up_limit]
        pts_L3 = np.array([pt5,pt6], np.int32)
        pts_L3 = pts_L3.reshape((-1,1,2))
        pt7 =  [0, down_limit]
        pt8 =  [w, down_limit]
        pts_L4 = np.array([pt7,pt8], np.int32)
        pts_L4 = pts_L4.reshape((-1,1,2))

        #Background Subtractor
        fgbg=cv2.createBackgroundSubtractorMOG2(detectShadows=True)

        #Kernals
        kernalOp = np.ones((3,3),np.uint8)

        font = cv2.FONT_HERSHEY_SIMPLEX
        cars = []
        max_p_age = 5
        pid = 1

        #time constraints
        timeout = 5
        timeout_start = time.time()

        while(time.time() < timeout_start + timeout):
            ret,frame=cap.read()
            for i in cars:
                i.age_one()
            fgmask=fgbg.apply(frame)
            fgmask2=fgbg.apply(frame)

            if ret==True:

                #Binarization
                ret,imBin=cv2.threshold(fgmask,200,255,cv2.THRESH_BINARY)
                ret,imBin2=cv2.threshold(fgmask2,200,255,cv2.THRESH_BINARY)
                #Opening i.e First Erode the dilate
                mask=cv2.morphologyEx(imBin,cv2.MORPH_OPEN,kernalOp)

                #Find Contours
                _, countours0,hierarchy=cv2.findContours(mask,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
                for cnt in countours0:
                    area=cv2.contourArea(cnt)
                    if area>areaTH:
                        ####Tracking######
                        m=cv2.moments(cnt)
                        cx=int(m['m10']/m['m00'])
                        cy=int(m['m01']/m['m00'])
                        x,y,w,h=cv2.boundingRect(cnt)

                        new=True
                        if cy in range(up_limit,down_limit):
                            for i in cars:
                                if abs(x - i.getX()) <= w and abs(y - i.getY()) <= h:
                                    new = False
                                    i.updateCoords(cx, cy)

                                    if i.going_DOWN(line_down)==True:
                                        cnt_down+=1
                                        print("Count:",cnt_down)
                                    break
                                if i.getState()=='1':
                                    if i.getDir()=='down'and i.getY()>down_limit:
                                        i.setDone()
                                if i.timedOut():
                                    index=cars.index(i)
                                    cars.pop(index)
                                    del i

                            if new==True: #If nothing is detected,create new
                                p=vehicles.Car(pid,cx,cy,max_p_age)
                                cars.append(p)
                                pid+=1
                                
                        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

        
                str_down='DOWN: '+str(cnt_down)
                frame=cv2.polylines(frame,[pts_L1],False,line_down_color,thickness=2)
                frame=cv2.polylines(frame,[pts_L3],False,(255,255,255),thickness=1)
                frame=cv2.polylines(frame,[pts_L4],False,(255,255,255),thickness=1)
                cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 255, 255), 2, cv2.LINE_AA)
                cv2.putText(frame, str_down, (10, 90), font, 0.5, (255, 0, 0), 1, cv2.LINE_AA)
                cv2.imshow('Frame',frame)

                if cv2.waitKey(1)&0xff==ord('q'):
                    break

            else:
                break

        cap.release()
        cv2.destroyAllWindows()
        return cnt_down