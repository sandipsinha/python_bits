import cv2
import os

def load_images_from_folder(folder):
    images=[]
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder, filename))
        #cv2.imshow("image",img)
        #cv2.waitKey(0)
        if img is not None:
            images.append(img)
    return images

if __name__ == '__main__':
    folder = '/Users/ssinha/pythonplay/example'
    get_images = load_images_from_folder(folder)
    print get_images
