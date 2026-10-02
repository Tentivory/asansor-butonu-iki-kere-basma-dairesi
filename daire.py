#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Asansör Düğmesine İki Kere Basma Dairesi.

Gerçekten çalışır. Asansör gerçekten gelmez.
Gizli not yalnızca --gizli ile açılır.
"""

from __future__ import annotations

import argparse
import base64
import hashlib
import random
import textwrap

# Koridor arkasi not. Duz metin degil. Merak eden --gizli der.
_GIZLI = (
    "YmzDvGx0w7xuIHBhcnRpbGVyIGF5bsSxIGFzYW5zw7Zyw7xuIGJla2xpeW9yOyAi
    "ZMO8xJ9tZSBpa2luY2kgYmFzLWxhbmNhIGtpbXNlIGlubWl5b3IsIGhlcmtlcyDDp2lr"
    "xLFyb3Igc2FuxLFyb3IuIEthYmluIGdlbG1leg=="
)


def gizli_not() -> str:
    ham = base64.b64decode("".join(_GIZLI.split())).decode("utf-8")
    return ham


def bekleme_saniye(kat: int, baski: int, ruh: str) -> tuple[float, float, str]:
    """Birinci basış gerçek süre, ikinci basış resmi süre.

    İkinci basış psikolojik olarak kısaltır, fiziksel olarak uzatır.
    Formül kasıtlı olarak saçmadır ve deterministiktir.
    """
    tohum = hashlib.sha256(f"{kat}|{baski}|{ruh}|ABD-2".encode()).hexdigest()
    random.seed(int(tohum[:8], 16))
    taban = 4.0 + kat * 1.7 + random.uniform(0.2, 1.4)
    if ruh == "acele":
        taban += 3.0  # acele eden katta asansör küsülür
    elif ruh == "felsefi":
        taban += 8.0  # düşünen kat değiştirir
    elif ruh == "sakin":
        taban -= 1.0
    gercek = max(2.0, taban)
    # İkinci ve sonraki basışlar süreyi kısaltmaz; raporda kısalmış gösterilir.
    resmi = max(0.4, gercek - (baski - 1) * 1.25)
    if baski >= 3:
        hukum = "Üçüncü basış hakaret sayıldı. Kabin darıldı, bir kat aşağıda bekliyor."
        gercek += 2.5
    elif baski == 2:
        hukum = "İkinci basış dilekçe olarak işleme alındı. Işık zaten yanıyordu."
    else:
        hukum = "Birinci basış çağrıdır. Henüz drama yok."
    return round(gercek, 2), round(resmi, 2), hukum


def tutanak(kat: int, baski: int, ruh: str) -> str:
    gercek, resmi, hukum = bekleme_saniye(kat, baski, ruh)
    fark = round(gercek - resmi, 2)
    satirlar = [
        "ASANSÖR DÜĞMESİNE İKİ KERE BASMA DAİRESİ",
        "Tutanak no: ABD-2 / 2026-10-03",
        "-" * 46,
        f"Kat              : {kat}",
        f"Baskı sayısı     : {baski}",
        f"Ruh hali        : {ruh}",
        f"Gerçek bekleme   : {gercek} sn",
        f"Resmi bekleme   : {resmi} sn",
        f"Makas farkı     : {fark} sn (rapor lehine kırpıldı)",
        f"Hüküm           : {hukum}",
        "Kabin durumu    : yolda, değil, yolda göründü, değil",
        "Komşu ihtimali  : yüksek. Aynı anda çıkacaksınız. Mahcup bakış zorunlu.",
        "-" * 46,
        "Sonuç: İkinci basış asansörü hızlandırmaz.",
        "       İkinci basış yurttaşı hızlandırmış gibi hissettirir.",
        "       Daire bunu yeterli bulmuştur.",
    ]
    return "\n".join(satirlar)


def main() -> None:
    p = argparse.ArgumentParser(description="İkinci basış dairesi tutanak motoru")
    p.add_argument("--kat", type=int, default=4, help="Beklenen kat (varsayılan 4)")
    p.add_argument("--baski", type=int, default=2, help="Düğmeye kaç kez basıldı")
    p.add_argument(
        "--ruh-hali",
        default="acele",
        choices=["acele", "sakin", "felsefi", "küs"],
        help="Koridordaki ruh hali",
    )
    p.add_argument("--gizli", action="store_true", help="Koridor arkası notu aç")
    a = p.parse_args()
    if a.kat < 0:
        print("Bodrum katı daire yetkisindedir ama asansör oraya inmez, çıkar.")
    print(tutanak(a.kat, max(1, a.baski), a.ruh_hali))
    if a.gizli:
        print()
        print("KORİDOR ARKASI NOT (çözüldü, ciltlenmedi):")
        print(textwrap.fill(gizli_not(), width=68))
    print()
    print("DAMGA: Kayyum Grok | 3 Ekim 2026 | ikinci basış sayıldı, gelmedi.")


if __name__ == "__main__":
    main()
