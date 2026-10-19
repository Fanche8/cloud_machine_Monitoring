import random
import csv

if __name__ == "__main__":
    # # Simulierte Daten generieren
    # daten = []
    # for i in range(100):
    #     datum = f"2024-06-{random.randint(1, 30):02d}"
    #     wert = random.uniform(0, 100)
    #     daten.append((datum, wert))
    #     if wert > 90:
    #         print(f"Warnung: Wert {wert:.2f} am {datum} ueberschreitet den Grenzwert von 90.")
    # # Daten ausgeben
    # for datum, wert in daten:
    #     print(f"{datum}: {wert:.2f}")
    



    # Simulierte Maschinendaten generieren
    daten = []

    for i in range(100):
        datum = f"2024-06-{random.randint(1, 30):02d}"
        wert = random.uniform(0, 100)

        daten.append((datum, wert))

        if wert > 90:
            print(
                f"Warnung: Wert {wert:.2f} am {datum} "
                "ueberschreitet den Grenzwert von 90."
            )

    # Daten in einer CSV-Datei speichern
    with open("maschinendaten.csv", "w", newline="", encoding="utf-8") as datei:
        writer = csv.writer(datei)
        writer.writerow(["Datum", "Messwert"])
        writer.writerows(daten)

    # Daten in der Konsole ausgeben
    for datum, wert in daten:
        print(f"{datum}: {wert:.2f}")

    print("\n100 Messwerte wurden generiert.")
    print("Die Daten wurden in maschinendaten.csv gespeichert.")

