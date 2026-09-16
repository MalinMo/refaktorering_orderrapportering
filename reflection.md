# Reflektion kring refaktoreringen

### Vilka var de viktigaste problemen i originalkoden?
Två problem bedömde jag som hög prioritet att åtgärda
1. Att hela programmet körs vid import
2. Att olika ansvar har blandats

### Vilka förändringar tycker du förbättrade programmet mest?
Att lösa de två vikitgaste problemen anser jag är de största förbättringarna:
1. Att lägga programmstart i en `__main__.py` med en main-guard
2. Att separera de olika ansvaren för filhantering, transformation och flöde.

### Varför valde du den projektstruktur du använde?
Den valda strukturen ger en tydlig uppdelning av olika ansvar i moduler:  
filhantering, validering, processning, rapportering, testning och en separat startknapp.

Jag valde också att i mappen tests lägga dataframen för inputfilen i en `conftest.py` så den kunde användas som en parameter.

### Var använde du OOP/dataclass och varför passade det där?
Jag skapade en dataklass i `config.py` därför att den samlar ihop de olika sökvägarna som används.


### Vilka viktiga beteenden skyddar dina automatiska tester, och vilken nytta ger testerna om programmet förändras i framtiden?
Testerna kontrollerar att filen hittas och läses korrekt och hanterar saknade eller felaktiga värden. De kontrollerar även beräkningar och sammanställningar.  
Om förändringar görs i programmet kan testerna visa om något blivit fel och verifiera att programmet fungerar som det ska efter förändringarna.

### Vad var svårast?
Kodgranskningen i sig tycker jag var utmanande men jag kämpade också en del med koden för själva pipelinen särskilt då det var fler filer som skulle skrivas ut.

### Vad hade du velat förbättra ytterligare om du haft mer tid?
Ytterligare förbättringar kan vara att validera outputfilerna och kontrollera att de har rätt kolumner och rimligt innehåll.  
Det kanske också hade varit rimligt att testa ifall `quanitity` eller `unit_price`är negativa.  
Sökvägen för indata är hårdkodad vilket hade kunnat ändras med argparse.