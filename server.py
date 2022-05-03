import clase
import Pyro4

Bolsa=clase.Bolsa()

Pyro4.Daemon.serveSimple({
    Bolsa: 'bolsa',
}, host="localhost", port=9090, ns=False, verbose=True)

