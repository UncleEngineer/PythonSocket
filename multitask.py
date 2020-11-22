# multitask.py
import time
import threading

def Toothbrush(brand):
	for i in range(10):
		print('แปรงฟันอยู่...ยาสีฟันยี่ห้อ' + brand)
		time.sleep(0.3)

def Shower(soap,gel):
	for i in range(10):
		print('กำลังอาบน้ำ...สบู่{} ยาสระผม{}'.format(soap,gel))
		time.sleep(1)

task1 = threading.Thread(target=Toothbrush, args=('คอลลี้',))
task2 = threading.Thread(target=Shower, args=('นกขุนทอง','ซัลจอยส์'))

start = time.time() # จับเวลาเริ่มต้น

#Toothbrush()
#Shower()
task1.start()
task2.start()
task1.join()
task2.join()

end = time.time()
print('All Time: ', end - start)
print('--------')
print('----ไปโรงเรียนได้แล้ว!-----')