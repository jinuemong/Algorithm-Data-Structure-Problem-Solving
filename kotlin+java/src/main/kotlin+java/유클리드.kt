
// a>b
fun gcd(a: Int, b: Int): Int {
    var x = a
    var y = b
    while (y!=0){
        val temp = x % y
        x = y
        y = temp
    }
    return x
}
