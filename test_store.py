from store import Task

def test_mark_done():
    task = Task(1, "Buy food", "Eggs, milk, cheese")
    task.mark_done()
    assert task.done is True

def test_starts_not_done():
    task = Task(1, "Buy food", "Eggs, milk, cheese")
    assert task.done is False

def test_delete():
    task = Task(1, "Buy food", "Eggs, milk, cheese")
    task.delete()
    assert task.deleted is True

def test_edit_description():
    task = Task(1, "Buy food", "Eggs, milk, cheese")
    task.edit_description("Blah")
    assert task.description == "Blah"