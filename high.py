import OpenImageIO as oiio
import glob

if __name__ == '__main__':

    for path in glob.glob('/for/bar/*.exr'):
        print(path)
        jpg_path = path.replace('.exr', '.jpg')

        #Read File
        buf = oiio.ImageBuf(path)

        #Write File
        buf.write(jpg_path)
