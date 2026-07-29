import RPG_Characters_Manager as manager

def test_ask_for_int_returns_whole_number(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda prompt: "5")

    result = manager.ask_for_int("Enter a number: ")

    assert result == 5

def test_ask_for_int_returns_none_for_invalid_input(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda prompt: "abc")

    result = manager.ask_for_int("Enter a number: ")
    captured = capsys.readouterr()

    assert result is None
    assert "Values must be in whole numbers." in captured.out

def test_view_characters_with_empty_list(capsys):
    manager.view_characters([])

    captured = capsys.readouterr()

    assert "You have no saved characters." in captured.out

def test_view_characters_displays_character(capsys):
    characters = [
        {
            "name": "Monty",
            "level": 5,
            "health": 80,
            "max_health": 100,
        }
    ]

    manager.view_characters(characters)

    captured = capsys.readouterr()

    assert "1. Monty" in captured.out
    assert "Level: 5" in captured.out
    assert "HP: 80/100" in captured.out
    assert "alive" in captured.out

