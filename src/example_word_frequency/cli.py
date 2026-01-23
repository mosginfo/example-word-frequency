from collections import defaultdict
import fileinput
import importlib.resources
import string
import sys

from rich.console import Console


console = Console(stderr=True)


def main() -> int:
    # __package__ is None если модуль исполняемый!!!
    package_resources = importlib.resources.files(f'{__package__}.resources')

    with importlib.resources.as_file(package_resources / 'config.ini') as p:
        console.print(f'[green bold]Loaded config: {p.absolute()}[/green bold]')

    word_frequency_map: dict[str, int] = defaultdict(int)
    total_words = 0

    with fileinput.input(files=sys.argv[1:]) as f:
        for line in f:
            words = [word.strip(string.punctuation) for word in line.lower().split()]

            for word in filter(bool, words):
                word_frequency_map[word] += 1
                total_words += 1

    console.print(
        f'[green bold]Total words: {total_words}, Unique words: {len(word_frequency_map)}[/green bold]'
    )

    for word, count in word_frequency_map.items():
        print(f'{count} {word}')

    return 0
