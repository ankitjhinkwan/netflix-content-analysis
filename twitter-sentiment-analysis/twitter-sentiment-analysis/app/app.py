"""
🩸 TWITTER SENTIMENT ANALYZER — BLOOD & FIRE EDITION 🩸
Black & Red Theme | Glitch + Drip + Fire + Pulse Effects
Author: Ankit Jinkwan
Portfolio: https://ankitjhinkwan.github.io/portfolio/
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import os, warnings
warnings.filterwarnings('ignore')

st.set_page_config(
    page_title="🩸 Twitter Sentiment Analyzer",
    page_icon="🩸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── FULL BLACK & RED CSS WITH ALL 4 EFFECTS ───────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Rajdhani:wght@400;600;700&family=Share+Tech+Mono&display=swap');

/* ── BASE ── */
.stApp {
    background-color: #0a0000 !important;
    background-image: radial-gradient(ellipse at top, #1a0000 0%, #0a0000 70%);
    overflow-x: hidden;
}

/* ── FIRE PARTICLE BACKGROUND ── */
.fire-container {
    position: fixed;
    bottom: 0; left: 0;
    width: 100%; height: 100%;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}
.particle {
    position: absolute;
    bottom: -20px;
    width: 6px; height: 6px;
    border-radius: 50%;
    animation: rise linear infinite;
    opacity: 0;
}
@keyframes rise {
    0%   { transform: translateY(0) scale(1);   opacity: 0.8; }
    50%  { transform: translateY(-40vh) scale(1.5); opacity: 0.4; }
    100% { transform: translateY(-80vh) scale(0);   opacity: 0; }
}

/* ── BLOOD DRIP ── */
.drip-container {
    position: fixed;
    top: 0; left: 0;
    width: 100%; height: 60px;
    pointer-events: none;
    z-index: 100;
}
.drip {
    position: absolute;
    top: 0;
    width: 4px;
    background: linear-gradient(to bottom, #8b0000, #ff0000, transparent);
    border-radius: 0 0 50% 50%;
    animation: drip-fall linear infinite;
    opacity: 0.7;
}
@keyframes drip-fall {
    0%   { height: 0px;  opacity: 0.9; top: 0; }
    60%  { height: 60px; opacity: 0.7; }
    100% { height: 80px; opacity: 0;   top: 5px; }
}

/* ── GLITCH TITLE ── */
.glitch-title {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 3.5rem;
    color: #ff0000;
    text-align: center;
    position: relative;
    letter-spacing: 8px;
    text-shadow: 0 0 20px #ff0000, 0 0 40px #ff0000;
    animation: glitch-main 4s infinite;
}
.glitch-title::before {
    content: attr(data-text);
    position: absolute;
    left: 0; top: 0;
    width: 100%;
    color: #ff0000;
    text-align: center;
    animation: glitch-before 4s infinite;
    clip-path: polygon(0 0, 100% 0, 100% 35%, 0 35%);
    text-shadow: -3px 0 #00ffff;
    opacity: 0.8;
}
.glitch-title::after {
    content: attr(data-text);
    position: absolute;
    left: 0; top: 0;
    width: 100%;
    color: #ff0000;
    text-align: center;
    animation: glitch-after 4s infinite;
    clip-path: polygon(0 65%, 100% 65%, 100% 100%, 0 100%);
    text-shadow: 3px 0 #ff00ff;
    opacity: 0.8;
}
@keyframes glitch-main {
    0%,89%,100% { transform: translate(0); filter: none; }
    90%  { transform: translate(-2px, 1px); filter: hue-rotate(90deg); }
    92%  { transform: translate(2px, -1px); filter: hue-rotate(-90deg); }
    94%  { transform: translate(0); }
}
@keyframes glitch-before {
    0%,89%,100% { transform: translate(0); }
    90% { transform: translate(-4px, 2px); }
    92% { transform: translate(4px, -2px); }
    94% { transform: translate(0); }
}
@keyframes glitch-after {
    0%,89%,100% { transform: translate(0); }
    90% { transform: translate(4px, -2px); }
    92% { transform: translate(-4px, 2px); }
    94% { transform: translate(0); }
}

/* ── SUBTITLE ── */
.blood-sub {
    font-family: 'Share Tech Mono', monospace;
    color: #cc0000;
    text-align: center;
    font-size: 0.8rem;
    letter-spacing: 5px;
    opacity: 0.8;
    margin-bottom: 10px;
}

/* ── SECTION DIVIDER ── */
.blood-divider {
    border: none;
    height: 2px;
    background: linear-gradient(90deg, transparent, #8b0000, #ff0000, #8b0000, transparent);
    margin: 20px 0;
    box-shadow: 0 0 10px #ff0000, 0 0 20px #8b0000;
    animation: pulse-line 2s ease-in-out infinite;
}
@keyframes pulse-line {
    0%,100% { box-shadow: 0 0 10px #ff0000, 0 0 20px #8b0000; }
    50%      { box-shadow: 0 0 20px #ff0000, 0 0 40px #8b0000; }
}

/* ── KPI CARDS WITH NEON RED PULSE ── */
.kpi-card {
    background: linear-gradient(135deg, #0a0000, #1a0000);
    border: 1px solid #8b0000;
    border-radius: 6px;
    padding: 20px;
    text-align: center;
    position: relative;
    overflow: hidden;
    animation: pulse-card 3s ease-in-out infinite;
    margin-bottom: 10px;
}
@keyframes pulse-card {
    0%,100% { box-shadow: 0 0 10px rgba(139,0,0,0.4), inset 0 0 10px rgba(139,0,0,0.1); border-color: #8b0000; }
    50%      { box-shadow: 0 0 25px rgba(255,0,0,0.6), inset 0 0 20px rgba(255,0,0,0.15); border-color: #ff0000; }
}
.kpi-card::before {
    content: '';
    position: absolute;
    top: -2px; left: -100%;
    width: 100%; height: 2px;
    background: linear-gradient(90deg, transparent, #ff0000, transparent);
    animation: card-scan 3s linear infinite;
}
@keyframes card-scan {
    0%   { left: -100%; }
    100% { left: 200%; }
}
.kpi-value {
    font-family: 'Bebas Neue', sans-serif;
    font-size: 2.2rem;
    color: #ff0000;
    text-shadow: 0 0 15px #ff0000, 0 0 30px #8b0000;
    letter-spacing: 2px;
}
.kpi-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem;
    color: #cc4444;
    letter-spacing: 3px;
    margin-top: 5px;
    text-transform: uppercase;
}
.kpi-icon { font-size: 1.5rem; margin-bottom: 6px; }

/* ── POSITIVE / NEGATIVE VARIANTS ── */
.pos-card { border-color: #006400 !important; animation: pulse-green 3s ease-in-out infinite !important; }
.pos-card .kpi-value { color: #00ff41 !important; text-shadow: 0 0 15px #00ff41 !important; }
@keyframes pulse-green {
    0%,100% { box-shadow: 0 0 10px rgba(0,100,0,0.4); border-color: #006400; }
    50%      { box-shadow: 0 0 25px rgba(0,255,65,0.5); border-color: #00ff41; }
}
.neg-card { border-color: #8b0000 !important; }
.neu-card { border-color: #666 !important; animation: pulse-grey 3s ease-in-out infinite !important; }
.neu-card .kpi-value { color: #aaa !important; text-shadow: 0 0 10px #aaa !important; }

/* ── SECTION LABEL ── */
.section-label {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.65rem;
    color: #cc0000;
    letter-spacing: 5px;
    opacity: 0.9;
    margin-bottom: -5px;
}

/* ── SIDEBAR ── */
div[data-testid="stSidebarContent"] {
    background: #050000 !important;
    border-right: 1px solid #3d0000;
}

/* ── HEADINGS ── */
h1,h2,h3 {
    font-family: 'Bebas Neue', sans-serif !important;
    color: #ff0000 !important;
    text-shadow: 0 0 10px #ff0000 !important;
    letter-spacing: 3px !important;
}
</style>

<!-- ── FIRE PARTICLES ── -->
<div class="fire-container" id="fireContainer"></div>

<!-- ── BLOOD DRIPS ── -->
<div class="drip-container" id="dripContainer"></div>

<script>
// Fire particles
const fc = document.getElementById('fireContainer');
const colors = ['#ff0000','#ff4400','#ff6600','#cc0000','#ff2200','#8b0000'];
for(let i = 0; i < 40; i++) {
    const p = document.createElement('div');
    p.className = 'particle';
    p.style.left = Math.random() * 100 + '%';
    p.style.background = colors[Math.floor(Math.random() * colors.length)];
    p.style.animationDuration = (Math.random() * 4 + 3) + 's';
    p.style.animationDelay = (Math.random() * 5) + 's';
    p.style.width = p.style.height = (Math.random() * 6 + 2) + 'px';
    p.style.boxShadow = '0 0 6px ' + colors[Math.floor(Math.random() * colors.length)];
    fc.appendChild(p);
}

// Blood drips
const dc = document.getElementById('dripContainer');
for(let i = 0; i < 20; i++) {
    const d = document.createElement('div');
    d.className = 'drip';
    d.style.left = (Math.random() * 100) + '%';
    d.style.width = (Math.random() * 4 + 2) + 'px';
    d.style.animationDuration = (Math.random() * 3 + 2) + 's';
    d.style.animationDelay = (Math.random() * 5) + 's';
    dc.appendChild(d);
}
</script>
""", unsafe_allow_html=True)

