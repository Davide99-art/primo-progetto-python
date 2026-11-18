mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
spese = [820, 760, 910, 700, 680, 1250, 890, 1420, 730, 770, 800, 1100]
budget = 900

for i in range(12):
    if spese[i]>budget:
        print('Si è sforato il budget nel mese di:',mesi[i])

print("Totale spese dell'anno:",sum(spese),"€")