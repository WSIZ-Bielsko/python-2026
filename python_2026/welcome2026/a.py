from dataclasses import dataclass


@dataclass
class ScoreItem:
    question: str
    score: float


def sort_scores(questions: list[str], scores: list[float]) -> list[tuple[str, float]]:
    """
    Posortować pytania/wyniki od pytań z najlepszym (najwyższym) score do pytań z najniższym.

    Wersja trudniejsza: zapewnić, że dla tego samego score, pytania będą się pojawiały w kolejności alfabetycznej.

    :param questions:
    :param scores:
    :return:
    """
    data = [ScoreItem(q, s) for q, s in zip(questions, scores)]
    data.sort(key=lambda x: (-x.score, x.question))
    return [(d.question, d.score) for d in data]


if __name__ == '__main__':
    questions = ['Q1', 'Q2', 'Q3', 'Q4', 'A4', 'Z4']
    scores = [4.5, 2.3, 3.1, 2.0, 2.0, 2.0]

    scores.sort()
    print(scores)

    # ff = sorted(scores)
    #
    # gg = [(2, 3), (4, 2), (4, 3)]
    # # print(sorted(gg, key=lambda x: x[0]))
    # print(sorted(gg, key=lambda x: (x[0], -x[1])))
    #
    # # zz = [(g[1], g[0]) for g in gg]
    #
    # # print(sorted(gg))
    # # print(sorted(zz))

    # -----------
