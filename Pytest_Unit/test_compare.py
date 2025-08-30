def test_set_comparison():
    set1 = set(
        ['Apples', 'Bananas', 'Watermelon', 'Pear']
    )
    set2 = set(
        ['Apples', 'Grapes', 'Watermelon', 'melon']
    )

    assert set1 == set2