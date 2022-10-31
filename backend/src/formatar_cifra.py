import sys

print('First param:'+sys.argv[1]+'#')

cifra_in = "[Intro]\n\n <b>Bm</b>\nHelp, I need somebody\n <b>G</b>\nHelp, Not just anybody\n <b>E</b>\nHelp, You know, I need someone\n <b>A</b>\nHelp!\n\n[Solo]\n\n\n\n[Riff]\n\n\n\n[Primeira Parte]\n\n<b>A</b>                            \n   When I was younger (When I was younger)\n         <b>C#m</b>\nSo much younger than today (I never needed)\n                     \n<b>F#m</b>                          \n   I never needed anybody's \n <b>D</b>      <b>G</b>    <b>A</b>\nHelp in any way\n\n<b>A</b>                                    \n   But now these days are gone (now these days are gone) \n     <b>C#m</b>\nI'm not so self-assured (Now I find)\n\n<b>F#m</b>                                    \n   Now I find I've changed my mind, \n    <b>D</b>      <b>G</b>       <b>A</b>\nI've opened up the doors\n                          \n[Refrão]\n\n <b>Bm</b>\nHelp me if you can\nI'm feeling down\n       <b>G</b>\nAnd I do appreciate \nYou're being'round\n <b>E</b>\nHelp me get my feet \nBack on the ground\n            <b>A</b>\nWon't you please\nPlease help me?\n\n[Segunda Parte]\n\nAnd now my life has changed in (Now my life has changed)\n<b>C#m</b>\nOh, so many ways\n\n<b>F#m</b>                          \n   My independence seems (My independence)  \n    <b>D</b>     <b>G</b>       <b>A</b>\nTo vanish in the haze (Vanish in the haze)\n        \n<b>A</b>                            \n   But every now and then (But every now and then)\n   <b>C#m</b>\nI feel so insecure\n\n<b>F#m</b>                                    \n   I know that I just need you like \n   <b>D</b>     <b>G</b>      <b>A</b>\nI never done before\n( I know that I )    (never done before)\n\n[Refrão]\n\n <b>Bm</b>\nHelp me if you can\nI'm feeling down\n       <b>G</b>\nAnd I do appreciate \nYou're being'round\n <b>E</b>\nHelp me get my feet \nBack on the ground\n            <b>A</b>\nWon't you please\nPlease help me?\n\n[Primeira Parte]\n\n<b>A</b>                            \n   When I was younger (When I was younger)\n         <b>C#m</b>\nSo much younger than today (I never needed)\n                     \n<b>F#m</b>                          \n   I never needed anybody's \n <b>D</b>      <b>G</b>    <b>A</b>\nHelp in any way\n\n<b>A</b>                                    \n   But now these days are gone (now these days are gone) \n     <b>C#m</b>\nI'm not so self-assured (Now I find)\n\n<b>F#m</b>                                    \n   Now I find I've changed my mind \n    <b>D</b>      <b>G</b>       <b>A</b>\nAnd opened up the doors\n\n\n[Refrão]\n\n <b>Bm</b>\nHelp me if you can\nI'm feeling down\n       <b>G</b>\nAnd I do appreciate \nYou're being'round\n <b>E</b>\nHelp me get my feet \nBack on the ground\n            <b>A</b>\nWon't you please, \nPlease help me?\n\n[Final]\n\n<b>F#m</b>               <b>A</b>\n   Help me, help me, ooh"

cifra_in_split = cifra_in.split("\n")
cifra_in_split = [cifra.strip()
                  for cifra in cifra_in_split if cifra.strip() != ""]
cifra_typed = []
for cifra in cifra_in_split:
    if cifra.startswith("[") and cifra.endswith("]"):
        cifra_dict = {"tipo": "titulo", "conteudo": cifra}
    elif cifra.startswith("<b>") and cifra.endswith("</b>"):
        cifra_dict = {"tipo": "acordes", "conteudo": cifra}
    else:
        cifra_dict = {"tipo": "letra", "conteudo": cifra}
    cifra_typed.append(cifra_dict)

cifra_formatada = ""
for cifra in cifra_typed:
    if cifra["tipo"] == "titulo":
        cifra_formatada += "\n\n" + cifra["conteudo"][1:-1] + ":\n"
    elif cifra["tipo"] == "acordes":
        lista_acordes = [c for c in cifra["conteudo"].split(" ") if c != ""]
        lista_acordes = [c[3:-4] for c in lista_acordes]
        for acorde in lista_acordes:
            acorde = acorde.replace("C", "1").replace("D", "2").replace("E", "3").replace(
                "F", "4").replace("G", "5").replace("A", "6").replace("B", "7")
            cifra_formatada += acorde + " / "
        cifra_formatada += "\n"
    else:
        cifra_formatada += "; " + cifra["conteudo"] + "\n"

f = open("cifraout.txt", "w")
f.write('<!DOCTYPE html>\n<meta charset="utf-8">\n<base href="https://dtinth-chordbook.netlify.app/">\n<script src="lib/entry.js"></script>\n<pre id="src">' + cifra_formatada + "</pre>")
f.close()
