from DefinitionOfAll.seq2seq import Seq2seq
from DefinitionOfAll.AttentionEncoder import AttentionEncoder
from DefinitionOfAll.AttentionDecoder import AttentionDecoder
from DefinitionOfAll.TimeSoftmaxWithLoss import TimeSoftmaxWithLoss

class AttentionSeq2seq(Seq2seq):
    def __init__(self, vocab_size, wordvec_size, hidden_size):
        args = vocab_size, wordvec_size, hidden_size
        self.encoder = AttentionEncoder(*args)
        self.decoder = AttentionDecoder(*args)
        self.softmax = TimeSoftmaxWithLoss()

        self.params = self.encoder.params + self.decoder.params
        self.grads = self.encoder.grads + self.decoder.grads