powershell rd -Force -Recurse .\dist\maixpy3_notebook\
pip install .\rpyc_ikernel\
pyinstaller maixpy3_notebook.spec -w --noconsole --clean --onefile --icon=app.ico
powershell rd -Force -Recurse .\dist\maixpy3_notebook\share
powershell copy -Force -Recurse .\dist\share .\dist\maixpy3_notebook
.\dist\maixpy3_notebook.lnk