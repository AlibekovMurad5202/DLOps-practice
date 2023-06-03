import numpy as np
import cv2

eps = 1e-4

ref_img = cv2.imread("../DLOps/reference_images/dog.jpg")
res_img = cv2.imread("../DLOps/result_images/dog.jpg")

# Computing the pixel-wise difference between the two images
diff = cv2.absdiff(ref_img, res_img)

# Computing image similarity
sim = np.sum(diff == 0) / diff.size
print("\tImage similarity: ", sim * 100, "%")

if (1 - sim) < eps:
    print("\tTest passed :)")
else:
    print("\tTest failed :(")