from app import is_senior_eligible


def test_eligible_senior():
    assert is_senior_eligible(65) is True
    assert is_senior_eligible(60) is True
    assert is_senior_eligible(70, True) is True


def test_not_eligible_due_to_age():
    assert is_senior_eligible(59) is False
    assert is_senior_eligible(45, True) is False


def test_not_eligible_due_to_residency():
    assert is_senior_eligible(65, False) is False
