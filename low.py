import OpenImageIO as oiio
import glob

if __name__ == '__main__':

    for path in glob.glob('/foo/bar/*.exr'):
        print(path)
        jpg_path = path.replace('.exr', '.jpg')

        #Read File
        inp = oiio.ImageInput.open(path)
        spec = inp.spec()
        pixels = inp.read_image("float")
        inp.close()

        #Write File
        out = oiio.ImageOutput.create(jpg_path)
        out.open(jpg_path, spec)
        out.write_image(pixels)
        out.close()
