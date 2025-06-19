class UchicaCard:
    def __init__(self):
        self.balance = 500

    def pay(self, fare: int) -> int:
        print(f"チャージ残高は{self.balance}円です。")
        if fare > self.balance:
            print("残高不足です。")
            while fare > self.balance:
                self.balance += 3000
                print("3000円自動チャージします。")
        self.balance -= fare
        print(f"精算後のチャージ残高は{self.balance}円です。")
        if self.balance < 500:
            self.balance += 3000
            print("残高が500円未満のため3000円自動チャージします。")
            print(f"チャージ残高は{self.balance}円です。")
        return self.balance

    def charge(self) -> int:
        charges = [1000 * (i + 1) for i in range(10)]
        while True:
            print("\n【チャージ機能】\n")
            print(f"チャージ残高は{self.balance}円です。\n")
            for i in range(len(charges)):
                print(f"{i + 1}:{charges[i]}円")
            print(
                "\nチャージする金額を選択してください。(キャンセルする場合には99を入力)"
            )
            try:
                selection = int(input())
                if 1 <= selection <= 10:
                    amount = charges[selection - 1]
                    print(f"{amount}円チャージします。")
                    self.balance += amount
                    print(f"チャージ残高は{self.balance}円です。")
                    return self.balance
                elif selection == 99:
                    print("チャージをキャンセルしました。")
                    return self.balance
                else:
                    print("正しい数値を入力してください。")
            except ValueError:
                print("正しい数値を入力してください。")


def menu() -> int:
    functions = ["乗車駅選択", "チャージ機能"]
    while True:
        print("\n【ウチダ電鉄 交通系ICカード検証システム】\n")
        for i in range(len(functions)):
            print(f"{i + 1}: {functions[i]}")
        print("\n使用する機能を入力してください(終了する場合には99を入力)")
        try:
            choice = int(input())
            if choice in range(1, len(functions) + 1) or choice == 99:
                return choice
            else:
                print("正しい数値を入力してください。")
        except ValueError:
            print("正しい数値を入力してください。")


def select_station() -> int:
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]
    while True:
        print("\n【乗車駅選択】\n")
        for i in range(len(stations)):
            print(f"{i + 1}:{stations[i]}駅から {fares[i]}円")
        print("\n乗車した駅を入力してください（キャンセルする場合には99を入力)")
        try:
            destination = int(input())
            if destination == 99:
                print("駅の選択をキャンセルしました。")
                return 0
            elif 1 <= destination <= len(stations):
                station_name = stations[destination - 1]
                fare = fares[destination - 1]
                print(f"\n乗車駅は{station_name}で運賃は{fare}円です。")
                return fare
            else:
                print("正しい数値を入力してください。")
        except ValueError:
            print("正しい数値を入力してください。")


def main():
    card = UchicaCard()
    while True:
        choice = menu()
        if choice == 1:
            fare = select_station()
            if fare != 0:
                card.pay(fare)
        elif choice == 2:
            card.charge()
        elif choice == 99:
            print("システムを終了します")
            break


if __name__ == "__main__":
    main()
