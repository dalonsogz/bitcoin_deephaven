@echo off

set JAVA_HOME="C:\Program Files\Java\jdk11"
set PATH=C:\Program Files\Java\jdk11\bin;%PATH%
explorer http://localhost:10000/ide/
venv\Scripts\python -m deephaven_example_app

rem Clean temp files
rm -rf "C:\Users\dalonso\AppData\Local\Deephaven Data Labs"
rm -rf "C:\Users\dalonso\AppData\Roaming\Deephaven Data Labs"

pause
