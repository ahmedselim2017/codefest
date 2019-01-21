function processData(input) {
    let satirlar = input.split("\r\n");
    let status = true;
    satirlar.map((satir, index) => {
        let degerler = satir.split(" "); 
        let degerler2 = satir.split(" "); 
        degerler.map((deger) => {
            degerler2.shift();
            if(degerler2.indexOf(deger) > -1) {
                status = false;
            }
        })
    })
    
    if(status) console.log('DOGRU');
    else console.log('YANLIS')
} 

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
    _input += input;
});

process.stdin.on("end", function () {
   processData(_input);
});
