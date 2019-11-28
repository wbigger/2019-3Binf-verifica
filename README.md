# 2019-3Binf School Library
Year-wide project for 3Binf, IIS G. Marconi, a.s. 2019/2020


# Come funziona
L'applicazione funziona con una semplice architettura client-server/

## Server: Python
Il codice lato server è scritto in Python e servito con Flask. Per eseguire l'applicazione, aprire il progetto su Visual Studio Code, aprire il terminale e scrivere:

```
python3 -m flask run
```

## Client: HTML5
La pagina lato client è tutta contenuta in index.html.

Per servirla, potete usare l'estensione "Live Server" su Visual Studio Code, e premere "Go Live" in basso a sinistra.

Attenzione: in questo modo avremo due web server per servire la stessa pagina, cosa che generalmente non è ritenuta sicura da molti browser (espone a possibili attacchi). Quindi evitare problemi, potete eseguire Chrome in modalità non sicura. Per fare questo, sempre da Visual Studio Code (solo per **Windows**):
- aprire le impostazioni, premendo la rotella in basso a sinistra e scegliendo "Settings" (o Impostazioni)
- scegliere la tab "Workspace" (di default è selezionato "User")
- nella barra di ricerca scrivere `liveserver.AdvanceCustomBrowserCmdLine`
- deve comparire la voce `Live Server › Settings: Advance Custom Browser Cmd Line`, premere in basso su `Edit in settings.json`
- subito dopo la prima parentesi graffa, incollare la riga
```
"liveServer.settings.AdvanceCustomBrowserCmdLine": "chrome.exe --disable-web-security --disable-gpu --user-data-dir=~/chromeTemp",
```
