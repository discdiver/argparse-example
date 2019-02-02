# videos.py
import argparse
parser = argparse.ArgumentParser(description='Videos to images')
parser.add_argument('indir', type=int, help='Input dir for videos', default=2)
parser.add_argument('outdir', type=int, help='Output dir for image', default=3)
args = parser.parse_args()

print(args.indir)
