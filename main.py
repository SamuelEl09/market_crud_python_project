def totalCost (checkout_list):
    totalPrice = sum(item['qty'] * item['harga'] for item in checkout_list)
    print(f"Total pembayaran: {totalPrice}")
    
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

def show_menu(x):
    print("Selamat Datang di Pasar Buah")
    print()

    for key, value in x.items():
        print(f"{key}. {value}")

def show_fruits(fruits):
    print("Daftar Buah")
    print()
    print("Index\t|Nama\t\t|Stock\t|Harga")

    for index, fruit in enumerate(fruits):
        print(f"{index}\t|{fruit['nama']}\t\t|{fruit['stock']}\t|{fruit['harga']}")

def add_fruits(fruit_name, fruit_stock, fruit_price, fruits):
    new_fruits_add = {"nama":fruit_name,
                      "stock":fruit_stock,
                      "harga":fruit_price}
    
    fruits.append(new_fruits_add)
    show_fruits(fruits)

def remove_fruits(fruit_removed, fruits):
    fruits.pop(fruit_removed)
    show_fruits(fruits)

def checkout_fruits(fruits_index, fruits_stock, fruits, checkout_list):
    if fruits_index < 0 or fruits_index >= len(fruits):
        print(f"Index {fruits_index} tidak tersedia")
        return

    if fruits[fruits_index]['stock'] < fruits_stock:
        print(f"Stok tidak cukup, stok {fruits[fruits_index]['nama']} tinggal {fruits[fruits_index]['stock']}")
        return

    cart = {
        "index": fruits_index,
        "qty": fruits_stock,
        "harga": fruits[fruits_index]['harga']
    }
    checkout_list.append(cart)

    print("Index\t|Stock\t|Harga")
    for char in checkout_list:
        print(f"{char['index']}\t|{char['qty']}\t|{char['harga']}")

    return checkout_list
def main():

    list_of_fruits = [
        {"nama": "Apel", "stock": 20, "harga": 10000},
        {"nama": "Jeruk", "stock": 15, "harga": 15000},
        {"nama": "Anggur", "stock": 25, "harga": 20000}
    ]

    menu = {
        1: "Menampilkan fruits",
        2: "Menambah fruits",
        3: "Menghapus fruits",
        4: "Membeli fruits",
        5: "Exit Program"
    }

    checkout = []

    while True:
        show_menu(menu)
        print()

        try:
            x = int(input("Masukkan angka Menu yang ingin dijalankan: "))
            if x > 5:
                raise ValueError(f"Menu {x} tidak tersedia")
            print()
        except ValueError as e:
            print("Terjadi Kesalahan:", e)
            continue

        if x == 1:
            show_fruits(list_of_fruits)
            print()

        elif x == 2:
            fruit_name = str(input("Masukkan Nama Buah\t: "))
            fruit_stock = int(input("Masukkan Stock Buah\t: "))
            fruit_price = int(input("Masukkan Harga Buah\t: "))
            add_fruits(fruit_name, fruit_stock, fruit_price, list_of_fruits)
            print()

        elif x == 3:
            fruit_removed = int(input("Masukkan index Buah yang ingin dihapus\t: "))
            remove_fruits(fruit_removed, list_of_fruits)
            print()

        elif x == 4:
            show_fruits(list_of_fruits)
            print()

            while True:
                fruits_index = int(input("Masukkan index Buah yang ingin dibeli\t: "))
                fruits_stock = int(input("Masukkan jumlah yang ingin dibeli\t: "))

                checkout = checkout_fruits(fruits_index, fruits_stock, list_of_fruits, checkout)

                user_input = input("Mau beli yang lain? (ya/tidak): ").strip().lower()
                if user_input == 'tidak':
                    total = totalCost(checkout)

                    totalCash = int(input("\nMasukkan jumlah uang : "))

                    payment(total,totalCash)

                    checkout = []  # Reset checkout list for future purchases
                    print()
                    break
                elif user_input == 'ya':
                    continue
                else:
                    print("Input tidak valid. Silakan masukkan 'ya' atau 'tidak'.")

        elif x == 5:
            break

main()