# Kodgranskning av order_report.py

## Utgångsläge  
Programmet går att köra och skapar en rapport över försäljning och returer.

**overview.csv**  
metric,value  
total_sales,138036.05  
order_count,80.0  
return_count,15.0  

**returns_by_category**  
product_category,order_count,returns,return_rate  
Electronics,26,7,0.269  
Home,17,4,0.235  
Sports,16,2,0.125  
Books,21,2,0.095  

**sales_by_category**  
product_category,order_count,total_sales,returns,return_rate  
Electronics,26,79589.3,7,0.269  
Sports,16,24416.15,2,0.125  
Home,17,23927.6,4,0.235  
Books,21,10103.0,2,0.095  

**sales_by_region**  
region,order_count,total_sales,returns,return_rate  
South,24,36737.95,6,0.25  
East,18,35585.35,3,0.167  
West,14,32624.8,2,0.143  
North,23,29891.95,3,0.13  
Unknown,1,3196.0,1,1.0  


## Granskningsfynd  

### Fynd 1 - Hela programmet körs vid import

**Observation:** Hela scriptet, inläsning, validering, bearbetning och export, ligger direkt på modulnivå.

**Konsekvens:** Så fort filen importeras körs hela flödet igång vilket gör det svårt att testa eller återanvända delar.

**Förslag:** Lägg programmstart i en __main__.py med en main-guard

### Fynd 2 - Olika ansvar har blandats

**Observation:** Scriptet blandar filhantering, validering, transformation och rapportering.

**Konsekvens:** Delarna kan inte testas eller återanvändas oberoende.

**Förslag:** Separera de olika ansvaren för filhantering, transformation och flöde.

### Fynd 3 - Upprepad kod

**Observation:** Koden för result 1, result 2 och returns_by_category är nästan identiska, samma gruppering, avrundning, berökning och sortering.

**Konsekvens:** Om beräkningslogiken behöver ändras måste ändringen göras på tre separata ställen i koden vilket ökar risken för fel.

**Förslag:** Bryt ur till en funktion som sedan anropas med respektive kolumnnamn.

### Fynd 4 - Generell felhantering

**Observation:** All kod ligger i ett enda try/except som fångar all typer av fel men inte specificerar vad som är fel.

**Konsekvens:** Felet blir svårt att hitta t.ex. om en kloumn saknas vilken. 

**Förslag:** Använda ValueError och specifika meddelanden om vad som är fel.

### Fynd 5 - print används istället för loggning

**Observation:** Statusmeddelanden skrivs genomgående som print.

**Konsekvens:** Det går inte att styra detaljnivå (debug/info/warning/error) på eller destination för meddelanden och det framgår inte varifrån de kom.

**Förslag:** Använd modulloggers och konfigurera loggningen centralt.

### Fynd 6 - Hårdkodade sökvägar och förutsättningar

**Observation:** Sökvägarna till indata och outputmapp är hårdkodade direkt i skriptet och koden förutsätter att outputmappen redan finns.

**Konsekvens:** Det blir svårt att köra programmet mot andra filer eller testa det med tillfälliga sökvägar. Om outputmappen saknas kraschar programmet vid skrivning, eftersom mappen inte skapas automatiskt.

**Förslag:** Samla sökvägar i en modul och låt sparfunktionen skapa målmappen automatiskt om den saknas.

## Sammanfattning

Scriptet skapar rätt orderrapport för exempeldatan, men programflödet har sidoeffekter vid import och blandar filhantering, validering, beräkning och sparning. De centrala reglerna är därför svåra att testa isolerat.

## Prioritering

### Hög prioritet

1. Fynd 1 - Hela programmet körs vid import
2. Fynd 2 - Olika ansvar har blandats

### Medelprioritet

3. Fynd 3 - Upprepad kod
4. Fynd 4 - Generell felhantering
5. Fynd 6 - Hårdkodade sökvägar och förutsättningar

### Låg prioritet

6. Fynd 5 - print används istället för loggning