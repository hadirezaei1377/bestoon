# Bestoon

                                        A simple Income and Expense system


source ------>  https://github.com/jadijadi❤️❤️❤️








## How to run

To run Bestoon in development mode; Just use steps below:

1. Install `python2`, `pip`, `virtualenv` in your system.
2. Clone the project `https://github.com/jadijadi/bestoon`.
3. Make development environment ready using commands below;

  ```bash
  git clone https://github.com/jadijadi/bestoon && cd bestoon
  virtualenv -p python2 build  # Create virtualenv named build
  source build/bin/activate
  pip install -r requirements.txt
  mv  bestoon/settings.py.sample bestoon/settings.py
  python manage.py migrate  # Create database tables
  ```

4. Run `Bestoon` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your Bestoon version.

## Run On Windows

If You're On A Windows Machine , Make Environment Ready By Following Steps Below:
1. Install `python2`, `pip`, `virtualenv` 
2. Clone the project using:  `git clone https://github.com/jadijadi/bestoon`.
3. Make Environment Ready Like This:
``` Command Prompt
cd bestoon
virtualenv -p "PATH\TO\Python.exe" build # Give Full Path To python.exe
build\Scripts\activate # Activate The Virutal Environment
pip install -r requirements.txt
move bestoon\settings.py.sample bestoon/settings.py
python manage.py migrate # Create Database Tables
```
4. Run `Bestoon` using `python manage.py runserver`
5. Go to [http://localhost:8000](http://localhost:8000) to see your Bestoon version.

## Run tests

To run tests in Bestoon simply use `python manage.py test`.

If you want more verbosity you can use `-v` option with `0, 1, 2, or 3.`; e.g. `python manage.py test -v2`

