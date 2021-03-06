#!/usr/bin/env python
# -*- coding: utf-8 -*
import os

class Main(object):

    def main(self):
        carpetaF = "entrada"
        carpetaT = "ann"
        carpetaO = "originales"

        for f in os.listdir(carpetaF):
            try:    
                self.ini = 0
                self.fin = 0
                self.idT = 0
                #la salida tiene el mismo nombre que el .txt pero con .ann
                nameF = f.split(".")
                salida = nameF[0] + ".ann"
                self.convertirTexto((carpetaF + "/" + f), (carpetaT + "/" + salida), (carpetaO + "/" + nameF[0]+".txt"))

            except Exception as e:
                print("[ERROR] Fallo al convertir el fichero %s de Freeling a Brat" % f)
                print(e)


    def convertirTexto(self, fichero, salida, textoOriginal):
        f = open(salida, "w")
        texto, lineas = self.leerArchivo(fichero)
        original=open(textoOriginal, "r").read()

        #cogemos los distintos componentes de las lineas de freeling (forma, lema, etiqueta, porcentaje(despreciable))
        for t in texto:
            forma = t[0]
            lema = t[1]
            etiqueta = t[2]

            #calculamos el inicio y el final de la forma en el texto
            self.ini =original.find(forma,self.fin)
            self.fin = self.ini + len(forma)
            self.idT += 1

            # comprobamos si es un punto, que es lo que buscamos en este script
            if forma != '.':
                continue

            #escribimos una linea para etiquetar la palabra en brat (Tx    etiquetaSimple inicio fin    forma)
            f.write("T" + str(self.idT) + "\t" + etiqueta + " " + str(self.ini) + " " + str(self.fin) + "\t" + forma + "\n")


    def leerArchivo(self, fichero):
        # Leemos el fichero
        f = open(fichero, 'r')
        lines = f.readlines()
        texto = []
        lineas = 0

        for x in lines:
            #si la linea no esta vacía la guardamos
            if len(x) > 1:
                texto.append(x.split())
                lineas += 1

        f.close()
        return texto, lineas


if __name__ == "__main__":
    Main().main()

