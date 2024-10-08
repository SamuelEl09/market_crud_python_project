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

def payment (price, cash):
    if (price > cash):
        i = price - cash
        print(f"Transaksi anda dibatalkan uangnya kurang sebesar {i}")
    elif(price < cash):
        i = cash - price
        print("Terima Kasih\n")
        print(f"Uang kembali anda : {i}")
    else:
        print("Terima Kasih")

def validateInput(x):
    while True:
        try:
            return int(input(x))
        except ValueError:
            print("Input tidak valid. Silahkan masukkan angka.")

def checkStock(product, quantity, dataStock):
    if product in dataStock and quantity <= dataStock[product]:
        return True
    else:
        return False

def getQuantity(x, dataStock, product):
    while True:
        quantity = validateInput(x)
        if checkStock(product, quantity, dataStock):
            return quantity
        else:
            print(f"Stok {product} tidak mencukupi. Stok yang tersedia: {dataStock[product]}.")

def main():

    fruitsStock = {
        "apple": 20,
        "orange": 5,
        "grapes": 10
    }

    apple = getQuantity("Masukkan Jumlah Apel : ", fruitsStock, "apple")
    orange = getQuantity("Masukkan Jumlah Jeruk : ", fruitsStock, "orange")
    grapes = getQuantity("Masukkan Jumlah Anggur : ", fruitsStock, "grapes")

    print("\nDetail Belanja")

    total = totalCost(apple, orange, grapes)

    print(f"\nTotal : {total}")

    totalCash = validateInput("\nMasukkan jumlah uang : ")

    payment(total,totalCash)

main()