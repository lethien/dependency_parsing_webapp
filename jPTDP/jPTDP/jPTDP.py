# coding=utf-8
from __future__ import absolute_import, division, print_function, unicode_literals
from builtins import str
from io import open

from optparse import OptionParser
import pickle
import os, os.path, time
from . import utils, learner

class jPTDP_model():
    def __init__(self):
        modelparams_dir = os.path.join(os.path.dirname(__file__), 'model/model.params')
        words, w2i, c2i, pos, rels, stored_opt = pickle.load(open(modelparams_dir, 'rb'))
        
        print('Loading pre-trained model')
        parser = learner.jPosDepLearner(words, pos, rels, w2i, c2i, stored_opt)
        model_dir = os.path.join(os.path.dirname(__file__), 'model/model')
        parser.Load(model_dir)
        
        self.parser = parser

    def annotate(self, sentences):
        print('Predicting POS tags and parsing dependencies')
        
        results = []

        for anno_sentence in self.parser.Tag(sentences):            
            results.append(anno_sentence[1:])   

        for res_i in range(len(results[1:])):
            results[res_i+1] = results[res_i+1][len(results[res_i]):]

        return results