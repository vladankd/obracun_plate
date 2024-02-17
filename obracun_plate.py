# Bruto ugovorena plata
# print("Unesite koeficijent - Bruto ugovorena plata -")
# keoficijent_pl = float(input()) 
keoficijent_pl = 2386.80

# Broj radnih dana u mjesecu
# broj osnovnih sati u mjesecu u odnosu na broj dana
mj_dana = 23
br_osn_sati = mj_dana * 8

# Bruto cijena sata
cj_sat = keoficijent_pl / br_osn_sati
cj_nocni_sat = cj_sat * 1.3
cj_praznik_sat = cj_sat * 1.4
cj_praznik_noc = cj_sat * 1.7 
cj_odsustvo_sat = cj_sat
cj_ot_sat = cj_sat * 1.25
cj_ot_sat_noc = cj_sat * 1.55
cj_ot_sat_praznik = cj_sat * 1.65
cj_ot_sat_noc_praznik = cj_sat * 1.95

# Minuli rad 
# godine staza x 0.3% dobije se koeficijent
# koeficijent x osnovica = bruto minuli rad
# uzima se kao osnovica redovan rad bez OT-a
staz = 17
koeficijent_mr = staz * .003
# osnovica za mr = kupno sati bez OT (provjeriti nocni sati da li se racunaju kao nocni?)
osnovica_mr = 2469.82
bruto_mr = osnovica_mr * koeficijent_mr

# Prevoz
# cijena mjesecne karte 
# ne racuna se u bruto, dodaje se puni iznos nakon poreza
prevoz = 78

# Topli obrok
# broj radnih dana bez odsustava
# + jedan dan za svaki OT preko 3 sata (3 sta OT da li se racuna kao dan za TO?)
# dnevni iznos TO = prosjecna bruto plata za prethodnu godinu * 0.85%
# Trenutni iznos bruto TO u RS = 16.46 KM dnevno
# neto TO  trenutno u RS = 10.04 KM
bruto_to_dnevno = 16.46
br_dana = 18
bruto_to = br_dana * bruto_to_dnevno

# Obracun #
# ------- #

# Sabiranje(unos) odradjenih sati u toku mjeseca
redovni_sat = 120
nocni_sat = 0
praznik_sat = 16
praznik_noc = 0 
odsustvo_sat = 48
ot_sat = 7
ot_sat_noc = 1.13
ot_sat_praznik = 1
ot_sat_noc_praznik = 2

# Obracun bruto sati za mjesec
# broj sati po kategorijama * cijena sata po kategorijama

bruto_sat = redovni_sat * cj_sat
bruto_nocni_sat = nocni_sat * cj_nocni_sat
bruto_praznik_sat = praznik_sat * cj_praznik_sat
bruto_praznik_noc = praznik_noc * cj_nocni_sat
bruto_odsustvo_sat = odsustvo_sat * cj_odsustvo_sat
bruto_ot_sat = ot_sat * cj_ot_sat
bruto_ot_sat_noc = ot_sat_noc * cj_ot_sat_noc
bruto_ot_sat_praznik = ot_sat_praznik * cj_ot_sat_praznik
bruto_ot_sat_noc_praznik = ot_sat_noc_praznik * cj_ot_sat_noc_praznik

# Saberi sve bruto sate 
# sobije se ukupna bruto vrijednost odradjenih sati
bruto_ukupno_sati = round(bruto_sat,2) + round(bruto_nocni_sat,2) + round(bruto_praznik_sat,2) + round(bruto_praznik_noc,2) + round(bruto_odsustvo_sat,2) + round(bruto_ot_sat,2) + round(bruto_ot_sat_praznik,2) + round(bruto_ot_sat_noc,2) + round(bruto_ot_sat_noc_praznik,2)

# Dodati TO i Minuli rad na bruto sate za obracun doprinosa
# Bez prevoza prevoz se dodaje na kraju jer ne podlijeze porezu i doprinosima
bruto_plata = round(bruto_ukupno_sati,2) + round(bruto_to,2) + round(bruto_mr,2)

# Doprinosi 
# Na ukupnu bruto platu izbiti prevoz
# Ukupan iznos doprinosa 31%
doprinos_pio = 0.185
doprinos_fzo = 0.102
doprions_dz = 0.017
doprions_nzp = 0.006
doprinosi_stopa_ukupno = doprinos_pio + doprinos_fzo + doprions_dz + doprions_nzp
# Iznos doprinosa = bruto plata x doprinosi_stopa_ukupno
iznos_doprinosa = bruto_plata * doprinosi_stopa_ukupno

# Porez
# Na ukupnu bruto platu izbiti prevoz pa - 1000 KM mjesecnog odbitka 
# na preostali iznos 8% poreza
por_odbitak = 1000
por_stopa = 0.08
iznos_poreza = (bruto_plata - por_odbitak )* por_stopa

# Plata poslije poreza
plata_nakon_poreza_doprinosa = bruto_plata - iznos_doprinosa - iznos_poreza

print(plata_nakon_poreza_doprinosa)

# Odbitak za solidarnost 0.25% na platu poslije poreza
solidarnost_stopa = 0.0025
odbitak_solidarnost = plata_nakon_poreza_doprinosa * solidarnost_stopa
print(odbitak_solidarnost)

# Plata za isplatu - Neto plata
neto_plata = plata_nakon_poreza_doprinosa + prevoz - odbitak_solidarnost

print(round(neto_plata,2))

##### TO DO #####

# Unos podataka treba rjesiti
# da inputi budu uneseni od starane korisnika a ne hardcodirani
# Ukupno radno vrijeme broj sati u mjesecu - OT, praznici, nocni sati GO 

# UI razviti

