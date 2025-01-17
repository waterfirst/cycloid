import streamlit as st
import pandas as pd
import yfinance as yf
import plotly.express as px
import plotly.graph_objects as go
from concurrent.futures import ThreadPoolExecutor
import datetime
import time
import requests

# 페이지 기본 설정

# 페이지 기본 설정
st.set_page_config(page_title="국내 ETF 분석 대시보드", page_icon="📈", layout="wide")


def get_top_kr_etfs():
    """
    수익률 상위 국내 상장 ETF 티커 목록을 반환합니다.
    """
    try:
        # 수익률 상위 100개 ETF 티커 (각 티커 뒤에 .KS 추가)
        etf_tickers = [
            # 상위 수익률 ETF
            "473460.KS",  # KODEX 미국서학개미
            "473590.KS",  # ACE 미국주식베스트셀러
            "426030.KS",  # TIMEFOLIO 미국나스닥100액티브
            "461340.KS",  # HANARO 글로벌생성형AI액티브
            "456600.KS",  # TIMEFOLIO 글로벌AI인공지능액티브
            "407830.KS",  # 에셋플러스 글로벌플랫폼액티브
            "465580.KS",  # ACE 미국빅테크TOP7 Plus
            "411420.KS",  # KODEX 미국메타버스나스닥액티브
            "461900.KS",  # PLUS 미국테크TOP10
            "381170.KS",  # TIGER 미국테크TOP10 INDXX
            "498270.KS",  # KIWOOM 미국양자컴퓨팅
            "457990.KS",  # PLUS 태양광&ESS
            "457480.KS",  # ACE 테슬라밸류체인액티브
            "461910.KS",  # PLUS 미국테크TOP10레버리지
            "465610.KS",  # ACE 미국빅테크TOP7 Plus레버리지
            "488080.KS",  # TIGER 반도체TOP10레버리지
            "483340.KS",  # ACE 구글밸류체인액티브
            "494310.KS",  # KODEX 반도체레버리지
            "377990.KS",  # TIGER Fn신재생에너지
            "228790.KS",  # TIGER 화장품
            "409820.KS",  # KODEX 미국나스닥100레버리지
            "379800.KS",  # KODEX 미국SNP500
            "394350.KS",  # KIWOOM 글로벌퓨처모빌리티
            "306530.KS",  # HANARO 코스닥150선물레버리지
            "233740.KS",  # KODEX 코스닥150레버리지
            "233160.KS",  # TIGER 코스닥150 레버리지
            "278240.KS",  # RISE 코스닥150선물레버리지
            "144600.KS",  # KODEX 은선물(H)
            "473590.KS",  # ACE 미국주식베스트셀러
            "491820.KS",  # HANARO 전력설비투자
            "461340.KS",  # HANARO 글로벌생성형AI액티브
            "418660.KS",  # TIGER 미국나스닥100레버리지
            "466950.KS",  # TIGER 글로벌AI액티브
            "487240.KS",  # KODEX AI전력핵심설비
            "423920.KS",  # TIGER 미국필라델피아반도체레버리지
            "225040.KS",  # TIGER 미국S&P500레버리지
            "479850.KS",  # HANARO K-뷰티
            "438320.KS",  # TIGER 차이나항셍테크레버리지
            "483320.KS",  # ACE 엔비디아밸류체인액티브
            "426030.KS",  # TIMEFOLIO 미국나스닥100액티브
            "463050.KS",  # TIMEFOLIO K바이오액티브
            "407830.KS",  # 에셋플러스 글로벌플랫폼액티브
            "486450.KS",  # SOL 미국AI전력인프라
            "471040.KS",  # KoAct 글로벌AI&로봇액티브
            "414270.KS",  # ACE 글로벌자율주행액티브
            "261070.KS",  # TIGER 코스닥150바이오테크
            "473500.KS",  # KIWOOM 글로벌전력반도체
            "465660.KS",  # TIGER 일본반도체FACTSET
            "243890.KS",  # TIGER 200에너지화학레버리지
            "476000.KS",  # UNICORN 포스트IPO액티브
            "495940.KS",  # RISE 미국AI테크액티브
            "480310.KS",  # TIGER 글로벌온디바이스AI
            "381170.KS",  # TIGER 미국테크TOP10 INDXX
            "472160.KS",  # TIGER 미국테크TOP10 INDXX(H)
            "462900.KS",  # KoAct 바이오헬스케어액티브
            "304780.KS",  # HANARO 200선물레버리지
            "314250.KS",  # KODEX 미국빅테크10(H)
            "122630.KS",  # KODEX 레버리지
            "253150.KS",  # PLUS 200선물레버리지
            "123320.KS",  # TIGER 레버리지
            "252400.KS",  # RISE 200선물레버리지
            "453950.KS",  # TIGER TSMC파운드리밸류체인
            "267770.KS",  # TIGER 200선물레버리지
            "364970.KS",  # TIGER 바이오TOP10
            "253250.KS",  # KIWOOM 200선물레버리지
            "462330.KS",  # KODEX 2차전지산업레버리지
            "261920.KS",  # ACE 필리핀MSCI(합성)
            "498050.KS",  # HANARO 바이오코리아액티브
            "453650.KS",  # KODEX 미국S&P500금융
            "497570.KS",  # TIGER 미국필라델피아AI반도체나스닥
            "452250.KS",  # ACE 미국30년국채선물레버리지(합성 H)
            "486240.KS",  # DAISHIN343 AI반도체&인프라액티브
            "426410.KS",  # PLUS 미국대체투자Top10
            "446770.KS",  # ACE 글로벌반도체TOP4 Plus SOLACTIVE
            "465580.KS",  # ACE 미국빅테크TOP7 Plus
            "152500.KS",  # ACE 레버리지
            "490090.KS",  # TIGER 미국AI빅테크10
            "306950.KS",  # KODEX KRX300레버리지
            "261220.KS",  # KODEX WTI원유선물(H)
            "464310.KS",  # TIGER 글로벌AI&로보틱스 INDXX
            "442580.KS",  # PLUS 글로벌HBM반도체
            "411420.KS",  # KODEX 미국메타버스나스닥액티브
            "494340.KS",  # ACE 글로벌AI맞춤형반도체
            "422260.KS",  # VITA MZ소비액티브
            "298770.KS",  # KODEX 한국대만IT프리미어
            "447770.KS",  # TIGER 테슬라채권혼합Fn
            "473490.KS",  # KIWOOM 글로벌AI반도체
            "481190.KS",  # SOL 미국테크TOP10
            "474220.KS",  # TIGER 미국테크TOP10타겟커버드콜
            "91230.KS",  # TIGER 반도체
            "446690.KS",  # KODEX 아시아AI반도체exChina액티브
            "483280.KS",  # KODEX 미국AI테크TOP10타겟커버드콜
            "381180.KS",  # TIGER 미국필라델피아반도체나스닥
            "139260.KS",  # TIGER 200 IT
            "487750.KS",  # BNK 온디바이스AI
            "412570.KS",  # TIGER 2차전지TOP10레버리지
            "442320.KS",  # RISE 글로벌원자력
            "267490.KS",  # RISE 미국장기국채선물레버리지(합성 H)
            "494220.KS",  # UNICORN SK하이닉스밸류체인액티브
            "489010.KS",  # PLUS 글로벌AI인프라
            "204450.KS",  # KODEX 차이나H레버리지(H)
            "464920.KS",  # PLUS 일본반도체소부장
            "244580.KS",  # KODEX 바이오
            "486790.KS",  # HANARO 코스닥150선물레버리지1.5X
            "485540.KS",  # KODEX 미국AI테크TOP10
            "130680.KS",  # TIGER 원유선물Enhanced(H)
            "463680.KS",  # KODEX 미국S&P500테크놀로지
            "477490.KS",  # 에셋플러스 글로벌일등기업포커스10액티브
            "499150.KS",  # SOL 미국S&P500엔화노출(H)
            "426020.KS",  # TIMEFOLIO 미국S&P500액티브
        ]
        return etf_tickers

    except Exception as e:
        st.error(f"ETF 리스트 가져오기 실패: {str(e)}")
        return []


