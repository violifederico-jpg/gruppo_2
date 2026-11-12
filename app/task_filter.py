from app.models.task import Task



# Questa è la mia descrizione al metodo in questione per la mia issue
def cerca_per_titolo(tasks: list[Task], testo: str) -> list[Task]:
    testo = testo.casefold()
    return [task for task in tasks if testo in task.titolo.casefold()]
