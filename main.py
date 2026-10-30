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
    .profile-info { text-align: center; }
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
      transition: transform 0.15s ease, border-color 0.15s ease, background-
