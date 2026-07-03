from django import forms

from core.models import Mahsulot


class MahsulotForm(forms.ModelForm):
    class Meta:
        model = Mahsulot
        fields = [
            "nomi",
            "turi",
            "narxi",
            "soni",
            "chegirma_foizi",
            "tavsifi",
            "sotuvda",
        ]

    def clean_nomi(self):
        nomi: str = self.cleaned_data["nomi"]
        nomi_lower = nomi.lower()
        taqiqlangan_sozlar = ["test", "admin", "namuna"]

        for soz in taqiqlangan_sozlar:
            if soz in nomi_lower:
                raise forms.ValidationError(
                    f"Mahsulot nomida '{soz}' sozi qatnashmasligi kerak!"
                )

        if Mahsulot.objects.filter(nomi__iexact=nomi):
            raise forms.ValidationError(
                f"'{nomi}' nomli mahsuloti mavjud boshqa nom kiriting!"
            )

        return nomi

    def clean_chegirma_foizi(self):
        chegirma_foizi = self.cleaned_data["chegirma_foizi"]

        if chegirma_foizi > 70:
            raise forms.ValidationError(
                "Chegirma foizi 70 dan yuqori bo'lmasligi kerak!"
            )

        return chegirma_foizi

    def clean_tavsifi(self):
        tavsifi: str = self.cleaned_data["tavsifi"]

        if len(tavsifi.split(" ")) < 5:
            raise forms.ValidationError("Tavsifda kamida 5 ta so‘z bo‘lishi kerak!")

        return tavsifi

    def clean(self):
        cleaned_data = super().clean()
        soni = cleaned_data.get("soni")
        sotuvda = cleaned_data.get("sotuvda")

        if not soni and sotuvda:
            raise forms.ValidationError(
                "Mahsulot soni 0 bo‘lsa sotuvda bo‘lishi mumkin emas!"
            )

        chegirma_foizi = cleaned_data.get("chegirma_foizi")
        narxi = cleaned_data.get("narxi")

        if chegirma_foizi > 50 and narxi < 100_000:
            raise forms.ValidationError(
                "Chegirma foizi 50 dan katta bo‘lsa, mahsulot narxi kamida 100 000 bo‘lishi kerak!"
            )

        turi: str = cleaned_data.get("turi")

        if turi.lower() == "elektronika" and narxi < 500_000:
            raise forms.ValidationError(
                "Elektronika turidagi mahsulotlar uchun narx kamida 500 000 bo‘lishi kerak!"
            )

        tavsifi = cleaned_data.get("tavsifi")

        if turi.lower() == "premium" and not tavsifi:
            raise forms.ValidationError(
                "Premium turidagi mahsulotlar uchun tavsif kiritilishi majburiy!"
            )

        nomi: str = cleaned_data.get("nomi")

        if "pro" in nomi.lower():
            raise forms.ValidationError(
                "Nomida 'Pro' so‘zi qatnashsa, uning narxi kamida 1 000 000 bo‘lishi kerak!"
            )

        if chegirma_foizi > 0 and "aksiya" not in tavsifi:
            raise forms.ValidationError(
                "Chegirma bo‘lsa, tavsifda aksiya so‘zi qatnashishi kerak!"
            )

        if chegirma_foizi > 30 and turi.lower() == "oziq-ovqat":
            raise forms.ValidationError(
                "Oziq-ovqat turidagi mahsulotlarda chegirma 30 foizdan oshmasligi kerak"
            )

        if narxi < 200_000 and "import" in tavsifi:
            raise forms.ValidationError(
                "Tavsifda import so‘zi ishlatilsa, mahsulot narxi kamida 200 000 bo‘lishi kerak!"
            )

        return cleaned_data
