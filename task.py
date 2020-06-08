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

    if len(sys.argv) > 1 and sys.argv[1]:  # Check for first argument (path)
        path = sys.argv[1]
    else:
        path = './TASK_1_Israpilov.txt'  # Default path

    print('Analyzing')

    if os.path.isfile(path):  # Check for file existance
        with open(path) as f:
            for n, line in enumerate(f):  # Lines enumeration (to get line index)
                python: bool = False
                for word in line.split(' '):  # Split line to words
                    for letter in word:  # Split word to letters
                        if letter.lower() in 'йцукенгшщзхъфывапролджэячсмитьбюё':  # Check for russian letters
                            russian_letters += 1
                        elif letter.lower() in string.ascii_lowercase:  # Check for english letters
                            english_letters += 1
                        elif letter in string.digits:  # Check for digits
                            digits += 1

                    if not python:
                        if word.endswith('\n'):  # Cut new line symbol
                            word = word[:-1]
                        if word.startswith('"') or word.startswith("'"):  # Cut opening quote
                            word = word[1:]
                        if word.endswith('"') or word.endswith("'"):  # Cut closing quote
                            word = word[:-1]

                        if word.lower() == 'python':  # Check for python word
                            lines.append(Line(n + 1, len(line[:-1]) - line.count(' ')))  # Save line symbols count
                            python = True
    else:
        print(f'File on this path ("{path}") does not exist')
        exit(1)

    print('Finished')

    print(f'File stats:\n\tPath: {path}\n\tRussian letters count: {russian_letters}\n\t'
          f'English letters count: {english_letters}\n\tDigits count: {digits}\n\tLines (with "Python" word):')
    for i in lines:
        print(f'\t\t{i!s}')
