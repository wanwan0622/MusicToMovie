import get_peaks
import draw

peaks = get_peaks.get_peaks(
    'wavs/sine_-06_05_01000.wav')   # ここにwavファイルのパス名を入れる
draw.draw_circle(peaks[0])
