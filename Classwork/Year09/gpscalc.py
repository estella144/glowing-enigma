lightspeed_kms: int = 300000

signal_time_ms = float(input("How long did the signal take to reach the receiver? (ms) "))
signal_time_s = signal_time_ms / 1000
satellite_distance_km = lightspeed_kms * signal_time_s

print(f"Distance of satellite from receiver: {satellite_distance_km} km")
