def cipher_formatter(cipher_in):
    cipher_in_split = cipher_in.split("\n")
    cipher_in_split = [cipher.strip()
                       for cipher in cipher_in_split if cipher.strip() != ""]
    cipher_typed = []
    for cipher in cipher_in_split:
        if cipher.startswith("[") and cipher.endswith("]"):
            cipher_dict = {"tipo": "titulo", "conteudo": cipher}
        elif cipher.startswith("<b>") and cipher.endswith("</b>"):
            cipher_dict = {"tipo": "acordes", "conteudo": cipher}
        else:
            cipher_dict = {"tipo": "letra", "conteudo": cipher}
        cipher_typed.append(cipher_dict)

    cipher_formatted = ""
    for cipher in cipher_typed:
        if cipher["tipo"] == "titulo":
            cipher_formatted += "\n\n" + cipher["conteudo"][1:-1] + ":\n"
        elif cipher["tipo"] == "acordes":
            chords_list = [
                c for c in cipher["conteudo"].split(" ") if c != ""]
            chords_list = [c[3:-4] for c in chords_list]
            for chord in chords_list:
                chord = chord.replace(
                    "C", "1").replace(
                    "D", "2").replace(
                    "E", "3").replace(
                    "F", "4").replace(
                    "G", "5").replace(
                    "A", "6").replace(
                    "B", "7")
                cipher_formatted += chord + " / "
            cipher_formatted += "\n"
        else:
            cipher_formatted += "; " + cipher["conteudo"] + "\n"

    cipher_formatted = '<!DOCTYPE html>\n<meta charset="utf-8">\n<base href="https://dtinth-chordbook.netlify.app/">\n<script src="lib/entry.js"></script>\n<pre id="src">' + cipher_formatted + "</pre>"

    # f = open("cipherout.txt", "w")
    # f.write(cipher_formatted)
    # f.close()

    return cipher_formatted
