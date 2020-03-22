# Domácí úkol 1 - třídění

## Motivace

Pokud zpracováváme velké množství dat, začne nás kromě správnosti zpracování
zajímat i rychlost zpracování. Rychlost můžeme ovlivnit konkrétním
počítačem či počítači, na kterém náš program spouštíme, zvoleným programovacím
jazykem a volbou algoritmu, který použijeme. Zatímco volba počítače a jazyka
obvykle ovlivňuje rychlost programu konstantním faktorem (násobí čas pro daný
vstup nějakou konstantou, například pokud program v jazyce *A* poběží *t* sekund,
program v "pomalejším" jazyce *B* poběží *2t* sekund), volba algoritmu může mít
výrazný vliv na rychlost programu vzhledem k velikosti dat. Pokud máme lineární
algoritmus, pak pro dvojnásobně velká data potřebujeme přibližně dvojnásobný
čas. Pokud je ale náš algoritmus kubický, potřebujeme 8x (2^3) více času na
výpočet. V rámci úkolu si rozdílné rychlosti algoritmů prakticky vyzkoušíte.

## Zadání

Napište program porovnávající jednotlivé třídící algoritmy, porovnejte jejich
rychlosti a zdůvodněte, proč se chovají tak, jak se chovají. Implementujte
Quicksort a 2 "pomalé" třídící algoritmy. Změřte rychlost běhu jednotlivých
algoritmů a standardního třídění (`list.sort()`) na datech velikostí *4^k*, kde
*k=3,...,10*. Změřte na následujících typech dat:
 - náhodné integery
 - stříděné integery
 - setříděné integery, které mají 1% dvojic prvků náhodně prohozených

Výsledky vyneste do grafů a odůvodněte. 

### Vstup
Program si vstupní data generuje sám, od uživatele nebere vstup.

### Výstup
Program průběžně vypisuje, za jak dlouho setřídil daný seznam. Přesný formát
není dán, ale měl by být takový, aby se naměřená data dala dále snadno
zpracovávat a neztrácela se v debugovacích výpisech.

Dále z naměřených dat vytvoříte zprávu v PDF s popisy iomplementovaných
algoritmů, grafy, zdůvodněními a použitou metodikou měření (kolikrát jste měřili
jaká data, jak jste generovali data, ...).

### Doporučení

Napište si funkce na jednotlivé třídící algoritmy. Nejprve se věnujte zdrojovému
kódu a nechte si ho zkontrolovat, ať pak nemusíte předělávat grafy a zdůvodnění.  

Pro měření rychlosti požijte `time.time_ns()`.

Rychlost berte jako průměr časů z více třídění dat dané velikosti (desítky běhů
u malých seznamů, jednotky běhů u velkých seznamů).  Měřte pouze rychlost
třídění, nikoli čas potřebný na generování vstupu či jiné podpůrné operace.

### Odevzdání
Odevzdávat budete kompletní zdrojové kódy projektu a zprávu s grafy a zdůvodněními. Vše
bude zabalené v zip souboru, který bude obsahovat adresář `du1_jmeno_prijmeni`,
ve kterém budou zdrojové kódy a soubor se zprávou, tedy například:
```
du3.zip
|
\du3_tomas_pokorny
  |- vysledky.pdf
  |- sort_measurement.py
```
Zip archiv mi pošlete mailem. Odevzdávat můžete samozřejmě i přes GitHub
(preferovaná varianta), požadavky viz níže (stejné jako 3. úkol z Úvodu do
programování).

Deadline zatím není stanovena, pokud dojde později k jejímu stanovení, dám vědět
emailem alespoň týden dopředu před deadlinem. Můžete odevzdávat
opakovaně, jako v [Úvodu do
programování](https://github.com/xtompok/uvod-do-prg_19/), a až budete chtít
odevzdat finálně, napíšete a já vám úkol oboduji. Každému, kdo mi pošle úkol,
odpovím, že jsem ho přijal. Pokud neodpovím, urgujte.

### Bodování
- 5b za správný zdrojový kód
- 3b za zprávu
- 2b za kvalitu kódu a komentáře

Kvalitou kódu se rozumí použití vhodných prostředků k dosažení cíle,
minimalizace opakujícího se kódu, vhodné odsazení a oddělení funkčních celků,
použití funkcí tam, kde to dává smysl.

Komentáře v kódu jsou důležité, aby člověk, co si váš kód čte, získal přehled o
tom, co kód dělá. Nekomentujte každý řádek, ale jednotlivé funkční celky. Pokud
používáte metody (a že byste měli), u každé napište, jaké má vstupy a co vrací
jako výstup, ideálně jako [Docstring](https://www.python.org/dev/peps/pep-0257/).
Komentářů by mělo být výrazně méně než kódu.

Samostatnou dokumentaci tentokrát vytvářet nemusíte, jednoduchá uživatelská
dokumentace (tedy jak se program používá, více viz Úvod do programování) by měla
být součástí zprávy.

Postup, jak domácí úkol napsat, spolu klidně konzultujte, ale kód pište každý
sám. Pokud objevím identické či nápadně podobné řešení, oboduji je jednou a body
rovnoměrně rozdělím mezi autory. 

## Bonusové body

Za různé nadstavby k zadání můžete získat bonusové body. 

### Používání Gitu pro vývoj (1 b)

Pokud budete pro verzování používat Git, vytvořte si účet na
[GitHubu](https://github.com) nebo jiné
podobné stránce a úkol můžete odevzdat přes něj. Kromě samotného odevzdání je
třeba, aby byl repozitář používán i pro vývoj, tedy by měl obsahovat průběžně
commitovanou práci a zprávy u commitů by měly popisovat, co se v daném commitu
změnilo. Repozitář by měl obsahovat jak program, tak zprávu, pokud chcete,
můžete ji napsat v 
[MarkDownu](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet),
pak nemusíte odevzdávat PDF.
Pokud budete potřebovat pomoct, pište mi.

### Výstup naměřených dat v CSV
Abyste nemuseli po konci běhu programu opisovat ručně do tabulkového editoru
naměřené hodnoty, můžete si hodnoty v průběhu programu zapamatovat a na konci
vytvořit CSV soubor, který lze snadno v tabulkovém procesoru otevřít. Soubor
vytvořte tak, aby k získání výsledných grafů nebylo ideálně potřeba s daty v
tabulce nijak manipulovat, jen zvolit, která data se použijí pro které sloupce a
které popisky. Je vhodné pro vytváření souborů CSV použít modul
[`csv`](https://docs.python.org/3/library/csv.html).


### Další třídící algoritmus (1 b za každý, max 2 body)
Implementujte další třídící algoritmus a přidejte ho do srovnání.