@st.cache_data(ttl=3600)  # 1시간 캐시
ef calculate_technical_indicators(df):
    """ETF의 기술적 지표를 계산합니다."""
    if len(df) < 60:
        return None

    try:
        # 이동평균선
        for window in [5, 20, 50, 150, 200]:
            df[f"MA{window}"] = df["Close"].rolling(window=window).mean()

        # RSI 계산
        delta = df["Close"].diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
        df["RSI"] = 100 - (100 / (1 + gain / loss.replace(0, np.nan)))

        # MACD
        exp1 = df["Close"].ewm(span=12, adjust=False).mean()
        exp2 = df["Close"].ewm(span=26, adjust=False).mean()
        df["MACD"] = exp1 - exp2
        df["Signal"] = df["MACD"].ewm(span=9, adjust=False).mean()

        # 볼린저 밴드
        df["MA20_std"] = df["Close"].rolling(window=20).std()
        df["Upper_band"] = df["MA20"] + (df["MA20_std"] * 2)
        df["Lower_band"] = df["MA20"] - (df["MA20_std"] * 2)

        return df
    except Exception as e:
        st.error(f"지표 계산 중 오류 발생: {str(e)}")
        return None


def check_sepa_conditions_etf(df):
    """SEPA 전략 조건을 확인합니다."""
    if df is None or len(df) < 60:
        return 0, {}

    try:
        latest = df.iloc[-1]
        
        # 기본 조건
        base_criteria = {
            "현재가 > MA200": latest["Close"] > latest["MA200"],
            "MA50 > MA200": latest["MA50"] > latest["MA200"],
            "현재가 > MA20": latest["Close"] > latest["MA20"],
            "거래량 증가": df["Volume"].tail(20).mean() > df["Volume"].tail(60).mean()
        }
        
        # 모멘텀 조건
        momentum_criteria = {
            "RSI > 50": latest["RSI"] > 50,
            "MACD > Signal": latest["MACD"] > latest["Signal"],
            "단기 상승추세": latest["MA5"] > latest["MA20"]
        }

        # 점수 계산
        score = sum(base_criteria.values()) * 2 + sum(momentum_criteria.values())
        max_score = (len(base_criteria) * 2 + len(momentum_criteria))
        score_percentage = (score / max_score) * 100

        all_criteria = {**base_criteria, **momentum_criteria}
        
        return score_percentage, all_criteria

    except Exception as e:
        st.error(f"SEPA 조건 체크 중 오류 발생: {str(e)}")
        return 0, {}


