"""Constants for the Protegus integration."""
from __future__ import annotations

DOMAIN = "protegus"

CONF_REGION = "region"
CONF_SYSTEM_ID = "system_id"
CONF_DEVICE_ID = "device_id"
CONF_TOKEN = "token"
CONF_EMAIL = "email"
CONF_PASSWORD = "password"

CONF_SCAN_INTERVAL = "scan_interval"
DEFAULT_SCAN_INTERVAL = 60  # seconds; websocket pushes updates in between
MIN_SCAN_INTERVAL = 10      # do not hammer the vendor API
MAX_SCAN_INTERVAL = 3600
POLL_INTERVAL = DEFAULT_SCAN_INTERVAL  # backwards compatible alias

# Area status codes (from the web app's `N` enum)
STATUS_DISARMED = 1
STATUS_ARMED = 2
STATUS_STAY = 3
STATUS_SLEEP = 4
STATUS_ARMING = 5
STATUS_DISARMING = 6
STATUS_DISARMED_READY = 7
STATUS_DISARMED_NOT_READY = 8