import glob
import gzip
import json
import os


# TODO: the s3 file is of the form search_dataset.json.gz so this might come in handy: https://stackoverflow.com/questions/12902540/read-from-a-gzip-file-in-python
# TODO: the data is likely to be a zip file so lets use this: https://medium.com/dev-bits/ultimate-guide-for-working-with-i-o-streams-and-zip-archives-in-python-3-6f3cf96dca50
def reader(path, file_ending):
    file_names = (filename for filename in glob.glob(os.path.join(path, file_ending)) )
    for filename in file_names:
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            yield f

def get_files(path = os.getcwd() + "/data", file_ending="*.json", reader=reader):
    return reader(path, file_ending)


def gzip_reader(path=os.getcwd(), file_ending="ex1.json.gz"):
    file_path = os.path.join(path, file_ending)
    with gzip.open(file_path,'rb') as f:
        yield f


# this just loads the whole file from memory - bad (wont work for huge files)
# instead we should stream the data in
# if the file was json line deliminated this would be a bit easier
def get_docs_from_json_file(f: gzip.GzipFile):
    return json.loads(next(f).read())
