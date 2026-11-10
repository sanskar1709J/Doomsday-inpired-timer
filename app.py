import streamlit as st
import streamlit.components.v1 as components

# Configure page
st.set_page_config(
    page_title="Cinematic Countdown",
    page_icon="⏳",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Target countdown date: Adjust this to any ISO-formatted target date
TARGET_DATE = "2027-05-07T00:00:00"

countdown_html = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Montserrat:wght@300;600&display=swap" rel="stylesheet">

  <style>
    * {{
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }}

    body {{
      background: radial-gradient(ellipse at center, rgba(10, 30, 20, 0.75) 0%, rgba(5, 10, 8, 0.95) 100%), #050706;
      color: #ffffff;
      font-family: 'Montserrat', sans-serif;
      min-height: 100vh;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      overflow: hidden;
      position: relative;
    }}

    /* Subtle cinematic glow and scanline effect */
    body::before {{
      content: "";
      position: absolute;
      top: 0; left: 0; right: 0; bottom: 0;
      background: radial-gradient(circle at 50% 45%, rgba(60, 160, 100, 0.15) 0%, transparent 65%);
      pointer-events: none;
    }}

    .container {{
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      z-index: 1;
      padding: 20px;
    }}

    .timer-display {{
      display: flex;
      align-items: center;
      justify-content: center;
      gap: 18px;
    }}

    .unit-block {{
      display: flex;
      flex-direction: column;
      align-items: center;
      min-width: 90px;
    }}

    .value {{
      font-family: 'Share Tech Mono', monospace;
      font-size: clamp(38px, 6vw, 76px);
      letter-spacing: 4px;
      font-weight: 400;
      color: #f0f6f4;
      text-shadow: 0 0 12px rgba(220, 255, 235, 0.35);
    }}

    .separator {{
      font-family: 'Share Tech Mono', monospace;
      font-size: clamp(32px, 5vw, 64px);
      color: rgba(220, 240, 230, 0.6);
      margin-bottom: 24px;
      user-select: none;
    }}

    .label {{
      margin-top: 8px;
      font-size: clamp(9px, 1.2vw, 13px);
      letter-spacing: 5px;
      text-transform: uppercase;
      color: rgba(210, 230, 220, 0.7);
      font-weight: 600;
    }}

    .sub-footer {{
      margin-top: 50px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 6px;
      opacity: 0.55;
      font-size: 11px;
      letter-spacing: 3px;
    }}

    .sub-footer .rating-box {{
      border: 1px solid rgba(255, 255, 255, 0.4);
      padding: 2px 8px;
      font-size: 10px;
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="timer-display">
      <div class="unit-block">
        <span class="value" id="months">00</span>
        <span class="label">Months</span>
      </div>

      <span class="separator">:</span>

      <div class="unit-block">
        <span class="value" id="days">00</span>
        <span class="label">Days</span>
      </div>

      <span class="separator">:</span>

      <div class="unit-block">
        <span class="value" id="hours">00</span>
        <span class="label">Hours</span>
      </div>

      <span class="separator">:</span>

      <div class="unit-block">
        <span class="value" id="minutes">00</span>
        <span class="label">Minutes</span>
      </div>

      <span class="separator">:</span>

      <div class="unit-block">
        <span class="value" id="seconds">00</span>
        <span class="label">Seconds</span>
      </div>
    </div>

    <div class="sub-footer">
      <span class="rating-box">THIS FILM IS NOT YET RATED</span>
      <span>MARVEL STUDIOS</span>
    </div>
  </div>

  <script>
    const target = new Date("{TARGET_DATE}").getTime();

    function pad(num) {{
      return String(Math.floor(num)).padStart(2, '0');
    }}

    function updateCountdown() {{
      const now = new Date().getTime();
      let diff = target - now;

      if (diff <= 0) {{
        document.getElementById('months').textContent = "00";
        document.getElementById('days').textContent = "00";
        document.getElementById('hours').textContent = "00";
        document.getElementById('minutes').textContent = "00";
        document.getElementById('seconds').textContent = "00";
        return;
      }}

      const sec = 1000;
      const min = sec * 60;
      const hr = min * 60;
      const day = hr * 24;
      const month = day * 30.4375; // Average days per month

      const months = Math.floor(diff / month);
      diff -= months * month;

      const days = Math.floor(diff / day);
      diff -= days * day;

      const hours = Math.floor(diff / hr);
      diff -= hours * hr;

      const minutes = Math.floor(diff / min);
      diff -= minutes * min;

      const seconds = Math.floor(diff / sec);

      document.getElementById('months').textContent = pad(months);
      document.getElementById('days').textContent = pad(days);
      document.getElementById('hours').textContent = pad(hours);
      document.getElementById('minutes').textContent = pad(minutes);
      document.getElementById('seconds').textContent = pad(seconds);
    }}

    setInterval(updateCountdown, 1000);
    updateCountdown();
  </script>
</body>
</html>
"""

# Render full viewport iframe
components.html(countdown_html, height=750, scrolling=False)
