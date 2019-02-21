
import numpy as np
from numba import jit
from PIL import Image

@jit
def mandelbrot_test(c, max_iter=100, colors=None):
    z = 0
    for i in range(max_iter):
        if abs(z) > 2:
            return i
        z = z*z + c
        
    return 0

@jit
def mandelbrot(y0, y1, x0, x1, height, width, max_iter):
    cols = np.linspace(y0, y1, height)
    rows = np.linspace(x0, x1, width)
    output = np.empty((height, width))
    for i in range(height):
        for j in range(width):
            output[i,j] = mandelbrot_test(rows[j] + 1j*cols[i], max_iter=max_iter)
    return output

def mandelbrot_at(y, x, radius, side, max_iter):
    return mandelbrot(y-radius, y+radius, x-radius, x+radius, side, side, max_iter)

if __name__ == "__main__":
    height = 800
    width = 800
    #img = np.array(mandelbrot(-1, 1, -1.5, .5, height, width, 100)[2]).astype(np.uint8)
    
    img = np.array(mandelbrot_at(0, -.75, 0.25, 800, 100)).astype(np.uint8)
    colors = np.array([np.arange(0, 256, 2)[:100],
                       [0]*100,
                       np.arange(256, 0, -2)[:100]]).T

    im = Image.fromarray(colors[img].astype(np.uint8))

    
    im.save("foo.png", "PNG")
