def find_min_star_distance(s: str) -> int:
    """
    The input string contains only '.' and '*'.
    Finds the smallest number of '.' that separate two adjacent `*`'s. Returns 0
    if the string contains fewer than two '*'.
    """
    if s.count('*') < 2:
        return 0

    # *....*...**..
    # ...*....*....
    # ....*........

    answer = len(s)
    seen_star = False
    n_dots = 0
    for c in s:
        if c == '*':
            if not seen_star:
                seen_star = True
            else:
                answer = min(answer, n_dots)
            n_dots = 0
        else:
            n_dots += 1
    return answer

def test_no_stars():
    """Test with no stars in the string."""
    assert find_min_star_distance('......') == 0


def test_single_star():
    """Test with only one star."""
    assert find_min_star_distance('...*...') == 0


def test_adjacent_stars():
    """Test with stars directly adjacent (no dots between)."""
    assert find_min_star_distance('**') == 0
    assert find_min_star_distance('.*.*') == 1


def test_single_dot_between():
    """Test with one dot separating stars."""
    assert find_min_star_distance('*.*') == 1
    assert find_min_star_distance('..*..*.') == 2


def test_multiple_dots_uniform():
    """Test with uniform spacing between all stars."""
    assert find_min_star_distance('*...*...*') == 3


def test_minimum_among_varying_distances():
    """Test finding minimum distance when distances vary."""
    assert find_min_star_distance('....*....*...*....*.') == 3
    assert find_min_star_distance('*.....*.*') == 1


def test_minimum_at_start():
    """Test when minimum distance is at the beginning."""
    assert find_min_star_distance('*.*.....*') == 1


def test_minimum_at_end():
    """Test when minimum distance is at the end."""
    assert find_min_star_distance('*.....*.*') == 1


def test_all_same_distances():
    """Test when all gaps between stars are equal."""
    assert find_min_star_distance('*.*.*.') == 1
    assert find_min_star_distance('*..*..*') == 2


if __name__ == '__main__':
    s = '....*....*...*....*'

    # jakieś dodatkowe przydatne zmienne
    best_solution = 10 ** 7
    n_stars = 0
    for c in s:
        print(f'--> {c}')
        # jakieś if-y
        if c == '*':
            print('gwiazdka!')
            n_stars += 1
        else:
            print('.')

    print(min(4, 7))  # --> 4
    print(f'{n_stars=}')
