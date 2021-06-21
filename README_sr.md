# Text to Speech za Srpski jezik 🇷🇸
**ANDREJ RAJKOV - PETNIČKI PROJEKAT 2021**

Prva verzija TTS-a na srpskom jeziku. 

Ovaj program pretvara željeni tekst iz tekst fajla u govor u vidu audio fajla.

## Način rada

+ Projekat je/će biti rađen u Python-u u potpunosti. 
+ Projekat koristi [PYDUB](http://pydub.com/) biblioteku za manipulaciju zvuka.
+ U najosnovnijem obliku (verziji 1.0) program uzima slova i pauze iz stringa i nadovezuje audio fajlove sa imenom slova.
```
for x in string:
    combined+=AudioSegment.from_mp3(x+".mp3")
```

## NAPOMENA

+ Ova verzija TTS-a **nije** finalna verzija, već samo proof of concept.
+ U finalnoj verziji, v2.0, biće implementirane bolje audio biblioteke, akcentacija, interpunkcija.
Postoji mogućnost uvođenja algoritama za kontekst u narednim verzijama.

## Sistemski zahtevi

Program je testiran na Linuxu, ali verovatno radi i na Windows sistemima.

+ [FFMPEG](https://ffmpeg.org/)

## Dalji napredak

Za sledeću verziju planirana su sledeća poboljšanja:

+ Nova audio biblioteka (engine će imati tečniji i prirodniji izgovor slova i reči)
+ Akcentacija po pravilima srpskog jezika (modulacija reči - dužina i promena tona)
+ Interpunkcija (promena tona u zavisnosti od .,!?)
+ Dodavanje prostog GUI-a i dodavanje EXE fajla

Kasnije verzije će sadržati i:

+ Algoritmi za kontekst (rešava probleme Luka/ luka, da dâ)
