import sys
import array
import tkinter as tk

def calc_mandelbrot_vals(maxiters, xmin, xmax, ymin, ymax, imgwd, imght):
    escapevals = []
    xwd = xmax - xmin
    yht = ymax - ymin
    for y in range(0, imght):
        for x in range(0, imgwd):
            r = xmin + xwd * x / imgwd
            i = ymin + yht * y / imght
            z = complex(r, i)
            for n in range(maxiters + 1):
                z = complex(z*z+0.318, 0.5)
                if abs(z) > 1.5:
                    break
            escapevals.append(n)
    return escapevals

def escapeval_to_color(n, maxiters):
    v = float(n) / float(maxiters)
    n = int(v * 4096.0)

    r = g = b = 0
    if (n == maxiters):
        pass
    elif (n < 64):
        b = n * 2
    elif (n < 128):
        b = (((n - 64) * 128) / 126) + 128
    elif (n < 256):
        b = (((n - 128) * 62) / 127) + 193
    elif (n < 512):
        b = 255
        r = (((n - 256) * 62) / 255) + 1
    elif (n < 1024):
        b = 255
        r = (((n - 512) * 63) / 511) + 64
    elif (n < 2048):
        b = 255
        r = (((n - 1024) * 63) / 1023) + 128
    elif (n < 4096):
        b = 255
        r = (((n - 2048) * 63) / 2047) + 192

    return (int(r), int(g), int(b))

def mb_to_tkinter(maxiters, xmin, xmax, ymin, ymax, imgwd, imght):

    array = calc_mandelbrot_vals(maxiters, xmin, xmax, ymin, ymax, imgwd, imght)
    window = tk.Tk()
    canvas = tk.Canvas(window, width=imgwd, height=imght, bg="#000000")
    img = tk.PhotoImage(width=imgwd, height=imght)
    canvas.create_image((0, 0), image=img, state="normal", anchor=tk.NW)

    i = 0
    for y in range(imght):
        for x in range(imgwd):
            n = array[i]
            color = escapeval_to_color(n, maxiters)
            r = hex(color[0])[2:].zfill(2)
            g = hex(color[1])[2:].zfill(2)
            b = hex(color[2])[2:].zfill(2)
            img.put("#" + r + g + b, (x, y))
            i += 1

    canvas.pack()
    tk.mainloop()

if __name__ == "__main__":
    mb_to_tkinter(80, -1.5, 1.5, -1.5, 1.5, 400, 400)