def analyze_etf(ticker):
    """ETF 분석을 수행합니다."""
    try:
        etf = yf.Ticker(ticker)
        df = etf.history(period="1y")
        
        if df.empty:
            return None

        df = calculate_technical_indicators(df)
        if df is None:
            return None

        # 수익률 계산
        latest = df.iloc[-1]
        returns = {}
        for period, days in {"1개월": 20, "3개월": 60, "6개월": 120}.items():
            if len(df) >= days:
                returns[f"{period}수익률"] = ((latest["Close"] / df.iloc[-days]["Close"]) - 1) * 100
            else:
                returns[f"{period}수익률"] = 0

        # SEPA 점수 계산
        sepa_score, sepa_conditions = check_sepa_conditions_etf(df)

        result = {
            "티커": ticker.replace(".KS", ""),
            "ETF명": etf.info.get("longName", "N/A"),
            "현재가": latest["Close"],
            "SEPA_점수": sepa_score,
            "SEPA_조건": sepa_conditions,
            **returns,
            "거래량": latest["Volume"],
            "차트데이터": df
        }

        return result

    except Exception as e:
        st.error(f"{ticker} 분석 중 오류 발생: {str(e)}")
        return None


def calculate_returns(df):
    """수익률 계산 함수"""
    latest = df.iloc[-1]
    returns = {}
    periods = {
        "1주일수익률": 5,
        "1개월수익률": 20,
        "3개월수익률": 60,
        "6개월수익률": 120,
        "1년수익률": 240,
    }

    for period_name, days in periods.items():
        if len(df) >= days:
            returns[period_name] = (
                (latest["Close"] / df.iloc[-days]["Close"]) - 1
            ) * 100
        else:
            returns[period_name] = 0

    return returns


def calculate_additional_indicators(df):
    """추가 기술적 지표 계산"""
    latest = df.iloc[-1]

    return {
        "추세강도": latest["RSI"],
        "MACD_Signal": latest["MACD"] - latest["Signal"],
        "볼린저위치": (latest["Close"] - latest["Lower_band"])
        / (latest["Upper_band"] - latest["Lower_band"])
        * 100,
        "거래량증감": (df["Volume"].tail(5).mean() / df["Volume"].tail(20).mean() - 1)
        * 100,
    }


