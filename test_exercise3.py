#!/usr/bin/env python3

import pytest

from exercise3 import decide_rps


def test_checksum():
    """
    Inputs that are the correct format and length
    """
    rock-0, paper 1 scissors 2
    # check that expected input behaves correctly
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Rock", "Paper") == 1
    assert decide_rps("Rock", "Scissors") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Scissors") == 0
    assert decide_rps("Paper", "Paper") == 1
    assert decide_rps("Paper", "Rock") == 2
    # check that correct exception is thrown for bad value
    with pytest.raises(ValueError):
        decide_rps("Rock", "Banana") == 1

    # check that correct exception is thrown for bad type
    with pytest.raises(TypeError):
        decide_rps("Rock", 2) == 1
    # other tests

test_checksum()