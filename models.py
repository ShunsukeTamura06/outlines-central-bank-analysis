"""中央銀行声明分析用のPydanticモデル定義"""

from pydantic import BaseModel, Field
from typing import Optional, List


class PolicyRateInfo(BaseModel):
    """政策金利に関する情報"""
    current_rate: Optional[str] = Field(description="現在の政策金利（例: 0.5%）")
    rate_change: Optional[str] = Field(description="金利の変更内容（据え置き、引き上げ、引き下げ）")
    change_rationale: Optional[str] = Field(description="金利決定の理由や背景")
    future_outlook: Optional[str] = Field(description="将来の金利政策の方向性")


class EconomicGrowthInfo(BaseModel):
    """経済成長に関する情報"""
    gdp_growth_rate: Optional[str] = Field(description="実質GDP成長率の見通しや実績")
    growth_drivers: Optional[str] = Field(description="経済成長の主な要因")
    risk_factors: Optional[str] = Field(description="成長を阻害する可能性のあるリスク")
    outlook: Optional[str] = Field(description="今後の経済成長の見通し")


class InflationInfo(BaseModel):
    """インフレーションに関する情報"""
    current_inflation: Optional[str] = Field(description="現在のインフレ率（CPI等）")
    inflation_target: Optional[str] = Field(description="中央銀行の物価安定目標")
    price_trend: Optional[str] = Field(description="物価の上昇・下落傾向")
    inflation_outlook: Optional[str] = Field(description="今後の物価動向の予測")


class CentralBankStatementAnalysis(BaseModel):
    """中央銀行声明文の分析結果"""
    statement_date: str = Field(description="声明が発表された日付")
    central_bank_name: str = Field(description="中央銀行の名称")
    policy_rate: PolicyRateInfo = Field(description="政策金利に関する情報")
    economic_growth: EconomicGrowthInfo = Field(description="経済成長に関する情報")
    inflation: InflationInfo = Field(description="インフレーションに関する情報")
    summary: str = Field(description="声明全体の要約（2-3文）")


# より詳細な分析が必要な場合のモデル

class RateDecisionFactors(BaseModel):
    """金利決定の背景要因"""
    domestic_factors: Optional[List[str]] = Field(description="国内の経済要因")
    international_factors: Optional[List[str]] = Field(description="海外の経済要因")
    market_conditions: Optional[List[str]] = Field(description="金融市場の動向")


class DetailedCentralBankAnalysis(BaseModel):
    """詳細な中央銀行声明分析"""
    statement_date: str = Field(description="声明が発表された日付")
    central_bank_name: str = Field(description="中央銀行の名称")
    
    # 政策金利
    policy_rate_current: Optional[str] = Field(description="現在の政策金利")
    policy_rate_change: Optional[str] = Field(description="金利の変更内容")
    rate_decision_background: RateDecisionFactors = Field(description="金利決定の背景要因")
    
    # 経済成長
    real_gdp_current_year: Optional[str] = Field(description="当年度の実質GDP成長率見通し")
    real_gdp_next_year: Optional[str] = Field(description="翌年度の実質GDP成長率見通し")
    growth_drivers: Optional[List[str]] = Field(description="成長の牽引要因")
    downside_risks: Optional[List[str]] = Field(description="下方リスク")
    
    # インフレ
    current_cpi: Optional[str] = Field(description="現在の消費者物価指数")
    cpi_yoy: Optional[str] = Field(description="CPIの前年比")
    inflation_target: Optional[str] = Field(description="インフレ目標")
    inflation_drivers: Optional[List[str]] = Field(description="物価上昇の要因")
    inflation_outlook_current_year: Optional[str] = Field(description="当年度の物価見通し")
    inflation_outlook_next_year: Optional[str] = Field(description="翌年度の物価見通し")
    
    # その他
    exchange_rate_comment: Optional[str] = Field(description="為替レートに関する言及")
    employment_situation: Optional[str] = Field(description="雇用・賃金動向")
    key_points: List[str] = Field(description="特に注目すべきポイント3つ")
