function uzemanyagszamitas() {
    km = parseFloat(uzemanyag.km.value);
    l = parseFloat(uzemanyag.mennyiseg.value);

    f = l / km * 100
    document.getElementById("e").innerHTML = Math.round(f);
}

function osszegszamitas() {
    jegy1 = parseFloat(jegyek.jegy1.value) * 1000;
    jegy2 = parseFloat(jegyek.jegy2.value) * 1500;
    jegy3 = parseFloat(jegyek.jegy3.value) * 2000;

    vegosszeg = jegy1 + jegy2 + jegy3
    document.getElementById("ossz").innerHTML = Math.round(vegosszeg);
}