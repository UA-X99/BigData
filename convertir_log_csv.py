import csv

input_file = "Enroll Log Sept 29 2025.log"
output_file = "enroll_log_sept_29_2025.csv"

with open(input_file, "r", encoding="utf-8", errors="ignore") as log, \
     open(output_file, "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(["Fecha", "Hora", "Nivel", "Mensaje"])

    contador = 0

    for line in log:
        line = line.strip()
        if not line:
            continue

        parts = line.split()

        if len(parts) < 4:
            continue

        fecha = parts[0]
        hora = parts[1]
        nivel = parts[2]
        mensaje = " ".join(parts[3:])

        writer.writerow([fecha, hora, nivel, mensaje])
        contador += 1

print("Filas escritas:", contador)
print("CSV generado correctamente")

