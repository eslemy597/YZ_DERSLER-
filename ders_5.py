kelime1 = "kulaklik"
kelime2 = "kulakliklar"

kume1 = set(kelime1)
kume2 = set(kelime2)

ortak_harfler = kume1.intersection(kume2)

tum_harfler = kume1.union(kume2)

benzerlik_skoru = len(ortak_harfler) / len(tum_harfler)

print("Kelime 1 Harfleri:", kume1)
print("Kelime 2 Harfleri:", kume2)
print("Ortak Harfler:", ortak_harfler)
print("Hesaplanan benzerlik skoru:", round(benzerlik_skoru , 2))
