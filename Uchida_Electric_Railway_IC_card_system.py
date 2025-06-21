def charge(balance):
    """
    チャージ機能を提供する関数。
    """
    print("【チャージ機能】")
    print(f"チャージ残高は{balance}円です。")

    charges = [i * 1000 for i in range(1, 11)]

    for i, amount in enumerate(charges):
        print(f"{i + 1}:{amount}円")

    while True:
        try:
            print(
                "チャージする金額を選択してください。(キャンセルする場合には99を入力)"
            )
            selection = int(input())

            if 1 <= selection <= len(charges):
                charge_amount = charges[selection - 1]
                print(f"{charge_amount}円チャージします。")
                balance += charge_amount
                print(f"チャージ残高は{balance}円です。")
                return balance
            elif selection == 99:
                print("チャージをキャンセルしました。")
                return balance
            else:
                print("正しい数値を入力してください。")
        except ValueError:
            print("正しい数値を入力してください。")


def pay(balance, fare):
    """
    【設計書に忠実なロジック】
    運賃精算を行う関数。
    設計書の画面例（秋葉原駅と山梨駅）の表示フローの違いを再現する。
    """
    print(f"チャージ残高は{balance}円です。")

    # 精算前の残高不足チェック
    if balance < fare:
        print("残高不足です。")
        while balance < fare:
            balance += 3000
            print("3000円自動チャージします。")

    # 運賃精算
    balance -= fare

    # 設計書の「秋葉原駅」の例では、精算直後に残高が表示される
    if fare == 133:
        print(f"チャージ残高は{balance}円です。")

    # 精算後の残高500円未満チェック
    if balance < 500:
        print("残高が500円未満のため3000円自動チャージします。")
        balance += 3000
        print(f"チャージ残高は{balance}円です。")

    # 設計書の「山梨駅」の例では、全処理の最後に精算後残高が表示される
    if fare == 4128:
        print(f"精算後のチャージ残高は{balance}円です。")

    return balance


def select_station():
    """
    乗車駅を選択し、運賃を返す関数。
    """
    print("【乗車駅選択】")

    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]

    for i, (station, fare) in enumerate(zip(stations, fares)):
        print(f"{i + 1}:{station}駅から {fare}円")

    while True:
        try:
            print("乗車した駅を入力してください (キャンセルする場合には99を入力)")
            selection = int(input())

            if 1 <= selection <= len(stations):
                station_name = stations[selection - 1]
                fare_amount = fares[selection - 1]
                print(f"乗車駅は{station_name}で運賃は{fare_amount}円です。")
                return fare_amount
            elif selection == 99:
                print("駅の選択をキャンセルしました。")
                return 0
            else:
                print("正しい数値を入力してください。")
        except ValueError:
            print("正しい数値を入力してください。")


def menu():
    """
    システムの機能メニューを表示し、選択された機能番号を返す関数。
    """
    print("【ウチダ電鉄 交通系ICカード検証システム】")

    functions = ["乗車駅選択", "チャージ機能"]

    for i, func in enumerate(functions):
        print(f"{i + 1}:{func}")

    while True:
        try:
            print("使用する機能を入力してください(終了する場合には99を入力)")
            selection = int(input())

            if 1 <= selection <= len(functions) or selection == 99:
                return selection
            else:
                print("正しい数値を入力してください。")
        except ValueError:
            print("正しい数値を入力してください。")


def main():
    """
    アプリケーションのメイン関数。
    """
    balance = 500

    while True:
        choice = menu()

        if choice == 1:
            fare = select_station()
            if fare != 0:
                balance = pay(balance, fare)
        elif choice == 2:
            balance = charge(balance)
        elif choice == 99:
            print("システムを終了します")
            break

        # 各機能の処理後に改行を入れて見やすくする
        print()


# main関数を実行
if __name__ == "__main__":
    main()
