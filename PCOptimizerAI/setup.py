# setup.py
from cx_Freeze import setup, Executable

executables = [Executable("PCOptimizerAI.py")]

setup(
    name="PCOptimizerAI",
    version="1.0",
    description="Descrizione della tua applicazione",
    executables=executables
)
   
