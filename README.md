﻿# XPlorer
**XPlorer** je vyhledávací aplikace imitující vzhled původních Windows XP. Vychází ze stylesheetu [XP.css](https://botoxparty.github.io/XP.css/). Po zadání vyhledávacího dotazu prohledá soubory v předem definované složce (defaultně `\zvířátka` - lze změnit v `app.py`). Backend aplikace běží na frameworku Flask.

## Jak spustit (Docker)

```bash
git clone https://github.com/afffectionate/xplorer.git
cd xplorer
docker build -t xplorer .
docker run -p 5000:5000 xplorer
```

Aplikace poběží na [http://localhost:5000/home](http://localhost:5000/home).

## Jak spustit bez Dockeru

```bash
pip install -r requirements.txt
python app.py
```
