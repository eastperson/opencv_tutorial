import cv2
import numpy as np
from skimage import io

img = io.imread('https://lh6.googleusercontent.com/proxy/ex49GHIGlsSiyCFNyXjgGTrz99fZiN9OcREXpEv3jfUg-Bw6LBAFtEAjkPbtY_Sjobz_sX24bwj-FteD-BxYbNjmCvmrICivdxE0PCkxTTU3unQdikw4LchqDvOADipt3xe25eU5aPxDMWEaPW3kcE00QQ=s0-d')[:, :, :-1]


average = img.mean(axis=0).mean(axis=0)

pixels = np.float32(img.reshape(-1, 3))

n_colors = 5
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 200, .1)
flags = cv2.KMEANS_RANDOM_CENTERS

_, labels, palette = cv2.kmeans(pixels, n_colors, None, criteria, 10, flags)
_, counts = np.unique(labels, return_counts=True)

dominant = palette[np.argmax(counts)]

import matplotlib.pyplot as plt

avg_patch = np.ones(shape=img.shape, dtype=np.uint8) * np.uint8(average)

indices = np.argsort(counts)[::-1]
freqs = np.cumsum(np.hstack([[0], counts[indices] / counts.sum()]))
rows = np.int_(img.shape[0] * freqs)

dom_patch = np.zeros(shape=img.shape, dtype=np.uint8)
for i in range(len(rows) - 1):
    dom_patch[rows[i]:rows[i + 1], :, :] += np.uint8(palette[indices[i]])

fig, (ax0, ax1) = plt.subplots(1, 2, figsize=(12, 6))
ax0.imshow(avg_patch)
ax0.set_title('Average color')
ax0.axis('off')
ax1.imshow(dom_patch)
ax1.set_title('Dominant colors')
ax1.axis('off')
plt.show()