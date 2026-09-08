# -*- coding: utf-8 -*-
"""Kleine lokale server om de demo te bekijken.

Waarom niet gewoon `python -m http.server`: die kapt op Windows regelmatig
bestanden af op precies 65280 bytes (0xFF00). Dat komt doordat de socket
niet alles in een keer kwijt kan en het resultaat van send() genegeerd
wordt. Foto's boven de 64 kilobyte komen dan half binnen, en je ziet een
kapot beeld dat niets met de site te maken heeft.

Hier wordt het bestand in blokken van 32 kilobyte verstuurd met sendall(),
dat wel wacht tot alles weg is. Verder is het dezelfde server.

Draaien vanuit de projectmap:  python bouwscript/server.py
Daarna:                        http://localhost:8080/varianten.html
"""
import os
import sys
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer

BLOK = 32 * 1024
POORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
WORTEL = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")


class Handler(SimpleHTTPRequestHandler):
    def copyfile(self, bron, uit):
        """In blokken versturen en wachten tot elk blok echt weg is."""
        while True:
            blok = bron.read(BLOK)
            if not blok:
                break
            try:
                self.connection.sendall(blok)
            except (BrokenPipeError, ConnectionResetError):
                # Browser heeft de verbinding dichtgegooid, bijvoorbeeld
                # omdat je doorklikte. Niets aan de hand.
                return

    def end_headers(self):
        # Tijdens het bouwen wil je geen oude stylesheet uit de cache zien.
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, formaat, *args):
        if "200" not in (args[1] if len(args) > 1 else ""):
            super().log_message(formaat, *args)


if __name__ == "__main__":
    os.chdir(WORTEL)
    server = ThreadingHTTPServer(("127.0.0.1", POORT), partial(Handler))
    print("Draait op http://localhost:%d/" % POORT)
    print("Stoppen met Ctrl+C")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nGestopt.")
