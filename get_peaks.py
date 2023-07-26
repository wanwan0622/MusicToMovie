import sys
import scipy.io.wavfile
import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

def get_peaks(filename):

    # 音声ファイル読み込み
    rate, data = scipy.io.wavfile.read(filename)

    # （振幅）の配列を作成
    data = data / 32768

    # 周波数成分を表示
    # 縦軸：dataを高速フーリエ変換する（時間領域から周波数領域に変換する）
    fft_data = np.abs(np.fft.fft(data))
    # 横軸：周波数の取得　　#np.fft.fftfreq(データ点数, サンプリング周期)
    freqList = np.fft.fftfreq(data.shape[0], d=1.0 / rate)

    # データプロット(デバッグ用)
    # plt.plot(freqList, fft_data)
    # plt.xlim(0, 8000)  # 0～8000Hzまで表示

    # ピークを取得
    peaks, _ = scipy.signal.find_peaks(fft_data, height=10000)
    # plt.plot(freqList[peaks], fft_data[peaks],'o')
    peak_freqs = [] # ピークの周波数
    for i in peaks:
        if freqList[i] > 0:
            peak_freqs.append(freqList[i])
    return peak_freqs

    # plt.show()