# ── PLOTLY RED TEMPLATE ───────────────────────────────────
BLOOD = dict(layout=go.Layout(
    paper_bgcolor='#0a0000',
    plot_bgcolor='#0f0000',
    font=dict(color='#cc4444', family='Share Tech Mono'),
    title_font=dict(color='#ff0000', size=13, family='Bebas Neue'),
    xaxis=dict(gridcolor='rgba(139,0,0,0.2)', linecolor='rgba(255,0,0,0.3)',
               tickfont=dict(color='rgba(204,68,68,0.8)')),
    yaxis=dict(gridcolor='rgba(139,0,0,0.2)', linecolor='rgba(255,0,0,0.3)',
               tickfont=dict(color='rgba(204,68,68,0.8)')),
    legend=dict(bgcolor='rgba(0,0,0,0.6)', bordercolor='rgba(139,0,0,0.5)',
                font=dict(color='#cc4444')),
    colorway=['#ff0000','#00ff41','#888888','#ff6600','#cc00cc','#ffcc00'],
))

RED_SCALE  = [[0,'#0a0000'],[0.3,'#3d0000'],[0.6,'#8b0000'],[1,'#ff0000']]
SENT_COLORS = {'Positive':'#00ff41', 'Negative':'#ff0000', 'Neutral':'#888888'}

