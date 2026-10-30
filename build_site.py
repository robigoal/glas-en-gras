"""Bouwt de losse website/app (PWA) van Glas & Gras in de map site/."""
import hashlib
import pathlib
import re

HERE = pathlib.Path(__file__).parent
template = (HERE / "padel-template.html").read_text(encoding="utf-8")
manifest = (HERE / "site" / "manifest.webmanifest").read_text(encoding="utf-8")

head = """<!doctype html>
<html lang="nl">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#1f5fa8">
<meta name="description" content="Voorspelt per uur of de glazen wanden en de padelbaan droog of nat zijn.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Glas &amp; Gras">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>:root{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px)}body{margin:0}img{max-width:100%}</style>
</head>
<body>
"""
body = (template.replace("__DATA__", "null").replace("__STANDALONE__", "true")
        .replace('<meta charset="utf-8">\n', "", 1)
        .replace('<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n', "", 1)
        .replace("<title>Glas &amp; Gras Baarn</title>", "<title>Glas &amp; Gras</title>", 1))
html = head + body + "\n</body>\n</html>\n"
(HERE / "site" / "index.html").write_text(html, encoding="utf-8")

# Nieuwe cacheversie bij elke wijziging, zodat geïnstalleerde apps de update ophalen
sw = HERE / "site" / "sw.js"
version = hashlib.sha256((html + manifest).encode()).hexdigest()[:10]
sw.write_text(re.sub(r'const CACHE = "[^"]*";', f'const CACHE = "glas-en-gras-{version}";', sw.read_text(encoding="utf-8")), encoding="utf-8")
print("site/index.html geschreven, cache", version)