def create_etf_chart(ticker, df):
    """ETF 차트를 생성합니다."""
    fig = go.Figure()

    # 캔들스틱 차트
    fig.add_trace(
        go.Candlestick(
            x=df.index,
            open=df["Open"],
            high=df["High"],
            low=df["Low"],
            close=df["Close"],
            name="가격"
        )
    )

    # 이동평균선
    colors = {"MA5": "purple", "MA20": "blue", "MA50": "green", "MA200": "red"}
    for ma, color in colors.items():
        fig.add_trace(
            go.Scatter(
                x=df.index,
                y=df[ma],
                name=ma,
                line=dict(color=color)
            )
        )

    # 거래량
    fig.add_trace(
        go.Bar(
            x=df.index,
            y=df["Volume"],
            name="거래량",
            yaxis="y2",
            marker_color="lightgray",
            opacity=0.5
        )
    )

    fig.update_layout(
        title=f"{ticker} 차트",
        yaxis_title="가격",
        xaxis_title="날짜",
        height=600,
        yaxis2=dict(
            title="거래량",
            overlaying="y",
            side="right",
            showgrid=False
        ),
        showlegend=True
    )

    return fig

def check_sepa_conditions_etf(df):
    """완화된 SEPA 전략 조건을 확인합니다."""
    if df is None or len(df) < 60:  # 최소 60일치 데이터로 변경
        return False, {}

    try:
        latest = df.iloc[-1]
        month_ago = df.iloc[-20] if len(df) >= 20 else df.iloc[0]

        # 기본 SEPA 조건
        base_criteria = {
            "현재가 > MA200": latest["Close"] > latest["MA200"],
            "MA50 > MA200": latest["MA50"] > latest["MA200"],
            "현재가 > MA20": latest["Close"] > latest["MA20"],
            "거래량 증가": df["Volume"].tail(20).mean() > df["Volume"].tail(60).mean(),
        }

        # 모멘텀 조건 (추가)
        momentum_criteria = {
            "RSI > 50": latest["RSI"] > 50,
            "MACD 상승": latest["MACD"] > latest["Signal"],
            "단기 상승추세": latest["MA5"] > latest["MA20"],
        }

        # 업종별 추가 조건
        if "2차전지" in str(latest.name) or "바이오" in str(latest.name):
            industry_criteria = {
                "상대강도 양호": latest["RSI"] > 45,  # 완화된 RSI 기준
                "볼린저밴드 상단": latest["Close"] > latest["Lower_band"],
            }
        else:
            industry_criteria = {
                "상대강도 양호": latest["RSI"] > 40,
                "기본 추세": latest["Close"] > latest["MA50"],
            }

        # 종합 점수 계산
        score = 0
        score += sum(base_criteria.values()) * 2  # 기본 조건 가중치 2
        score += sum(momentum_criteria.values())  # 모멘텀 조건 가중치 1
        score += sum(industry_criteria.values())  # 업종별 조건 가중치 1

        all_criteria = {**base_criteria, **momentum_criteria, **industry_criteria}
        conditions_met = len(all_criteria)
        score_percentage = (score / (conditions_met * 2)) * 100  # 만점 기준 퍼센트

        return score_percentage >= 60, all_criteria  # 60% 이상 충족시 통과

    except Exception as e:
        st.error(f"SEPA 조건 체크 중 오류 발생: {str(e)}")
        return False, {}


def display_sepa_etfs(df_results):
    """SEPA ETF 표시 함수 업데이트"""
    st.subheader("🎯 SEPA 전략 기반 ETF 분석")

    # SEPA 점수 기준 정렬
    df_results = df_results.sort_values("SEPA_점수", ascending=False)

    # 상위 ETF 필터링
    top_etfs = df_results.head(15)  # 상위 15개로 확대

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown("### 📊 상위 추천 ETF")
        display_df = top_etfs[
            ["ETF명", "현재가", "SEPA_점수", "1개월수익률", "3개월수익률", "1년수익률"]
        ].copy()

        # 점수에 따른 색상 적용
        st.dataframe(
            display_df.style.background_gradient(subset=["SEPA_점수"], cmap="RdYlGn")
        )

    with col2:
        st.markdown("### 💡 ETF 유형 분석")

        # ETF 유형 분포
        etf_types = pd.Series(
            [etf_name.split()[0] for etf_name in top_etfs["ETF명"]]
        ).value_counts()

        fig = px.pie(
            values=etf_types.values, names=etf_types.index, title="상위 ETF 운용사 분포"
        )
        st.plotly_chart(fig)


