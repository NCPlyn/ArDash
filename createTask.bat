schtasks /Create /TR "python.exe '%~dp0ArDash.py'" /TN ArDash /SC ONLOGON /RL HIGHEST
