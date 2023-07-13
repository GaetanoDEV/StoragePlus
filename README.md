
# StoragePlus

Un software Python per la Gestione Magazzino basilare per privati.


## Per Windows

- Scarica il pacchetto più aggiornato da [QUI](https://github.com/GaetanoDEV/StoragePlus/releases)
- Estrai il pacchetto in una directory comoda
- Avvia il file "FirstInstall.bat" per l'installazione dei componenti necessari.
- Esegui "StoragePlus - AVVIABILE.bat" oppure /etc/StoragePlus.py

## Per Linux

- Scarica il pacchetto più aggiornato da [QUI](https://github.com/GaetanoDEV/StoragePlus/releases)
- Estrai il pacchetto in una directory comoda
- A seconda della distribuzione Installa Python con:
```
 sudo apt install python 3 -y (Ubuntu / Debian)
```
```
> yum install -y python3 (RedHat / CentOS)
```
- Esegui il comando da terminale per l'installazione delle librerie:
```
> pip install mysql-connector-python
```

## Configurazione per Privati

Il software richiede la connessione ad un databse MySQL, locale o remoto, se si dispone di questo, la connessione da client a server viene gestita al file "StoragePlus.py" in /etc/

Esempio: 
* host="hostname",
* user="username",
* password="password",
* database="nomedatabase"

L'hostname può essere identificato come indirizzo IP o dominio, esempio:
* 127.0.0.1 o localhost // 95.46.xxx.xxx o sql.miosito.com
## Importa Database SQL
- Puoi scaricare il database SQL dalla pagina delle Release,[QUI](https://github.com/GaetanoDEV/StoragePlus/releases)
## Screenshots

![Main](https://i.imgur.com/xlukcn6.png)


![Main](https://i.imgur.com/eboDRzn.png)


![Main](https://i.imgur.com/GUm0INk.png)


![Main](https://i.imgur.com/pQhudup.png)
