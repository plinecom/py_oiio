# Convert OpenEXR to JPEG using OpenImageIO(OIIO) in Python
# Self Introduction
I am Masataka @plinecom, a VFX pipeline engineer at digitalbigmo Inc.

# What is this?
I'm an OpenEXR pusher, but I often need help to preview OpenEXR easily, so I wanted to convert it per JPEG. But I already have tens of millions of JPEGs, which will increase in the future, so I want to process them in Python. I discovered that OpenImageIO is a convenient way to do this, so I used OpenCV. And since it handles image data in NumPy arrays, it will be helpful later. It needed to support DPX as well.

# Code (low-level API version)
```python:low.py
import OpenImageIO as oiio
import glob

if __name__ == '__main__':

    for path in glob.glob('/foo/bar/*.exr'):
        print(path)
        jpg_path = path.replace('.exr', '.jpg')

        #Read File
        ImageInput.open(path)
        spec = inp.spec()
        pixels = inp.read_image("float")
        inp.close()

        #Write File
        ImageOutput.create(jpg_path)
        out.open(jpg_path, spec)
        out.write_image(pixels)
        out.close()
```

# Code (high-level API version).
```python:high.py
import OpenImageIO as oiio
import glob

if __name__ == '__main__':

    for path in glob.glob('/foo/bar/*.exr'):
        print(path)
        jpg_path = path.replace('.exr', '.jpg')

        #Read File
        buf = oiio.ImageBuf(path)

        #Write File
        buf.write(jpg_path)
```

# Required Python external modules.
* OpenImageIO
* NumPy

I also prepared a Dockerfile.
```Dockerfile:Dockerfile
FROM rockylinux:8
RUN dnf install -y which python3 epel-release
RUN dnf config-manager --set-enabled powertools
RUN dnf install -y python3-openimageio python3-numpy
```
```terminal:terminal
docker pull plinecom/py_oiio
```

# Description of the low-level API version of the code
It is faster to use the low-level API if you are trying to get a NumPy array. (There is also a way to take a NumPy array from the high-level API.)

## Instructions on how to read EXR files.
```python:
        #Read File
        inp = oiio.ImageInput.open(path)
        spec = inp.spec()
        pixels = inp.read_image("float")
        inp.close()
```
The object pixels you can retrieve from the read_image() function is a NumPy array. Since this is OpeEXR, we instruct it to output the image data as a float type.

## Instructions for exporting and converting image data
```python:
        #Write File
        out = oiio.ImageOutput.create(jpg_path)
        out.open(jpg_path, spec)
        out.write_image(pixels)
        out.close()
```
Specify the destination and file name to write to. The image format is automatically processed based on the file extension, so if you change the extension, OpenImageIO will output to a supported format.
# Description of the high-level API version of the code
Nothing special. There is only one line for each read/write, and you should be able to figure it out if you see it.

# Advertising
digitalbigmo Inc. sells skin beauty plug-ins and does video VFX production work. If you are interested, please visit our web page. Let's work together.

https://digitalbigmo.com

# References
[OpenImageIO main house (English)](https://sites.google.com/site/openimageio/home)
[OpenImageIO Reference (English)](https://openimageio.readthedocs.io/en/latest/index.html)
