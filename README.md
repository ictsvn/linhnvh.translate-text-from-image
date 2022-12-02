#### Description:

```
Translating text from image
Work better in high quality
```

#### Requirements

```
python3.9 and above
```

#### Setup your environment:

```
python -m venv venv
source venv/bin/activate
```

#### Installation:

```
python -m pip install -r requirements.txt
python -m textblob.download_corpora
```

#### How to run:

```
put your image in the root folder

python img_trans.py --image your_image_name --from_lang from_language_code --to_lang to_language_code
```

#### example:

```
python img_trans.py --image example.png --from_lang ja --to_lang en

ORIGINAL
========
おはようございます。

TRANSLATED
==========
good morning.
```

#### note:

```
For language code use ISO 639-1 Code
```
