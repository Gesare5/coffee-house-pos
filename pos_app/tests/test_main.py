from main import prelim_list, manage_coffee_items_list


def test_prelim_list():
    assert prelim_list() == [
        "A: Order Coffee",
        "B: Manage Coffee Items",
        "C: Exit",
    ]


def test_manage_coffee_items_list():
    assert manage_coffee_items_list() == [
        ["1", "Add Coffee Item"],
        ["2", "Delete Coffee Item"],
        ["3", "View Coffee Items"],
    ]
