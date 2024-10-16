Some informations useful

Testing with curl our flask API

Required: opening the flask API this way:

after chmod u+x *.py

```bash
./task_04_flask.py &
```

Here is an example the important point is to add `&` to be able to use the terminal while having the server open.

then doing your curl

```bash
curl http://localhost:5000
```

Then, when finish, CTRL+C doesn't kill the process and so, doesn't close the server. To do so you have to kill yourself the PID of the server. And so, to find the PID you just have to run:

```bash
ps aux | grep python
```

While doing so you will see all the current running process. Find the right one, see the PID and use it in the kill process.

Example:

```bash
arc@Chaggie:~/git/holbertonschool-higher_level_programming/restful-api$ ps aux | grep python
arc        132  0.0  0.0   4824  3524 pts/0    S+   09:23   0:00 /home/arc/.vscode-server/extensions/ms-python.python-2024.16.1-linux-x64/python-env-tools/bin/pet server
arc        274  0.0  0.2 196956 44380 pts/0    Sl+  09:23   0:01 /bin/python3 /home/arc/.vscode-server/extensions/ms-python.autopep8-2024.0.0/bundled/tool/lsp_server.py
arc        283  0.5  2.5 12965428 420108 pts/0 Sl+  09:23   0:41 /home/arc/.vscode-server/bin/384ff7382de624fb94dbaf6da11977bba1ecd427/node /home/arc/.vscode-server/extensions/ms-python.vscode-pylance-2024.10.1/dist/server.bundle.js --cancellationReceive=file:c30e1ac93349a3d6b58a614239c657edc5c63de4e9 --node-ipc --clientProcessId=115
arc      10372  0.0  0.1 181856 30884 pts/3    S    11:06   0:00 /usr/bin/python3 ./task_05_basic_security.py
arc      12502  0.0  0.0   4024  2020 pts/3    R+   11:24   0:00 grep --color=auto python
```

Here the server I wanted to kill is in the task_05

so the PID is "10372"

And so:

```bash
kill 10372
```

And here is the result of that command:

```bash
[1]+  Terminated              ./task_05_basic_security.py
```