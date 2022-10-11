def isBitSet (num, bitNum):
    num //= 2 ** (bitNum)
    return bool(num % 2)

for n in range(0b111 + 1):
    x = isBitSet(n, 0)
    y = isBitSet(n, 1)
    z = isBitSet(n, 2)
    print(f"X: {int(x)} Y: {int(y)} Z: {int(z)}", end = "")
    print(f"     Expr. result: {int(not(x or y or z) == (not x and not y and not z))}")