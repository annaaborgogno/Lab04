import time
import flet as ft
import model as md

class SpellChecker:

    def __init__(self, view):
        self._multiDic = md.MultiDictionary()
        self._view = view

    def handleSentence(self, txtIn, language, modality):
        txtIn = replaceChars(txtIn.lower())

        words = txtIn.split()
        paroleErrate = " - "

        match modality:
            case "Default":
                t1 = time.time()
                parole = self._multiDic.searchWord(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Linear":
                t1 = time.time()
                parole = self._multiDic.searchWordLinear(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " "
                t2 = time.time()
                return paroleErrate, t2 - t1

            case "Dichotomic":
                t1 = time.time()
                parole = self._multiDic.searchWordDichotomic(words, language)
                for parola in parole:
                    if not parola.corretta:
                        paroleErrate = paroleErrate + str(parola) + " - "
                t2 = time.time()
                return paroleErrate, t2 - t1
            case _:
                return None


    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


    def handleLanguageSelection(self, e):
        self._view.txtOut.controls.append(ft.Text(value="Lingua scelta correttamente: " + self._view.ddLanguage.value))
        self._view.update()

    def handleModalitySelection(self, e):
        self._view.txtOut.controls.append(ft.Text(value="Modalità scelta correttamente: " + self._view.ddModality.value))
        self._view.update()

    def handleSpellCheck(self, e):
        lingua = self._view.ddLanguage.value
        modalita = self._view.ddModality.value
        frase = self._view.testo.value

        if lingua == "":
            self._view.txtOut.controls.append(ft.Text(value="Attenzione, selezionare una lingua", color="red"))
            self._view.update()
            return
        if modalita == "":
            self._view.txtOut.controls.append(ft.Text(value="Attenzione, selezionare una modalita", color="red"))
            self._view.update()
            return
        if frase == "":
            self._view.txtOut.controls.append(ft.Text(value="Attenzione, selezionare una frase", color="red"))
            return

        paroleSbagliate, tempo = self.handleSentence(frase, lingua, modalita)

        self._view.txtOut.controls.append(ft.Text(value=f"Frase inserita: {frase}\n Parole sbagliate: {paroleSbagliate}\n Tempo impiegato: {tempo}"))
        self._view.update()


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$?%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text