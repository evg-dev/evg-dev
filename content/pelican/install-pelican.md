Title: Python Pelican Tutorial
Date: 2020-10-25 12:00
Category: Pelican
Slug: install-pelican

python3 install from pip3

```bash
pip3 install pelican markdown
```

Quick initial project

```bash
pelican-quickstart
```

Set on pelicanconf.py for local developing

```python
RELATIVE_URLS = True
```

Run develop server

```bash
make devserver
```

```bash
pelican --list
```



Build with options

```bash
pelican -s pelicanconf.py -o output -D
```

Download templates

```bash
git clone --recursive https://github.com/getpelican/pelicanthemes.git
```

Select theme, copy to ```/theme/``` on root project and set you THEME on pelicanconf.py for customisation  

```python
THEME = '/theme/{{your_theme}}/'
```


