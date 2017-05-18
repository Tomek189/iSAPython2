import smtplib
from dzien8 import secrets

# definiuje dane do logowania
adresat = secrets.login
nadawca = secrets.login
haslo = secrets.haslo

# tworze silnik mailera
mailer = smtplib.SMTP('smtp.gmail.com', 587)
# witam sie z serwerem
mailer.ehlo()
# właczam szyfrowanie
mailer.starttls()
# loguje się
mailer.login(nadawca, haslo)

temat = "Subject: Hello from Arek\n"
wiadomosc = "To jest tresc wiadomosci"
tresc = temat + wiadomosc

# wysyłam
mailer.sendmail(nadawca, adresat, tresc)
print("Wysłano maila")

mailer.quit()

