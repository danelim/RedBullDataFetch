import os
from subprocess import Popen as popen

def splitVideo(avFile, interval=200 ,saveDir=os.getcwd() + '/screens'):
    # interval is in milliseconds - convert to fps
    fps = '%f' % (10**3 / interval)

    # check if save directory exists. create it if not
    if not os.path.exists(saveDir):
        os.makedirs(saveDir)

    # generate screencaptures
    popen('ffmpeg -i ' + './' +  avFile + ' -vf fps=' + fps
        + ' ' + saveDir + '/img%05d.bmp') 

    return

if __name__ == '__main__':
    import sys

    videoPath = sys.argv[1]

    print('Generating frames ...')
    splitVideo(videoPath)
    print('Done ...')