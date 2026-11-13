from app.models.task import Task


def filtra_per_stato(tasks: list[Task], completato: bool) -> list[Task]:
    return [task for task in tasks if task.completato == completato]

# Questa è la mia descrizione al metodo in questione per la mia issue
def cerca_per_titolo(tasks: list[Task], testo: str) -> list[Task]:
    testo = testo.casefold()
    return [task for task in tasks if testo in task.titolo.casefold()]

# Questa è la mia descrizione al metodo in questione per la mia issue
def cerca_per_titolo(tasks: list[Task], testo: str) -> list[Task]:
    testo = testo.casefold()
    return [task for task in tasks if testo in task.titolo.casefold()]