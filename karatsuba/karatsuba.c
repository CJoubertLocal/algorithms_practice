#include <stdio.h>
#include <math.h>

long long karatsuba(long long int_one, long long int_two);
int numberOfDigitsInLongLong(long long int_in, int acc);

int main() {
    printf("starting\n");
    printf("%d, %d, %d\n", karatsuba(12, 345), 12*345, karatsuba(12, 345) == 12*345);
    return 0;
}

long long karatsuba(long long int_one, long long int_two) {
    // TODO: Overflow problem?
    if ((-10 < int_one && int_one < 10) || (-10 < int_two && int_two < 10)) {
        return int_one * int_two;
    }

    int negativeMultiplier = 1;
    long long abs_one = int_one;
    if (int_one < 0) {
        abs_one *= -1;
        negativeMultiplier *= -1;
    }
    long long abs_two = int_two;
    if (int_two < 0) {
        abs_two *= -1;
        negativeMultiplier *= -1;
    }

    int len_one = numberOfDigitsInLongLong(abs_one, 1);
    int len_two = numberOfDigitsInLongLong(abs_two, 1);
    int indexToSplitOneOn = len_one / 2;
    int indexToSplitTwoOn = len_two / 2;

    if (len_one < len_two) {
        indexToSplitTwoOn = len_two - indexToSplitOneOn;
    } else if (len_one < len_two) {
        indexToSplitOneOn = len_one - indexToSplitTwoOn;
    }

    long long a = abs_one / (long long) pow(10, indexToSplitOneOn);
    long long b = abs_one % (long long) pow(10, indexToSplitOneOn);
    long long c = abs_two / (long long) pow(10, indexToSplitOneOn);
    long long d = abs_two % (long long) pow(10, indexToSplitOneOn);

    long long ac = a * c;
    long long bd = b * d;
    long long leftOver = karatsuba(a + b, c + d) - ac - bd;

    int multiplier = (len_one - indexToSplitOneOn > len_two - indexToSplitTwoOn) ? len_one - indexToSplitOneOn : len_two - indexToSplitTwoOn;

    return (long long) (ac * pow(pow(10, multiplier), 2) + leftOver * pow(10, multiplier) + bd) * negativeMultiplier;
}

int numberOfDigitsInLongLong(long long int_in, int acc) {
    if (int_in < 0) {
        return numberOfDigitsInLongLong(int_in * -1, acc);
    }

    if (int_in < 10) {
        return acc;
    }

    return numberOfDigitsInLongLong(int_in / 10, acc + 1);
}
