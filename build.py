"""Haalt de actuele weerdata voor BLTC Baarn op en bakt die in padel-droog.html."""
import datetime
import json
import pathlib
import urllib.request

HERE = pathlib.Path(__file__).parent
template = (HERE / "padel-template.html").read_text(encoding="utf-8")

LAT, LON = 52.211, 5.288
URL = (
    f"https://api.open-meteo.com/v1/forecast?latitude={LAT}&longitude={LON}"
    "&hourly=temperature_2m,relative_humidity_2m,dew_point_2m,precipitation,precipitation_probability,"
    "cloud_cover,wind_speed_10m,shortwave_radiation,et0_fao_evapotranspiration"
    "&past_days=92&forecast_days=7&timezone=Europe%2FAmsterdam"
)
with urllib.request.urlopen(URL, timeout=30) as r:
    data = json.load(r)
data = {"hourly": data["hourly"], "_fetched": datetime.datetime.now(datetime.timezone.utc).isoformat()}

out = template.replace("__DATA__", json.dumps(data, separators=(",", ":"))).replace("__STANDALONE__", "false")
(HERE / "padel-droog.html").write_text(out, encoding="utf-8")
print("padel-droog.html geschreven,", len(data["hourly"]["time"]), "uren")