# ── LOAD DATA ─────────────────────────────────────────────
@st.cache_data
def load_data():
    base = os.path.dirname(__file__)
    return pd.read_csv(os.path.join(base, '..', 'data', 'twitter_data.csv'))

df = load_data()

# ── GLITCH HEADER ─────────────────────────────────────────
st.markdown('''
<div class="glitch-title" data-text="🩸 TWITTER SENTIMENT ANALYZER 🩸">
    🩸 TWITTER SENTIMENT ANALYZER 🩸
</div>
<div class="blood-sub">[ BLOOD & FIRE INTELLIGENCE SYSTEM ] — ANKIT JINKWAN</div>
''', unsafe_allow_html=True)
st.markdown('<hr class="blood-divider">', unsafe_allow_html=True)

# ── SIDEBAR ───────────────────────────────────────────────
st.sidebar.markdown('<p style="font-family:Bebas Neue;color:#ff0000;font-size:1rem;letter-spacing:4px;text-shadow:0 0 10px #ff0000">⚙ FILTERS</p>', unsafe_allow_html=True)

sentiments = st.sidebar.multiselect("SENTIMENT", ["Positive","Negative","Neutral"], default=["Positive","Negative","Neutral"])
topics     = st.sidebar.multiselect("TOPIC", sorted(df['Topic'].unique()), default=sorted(df['Topic'].unique()))
languages  = st.sidebar.multiselect("LANGUAGE", sorted(df['Language'].unique()), default=sorted(df['Language'].unique()))
min_likes  = st.sidebar.slider("MIN LIKES", 0, 500, 0)
verified   = st.sidebar.radio("VERIFIED ONLY", ["All","Verified Only"], index=0)

