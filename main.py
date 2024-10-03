def totalCost (x, y, z):
    applePrice = 10_000
    orangePrice = 15_000
    grapesPrice = 20_000

    totalApplePrice = x * applePrice
    totalOrangePrice = y * orangePrice
    totalGrapesPrice = z * grapesPrice

    print(f"\nApel : {x} x {applePrice} = {totalApplePrice}")
    print(f"Jeruk : {y} x {orangePrice} = {totalOrangePrice}")
    print(f"Anggur : {z} x {grapesPrice} = {totalGrapesPrice}")

    totalPrice = totalApplePrice + totalGrapesPrice + totalOrangePrice

    return totalPrice

def inputInteger(x):
    while True:
        try:
            return int(input(x))
        except ValueError:
            print("Input tidak valid. Silahkan masukan Angka")


def main():
    apple = inputInteger("Masukkan Jumlah Apel : ")
    orange = inputInteger("Masukkan Jumlah Jeruk : ")
    grapes = inputInteger("Masukkan Jumlah Anggur : ")

    print("\nDetail Belanja")

    total = totalCost(apple, orange, grapes)

    print(f"\nTotal : {total}")

main()