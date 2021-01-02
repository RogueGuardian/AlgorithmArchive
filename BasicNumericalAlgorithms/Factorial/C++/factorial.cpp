int nonRecursiveFactorial(int n){
    // Returning -1 when n is not valid
    if(n < 0){
        return -1;
    }

    int fact = 1;
    while(n != 0){
        fact *= n;
        n--;
    }
    return fact;
}

int recursiveFactorial(int n){
    // Returning -1 when n is not valid
    if(n < 0){
        return -1;
    }

    if(n == 0){
        return 1;
    }
    return n * recursiveFact(n-1);
}