fdf = df[
    (df['Sentiment'].isin(sentiments)) &
    (df['Topic'].isin(topics)) &
    (df['Language'].isin(languages)) &
    (df['Likes'] >= min_likes)
]
if verified == "Verified Only":
    fdf = fdf[fdf['Verified'] == 1]

st.sidebar.markdown('<hr class="blood-divider">', unsafe_allow_html=True)
st.sidebar.markdown(f'''
<div style="background:#050000;border:1px solid #3d0000;padding:12px;font-family:Share Tech Mono;color:#cc0000;font-size:0.75rem;line-height:1.8;border-radius:4px;box-shadow:0 0 10px rgba(139,0,0,0.3)">
&gt; TWEETS LOADED: {len(fdf)}<br>
&gt; TOPICS: {fdf["Topic"].nunique()}<br>
&gt; TOTAL LIKES: {fdf["Likes"].sum():,}<br>
&gt; AVG SCORE: {fdf["SentimentScore"].mean():.3f}<br>
&gt; STATUS: <span style="color:#ff0000">ONLINE ■</span>
</div>
''', unsafe_allow_html=True)

if len(fdf) == 0:
    st.warning("⚠️ No data matches your filters.")
    st.stop()

# ── KPI CARDS ─────────────────────────────────────────────
k1,k2,k3,k4,k5 = st.columns(5)
pos = (fdf['Sentiment']=='Positive').sum()
neg = (fdf['Sentiment']=='Negative').sum()
neu = (fdf['Sentiment']=='Neutral').sum()
for col, icon, val, label, cls in [
    (k1,"🐦",f"{len(fdf):,}",   "TOTAL TWEETS", ""),
    (k2,"💚",f"{pos:,}",         "POSITIVE",     "pos-card"),
    (k3,"❤️",f"{neg:,}",         "NEGATIVE",     "neg-card"),
    (k4,"🤍",f"{neu:,}",         "NEUTRAL",      "neu-card"),
    (k5,"❤️",f"{fdf['Likes'].sum():,}", "TOTAL LIKES", ""),
]:
    col.markdown(f'<div class="kpi-card {cls}"><div class="kpi-icon">{icon}</div><div class="kpi-value">{val}</div><div class="kpi-label">{label}</div></div>', unsafe_allow_html=True)

st.markdown('<hr class="blood-divider">', unsafe_allow_html=True)

# ── ROW 1: Sentiment Donut + Topic Bar + Gauge ────────────
st.markdown('<p class="section-label">// SENTIMENT INTELLIGENCE //</p>', unsafe_allow_html=True)
r1c1, r1c2, r1c3 = st.columns(3)

with r1c1:
    st.markdown("### 🩸 Sentiment Split")
    sc = fdf['Sentiment'].value_counts()
    fig = go.Figure(go.Pie(
        values=sc.values, labels=sc.index, hole=0.6,
        marker=dict(colors=['#00ff41','#ff0000','#888888'],
                    line=dict(color='#0a0000', width=3)),
        textfont=dict(color='white', family='Share Tech Mono')
    ))
    fig.add_annotation(text=f"<b>{len(fdf)}</b><br>TWEETS", x=0.5, y=0.5,
                       showarrow=False, font=dict(size=14, color='#ff0000', family='Bebas Neue'))
    fig.update_layout(template=BLOOD, height=300, margin=dict(l=5,r=5,t=30,b=30),
                      legend=dict(orientation='h', y=-0.15))
    st.plotly_chart(fig, use_container_width=True)

