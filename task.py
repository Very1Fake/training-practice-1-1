import os
import string
import sys
from dataclasses import dataclass


@dataclass
class Line:  # Class to validate line stats
    __slots__ = ['number', 'symbols']

    number: int
    symbols: int

    def __post_init__(self):
        if not isinstance(self.number, int):
            raise TypeError('number must be int')
        if not isinstance(self.symbols, int):
            raise TypeError('symbols must be int')

    def __str__(self) -> str:
        return f'Line {self.number}: {self.symbols} symbol(s)'


if __name__ == '__main__':
    russian_letters: int = 0
    english_letters: int = 0
    digits: int = 0
    lines: list[Line] = []

    if len(sys.argv) > 1 and sys.argv[1]:
        path = sys.argv[1]
    else:
        path = './TASK_1_Israpilov.txt'

    print('Analyzing')

    if os.path.isfile(path):
        with open(path) as f:
            for n, line in enumerate(f):
                python: bool = False
                for word in line.split(' '):
                    for letter in word:
                        if letter.lower() in 'йцукенгшщзхъфывапролджэячсмитьбюё':
                            russian_letters += 1
                        elif letter.lower() in string.ascii_lowercase:
                            english_letters += 1
                        elif letter in string.digits:
                            digits += 1

                    if not python:
                        if word.endswith('\n'):
                            word = word[:-1]
                        if word.startswith('"') or word.startswith("'"):
                            word = word[1:]
                        if word.endswith('"') or word.endswith("'"):
                            word = word[:-1]

                        if word.lower() == 'python':
                            lines.append(Line(n + 1, len(line[:-1]) - line.count(' ')))
                            python = True
    else:
        print(f'File on this path ("{path}") does not exist')
        exit(1)

    print('Finished')

    print(f'File stats:\n\tPath: {path}\n\tRussian letters count: {russian_letters}\n\t'
          f'English letters count: {english_letters}\n\tDigits count: {digits}\n\tLines (with "Python" word):')
    for i in lines:
        print(f'\t\t{i!s}')
