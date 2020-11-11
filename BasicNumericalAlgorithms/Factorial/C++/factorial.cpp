int nonRecursiveFactorial(int n){
    int fact = 1;
    while(n != 0){
        fact *= n;
        n--;
    }
    return fact;
}

int recursiveFactorial(int n){
    if(n == 1){
        return 1
    }
    return n * recursiveFact(n-1)
}
