import time

t=time.time()

hour=int(((t//3600)%24))
min=int(((t//60)%60))

print("현재시간(영국 그리니치 시각) :",hour,"시",min,"분")