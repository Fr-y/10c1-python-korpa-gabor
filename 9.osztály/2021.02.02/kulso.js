// // első feladat


// // x = parseFloat(prompt("Add meg az érdemjegyet"));
// // y = prompt("Add meg az osztályzatot")

// // switch (x) {
// //     case 1:
// //         document.write(x + "-es elégtelen <br>");
// //         break;
// //     case 2:
// //         document.write(x + "-es elégséges <br>");
// //         break;
// //     case 3:
// //         document.write(x + "-as közepes <br>");
// //         break;
// //     case 4:
// //         document.write(x + "-es jó <br>");
// //         break;
// //     case 5:
// //         document.write(x + "-ös jeles <br>");
// //         break;
// //     default:
// //         document.write("Nem érdemjegyet adtál meg <br>");
// // }

// // switch (y) {
// //     case "elégtelen":
// //         document.write(y + " az egyes <br>");
// //         break;
// //     case "elégséges":
// //         document.write(y + " az kettes <br>");
// //         break;
// //     case "közepes":
// //         document.write(y + " az hármas <br>");
// //         break;
// //     case "jó":
// //         document.write(y + " az négyes <br>");
// //         break;
// //     case "jeles":
// //         document.write(y + " az ötös <br>");
// //         break;
// //     default:
// //         document.write("Nem osztályzatot adtál meg <br>");
// // }


// második feladat

// x = parseFloat(prompt("Hanyadik hónap van?"))

// switch (x) {
//     case 1:
//         document.write("Január")
//         break;
//     case 2:
//         document.write("Február")
//         break;
//     case 3:
//         document.write("Március")
//         break;
//     case 4:
//         document.write("Április")
//         break;
//     case 5:
//         document.write("Május")
//         break;
//     case 6:
//         document.write("Június")
//         break;
//     case 7:
//         document.write("Július")
//         break;
//     case 8:
//         document.write("Augusztus")
//         break;
//     case 9:
//         document.write("Szeptember")
//         break;
//     case 10:
//         document.write("Október")
//         break;
//     case 11:
//         document.write("November")
//         break;
//     case 12:
//         document.write("December")
//         break;
//     default:
//         document.write("Nem jól adtad meg")
// }



// harmadik feladat

x = parseFloat(prompt("Hanyadik hónap van?"))

switch (x) {
    case 12, 1, 2:
        document.write("Tél")
        break;

    case 3, 4, 5:
        document.write("Tavasz")
        break;

    case 6, 7, 8:
        document.write("Nyár")
        break;

    case 9, 10, 11:
        document.write("Ősz")
        break;
}