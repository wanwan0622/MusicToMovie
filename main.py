import get_peaks
import draw

peaks = get_peaks.get_peaks('wavs/sine_-06_05_01000.wav')
draw.draw_circle(peaks[0])
