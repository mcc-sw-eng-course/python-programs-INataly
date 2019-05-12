#!/usr/bin/python
# -*- coding: utf-8 -*-

# Ejemplo cliente - servidor en python
# Programa Cliente
# www.elfreneticoinformatico.com

import socket  # utilidades de red y conexion

# declaramos las variables
from pip._vendor.distlib.compat import raw_input

class Tic_tac_Toe_Client:

    def __init__(self):
        ipServidor = "127.0.0.1"  # es lo mismo que "localhost" o "0.0.0.0"
        puertoServidor = 9797

        # Configuramos los datos para conectarnos con el servidor
        # socket.AF_INET para indicar que utilizaremos Ipv4
        # socket.SOCK_STREAM para utilizar TCP/IP (no udp)
        # Estos protocolos deben ser los mismos que en el servidor
        self.cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.cliente.connect((ipServidor, puertoServidor))
        print("Conectado con el servidor ---> %s:%s" % (ipServidor, puertoServidor))

    def sendMessage(self, player):
        respuesta = ""
        while True:
            msg = raw_input("> ")
            self.cliente.send(msg)
            respuesta = self.cliente.recv(4096)
            break

        print("------- CONEXIÓN CERRADA ---------")
        self.cliente.close()
        return respuesta