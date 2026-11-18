mesi = ["gen", "feb", "mar", "apr", "mag", "giu", "lug", "ago", "set", "ott", "nov", "dic"]
spese = [820, 760, 910, 700, 680, 1250, 890, 1420, 730, 770, 800, 1100]
budget = 900

#Quando si sfora il budget?
for i in range(12):
    if spese[i]>budget:
        print('Si è sforato il budget nel mese di:',mesi[i])

#Totale spese dell'anno
print("Totale spese dell'anno:",sum(spese),"€")

#Media mensile delle spese
media=sum(spese)/len(spese)
print("Media mensile:", f"{media:.2f}€")

#Mese più caro e mese più economico
massimo=spese[0]
minimo=spese[0]
for i in range(len(spese)):
    if spese[i]>massimo:
            massimo=spese[i]
    elif spese[i]<minimo:
        minimo=spese[i]
for i in range(len(spese)):
    if massimo==spese[i]:
        print('Mese più caro:',mesi[i],f"({spese[i]}€)")
    if minimo==spese[i]:
        print('Mese più economico:',mesi[i],f"({spese[i]}€)")
#Quanti mesi sforano il budget?
def conta_sopra(numeri,soglia):
    contatore=0
    for i in numeri:
        if i>soglia:
            contatore+=1
    return contatore

print("Numero di mesi in cui si supera il budget:",conta_sopra(spese,budget))

#Di quanto si è sforato (o rispramiato) sull'anno rispetto a 12 volte il budget?
budget_annuo=budget*12
eccesso=budget_annuo-sum(spese)
if eccesso>=0:
    risparmio=eccesso
else:
    eccesso=-eccesso
print("Sull'intero anno si è sforato di:",f"{eccesso}€")