from credit import calculate_risk


# Partie A - Cas normaux
def test_high_risk():
    result = calculate_risk(1000, 700)
    assert result == "HIGH"


def test_medium_risk():
    result = calculate_risk(1000, 400)
    assert result == "MEDIUM"


def test_low_risk():
    result = calculate_risk(1000, 100)
    assert result == "LOW"


# Partie B - Cas limites
def test_zero_income():
    assert calculate_risk(0, 500) == -1


def test_negative_income():
    assert calculate_risk(-1000, 500) == -1


def test_zero_debt():
    assert calculate_risk(1000, 0) == "LOW"


def test_ratio_equal_0_3():
    assert calculate_risk(1000, 300) == "LOW"


def test_ratio_equal_0_6():
    assert calculate_risk(1000, 600) == "MEDIUM"
