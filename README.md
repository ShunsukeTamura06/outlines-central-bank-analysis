# Central Bank Statement Analysis with Outlines

LLMを使って中央銀行の声明文から政策金利・経済成長・インフレーション情報を構造化して抽出し、Markdown形式で出力するツールです。

## 特徴

- **構造化出力**: Outlinesライブラリを使用して、LLMの出力を確実に構造化
- **Pydanticモデル**: 型安全な方法で情報を抽出
- **Markdown出力**: 読みやすい形式で分析結果を出力
- **OpenAI API対応**: GPT-4などの最新モデルを使用可能

## インストール

```bash
pip install -r requirements.txt
```

## 必要な環境変数

```bash
export OPENAI_API_KEY="your-api-key-here"
```

## 使い方

### 基本的な使い方

```python
from analyzer import analyze_central_bank_statement
import os

statement = """
日本銀行は本日、政策委員会・金融政策決定会合において、以下のとおり決定した。

1. 長短金利操作について、無担保コールレート（オーバーナイト物）を
   -0.1%程度で推移するよう促す。

2. わが国の景気は、緩やかに回復している。実質GDPは、
   2023年度は前年比+1.8%、2024年度は+1.2%と見込まれる。

3. 消費者物価の前年比は、エネルギー価格の上昇などから、
   2023年度は+2.5%、2024年度は+1.9%と見込まれる。
"""

api_key = os.getenv("OPENAI_API_KEY")
markdown_output = analyze_central_bank_statement(statement, api_key)
print(markdown_output)
```

### ファイルから読み込んで処理

```python
from analyzer import process_statement_file
import os

api_key = os.getenv("OPENAI_API_KEY")
result = process_statement_file(
    file_path="examples/sample_statement.txt",
    api_key=api_key,
    output_path="output/analysis.md"
)
```

### 複数の声明を一括処理

```python
from analyzer import batch_analyze_statements
import os

statements = [
    {"date": "2024-01-23", "text": "..."},
    {"date": "2024-03-19", "text": "..."},
]

api_key = os.getenv("OPENAI_API_KEY")
results = batch_analyze_statements(statements, api_key)

for result in results:
    filename = f"output/analysis_{result['date']}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(result['markdown'])
```

## データモデル

### CentralBankStatementAnalysis

中央銀行声明文の分析結果を格納するメインモデル。

- `statement_date`: 声明の発表日
- `central_bank_name`: 中央銀行名
- `policy_rate`: 政策金利情報
- `economic_growth`: 経済成長情報
- `inflation`: インフレ情報
- `summary`: 全体の要約

### PolicyRateInfo

政策金利に関する情報。

- `current_rate`: 現在の政策金利
- `rate_change`: 金利の変更内容
- `change_rationale`: 変更理由
- `future_outlook`: 今後の見通し

### EconomicGrowthInfo

経済成長に関する情報。

- `gdp_growth_rate`: GDP成長率
- `growth_drivers`: 成長要因
- `risk_factors`: リスク要因
- `outlook`: 展望

### InflationInfo

インフレーションに関する情報。

- `current_inflation`: 現在のインフレ率
- `inflation_target`: 物価目標
- `price_trend`: 物価動向
- `inflation_outlook`: 物価見通し

## 出力例

```markdown
# 日本銀行 金融政策声明分析

**発表日**: 2024年1月23日

## 総括

日本銀行は政策金利を-0.1%で据え置き、10年物国債金利をゼロ%程度に誘導する方針を継続。
景気は緩やかに回復しており、物価は2%前後で推移する見通し。

---

## 🏦 政策金利

**現在の金利**: -0.1%

**金利変更**: 据え置き

**変更理由**:
物価安定の目標の実現には、なお時間を要すると判断。引き続き金融緩和を継続する必要がある。

---

## 📈 経済成長

**GDP成長率**: 2023年度+1.8%、2024年度+1.2%

---

## 💰 インフレーション

**現在の物価水準**: 前年比+2.5%（2023年度見込み）

**物価目標**: 2%
```

## プロジェクト構成

```
outlines-central-bank-analysis/
├── README.md
├── requirements.txt
├── .gitignore
├── models.py              # Pydanticモデル定義
├── analyzer.py            # 分析メイン関数
├── example.py             # 使用例
├── examples/
│   └── sample_statement.txt
└── output/                # 出力ディレクトリ（.gitignoreで除外）
```

## ライセンス

MIT License

## 参考リンク

- [Outlines Documentation](https://outlines-dev.github.io/outlines/)
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [Pydantic Documentation](https://docs.pydantic.dev/)
