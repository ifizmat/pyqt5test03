Python Virtual Environments

cd test_nev
python -m venv project_env
project_env\Scripts\activate.bat
(project_env) ..\test_env\project_env\Scripts>
where python
pip list
pip install requests
pip install pyqt5
pip install pyinstaller

project_env\Scripts\deactivate.bat

ui2py.cmd
.\project_env\Scripts\pyuic5.exe -x mainwindow.ui -o mainwindow.py

py2exe.cmd
.\project_env\Scripts\pyinstaller --onefile --windowed pyqt5test2.py --noconsole --name test1 --noconfirm

=====
Links:

https://www.pythontutorial.net/python-basics/python-virtual-environments/
https://www.pythontutorial.net/pyqt/pyqt-to-exe/


https://www.pythonguis.com/installation/install-qt-designer-standalone/
pip install pyqt5-tools
pyqt5-tools designer
