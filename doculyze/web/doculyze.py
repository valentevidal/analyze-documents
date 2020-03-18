

import sys, os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "doculyze.settings")
django.setup()

from collections import Counter

from doculyze.settings import *
import nltk.data






doc_root = os.path.join(MEDIA_ROOT, 'documents')
class Doculyze():
    


    def __init__(self, text_list):
        self.text_list = text_list



    def read_file(self, txt_file):
        file_dir = os.path.join(doc_root, txt_file)
        file_text = open(file_dir, "r", encoding="utf8").read()
        return file_text


    def all_text(self):
        all_text = {}
        for f in self.text_list:
            all_text[f] = {}
            all_text[f]['text'] = self.read_file(f)
        return all_text

    def most_common(self):
        all_text = self.all_text()
        stopwords = set(line.strip() for line in open(STOP_WORDS_DIR, 'r', encoding="utf8",))
        cstopwords = [word.capitalize() for word in stopwords]
        all_stopwords = cstopwords + list(stopwords)

        for txt_f, info in all_text.items():
            #print (all_text)
            new_words = [word for word in info['text'].strip().split() if word not in all_stopwords]
            counter = Counter(new_words)
            info['10_most_common'] = counter.most_common(10)
        return all_text

    def sentences(self, text):
        tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        return list(tokenizer.tokenize(text))


    def join_most_common(self):
        all_data = self.most_common()
        all_data['total_most_common'] = []
        for key in all_data:
            if key != 'total_most_common':
                print (all_data[key]['10_most_common'])
                all_data['total_most_common'] += all_data[key]['10_most_common'] 

        #all_data['total_most_common'] = (all_data['total_most_common'])[:10]    
        all_data['total_most_common'] = sorted(all_data['total_most_common'], key=lambda tup: tup[1], reverse=True)[:10]
        print (all_data['total_most_common'])
        return all_data

 

    def most_common_sentences(self):
        all_data = self.join_most_common()

        for key, info in all_data.items():


            if key != 'total_most_common':
                info['sentences'] = []
                for word in all_data['total_most_common']:
                
                    
                    for sentence in self.sentences(info['text']):
        
                        if word[0] in sentence.split():
                            word_in_bold = "<strong>{}</strong>".format(word[0])
                            sentence = sentence.replace(word[0], word_in_bold )
                            sentence += "<i> - in document {} </i>".format(key)
                            info['sentences'].append(sentence)
        return all_data

    def add_txt_files(self):
        all_data = self.most_common_sentences()
        all_data["files"] = []
        for key in all_data:
            if key != 'total_most_common' and key != "files":
                all_data["files"].append(key)
        return all_data
        
    def get_data(self):
        data = self.add_txt_files()
        return data
"""
all_data {"doc1": { {'text': "all the text unformated",
                '10_most_common': [("word", 5), ("word2", 4)]
                'sentences': []    

                },
      "files": ["doc1", "doc2"]
      "total_most_common": [("word", 7), ("word2", 6)]


}
"""