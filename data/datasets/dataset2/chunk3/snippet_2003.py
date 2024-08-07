#Source: https://stackoverflow.com/questions/67366751/typeerror-init-missing-2-required-positional-arguments
import os
from tqdm import tqdm

from utils import SOS, EOS, UNK, process


class Corpus(object):
    def __init__(self, path, path2, path3, order, lower=False, max_lines=-1):
        self.order = order
        self.lower = lower
        self.max_lines = max_lines
        self.vocab = set()
        self.train = self.tokenize(os.path.join(path), training_set=True)
        self.valid = self.tokenize(os.path.join(path2))
        self.test = self.tokenize(os.path.join(path3))

    def tokenize(self, path, training_set=False):
        """Tokenizes a text file."""
        #assert os.path.exists(path)
        with open(path, path2, path3) as fin:
            num_lines = sum(1 for _ in fin.readlines())
        with open(path, path2, path3, 'r', encoding="utf8") as f:
            words = []
            for i, line in enumerate(tqdm(f, total=num_lines)):
                if self.max_lines > 0 and i > self.max_lines:
                    break
                line = line.strip()
                if not line:
                    continue  # Skip empty lines.
                elif line.startswith('='):
                    continue  # Skip headers.
                else:
                    sentence = (self.order - 1) * [SOS] + \
                        [process(word, self.lower) for word in line.split()] + [EOS]
                    if training_set:
                        words.extend(sentence)
                        self.vocab.update(sentence)
                    else:
                        sentence = [word if word in self.vocab else UNK for word in sentence]
                        words.extend(sentence)
        return words


if __name__ == '__main__':
    path = 'C://Users//supre//Documents//Python Programme//kenlm//wikitext-2//wiki.train.tokens'
    path2 = 'C://Users//supre//Documents//Python Programme//kenlm//wikitext-2//wiki.valid.tokens'
    path3 = 'C://Users//supre//Documents//Python Programme//kenlm//wikitext-2//wiki.test.tokens'
    corpus = Corpus(path, order=3)
    print(len(corpus.test))
    print(corpus.test[:100])