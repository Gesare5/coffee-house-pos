from pos_app.main import prelim_list


def test_prelim_list():
    assert prelim_list() == [
        "A: Order Coffee",
        "B: Manage Coffee Items",
        "C: Exit",
    ]