with r1c2:
    st.markdown("### 🔥 Sentiment by Topic")
    tp = fdf.groupby(['Topic','Sentiment']).size().reset_index(name='Count')
    fig = px.bar(tp, x='Topic', y='Count', color='Sentiment',
                 color_discrete_map=SENT_COLORS, barmode='stack')
    fig.update_layout(template=BLOOD, height=300, margin=dict(l=5,r=5,t=30,b=5),
                      xaxis=dict(tickangle=30, tickfont=dict(size=8)),
                      legend=dict(orientation='h', y=1.1))
    fig.update_traces(marker_line_width=0)
    st.plotly_chart(fig, use_container_width=True)

with r1c3:
    st.markdown("### 📊 Sentiment Score Gauge")
    avg_score = fdf['SentimentScore'].mean()
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=avg_score,
        delta={'reference': 0, 'valueformat': '.3f'},
        title={'text': "AVG SENTIMENT SCORE", 'font': {'color':'#cc4444','family':'Bebas Neue'}},
        gauge={
            'axis': {'range': [-1, 1], 'tickcolor':'#cc4444'},
            'bar':  {'color': '#ff0000' if avg_score < 0 else '#00ff41'},
            'bgcolor': '#0f0000',
            'steps': [
                {'range': [-1, -0.3], 'color': '#3d0000'},
                {'range': [-0.3, 0.3], 'color': '#1a1a1a'},
                {'range': [0.3, 1],   'color': '#003d00'},
            ],
            'threshold': {'line': {'color':'#ff0000','width':3}, 'value': 0}
        },
        number={'font': {'color':'#ff0000','family':'Bebas Neue'}}
    ))
    fig.update_layout(template=BLOOD, height=300, margin=dict(l=20,r=20,t=50,b=10))
    st.plotly_chart(fig, use_container_width=True)

st.markdown('<hr class="blood-divider">', unsafe_allow_html=True)

# ── ROW 2: Timeline + Hourly Heatmap ─────────────────────
st.markdown('<p class="section-label">// TEMPORAL BLOOD FLOW //</p>', unsafe_allow_html=True)
r2c1, r2c2 = st.columns(2)

with r2c1:
    st.markdown("### 📅 Sentiment Over Time")
    fdf2 = fdf.copy()
    fdf2['Date'] = pd.to_datetime(fdf2['Date'])
    fdf2['YearMonth'] = fdf2['Date'].dt.to_period('M').astype(str)
    monthly = fdf2.groupby(['YearMonth','Sentiment']).size().reset_index(name='Count')
    fig = px.area(monthly, x='YearMonth', y='Count', color='Sentiment',
                  color_discrete_map=SENT_COLORS, line_shape='spline')
    fig.update_traces(opacity=0.75)
    fig.update_layout(template=BLOOD, height=320, margin=dict(l=5,r=5,t=30,b=5),
                      xaxis=dict(tickangle=30, tickfont=dict(size=8)),
                      legend=dict(orientation='h', y=1.1))
    st.plotly_chart(fig, use_container_width=True)

