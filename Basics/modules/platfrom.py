import multiprocessing
import platform

print(platform.architecture())
print(platform.processor())
print(platform.system())
print(multiprocessing.cpu_count())
print(multiprocessing.sys.getwindowsversion())
