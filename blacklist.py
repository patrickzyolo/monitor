#!/usr/bin/python
# -*- coding: utf-8 -*-

bad = ["haelt", "sicher", "tritt", "essen", "rein", "eigene",
       "sich", "offen", "Leute", "Fuenf", "echt", "Ihre", "stehen",
       "legt", "laenger", "zeigt", "lang", "gibt", "gern", "deckt",
       "Woche", "Jahren", "kein", "euch", "Kein", "Test", "halte",
       "eine", "muss", "oben", "haben", "sein", "richtig", "Bayer",
       "laesst", "startet", "Video", "unter", "here", "drei", "gehen",
       "wird", "Eine", "allen", "Geri", "grosse", "lege", "Hier",
       "sind", "auch", "+++:", "einen", "fahren", "biete", "besser",
       "nicht", "noch", "ohne", "seit", "letzte", "Drei", "Unter", "Wochen",
       "Diese", "diese", "immer", "einer", "bring", "erste", "reiche",
       "Neue", "nach", "fuer", "ueber", "frei", "macht", "dieser", "lieb",
       "UeBERSICHT", "unter", "will", "Ueber", "alte", "keine", "zehn",
       "Zwei","zwei", "alle", "eins", "Nach", "holt", "wirft", "isch",
       "weiter", "mein", "Deutschland", "nehmen", "Inter", "wach", "ihren",
       "Internet:", "Sport", "mehr", "Mehr", "soll", "durch", "halten",
       "kommt", "zurueck", "halt", "erst", "acht", "aller", "raus", "Keine",
       "beste", "Ukraine-", "geben", "geben", "machen", "Tuer", "fest",
       "wegen", "Fußball", "gegen", "kann", "20.10.", "Vergleich", "neues",
       "dies", "geht", "Auto", "neue", "aufs", "oder", "recht", "wurde",
       "echte", "Wind", "werde", "Tage", "2014", "reist", "werden", "ziert",
       "Meter", "meist", "Wenn", "habe", "Groß", "wieder", "stand", "große",
       "Jahr", "heim", "weit", "deutsche", "Frau", "Zeit", "Familie", "Liebe",
       "beim", "Erst", "Komm", "eines", "ihre", "Haus", "\"Ich", "Mann", "kommen",
       "teil", "teilt", "eure", "hart", "Welt", "Fuss", "mach", "eben",
       "neuen", "Hand", "Warum", "Alle", "lange", "seine", "koennte", "gemein",
       "zweites", "alten", "sucht", "\"Die", "vier", "fuenf", "voll", "andere",
       "einem", "muessen", "Klaus", "statt", "Will", "fort", "fort", "gleich",
       "wollen", "aber", "neuer", "Ende", "muessen", "bringt", "statt", "setzt",
       "enden", "viel", "Ende", "plant", "bringt", "Nachrichten", "droht",
       "Arme", "statt", "setzt", "ganz", "Deutsch", "gebe", "eher", "steht",
       "sehen", "gehe", "eher", "sieht", "\"Das", "jede", "denken", "stark",
       "Drei-", "komme", "jetzt", "bitte", "lassen", "rund", "stellt", "Frank",
       "doch", "nimmt", "Viel", "sechs", "Vier", "sagt", "lass", "Wiesn",
       "Erste", "Voll", "reich", "rote", "renn", "ringt", "einig", "esse",
       "enge", "start", "bereit", "Miss", "zieht", "ieder", "hatte",
       "Spiele", "Allgemein", "schon", "Fussball", "rich",
       "erhoeht", "warnt", "Nord", "ruck", "Profi", "ersten", "Fussball:",
       "liess", "ausser", "erneut", "feiert", "spielt", "Moto", "euer",
       "Star", "Neues", "bleibt", "bitten", "fordert", "West", "dass",
       "weitere", "siegt", "achte", "Gross", "Sued", "verlaesst",
       "Zustand", "sollen", "lame", "faellt", "Eins", "laut", "Mass",
       "darf", "meiste", "Deutsche", "teuer", "Bund", "spaet", "Neuer",
       "Kommentar", "Recht", "ehrt", "spaet", "Grund", "Ein-", "Bode",
       "ordnet", "sehe", "enger", "erstmals", "endet", "willige",
       "ordnet", "trotz", "enger", "sehe", "ante", "Auch", "morgen",
       "fuehren", "schwarze", "Aufs", "Bahn-", "griff", "wert", "zahlen",
       "nich", "Mens", "eiert" , "ruft", "gross", "Schlagzeilen", "für",
       "über", "rät", "Über", "zurück", "können", "Tür", "Fuß", "fahr",
       "hält", "führt", "Für", "lässt", "hält", "setzen", "sollte", "dann"
       "wohl", "führt", "sicht", "Sicht", "lässt", "hält", "passt",
       "dank", "hoch", "sagen", "Wirt", "inne", "Prof", "schwer",
       "gleichen", "fallen", "Expo", "isst", "Fall", "wenig", "müssen",
       "großen", "lebe", "kleine", "groß", "hält", "class=headline-link",
       "hier", "Mini", "Dies", "Mein", "diesen", "zweite", "Tür", "fein",
       "könnte", "seinen", "fünf", "zurück", "Rund", "lässt", "warte",
       "lasse", "weite", "trifft", "gleiche", "findet", "besten",
       "ließ", "trifft", "Seit", "Teil", "unser", "Main", "kennen",
       "hör", "Dieser", "nehm", "nahm", "wenige", "geplante",
       "gewinnt", "Stan", "ziehen", "alles", "miss"]

exception = ["EU", "Eu", "USA", "BND", "IS", "Tod", "CIA", "NSA", "ARD", "ZDF",
	   		 "Uni", "UNI", "UNO", "CDU", "CSU", "SPD", "AFD", "Afd", "FDP", "Uno",
	   		 "BMW", "PKK", "Dax", "DAX", "IBM", "DDR", "IT", "Mac", "SAP", "RWE",
	   		 "EZB", "NPD", "MAD", "VW", "IAA", "UN"]
