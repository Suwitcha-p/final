"""
Digital Threat Intelligence Dashboard
Main Application Entrypoint
"""

import os
import streamlit as st
import pandas as pd

from components.header import render_header
from tabs.tab1_overview import render_tab1
from tabs.tab2_ai_risk import render_tab2
from tabs.tab3_disinformation import render_tab3
from tabs.tab4_online_scam import render_tab4

# Page Configuration
st.set_page_config(
    page_title="Digital Threat Intelligence Dashboard",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load CSS
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
css_path = os.path.join(BASE_DIR, "assets", "style.css")
if os.path.exists(css_path):
    with open(css_path, "r", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


@st.cache_data(show_spinner="กำลังโหลดฐานข้อมูลภัยคุกคามดิจิทัล...")
def load_all_datasets():
    cache_dir = os.path.join(BASE_DIR, "data", "cache")
    
    # If cache does not exist, run preprocessor
    ai_cache = os.path.join(cache_dir, "ai_incidents.parquet")
    if not os.path.exists(ai_cache):
        from data.preprocessor import run_full_pipeline
        run_full_pipeline()
        
    df_ai = pd.read_parquet(os.path.join(cache_dir, "ai_incidents.parquet"))
    df_fotn = pd.read_parquet(os.path.join(cache_dir, "freedom_on_the_net.parquet"))
    df_eu = pd.read_parquet(os.path.join(cache_dir, "euvsdisinfo.parquet"))
    df_afnc = pd.read_parquet(os.path.join(cache_dir, "afnc_items.parquet"))
    df_acsc = pd.read_parquet(os.path.join(cache_dir, "acsc_weekly.parquet"))
    df_panel = pd.read_parquet(os.path.join(cache_dir, "weekly_panel.parquet"))
    
    return df_ai, df_fotn, df_eu, df_afnc, df_acsc, df_panel


def main():
    # Load Data
    try:
        df_ai, df_fotn, df_eu, df_afnc, df_acsc, df_panel = load_all_datasets()
    except Exception as e:
        st.error(f"❌ เกิดข้อผิดพลาดในการโหลดข้อมูล: {e}")
        st.stop()

    # Render Header
    render_header()

    # Sidebar Navigation
    with st.sidebar:
        st.markdown("### 🧭 เมนูการนำทาง (Navigation)")
        st.caption("เลือกระบบวิเคราะห์ภัยคุกคามตามมิติข้อมูล:")
        
        selected_tab = st.radio(
            "เลือกแท็บการวิเคราะห์:",
            [
                "TAB 1: ภาพรวมภัยคุกคาม (Overview)",
                "TAB 2: ความเสี่ยงจาก AI และเสรีภาพเน็ต (AI & Digital Risk)",
                "TAB 3: การวิเคราะห์ข่าวปลอม (Disinformation)",
                "TAB 4: สถิติคดีหลอกลวงออนไลน์ (Online Scam)"
            ],
            index=0
        )
        
        st.markdown("---")
        st.markdown("### 📁 ฐานข้อมูลในระบบ (Active Telemetry)")
        st.markdown(f"""
        - 🤖 **AI Incidents:** `{len(df_ai):,}` เหตุการณ์
        - 🌐 **Freedom on the Net:** `{df_fotn['country'].nunique()}` ประเทศ
        - 📰 **EUvsDisinfo:** `{len(df_eu):,}` บทความ
        - 🇹🇭 **AFNC (ไทย):** `{len(df_afnc):,}` โพสต์
        - 💸 **ACSC (ไทย):** `{len(df_acsc)}` สัปดาห์
        """)
        
        st.markdown("---")
        st.caption("🔒 **Enterprise Threat Intelligence Platform**<br>เวอร์ชัน 1.0.0 | รองรับการทำงานแบบ Full-Stack", unsafe_allow_html=True)

    # Route to selected Tab
    if "TAB 1" in selected_tab:
        render_tab1(df_ai, df_fotn, df_eu, df_afnc, df_acsc, df_panel)
    elif "TAB 2" in selected_tab:
        render_tab2(df_ai, df_fotn)
    elif "TAB 3" in selected_tab:
        render_tab3(df_eu, df_afnc)
    elif "TAB 4" in selected_tab:
        render_tab4(df_acsc, df_panel)


if __name__ == "__main__":
    main()
