height = int(input('Nhap vao chieu cao(cm): '))
weight = int(input('Nhap vao can nang(kg): '))

BMI = weight / (height * 0.02)
print('Chi so BMI cua ban la:',BMI)

if BMI < 16:
    print('Gay cap do III')
elif BMI < 17:
    print('Gay cap do II')
elif BMI <18.5:
    print('Gay cap do I')
elif BMI < 25:
    print('The trang binh thuong')
elif BMI < 30:
    print('The trang thua can')
elif BMI < 35:
    print('Beo phi cap do I')
elif BMI < 40:
    print('Beo phi cap do II')
else:
    print('Beo phi cap do III')