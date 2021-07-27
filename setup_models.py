import gdown
import phonlp
import os

def ensure_dir(d):
    if not os.path.exists(d):
        os.makedirs(d)

# Download the pre-trained PhoNLP model 
# and save it in a local machine folder
phonlp_dir = 'webapp/dependency_api/pretrained_phonlp/'
ensure_dir(phonlp_dir)
if not os.path.exists(phonlp_dir + "phonlp.pt"):
    phonlp.download(save_dir=phonlp_dir)

# Download the pre-trained VNCoreNLP model 
# and save it in a local machine folder
vncorenlp_dir = 'webapp/dependency_api/vncorenlp/'
ensure_dir(vncorenlp_dir)
if not os.path.exists(vncorenlp_dir+'VnCoreNLP-1.1.1.jar'):
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/VnCoreNLP-1.1.1.jar', vncorenlp_dir+'VnCoreNLP-1.1.1.jar')

vncorenlp_wordseg_dir = vncorenlp_dir + 'models/wordsegmenter/'
ensure_dir(vncorenlp_wordseg_dir)
if not os.path.exists(vncorenlp_wordseg_dir+'vi-vocab'):
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/wordsegmenter/vi-vocab', vncorenlp_wordseg_dir+'vi-vocab')
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/wordsegmenter/wordsegmenter.rdr', vncorenlp_wordseg_dir+'wordsegmenter.rdr')

vncorenlp_dep_dir = vncorenlp_dir + 'models/dep/'
ensure_dir(vncorenlp_dep_dir)
if not os.path.exists(vncorenlp_dep_dir+'vi-dep.xz'):
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/dep/vi-dep.xz', vncorenlp_dep_dir+'vi-dep.xz')

vncorenlp_ner_dir = vncorenlp_dir + 'models/ner/'
ensure_dir(vncorenlp_ner_dir)
if not os.path.exists(vncorenlp_ner_dir+'vi-ner.xz'):
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/ner/vi-500brownclusters.xz', vncorenlp_ner_dir+'vi-500brownclusters.xz')
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/ner/vi-ner.xz', vncorenlp_ner_dir+'vi-ner.xz')
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/ner/vi-pretrainedembeddings.xz', vncorenlp_ner_dir+'vi-pretrainedembeddings.xz')

vncorenlp_postagger_dir = vncorenlp_dir + 'models/postagger/'
ensure_dir(vncorenlp_postagger_dir)
if not os.path.exists(vncorenlp_postagger_dir+'vi-tagger'):
    gdown.download('https://raw.githubusercontent.com/vncorenlp/VnCoreNLP/master/models/postagger/vi-tagger', vncorenlp_postagger_dir+'vi-tagger')

# Download the pre-trained jPTDP model 
# and save it in a local machine folder
jptdp_dir = 'jPTDP/jPTDP/model/'
ensure_dir(jptdp_dir)
if not os.path.exists(jptdp_dir+'model'):
    gdown.download('https://drive.google.com/file/d/1Ki1qq7YTmTFA8hb313lJrM1cbUYN_ou0/view?usp=sharing', jptdp_dir+'model')
if not os.path.exists(jptdp_dir+'model.params'):
    gdown.download('https://drive.google.com/file/d/1U8rNI4CGH_UHjVpzBmSwgrHikjS4thRV/view?usp=sharing', jptdp_dir+'model.params')
    