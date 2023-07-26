# import wave
# import numpy as np
# import matplotlib.pyplot as plt

# def to_db(x, N):
#     """
#     窓で区切りながらdbに変換する関数

#     Parameters
#     ----------
#     x
#         wavファイル
#     N : int
#         窓幅

#     Returns
#     ----------
#     db : numpy array
#         db
#     """
#     pad = np.zeros(N//2)
#     print("pad")
#     print(pad.shape)
#     pad_data = np.concatenate([pad, x, pad])
#     rms = np.array([np.sqrt((1/N) * (np.sum(pad_data[i:i+N]))**2) for i in range(len(x))])
#     return 20 * np.log10(rms)

# def get_volume(filename):
#     wave_file = wave.open(filename, "rb") #Open
#     x = wave_file.readframes(wave_file.getnframes()) #frameの読み込み
#     x = np.frombuffer(x, dtype= "int16") #numpy.arrayに変換
#     print("x")
#     print(x.shape)

#     print(to_db(filename, 1024))

# get_volume('wavs/sine_-06_05_01000.wav')

# -----------------------

# import sys
# import wave 
# import numpy as np
# import math

# FLAME_SIZE  = 8192

# def read_wavefile(file_path):
#     wf        = wave.open(file_path, 'rb')
#     frames   = wf.getnframes()      # フレーム数を取得
#     Channels = wf.getnchannels()
#     sampWidth = wf.getsampwidth()
#     framerate = wf.getframerate()
#     print( str(frames) + " Frames")
#     print( str(Channels) + " channels")
#     print( str(sampWidth*8) + " bit" )
#     print( str(framerate) + " hz" )
#     print("\n")
#     wf.setpos(int(frames/2))   # 全フレームの真ん中に位置を移動
#     buf = wf.readframes(FLAME_SIZE)  # セットした位置からFLAME_SIZEフレームを取得
#     wf.close()
#     return buf

# def get_db(data):
#     squaressum = 0
#     # 累積二乗和を算出
#     for i in range(FLAME_SIZE):
#         squaressum += data[i] * data[i]
        
#     # 平均平方根を算出
#     meansquare = squaressum / (FLAME_SIZE/2)

#     # 二乗平均平方を取得  (入出力信号レベル)
#     rms = math.sqrt(meansquare)
#     decibel = 20 * math.log10(rms)
#     print( str( int(decibel) ) + "db" )

# data = read_wavefile('wavs/laser1_big.wav')
# get_db(data)

import librosa
import matplotlib.pyplot as plt
import soundfile as sf

def wav_read(path):
    wave, fs = sf.read(path) #音データと周波数を読み込む
    return wave, fs

wave, fs = wav_read('wavs/laser1_big.wav')
rms = librosa.feature.rms(y=wave) #音量の計算
times = librosa.times_like(rms, sr=fs) #時間軸の生成
plt.plot(times, rms[0]*2**(1/2)) #rms➡振幅に変換
plt.show()
plt.close()