with r2c2:
    st.markdown("### ⏰ Hourly Activity Heatmap")
    dow_order = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
    heat = fdf.groupby(['DayOfWeek','Hour']).size().reset_index(name='Count')
    heat['DayOfWeek'] = pd.Categorical(heat['DayOfWeek'], categories=dow_order, ordered=True)
    heat = heat.sort_values('DayOfWeek')
    pivot = heat.pivot_table(values='Count', index='DayOfWeek', columns='Hour', fill_value=0)
    fig = go.Figure(go.Heatmap(
        z=pivot.values, x=pivot.columns, y=pivot.index,
        colorscale=[[0,'#0a0000'],[0.3,'#3d0000'],[0.6,'#8b0000'],[1,'#ff0000']],
        hovertemplate='Day: %{y}<br>Hour: %{x}:00<br>Tweets: %{z}<extra></extra>'
    ))
    fig.update_layout(template=BLOOD, height=320, margin=dict(l=5,r=5,t=30,b=5),
                      xaxis_title='Hour of Day', yaxis=dict(tickfont=dict(size=9)))
    st.plotly_chart(fig, use_container_width=True)

st.markdown('<hr class="blood-divider">', unsafe_allow_html=True)

# ── ROW 3: Engagement + Language + Score Distribution ─────
st.markdown('<p class="section-label">// DEEP ANALYSIS //</p>', unsafe_allow_html=True)
r3c1, r3c2, r3c3 = st.columns(3)

with r3c1:
    st.markdown("### 💥 Avg Engagement by Sentiment")
    eng = fdf.groupby('Sentiment').agg(
        Likes=('Likes','mean'),
        Retweets=('Retweets','mean'),
        Replies=('Replies','mean')
    ).round(1).reset_index()
    fig = go.Figure()
    for metric, color in [('Likes','#ff0000'),('Retweets','#ff6600'),('Replies','#cc0000')]:
        fig.add_trace(go.Bar(name=metric, x=eng['Sentiment'], y=eng[metric],
                             marker_color=color, marker_line_width=0))
    fig.update_layout(template=BLOOD, height=300, barmode='group',
                      margin=dict(l=5,r=5,t=30,b=5), legend=dict(orientation='h', y=1.1))
    st.plotly_chart(fig, use_container_width=True)

with r3c2:
    st.markdown("### 🌍 Language Breakdown")
    lang = fdf['Language'].value_counts().reset_index()
    lang.columns = ['Language','Count']
    fig = px.bar(lang, x='Count', y='Language', orientation='h',
                 color='Count', color_continuous_scale=RED_SCALE, text='Count')
    fig.update_traces(textposition='outside', textfont=dict(color='#ff0000', size=10),
                      marker_line_width=0)
    fig.update_layout(template=BLOOD, height=300, showlegend=False,
                      coloraxis_showscale=False, margin=dict(l=5,r=50,t=30,b=5),
                      yaxis=dict(categoryorder='total ascending'))
    st.plotly_chart(fig, use_container_width=True)

with r3c3:
    st.markdown("### 📈 Sentiment Score Distribution")
    fig = go.Figure()
    for sent, color in SENT_COLORS.items():
        data = fdf[fdf['Sentiment']==sent]['SentimentScore']
        if len(data) > 0:
            fig.add_trace(go.Histogram(x=data, name=sent, marker_color=color,
                                        opacity=0.75, nbinsx=20, marker_line_width=0))
    fig.add_vline(x=0, line_dash='dash', line_color='white', line_width=1)
    fig.update_layout(template=BLOOD, height=300, barmode='overlay',
                      margin=dict(l=5,r=5,t=30,b=5),
                      xaxis_title='Score', legend=dict(orientation='h', y=1.1))
    st.plotly_chart(fig, use_container_width=True)

st.markdown('<hr class="blood-divider">', unsafe_allow_html=True)

# ── ROW 4: Topic Radar + Device + Hashtags ────────────────
st.markdown('<p class="section-label">// PATTERN RECOGNITION //</p>', unsafe_allow_html=True)
r4c1, r4c2, r4c3 = st.columns(3)

