# import the necessary packages
from textblob import TextBlob
import pytesseract
import argparse
import cv2
import pycountry

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True,
	help="path to input image to be OCR'd")
ap.add_argument("-fl", "--from_lang", type=str, default="ja",
	help="language to translate OCR'd text to (default is Japanese)")
ap.add_argument("-tl", "--to_lang", type=str, default="en",
	help="language to translate OCR'd text to (default is English)")
args = vars(ap.parse_args())

# load the input image and convert it from BGR to RGB channel
# ordering
image = cv2.imread(args["image"])
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image, then replace newline characters
# with a single space
iso_1_lang = pycountry.languages.get(alpha_2=args["from_lang"])
text = pytesseract.image_to_string(rgb, config=f"-l {iso_1_lang.alpha_3}")
text = text.replace("\n", " ")

# show the original OCR'd text
print("ORIGINAL")
print("========")
print(text)
print("")

# translate the text to a different language
tb = TextBlob(text)
translated = tb.translate(from_lang=args["from_lang"], to=args["to_lang"])
# show the translated text
print("TRANSLATED")
print("==========")
print(translated)
