import random
import copy

class Choose:
    def __init__(self, **kwargs):
        self.dic = kwargs
        self.contents = []
        for k,v in self.dic.items():
            for x in range(v):
                self.contents.append(k)
        self.dup_contents = copy.copy(self.contents)

    def rand_choose(self, num_choices):
        if num_choices > len(self.contents):
            return "Error: num_choices greater than contents entered."
        self.choices = random.sample(self.contents, num_choices)
        for sc in self.choices:
            self.contents.remove(sc)
        if len(self.contents) == 0:
            for dc in self.dup_contents:
                self.contents.append(dc)
        return self.choices