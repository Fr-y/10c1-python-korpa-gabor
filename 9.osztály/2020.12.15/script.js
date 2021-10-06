function szamitas() {
    nev = elso.nev.value
    document.getElementById("proba").innerHTML = "Helló " + nev;
}

function negyzet() {
    a = parseFloat(Negyzet.oldal.value);
    k = 4 * a;
    t = a * a;
    t = Math.pow(a, 2)

    document.getElementById("n").innerHTML = "A négyzet kerülete: " + k + "<br/>" + "A négyzet területe: " + t;
}


function kor() {
    r = parseFloat(Kor.sugar.value);
    k = 2 * r * Math.PI;
    t = Math.pow(r, 2) * Math.PI;

    document.getElementById("m").innerHTML = "A kör kerülete: " + k + "<br/>" + "A kör területe: " + t;
}

function teglalap1() {
    a = parseFloat(Teglalap.aoldal.value);
    b = parseFloat(Teglalap.boldal.value);

    k = 2 * a + 2 * b;
    t = a * b;

    document.getElementById("tlap").innerHTML = "A téglalap kerülete: " + k + "<br/>" + "A téglalap területe:" + t;
}