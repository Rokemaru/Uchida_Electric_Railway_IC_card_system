# UchicaCardクラス:ICカードのチャージ残高を管理するクラス
class UchicaCard:
    def __init__(self):
        # 初期チャージ残高は500円
        self.balance = 500

    # 運賃を支払うための関数
    def pay(self, fare: int) -> int:

        # 残高不足の場合、自動チャージを繰り返す（3000円ずつ）
        if fare > self.balance:
            print(f"チャージ残高は{self.balance}円です。")
            print("残高不足です。")
            while fare > self.balance:
                self.balance += 3000
                print("3000円自動チャージします。")
            # 運賃を残高から差し引く
            self.balance -= fare
            print(f"精算後のチャージ残高は{self.balance}円です。")
        else:
            # 運賃を残高から差し引く
            self.balance -= fare
            print(f"チャージ残高は{self.balance}円です。")

        # 精算後の残高が500円未満ならもう一度自動チャージ
        if self.balance < 500:
            self.balance += 3000
            print("残高が500円未満のため3000円自動チャージします。")
            print(f"チャージ残高は{self.balance}円です。")

        return self.balance  # 処理後の残高を返す

    # ユーザーによるチャージ処理
    def charge(self) -> int:
        # チャージ可能な金額リスト（1000円〜10000円まで）
        charges = [1000 * (i + 1) for i in range(10)]
        print("\n【チャージ機能】\n")
        print(f"チャージ残高は{self.balance}円です。\n")

        # チャージ金額の選択肢を表示
        for i in range(len(charges)):
            print(f"{i + 1}:{charges[i]}円")

        print("\nチャージする金額を選択してください。(キャンセルする場合には99を入力)")

        while True:

            try:
                selection = int(input())

                # 正しい番号を入力したとき
                if 1 <= selection <= 10:
                    amount = charges[selection - 1]
                    print(f"{amount}円チャージします。")
                    self.balance += amount
                    print(f"チャージ残高は{self.balance}円です。")
                    return self.balance

                # キャンセルを選んだとき
                elif selection == 99:
                    print("チャージをキャンセルしました。")
                    return self.balance

                else:
                    print("正しい数値を入力してください。")

            except ValueError:
                # 数字以外が入力されたときのエラー
                print("正しい数値を入力してください。")


# ユーザーが使いたい機能を選ぶメニュー
def menu() -> int:
    functions = ["乗車駅選択", "チャージ機能"]
    print("\n【ウチダ電鉄 交通系ICカード検証システム】\n")

    # メニュー選択肢を表示
    for i in range(len(functions)):
        print(f"{i + 1}: {functions[i]}")

    print("\n使用する機能を入力してください(終了する場合には99を入力)")

    while True:

        try:
            choice = int(input())

            # 入力値が 1〜2 または 99 のときはそのまま返す
            if choice in range(1, len(functions) + 1) or choice == 99:
                return choice
            else:
                print("正しい数値を入力してください。")

        except ValueError:
            print("正しい数値を入力してください。")


# 乗車駅を選択する関数（キャンセル時は0を返す）
def select_station() -> int:
    stations = ["秋葉原", "山梨", "長野"]
    fares = [133, 4128, 7990]
    print("\n【乗車駅選択】\n")

    # 駅ごとの料金を表示
    for i in range(len(stations)):
        print(f"{i + 1}:{stations[i]}駅から\t{fares[i]}円")

    print("\n乗車した駅を入力してください（キャンセルする場合には99を入力)")

    while True:

        try:
            destination = int(input())

            # キャンセル時
            if destination == 99:
                print("駅の選択をキャンセルしました。")
                return 0

            # 正しい駅番号が入力された場合
            elif 1 <= destination <= len(stations):
                station_name = stations[destination - 1]
                fare = fares[destination - 1]
                print(f"\n乗車駅は{station_name}で運賃は{fare}円です。")
                return fare

            else:
                print("正しい数値を入力してください。")

        except ValueError:
            print("正しい数値を入力してください。")


# 全体の処理の流れを管理する関数
def main():
    card = UchicaCard()  # インスタンス化

    while True:
        choice = menu()  # 機能選択

        if choice == 1:
            fare = select_station()
            if fare != 0:
                card.pay(fare)

        elif choice == 2:
            card.charge()

        elif choice == 99:
            print("システムを終了します")
            break


# メイン関数を直接実行されたときだけ呼び出す
if __name__ == "__main__":
    main()
