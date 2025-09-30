"""使用例"""

import os
from analyzer import analyze_central_bank_statement, batch_analyze_statements

# 環境変数からAPIキーを取得
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEYが設定されていません。環境変数に設定してください。")

# サンプルの声明文
statement = """
日本銀行は本日、政策委員会・金融政策決定会合において、以下のとおり決定した。

1. 長短金利操作（イールドカーブ・コントロール）について、無担保コールレート（オーバーナイト物）を
   -0.1%程度で推移するよう促すとともに、10年物国債金利がゼロ%程度で推移するよう、上限を設けず必要な金額の
   長期国債の買入れを行う。

2. わが国の景気は、緩やかに回復している。実質GDPは、2023年度は前年比+1.8%、2024年度は+1.2%と見込まれる。

3. 消費者物価の前年比は、エネルギー価格の上昇などから、2023年度は+2.5%、2024年度は+1.9%と見込まれる。
   物価安定の目標である2%の実現を目指す。
"""

print("=== 単一の声明文を分析 ===")
print()

# 分析実行
markdown_output = analyze_central_bank_statement(statement, api_key)
print(markdown_output)

print()
print("=== 複数の声明文を一括分析 ===")
print()

# 複数の声明文を一括処理する例
statements = [
    {
        "date": "2024-01-23",
        "text": statement
    },
    # 他の声明文を追加可能
]

results = batch_analyze_statements(statements, api_key)

for result in results:
    print(f"\n分析日: {result['date']}")
    print(result['markdown'])
    print("\n" + "="*50 + "\n")