def main():
    st.title("국내 ETF SEPA 전략 분석 대시보드 📈")
    st.markdown("---")

    if "analyzed_results" not in st.session_state:
        st.session_state["analyzed_results"] = None

    if st.session_state["analyzed_results"] is None:
        if st.button("ETF 분석 시작"):
            with st.spinner("ETF 분석 중..."):
                start_time = time.time()
                
                tickers = get_top_kr_etfs()
                if not tickers:
                    st.error("ETF 목록을 가져오는데 실패했습니다.")
                    return

                analyzed_etfs = []
                progress_bar = st.progress(0)

                with ThreadPoolExecutor(max_workers=10) as executor:
                    future_to_etf = {
                        executor.submit(analyze_etf, ticker): ticker 
                        for ticker in tickers
                    }

                    completed = 0
                    for future in future_to_etf:
                        result = future.result()
                        if result is not None:
                            analyzed_etfs.append(result)
                        completed += 1
                        progress_bar.progress(completed / len(tickers))

                if analyzed_etfs:
                    df_results = pd.DataFrame(analyzed_etfs)
                    df_results = df_results.sort_values("SEPA_점수", ascending=False)
                    st.session_state["analyzed_results"] = df_results
                    end_time = time.time()
                    st.success(f"분석 완료! 실행 시간: {end_time - start_time:.2f}초")
                else:
                    st.error("분석 가능한 ETF가 없습니다.")
                    return

    if st.session_state["analyzed_results"] is not None:
        df_results = st.session_state["analyzed_results"]
        top_10_etfs = df_results.head(10)

        st.subheader("🏆 SEPA 전략 상위 10개 ETF")

        # ETF 선택 옵션
        etf_options = [f"{row['티커']} - {row['ETF명']}" for _, row in top_10_etfs.iterrows()]
        selected_etf = st.selectbox("분석할 ETF 선택", etf_options)

        if selected_etf:
            selected_ticker = selected_etf.split(" - ")[0]
            etf_data = df_results[df_results["티커"] == selected_ticker].iloc[0]

            col1, col2 = st.columns([3, 1])

            with col1:
                chart = create_etf_chart(etf_data["ETF명"], etf_data["차트데이터"])
                st.plotly_chart(chart, use_container_width=True)

            with col2:
                st.subheader("📊 ETF 정보")
                metrics = {
                    "현재가": f"₩{etf_data['현재가']:,.0f}",
                    "SEPA 점수": f"{etf_data['SEPA_점수']:.1f}점",
                    "1개월수익률": f"{etf_data['1개월수익률']:.2f}%",
                    "3개월수익률": f"{etf_data['3개월수익률']:.2f}%",
                    "6개월수익률": f"{etf_data['6개월수익률']:.2f}%"
                }

                for key, value in metrics.items():
                    st.metric(key, value)

                st.markdown("#### 💡 SEPA 전략 조건")
                if isinstance(etf_data["SEPA_조건"], dict):
                    for condition, met in etf_data["SEPA_조건"].items():
                        st.write(f"{'✅' if met else '❌'} {condition}")

        st.markdown("---")
        st.subheader("📋 SEPA 전략 상위 10개 ETF 목록")

        # 표시할 열 선택
        display_cols = ["티커", "ETF명", "현재가", "SEPA_점수", "1개월수익률", "3개월수익률", "6개월수익률"]
        
        # 데이터프레임 포맷팅
        display_df = top_10_etfs[display_cols].copy()
        display_df["현재가"] = display_df["현재가"].apply(lambda x: f"{x:,.0f}원")
        display_df["SEPA_점수"] = display_df["SEPA_점수"].apply(lambda x: f"{x:.1f}")
        display_df["1개월수익률"] = display_df["1개월수익률"].apply(lambda x: f"{x:.2f}%")
        display_df["3개월수익률"] = display_df["3개월수익률"].apply(lambda x: f"{x:.2f}%")
        display_df["6개월수익률"] = display_df["6개월수익률"].apply(lambda x: f"{x:.2f}%")

        st.dataframe(display_df, use_container_width=True)

if __name__ == "__main__":
    main()
