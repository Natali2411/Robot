from cx_Freeze import setup, Executable

executables = [
    Executable("general.py"),
    Executable("conftest.py"),
    Executable("config.json")
]

setup(
    name = "Robot",
    version = "1.0",
    description = "Robot Project",
    executables = executables
)