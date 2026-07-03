### **Topshiriq: Ombordagi mahsulotlarni boshqarish tizimi**

Ombordagi mahsulotlarni boshqaradigan Django loyihasi yarating. Loyihada mahsulot qo‘shish va tahrirlash imkoniyati bo‘lsin.

Quyidagi model yaratilishi kerak:

class Mahsulot(models.Model):  
   nomi \= models.CharField(max\_length=100, unique=True)  
   turi \= models.CharField(max\_length=50)  
   narxi \= models.DecimalField(max\_digits=10, decimal\_places=2)  
   soni \= models.PositiveIntegerField()  
   chegirma\_foizi \= models.PositiveIntegerField(default=0)  
   tavsifi \= models.TextField(blank=True)  
   sotuvda \= models.BooleanField(default=True)

Mahsulot qo‘shish formasini `ModelForm` yordamida yarating va quyidagi validatsiyalarni amalga oshiring.

### **`clean_<field>()` metodlari orqali**

1. Mahsulot nomida `"test"`, `"admin"` yoki `"namuna"` so‘zlari qatnashmasligi kerak.  
2. Mahsulot nomi boshqa mahsulot nomidan faqat katta-kichik harflar bilan farq qilsa ham, takroriy deb hisoblanishi kerak.

    Misol:

    Telefon  
   telefon  
   TELEFON

    faqat bittasi mavjud bo‘lishi mumkin.

3. Chegirma foizi 70 dan yuqori bo‘lsa, unga ruxsat berilmasin.  
4. Tavsif kiritilgan bo‘lsa, unda kamida 5 ta so‘z bo‘lishi kerak.

---

### **`clean()` metodi orqali**

5. Agar mahsulot soni 0 bo‘lsa, `sotuvda=True` bo‘lishi mumkin emas.  
6. Agar chegirma foizi 50 dan katta bo‘lsa, mahsulot narxi kamida 100 000 bo‘lishi kerak.  
7. `"Elektronika"` turidagi mahsulotlar uchun narx kamida 500 000 bo‘lishi kerak.  
8. `"Premium"` turidagi mahsulotlar uchun tavsif kiritilishi majburiy.  
9. Agar mahsulot nomida `"Pro"` so‘zi qatnashsa, uning narxi kamida 1 000 000 bo‘lishi kerak.  
10. Agar mahsulot sotuvda bo‘lsa, ombordagi son kamida 5 ta bo‘lishi kerak.  
11. Agar chegirma 0 dan katta bo‘lsa, tavsifda `"aksiya"` so‘zi qatnashishi kerak.  
12. `"Oziq-ovqat"` turidagi mahsulotlarda chegirma 30 foizdan oshmasligi kerak.  
13. Agar mahsulot narxi 5 000 000 dan yuqori bo‘lsa, u avtomatik ravishda `"Premium"` turiga tegishli bo‘lishi kerak.  
14. `"Mebel"` turidagi mahsulotlar uchun ombordagi son kamida 2 ta bo‘lishi kerak.  
15. Agar tavsifda `"import"` so‘zi ishlatilgan bo‘lsa, mahsulot narxi kamida 200 000 bo‘lishi kerak.

