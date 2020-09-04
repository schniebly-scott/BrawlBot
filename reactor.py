import numpy as np
import cv2
from PIL import ImageGrab

class Reactor:
    mouseX = 100
    mouseY = 100
    clicked = False
    track_window = (100, 100, 100, 100)

    def click_event(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN and self.clicked == False:
            self.mouseX = x
            self.mouseY = y
            self.clicked = True
            self.track_window = (self.mouseX, self.mouseY, 100, 100)

    def process_img(self, org_img):
        '''processes images'''
        processed_img = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
        processed_img = cv2.Canny(processed_img, 200, 300)
        return processed_img

    def start_watch(self):
        #fgbg = cv2.createBackgroundSubtractorMOG2()
        term_crit = ( cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
        while(1):
            #print("X: {}, Y: {}".format(self.mouseX, self.mouseY))
            screen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
            #fgmask = fgbg.apply(screen)
            
            line_screen = self.process_img(screen)
            ret, self.track_window = cv2.CamShift(line_screen, self.track_window, term_crit)

            pts = cv2.boxPoints(ret)
            pts = np.int0(pts)
            final_image = cv2.polylines(screen, [pts], True, (0, 255, 0), 2)
            #cv2.rectangle(screen, (self.mouseX-50, self.mouseY-50), (self.mouseX+50, self.mouseY+50), (0, 255, 0), 3)
            cv2.imshow('Tracker', cv2.cvtColor(final_image, cv2.COLOR_RGB2BGR))
            
            cv2.setMouseCallback('Tracker', self.click_event)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
    