with r4c1:
    st.markdown("### 🕸️ Topic Radar")
    tr = fdf['Topic'].value_counts().nlargest(8)
    fig = go.Figure(go.Scatterpolar(
        r=tr.values, theta=tr.index, fill='toself',
        fillcolor='rgba(139,0,0,0.25)',
        line=dict(color='#ff0000', width=2),
        marker=dict(color='#ff6600', size=7, symbol='diamond')
    ))
    fig.update_layout(template=BLOOD, height=300,
                      polar=dict(bgcolor='#0a0000',
                                 radialaxis=dict(gridcolor='rgba(139,0,0,0.3)',
                                                 tickfont=dict(color='rgba(204,68,68,0.5)', size=7)),
                                 angularaxis=dict(gridcolor='rgba(139,0,0,0.3)',
                                                  tickfont=dict(color='#cc4444', size=8))),
                      margin=dict(l=30,r=30,t=30,b=30))
    st.plotly_chart(fig, use_container_width=True)

with r4c2:
    st.markdown("### 📱 Device Usage")
    dev = fdf['Device'].value_counts().reset_index()
    dev.columns = ['Device','Count']
    fig = px.pie(dev, values='Count', names='Device', hole=0.45,
                 color_discrete_sequence=['#ff0000','#8b0000','#cc4400','#660000'])
    fig.update_traces(textfont=dict(color='white'), marker_line_width=2,
                      marker_line_color='#0a0000')
    fig.update_layout(template=BLOOD, height=300, margin=dict(l=5,r=5,t=30,b=30),
                      legend=dict(orientation='h', y=-0.15, font=dict(size=9)))
    st.plotly_chart(fig, use_container_width=True)

with r4c3:
    st.markdown("### #️⃣ Top Hashtags")
    ht = fdf['Hashtag'].value_counts().nlargest(10).reset_index()
    ht.columns = ['Hashtag','Count']
    fig = px.bar(ht.sort_values('Count', ascending=True), x='Count', y='Hashtag',
                 orientation='h', color='Count', color_continuous_scale=RED_SCALE, text='Count')
    fig.update_traces(textposition='outside', textfont=dict(color='#ff0000', size=9),
                      marker_line_width=0)
    fig.update_layout(template=BLOOD, height=300, showlegend=False,
                      coloraxis_showscale=False, margin=dict(l=5,r=50,t=30,b=5))
    st.plotly_chart(fig, use_container_width=True)

st.markdown('<hr class="blood-divider">', unsafe_allow_html=True)

# ── LIVE DATA TABLE ───────────────────────────────────────
st.markdown('<p class="section-label">// RAW DATA FEED //</p>', unsafe_allow_html=True)
st.markdown("### 🖥️ Live Tweet Feed")
cs, cn = st.columns([3,1])
with cs: search = st.text_input("SEARCH TWEETS", placeholder="search topic, hashtag, sentiment...", label_visibility='collapsed')
with cn: n_rows = st.selectbox("ROWS", [10,25,50], label_visibility='collapsed')

display = fdf.copy()
if search:
    mask = display.apply(lambda r: r.astype(str).str.contains(search, case=False).any(), axis=1)
    display = display[mask]

st.dataframe(
    display[['TweetID','Date','Topic','Hashtag','Sentiment','SentimentScore',
             'Language','Device','Likes','Retweets','Replies']].head(n_rows),
    use_container_width=True, hide_index=True
)

# ── FOOTER ────────────────────────────────────────────────
st.markdown('<hr class="blood-divider">', unsafe_allow_html=True)
st.markdown("""
<div style='text-align:center;font-family:Share Tech Mono;color:rgba(204,68,68,0.5);font-size:0.75rem;letter-spacing:3px;padding:10px'>
    [ SYSTEM: ONLINE ] ■ BUILT BY
    <a href='https://ankitjhinkwan.github.io/portfolio/' style='color:#ff0000;text-decoration:none'>ANKIT JINKWAN</a>
    ■ <a href='https://www.linkedin.com/in/ankit-jinkwan-a16882288/' style='color:#cc0000;text-decoration:none'>LINKEDIN</a>
    ■ [ END OF LINE ]
</div>
""", unsafe_allow_html=True)
