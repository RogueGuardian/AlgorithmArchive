int nonRecursiveGCD(int a, int b){
    // Return 0 if a or b are invald
    if(a < 1 || b < 1){
        return 0;
    }

    // Case where one of the values is 1
    if(a == 1 || b == 1){
        return 1;
    }

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
    // Return 0 if a or b are invald
    if(a < 1 || b < 1){
        return 0;
    }

    if(b == 0){
        return a
    }
    return recursiveGCD(b, a % b)
}
