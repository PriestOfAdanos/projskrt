# Zapis do pliku html
try:
    file_in = open("raport.txt", "r")
    lines = file_in.readlines()
    file_in.close()
except IOError:
    print("Nie znaleziono pliku")
    exit(-1)

try:
    x = int(lines[1])
    y = int(lines[3])
    z = int(lines[5])
    t = int(lines[7])
    q = int(lines[9])
except ValueError:
    print("Nieprawidłowe dane wejściowe, program zostanie wykonany na poniższych danych:")


try:
    file_html = open("output.html", "w")

    message = """
    <!DOCTYPE html>
    <html>
    <head>
    <link rel="stylesheet" href="styles.css">
    </head>
    <body>


    <table class="steelBlueCols">
    <thead>
    </thead>
    <tbody>
    <tr>
    <td>Przetworzone pliki</td><td>"""

    message_res_1 = x
    message_res_4 = y
    message_res_4_1 = q/x
    message_res_3 = "{}|{}".format(z/x,t/x)
    message2 = """
    </td>
    <td>Przetworzone pliki</td><td>"""
    message3 = """
    </td></tr>
    <tr>
    <td>Średnie punkty początkowe(b|g)</td><td>"""
    

    message4 = """
    </td></tr>
    <tr>
    <td>Pliki nieprzetworzone</td><td>"""
    message4_1 = """
    </td></tr>
    <tr>
    <td>Średni rozmiar drzewa</td><td>"""

    
    message5 = """
    </td></tr>
    <tr>
    </tbody>
    </tr>
    </table>

    </body>
    </html>"""
    file_html.writelines(str(message))
    #file_html.writelines(str(message2))
    file_html.writelines(str(message_res_1))
    file_html.writelines(str(message3))
    file_html.writelines(str(message_res_3))
    file_html.writelines(str(message4))
    file_html.writelines(str(message_res_4))
    file_html.writelines(str(message4_1))
    file_html.writelines(str(message_res_4_1))
    file_html.writelines(str(message5))
    file_html.close()
except IOError:
    print("Błąd zapisu danych")
    exit(0)
    
exit(1)