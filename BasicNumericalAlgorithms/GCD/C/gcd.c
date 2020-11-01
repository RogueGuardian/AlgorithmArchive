int nonRecursiveGCD(int a, int b){
    while(a != b){
        if(a > b){
            a -= b
        } else {
            b -= a
        }
    }
    return a
}

int recursiveGCD(int a, int b){
    if(b == 0){
        return a
    }
    return recursiveGCD(b, a%b)
}
