# Data Dictionary

| Column | Meaning |
| --- | --- |
| `dataset_id` | Stable public run identifier. |
| `receiver_id` | Abstract receiver role: `receiver-01`, `receiver-02`, or `receiver-03`. |
| `record_index` | Zero-based accepted-row index within one run/receiver stream. |
| `capture_segment` | Zero-based segment index incremented when the source host clock resets. |
| `relative_host_ms` | Host-side milliseconds relative to the first accepted row in the capture segment. |
| `relative_device_time_us` | Device-counter microseconds relative to the first accepted row in the capture segment, modulo 2^32. |
| `total` | Firmware accepted-summary counter. |
| `interval` | Firmware interval counter. |
| `dropped` | Firmware dropped-record counter. |
| `seen` | Firmware observed-frame counter. |
| `mismatch` | Firmware frame-filter mismatch counter. |
| `zero_len` | Firmware zero-length CSI counter. |
| `rssi_dbm` | Received signal strength in dBm. |
| `noise_floor_dbm` | Reported noise floor in dBm. |
| `rate` | ESP-IDF receive-rate code recorded by the firmware. |
| `channel` | Primary Wi-Fi channel number. |
| `secondary_channel` | ESP-IDF secondary-channel code. |
| `estimator_valid` | Firmware estimator-valid flag. |
| `estimator_length` | Firmware-estimated CSI length. |
| `signal_length` | Received 802.11 signal length. |
| `rx_state` | ESP-IDF receive-state value. |
| `rx_sequence` | Firmware receive-sequence value. |
| `csi_length` | Full CSI-vector length reported by the firmware; the vector itself was not logged. |
| `first_word_invalid` | ESP-IDF first-word-invalid flag. |
| `csi_iq_preview` | JSON array containing the exact 8 or 16 signed I/Q byte values emitted in the summary. |

Relative time restarts at zero for each capture segment. Counters are source
observations, not repaired estimates, and may reset when a receiver restarts.
The `rate` and secondary-channel fields are retained as firmware codes rather
than relabelled into unverified PHY interpretations.
