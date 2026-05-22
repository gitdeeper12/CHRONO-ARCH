"""Early warning signals for phase transitions"""

import numpy as np
from typing import List, Dict, Tuple

def compute_variance_ews(trajectory: List[float], window: int = 20) -> List[float]:
    n = len(trajectory)
    variance = np.zeros(n)
    for i in range(window, n):
        window_data = trajectory[i - window:i]
        variance[i] = np.var(window_data)
    return variance.tolist()

def compute_autocorrelation_ews(trajectory: List[float], lag: int = 1, window: int = 20) -> List[float]:
    n = len(trajectory)
    ac = np.zeros(n)
    for i in range(window, n):
        window_data = np.array(trajectory[i - window:i])
        if len(window_data) > lag:
            corr = np.corrcoef(window_data[:-lag], window_data[lag:])
            ac[i] = corr[0, 1] if corr.shape == (2, 2) else 0
    return ac.tolist()

def compute_critical_slowing_down(trajectory: List[float], window: int = 20) -> List[float]:
    n = len(trajectory)
    csd = np.zeros(n)
    for i in range(window, n):
        window_data = np.array(trajectory[i - window:i])
        csd[i] = np.var(window_data)
    return csd.tolist()

def compute_all_ews(trajectory: List[float], window: int = 20) -> Dict[str, List[float]]:
    return {
        'variance': compute_variance_ews(trajectory, window),
        'autocorrelation_lag1': compute_autocorrelation_ews(trajectory, 1, window),
        'critical_slowing_down': compute_critical_slowing_down(trajectory, window)
    }

def collapse_alert(ews_signals: Dict[str, List[float]], threshold_factor: float = 2.0) -> Tuple[bool, float]:
    signals = []
    for name, signal in ews_signals.items():
        if len(signal) > 10:
            recent = np.mean(signal[-10:])
            baseline = np.mean(signal[:10]) if len(signal) > 20 else np.mean(signal[:5])
            if baseline > 0:
                ratio = recent / baseline
                if ratio > threshold_factor:
                    signals.append(min(ratio / 3, 1.0))
    if not signals:
        return False, 0.0
    confidence = np.mean(signals)
    return confidence > 0.6, confidence
