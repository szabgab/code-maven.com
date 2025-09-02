# Add the application source code


Switch to the user:

```
su - dev
```

By cloning:

```
git clone https://github.com/szabgab/python-flask-demo.git
cd python-flask-demo
virtualenv venv
```

By upload using scp, run the command on your desktop:

```
scp -r . root@IP:
```

This is just an example, you need to zip the files on your computer, scp the zip file and unzip in user dev.


## Install the Python dependencies

```
source venv/bin/activate
pip install -r requirements.txt
```

## Try the development flask server

```
flask run --port 5000 --host 0.0.0.0
```

Access `http://IP:5000/`
