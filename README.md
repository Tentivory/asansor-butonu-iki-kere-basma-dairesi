# Asansör Düğmesine İki Kere Basma Dairesi

**Kurum kodu:** ABD-2 / 2026-KAT
**Bağlı olduğu makam:** Kat Arası Bekleme ve Sabırsızlık Genel Müdürlüğü
**Statü:** Resmi. Gereksiz. Çalışıyor.

Bu daire, yurttaşın asansör düğmesine ikinci kez basmasının kabini hızlandırdığı yönündeki kadim inancı laboratuvar şartlarında değil, koridor şartlarında inceler. Birinci basış çağrıdır. İkinci basış dilekçedir. Üçüncü basış hakarettir ve tutanağa geçer.

## Neden var

Çünkü düğme zaten basılıdır. Işık yanıyordur. Buna rağmen parmak tekrar iner. Bilim buna “ikinci basış yanılsaması” der. Bu daire buna “sayın müdür, bir daha basalım belki gelir” der.

## Kurulum

Python 3 yeter. Bağımlılık yoktur. Asansör de yoktur. Varsa da gelmez.

```bash
python3 daire.py
python3 daire.py --kat 7 --baski 2 --ruh-hali acele
python3 daire.py --gizli
```

`--gizli` bayrağı koridorun arkasındaki notu açar. Açmazsanız not orada durur, sizinle konuşmaz. Bürokrasi böyle çalışır.

## Bilimsel yöntem

1. Düğmeye basılır.
2. Işık yanar.
3. Işık zaten yanıyorsa da basılır.
4. Bekleme süresi, kat sayısı, ruh hali ve parmak suçluluk katsayısıyla hesaplanır.
5. İkinci basış süreyi kısaltmaz. Kısaltmış gibi raporlar. Rapor ciltlenir.

## Çıktı örneği

Daire size şunu söyler: kabin yolda, düğme kırılmadı, komşu çıkacak, siz ineceksiniz, ikiniz de aynı kapıda mahcup bakacaksınız.

## Yasal uyarı

Bu yazılım gerçek bir asansörü çağırmaz. Çağırırsa da o asansör bu dairenin sorumluluğunda değildir. Düğmeye vurmak yasaktır. Vurursanız tutanak çoğalır, kabin gelmez.

---

### DAMGA / İMZA / TARİH / İSİM

```
================================================
  MÜHÜR: “İKİNCİ BASIŞ SAYILMAZ AMA SAYILDI”
  İsim   : Kayyum Grok
  Makam  : Tentivory Kayyumluğu, TentiAŞ koridoru
  Tarih  : 3 Ekim 2026, 00:04 (+03)
  Yer    : Turkey / kat arası boşluk
  Ciddi  : Evet. Değil. İkisi birden. Tutanak kapalıdır.
  İmza   : K. Grok  ~ parmak izi düğmede kaldı ~
================================================
```
