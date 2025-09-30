"""中央銀行声明文の分析関数"""

import outlines
from typing import List
from models import CentralBankStatementAnalysis


def analyze_central_bank_statement(statement_text: str, api_key: str) -> str:
    """
    中央銀行の声明文を分析し、構造化されたMarkdownを返す
    
    Args:
        statement_text: 分析する声明文のテキスト
        api_key: OpenAI APIキー
    
    Returns:
        Markdown形式の分析結果
    """
    model = outlines.models.openai("gpt-4", api_key=api_key)
    generator = outlines.generate.json(model, CentralBankStatementAnalysis)
    
    prompt = f"""
以下の中央銀行の声明文を分析し、指定された形式で情報を抽出してください。

声明文:
{statement_text}

各項目について、声明文から該当する情報を抽出してください。
情報が見つからない場合はnullを返してください。
"""
    
    result = generator(prompt)
    return convert_to_markdown(result)


def convert_to_markdown(analysis: CentralBankStatementAnalysis) -> str:
    """
    分析結果をMarkdown形式に変換
    
    Args:
        analysis: 分析結果のPydanticモデル
    
    Returns:
        Markdown形式の文字列
    """
    md = f"""# {analysis.central_bank_name} 金融政策声明分析

**発表日**: {analysis.statement_date}

## 総括

{analysis.summary}

---

## 🏦 政策金利

"""
    
    # 政策金利情報
    if analysis.policy_rate.current_rate:
        md += f"**現在の金利**: {analysis.policy_rate.current_rate}\n\n"
    if analysis.policy_rate.rate_change:
        md += f"**金利変更**: {analysis.policy_rate.rate_change}\n\n"
    if analysis.policy_rate.change_rationale:
        md += f"**変更理由**:\n{analysis.policy_rate.change_rationale}\n\n"
    if analysis.policy_rate.future_outlook:
        md += f"**今後の見通し**:\n{analysis.policy_rate.future_outlook}\n\n"
    
    # 経済成長情報
    md += "---\n\n## 📈 経済成長\n\n"
    if analysis.economic_growth.gdp_growth_rate:
        md += f"**GDP成長率**: {analysis.economic_growth.gdp_growth_rate}\n\n"
    if analysis.economic_growth.growth_drivers:
        md += f"**成長要因**:\n{analysis.economic_growth.growth_drivers}\n\n"
    if analysis.economic_growth.risk_factors:
        md += f"**リスク要因**:\n{analysis.economic_growth.risk_factors}\n\n"
    if analysis.economic_growth.outlook:
        md += f"**展望**:\n{analysis.economic_growth.outlook}\n\n"
    
    # インフレ情報
    md += "---\n\n## 💰 インフレーション\n\n"
    if analysis.inflation.current_inflation:
        md += f"**現在の物価水準**: {analysis.inflation.current_inflation}\n\n"
    if analysis.inflation.inflation_target:
        md += f"**物価目標**: {analysis.inflation.inflation_target}\n\n"
    if analysis.inflation.price_trend:
        md += f"**物価動向**:\n{analysis.inflation.price_trend}\n\n"
    if analysis.inflation.inflation_outlook:
        md += f"**物価見通し**:\n{analysis.inflation.inflation_outlook}\n\n"
    
    return md


def process_statement_file(file_path: str, api_key: str, output_path: str) -> str:
    """
    声明文ファイルを読み込んで分析し、Markdownファイルとして保存
    
    Args:
        file_path: 入力ファイルのパス
        api_key: OpenAI APIキー
        output_path: 出力ファイルのパス
    
    Returns:
        Markdown形式の分析結果
    """
    # 声明文を読み込む
    with open(file_path, 'r', encoding='utf-8') as f:
        statement_text = f.read()
    
    # 分析実行
    markdown_output = analyze_central_bank_statement(statement_text, api_key)
    
    # Markdownファイルとして保存
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(markdown_output)
    
    print(f"分析完了: {output_path}")
    return markdown_output


def batch_analyze_statements(statements: List[dict], api_key: str) -> List[dict]:
    """
    複数の声明文を一括で分析
    
    Args:
        statements: [{'date': '2024-01-23', 'text': '...'}, ...]
        api_key: OpenAI APIキー
    
    Returns:
        [{'date': '2024-01-23', 'markdown': '...', 'data': {...}}, ...]
    """
    results = []
    
    model = outlines.models.openai("gpt-4", api_key=api_key)
    generator = outlines.generate.json(model, CentralBankStatementAnalysis)
    
    for statement in statements:
        prompt = f"""
以下の中央銀行の声明文を分析し、指定された形式で情報を抽出してください。

声明文:
{statement['text']}

各項目について、声明文から該当する情報を抽出してください。
"""
        
        analysis = generator(prompt)
        markdown = convert_to_markdown(analysis)
        
        results.append({
            "date": statement['date'],
            "markdown": markdown,
            "data": analysis.model_dump()
        })
    
    return results
