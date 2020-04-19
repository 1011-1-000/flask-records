import pandas as pd
from collections import OrderedDict
from records import Record, RecordCollection

def as_dict(self, converters=None, ordered=False):
    record_dict = OrderedDict() if ordered else dict()

    for key, value in zip(self.keys(), self.values()):
        if converters and key in converters:
            record_dict[key] = converters[key](value)
        else:
            record_dict[key] = value

    return record_dict

def as_df(self):
    return pd.DataFrame(self.as_dict())

Record.as_dict = as_dict
RecordCollection.as_df = as_df