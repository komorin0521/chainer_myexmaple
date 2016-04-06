#!/usr/bin/env python
#encoding:utf-8

import chainer
import chainer.functions as F
import chainer.links as L


class ImageClassifyModel(chainer.Chain):
    def __init__(self, n_in, n_units, n_out):
        super(ImageClassifyModel, self).__init__(
            l1=L.Linear(n_in, n_units),     #入力層 -> 隠れ層
            l2=L.Linear(n_units, n_units),  #隠れ層 -> 隠れ層
            l3=L.Linear(n_units, n_out)     #隠れ層 -> 出力層
        )

    def __call__(self, x):
        # 順伝播を行う関数
        h1 = F.relu(self.l1(x))
        h2 = F.relu(self.l2(h1))
        return self.l3(h2)

class ImageClassifyModelwithDropOut(chainer.Chain):
    def __init__(self, n_in, n_units, n_out):
        super(ImageClassifyModelwithDropOut, self).__init__(
            l1=L.Linear(n_in, n_units),     #入力層 -> 隠れ層
            l2=L.Linear(n_units, n_units),  #隠れ層 -> 隠れ層
            l3=L.Linear(n_units, n_out)     #隠れ層 -> 出力層
        )
        self.train = None

    def __call__(self, x):
        # 順伝播を行う関数
        h1 = F.dropout(F.relu(self.l1(x)),train=self.train, ratio=0.2)
        h2 = F.dropout(F.relu(self.l2(h1)),train=self.train, ratio=0.5)
        return self.l3(h2)
