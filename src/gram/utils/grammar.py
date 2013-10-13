import yaml

from itertools import chain

from gram.exceptions import UserSideError


def get_grammar_tree(filename):
    with open(filename) as f:
        grammar = yaml.load(f)

    names = set(chain.from_iterable(grammar['grammar'].values()))
    for name in names:
        try:
            grammar[name] = {str(k): v for k, v in grammar[name].items()}
        except yaml.YAMLError as e:
            raise UserSideError('Error loading grammar file, %s' % e)

    return grammar
