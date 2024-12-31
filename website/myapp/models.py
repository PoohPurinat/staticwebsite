from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(null= False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=10.00) #decimal place = จุดทศนิยม , decimal = เก็บเป็นค่าทศนิยม
    image = models.ImageField(upload_to='product_images/' , null= True, blank=True) # ถ้าไม่ใส่  null กับ blank คือ ต้องกรอกข้อมูลทุกครั้งที่สร้าง field ตัวนี้มา null = true database ไม่ต้องกรอกก้ได้ blank true สำหรับ backend ไม่ต้องกรอก
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True) # บันทึกเวลา

    def __str__(self) :
        return self.name
    
class ProductStock(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True) #ถ้าหาก produc โดนลบ object ตัวนี้ก็โดนลบ
    instock = models.DecimalField(default=1 , max_digits=10, decimal_places=2)
    sold = models.DecimalField(default=1 , max_digits=10, decimal_places=2)

    def __str__(self):
        return self.product.name + 'instock : {} sold : {}'.format(self.instock, self.sold) # .format เอาไว้ใช้ตัวแปรไปใส่ในข้อความ
    
class Staff(models.Model):
    name = models.CharField(max_length=200)
    tel = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class ContactUs(models.Model):
    name = models.CharField(max_length=200,verbose_name='ชื่อผู้ถาม')
    title = models.CharField(max_length=200,verbose_name='ชื่อปัญหา(name)')
    detail = models.TextField(null=True , blank=True,verbose_name='รายละเอียดปัญหา')
    email = models.CharField(max_length=200,null=True,verbose_name='อีเมลผู้ติดต่อ')
    phonenumber = models.CharField(max_length = 10,null=True,verbose_name='เบอร์โทร')
    done = models.BooleanField(default=False,verbose_name='แก้ปัญหาจบหรือยัง')
    summary = models.TextField(null=True,blank=True,verbose_name='สรุปปัญหานี้แก้อย่างไร')

    def __str__(self):
        return self.title