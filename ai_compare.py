import cv2
from skimage.metrics import structural_similarity
def orb_sim(img1,img2):
    orb=cv2.ORB_create()
    kp_a,desc_a=orb.detectAndCompute(img1,None)
    kp_b,desc_b=orb.detectAndCompute(img2,None)
    bf=cv2.BFMatcher(cv2.NORM_HAMMING,crossCheck=True)
    matches=bf.match(desc_a,desc_b)
    similar_regions=[i for i in matches if i.distance<50]
    if len(matches)==0:
        return 0
    return len(similar_regions)/len(matches)
a=orb_sim(cv2.imread("cablu.jpg"),cv2.imread("try.jpg"))
print(a)