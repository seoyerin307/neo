onmessage = function(e) {
    let ouput = 0;
    let input = parseInt(e.data.input);
    let i = 2;
    while (i <= input) {
        if (input % i == 0) 
            break;
        else
        i++;
    }
    output = input
    output += (input == i) ? " is Primenumber" : " is not Primenumber";
    postMessage(output);
}
