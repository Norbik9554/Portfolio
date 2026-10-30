from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Norbik9554 Hub API")

HTML_CONTENT = """<!DOCTYPE html>
<html lang="pl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Norbik9554 | Hub & Portfolio</title>
  <style>
    :root {
      --bg: #0d1117;
      --card-bg: #161b22;
      --card-border: #30363d;
      --text: #c9d1d9;
      --text-bright: #f0f6fc;
      --accent-bmc: #FFDD00;
      --status-ok: #238636;
      --status-err: #da3633;
    }
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    body {
      background-color: var(--bg);
      color: var(--text);
      min-height: 100vh;
      display: flex;
      justify-content: center;
      align-items: center;
      padding: 30px 15px;
    }
    .container {
      width: 100%;
      max-width: 520px;
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 16px;
    }
    .avatar {
      width: 105px;
      height: 105px;
      border-radius: 50%;
      border: 3px solid var(--card-border);
      object-fit: cover;
      box-shadow: 0 4px 15px rgba(0, 0, 0, 0.4);
    }
    .profile-info { 
      text-align: center; 
    }
    .profile-info h1 {
      font-size: 1.6rem;
      color: var(--text-bright);
      margin-bottom: 4px;
    }
    .profile-info p {
      font-size: 0.95rem;
      color: #8b949e;
      line-height: 1.4;
    }
    .status-badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      padding: 6px 14px;
      background: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 20px;
      font-size: 0.85rem;
      font-weight: 500;
    }
    .status-dot {
      width: 10px;
      height: 10px;
      border-radius: 50%;
      background: #8b949e;
      box-shadow: 0 0 8px rgba(139, 148, 158, 0.6);
      transition: background 0.3s, box-shadow 0.3s;
    }
    .status-dot.online {
      background: var(--status-ok);
      box-shadow: 0 0 8px rgba(35, 134, 54, 0.8);
    }
    .status-dot.offline {
      background: var(--status-err);
      box-shadow: 0 0 8px rgba(218, 54, 51, 0.8);
    }
    .links-list {
      width: 100%;
      display: flex;
      flex-direction: column;
      gap: 12px;
      margin-top: 10px;
    }
    .link-card {
      display: flex;
      align-items: center;
      justify-content: space-between;
      padding: 14px 18px;
      background-color: var(--card-bg);
      border: 1px solid var(--card-border);
      border-radius: 12px;
      text-decoration: none;
      color: var(--text-bright);
      font-weight: 600;
      font-size: 0.98rem;
      transition: transform 0.15s ease, border-color 0.15s ease, background-color 0.15s ease;
    }
    .link-card:hover {
      transform: translateY(-2px);
      border-color: #58a6ff;
      background-color: #1f242c;
    }
    .link-left {
      display: flex;
      align-items: center;
      gap: 12px;
    }
    .link-left span.icon { 
      font-size: 1.3rem; 
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .arrow { 
      color: #8b949e; 
      font-size: 0.9rem; 
    }
    .link-card.bmc {
      background-color: var(--accent-bmc);
      color: #000000;
      border-color: var(--accent-bmc);
    }
    .link-card.bmc:hover {
      background-color: #ffea55;
      border-color: #ffea55;
    }
    .link-card.bmc .arrow { 
      color: #333333; 
    }
    footer {
      margin-top: 20px;
      text-align: center;
      font-size: 0.8rem;
      color: #6e7681;
    }
  </style>
</head>
<body>
  <div class="container">
    <img class="avatar" src="https://github.com/Norbik9554.png" alt="Norbik9554">

    <div class="profile-info">
      <h1>Norbik9554</h1>
      <p>Python Enthusiast & Developer</p>
    </div>

    <div class="status-badge">
      <span class="status-dot" id="statusDot"></span>
      <span id="statusText">Sprawdzanie AddonsLoader...</span>
    </div>

    <div class="links-list">
      <a href="https://buymeacoffee.com/Norbik9554" target="_blank" rel="noopener noreferrer" class="link-card bmc">
        <div class="link-left">
          <span class="icon">☕</span>
          <span>Postaw mi kawę (Buy Me a Coffee)</span>
        </div>
        <span class="arrow">➜</span>
      </a>

      <a href="https://addons-loader.vercel.app" target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-left">
          <span class="icon">⚡</span>
          <span>Addons Loader (Serwer / API)</span>
        </div>
        <span class="arrow">➜</span>
      </a>

      <a href="https://github.com/Norbik9554" target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-left">
          <span class="icon">🐙</span>
          <span>Mój profil GitHub</span>
        </div>
        <span class="arrow">➜</span>
      </a>

      <a href="https://discord.gg/TWÓJ_KOD_ZAPROSZENIA" target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-left">
          <span class="icon">💬</span>
          <span>Dołącz do Discorda</span>
        </div>
        <span class="arrow">➜</span>
      </a>

      <a href="https://steamcommunity.com/id/Norbik_/" target="_blank" rel="noopener noreferrer" class="link-card">
        <div class="link-left">
          <span class="icon">🎮</span>
          <span>Profil Steam</span>
        </div>
        <span class="arrow">➜</span>
      </a>
    </div>

    <footer>
      &copy; <span id="year"></span> Norbik9554 • Wszelkie prawa zastrzeżone
    </footer>
  </div>

  <script>
    document.getElementById("year").textContent = new Date().getFullYear();

    async function checkServerStatus() {
      const dot = document.getElementById("statusDot");
      const text = document.getElementById("statusText");

      try {
        await fetch("https://addons-loader.vercel.app", { 
          method: "HEAD",
          mode: "no-cors"
        });
        dot.className = "status-dot online";
        text.textContent = "AddonsLoader: Online";
      } catch (err) {
        dot.className = "status-dot offline";
        text.textContent = "AddonsLoader: Offline";
      }
    }

    checkServerStatus();
  </script>
</body>
</html>
"""

# Obsługuje zarówno wejście na domenę główną, jak i wewnętrzne wywołanie pliku przez Vercel
@app.get("/", response_class=HTMLResponse)
@app.get("/api", response_class=HTMLResponse)
@app.get("/api/index.py", response_class=HTMLResponse)
def serve_portfolio():
    return HTML_CONTENT

@app.get("/api/info")
def get_info():
    return {
        "status": "online",
        "creator": "Norbik9554",
        "primary_project": "AddonsLoader"
    }
  
