
import pytest

from python_2026.welcome2026.a import sort_scores


def test_sort_scores_empty_lists():
    """Test empty input lists return empty list."""
    assert sort_scores([], []) == []

def test_sort_scores_descending_order():
    """Test sorts by descending scores with matching questions."""
    questions = ["q1", "q2", "q3"]
    scores = [90.0, 80.0, 100.0]
    expected = [("q3", 100.0), ("q1", 90.0), ("q2", 80.0)]
    assert sort_scores(questions, scores) == expected

def test_sort_scores_with_duplicates():
    """Test handles duplicate scores correctly."""
    questions = ["easy", "hard", "medium"]
    scores = [85.5, 85.5, 90.0]
    expected = [("medium", 90.0), ("easy", 85.5), ("hard", 85.5)]
    assert sort_scores(questions, scores) == expected

def test_sort_scores_single_item():
    """Test single question/score pair returns unchanged."""
    assert sort_scores(["q1"], [95.0]) == [("q1", 95.0)]

def test_sort_scores_stable_with_tiebreak():
    """Test descending scores, alphabetical tiebreak on questions."""
    questions = ['Q1', 'Q2', 'Q3', 'Q4', 'A4', 'Z4']
    scores = [4.5, 2.3, 3.1, 2.0, 2.0, 2.0]
    expected = [('Q1', 4.5), ('Q3', 3.1), ('Q2', 2.3),
                ('A4', 2.0), ('Q4', 2.0), ('Z4', 2.0)]
    assert sort_scores(questions, scores) == expected

def test_sort_scores_ties_only():
    """Test alphabetical sort when all scores equal."""
    questions = ['banana', 'apple', 'cherry']
    scores = [1.0, 1.0, 1.0]
    expected = [('apple', 1.0), ('banana', 1.0), ('cherry', 1.0)]
    assert sort_scores(questions, scores) == expected