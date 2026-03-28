import sys
import os
from pathlib import Path
from unittest.mock import patch
from datetime import datetime, date

# Add src to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))

from acolito_manager.utils import detect_weekday, names_list_to_text, is_currently_suspended
from acolito_manager.models import Acolyte, Suspension

def test_detect_weekday_full_date():
    assert detect_weekday("23/10/2023") == "Segunda-feira"
    assert detect_weekday("24/10/2023") == "Terça-feira"
    assert detect_weekday("25/10/2023") == "Quarta-feira"
    assert detect_weekday("26/10/2023") == "Quinta-feira"
    assert detect_weekday("27/10/2023") == "Sexta-feira"
    assert detect_weekday("28/10/2023") == "Sábado"
    assert detect_weekday("29/10/2023") == "Domingo"

def test_detect_weekday_with_spaces():
    assert detect_weekday(" 23/10/2023 ") == "Segunda-feira"

def test_detect_weekday_no_year():
    # Mock datetime.now() to return a fixed date, e.g., in 2024 (leap year)
    with patch("acolito_manager.utils.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 1, 1)
        mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
        # 01/01/2024 was a Monday (Segunda-feira)
        assert detect_weekday("01/01") == "Segunda-feira"
        # 29/02/2024 was a Thursday (Quinta-feira)
        assert detect_weekday("29/02") == "Quinta-feira"

    # Mock datetime.now() to return a date in 2023 (non-leap year)
    with patch("acolito_manager.utils.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2023, 1, 1)
        mock_datetime.side_effect = lambda *args, **kwargs: datetime(*args, **kwargs)
        # 01/01/2023 was a Sunday (Domingo)
        assert detect_weekday("01/01") == "Domingo"

def test_detect_weekday_invalid_dates():
    # Invalid day/month
    assert detect_weekday("32/01/2023") == ""
    assert detect_weekday("01/13/2023") == ""
    # Invalid Feb 29th
    assert detect_weekday("29/02/2023") == ""
    # Not enough parts
    assert detect_weekday("23/10") != "" # This should be valid as DD/MM
    assert detect_weekday("23") == ""
    # Non-numeric parts
    assert detect_weekday("abc/def/ghi") == ""
    assert detect_weekday("23/oct/2023") == ""

def test_detect_weekday_edge_cases():
    assert detect_weekday("") == ""
    assert detect_weekday("   ") == ""
    assert detect_weekday("/") == ""
    assert detect_weekday("//") == ""

def test_names_list_to_text():
    # Empty list
    assert names_list_to_text([]) == ""
    # One name
    assert names_list_to_text(["João"]) == "João"
    # Two names
    assert names_list_to_text(["João", "Maria"]) == "João e Maria"
    # Three names
    assert names_list_to_text(["João", "Maria", "José"]) == "João, Maria e José"

def test_is_currently_suspended():
    ac = Acolyte(name="Test")

    # No suspensions
    assert not is_currently_suspended(ac)

    # Inactive suspension
    s1 = Suspension(reason="R1", start_date="01/01/2020", end_date="31/12/2030", is_active=False)
    ac.suspensions.append(s1)
    assert not is_currently_suspended(ac)

    # Mock datetime to control "today"
    # We patch the datetime class in utils module because it's imported as 'from datetime import datetime'
    with patch("acolito_manager.utils.datetime") as mock_datetime:
        # Mocking now().date()
        mock_now = datetime(2023, 6, 1)
        mock_datetime.now.return_value = mock_now
        mock_datetime.strptime.side_effect = datetime.strptime

        # Active suspension, currently in range
        s2 = Suspension(reason="R2", start_date="01/01/2023", end_date="31/12/2023", is_active=True)
        ac.suspensions.append(s2)
        assert is_currently_suspended(ac)

        # Future suspension
        s2.start_date = "01/01/2024"
        s2.end_date = "31/12/2024"
        s2._parse_dates()
        assert not is_currently_suspended(ac)

        # Past suspension
        s2.start_date = "01/01/2022"
        s2.end_date = "31/12/2022"
        s2._parse_dates()
        assert not is_currently_suspended(ac)

        # Invalid start date should be skipped (not suspended)
        s3 = Suspension(reason="R3", start_date="invalid", is_active=True)
        ac.suspensions = [s3]
        assert not is_currently_suspended(ac)

        # Empty start date should be skipped
        s4 = Suspension(reason="R4", start_date="", is_active=True)
        ac.suspensions = [s4]
        assert not is_currently_suspended(ac)

        # Valid start date but invalid end date should be skipped
        s5 = Suspension(reason="R5", start_date="01/01/2023", end_date="invalid", is_active=True)
        ac.suspensions = [s5]
        assert not is_currently_suspended(ac)

if __name__ == "__main__":
    test_detect_weekday_full_date()
    test_detect_weekday_with_spaces()
    test_detect_weekday_no_year()
    test_detect_weekday_invalid_dates()
    test_detect_weekday_edge_cases()
    test_names_list_to_text()
    test_is_currently_suspended()
    print("All tests passed!")
