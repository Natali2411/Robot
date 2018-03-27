from cx_Freeze import setup, Executable

setup(
    name = "21",
    version = "0.1",
    description = "Blackjack",
    executables = [Executable("21.py")]
)