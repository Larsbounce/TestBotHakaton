from aiogram.dispatcher.filters.state import State, StatesGroup

class FSMath(StatesGroup):
    percent = State()
    mass = State()
    multiplicate = State()
    hour = State()
    barrel = State()
    abscis = State()
    planimetry = State()
    protractor = State()
    eratosthenes = State()
    theorem = State()

class FSSelf(StatesGroup):
    holidays = State()
    one_or_two = State()
    company = State()
    marry = State()
