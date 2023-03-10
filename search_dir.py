# 使い方
# python3 search_dir.py [検索パス] [検索ワード] [出力ファイル]
# python3 search_dir.py ./sample/ "staging.ERROR" debug_all.log
import os
import sys

# 引数から検索するディレクトリパス、検索するキーワード、出力するファイル名を取得する
search_directory = sys.argv[1]
search_keyword = sys.argv[2]
output_file = sys.argv[3]

# ファイル出力用のファイルハンドルを開く
output_handle = open(output_file, "w")

# 検索対象のファイルを検索する
for root, dirs, files in os.walk(search_directory):
    for file in files:
        # ファイルパスを作成する
        file_path = os.path.join(root, file)
        # ファイルを開く
        with open(file_path, "r") as file_handle:
            # ファイルの中身を読み込む
            file_content = file_handle.read()
            # キーワードを検索する
            if search_keyword in file_content:
                # ファイルパスをファイルに書き込む
                output_handle.write(file_path + "\n")

# ファイルハンドルを閉じる
output_handle.close()

# 処理完了メッセージを表示する
print("検索が完了しました。結果は " + output_file + " に出力されています。")