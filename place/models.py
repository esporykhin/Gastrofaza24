from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from unidecode import unidecode

class Place(models.Model):
    name = models.CharField('Nazwa lokalu', max_length=200)
    slug = models.SlugField('Link', max_length=300, default='', blank=True)
    img = models.ImageField('Zdjęcie Lokalu', upload_to='Place/static/locals/img', blank=True, max_length=500)
    address = models.CharField('Adres', max_length=1000)
    number_phone = models.CharField('Numer telefonu', max_length=26)
    hours = models.TextField(verbose_name='Godziny otwarcia', max_length=2000)
    news = models.TextField('Aktualności', default='', blank=True, max_length=2000)
    maps = models.CharField('Mapa', default='',blank=True, max_length=1000)
    status = models.BooleanField('Opublikuj', default=False)
    description = models.TextField("Opis i Informacje", default='', blank=True, max_length=3000)
    
    class Meta:
        verbose_name = 'Lokal'
        verbose_name_plural = 'Lokale'
        
    def get_absolute_url(self):
        kwargs = {
            'pk': self.id,
            'slug': self.slug
        }
        return reverse("place_list_view", kwargs=kwargs)

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(unidecode(value))
        super(Place, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name
    

class Menu(models.Model):
    place = models.ForeignKey(Place, related_name='place', on_delete=models.CASCADE)
    pizza = 'Pizza'
    kebab = 'Kebab'
    burgery = 'Burgery'
    kanapki = 'Kanapki'
    salatki = 'Sałatki'
    napoje = 'Napoje'
    inne = 'Inne'
    multi = 'rozmiar i cenna'
    zestaw_obiadowy = 'zestaw obiadowy'
    zapiekanki = 'zapiekanki'
    cat_dish = (
        (pizza, 'Pizza'),
        (kebab, 'Kebab'),
        (burgery, 'Burgery'),
        (kanapki, 'Kanapki'),
        (salatki, 'Sałatki'),
        (napoje, 'Napoje'),
        (inne, 'Inne'),
        (multi, 'rozmiar i cenna'),
        (zestaw_obiadowy, 'zestaw obiadowy'),
        (zapiekanki, 'zapiekanki'),
    )
    dish = models.CharField('Nazwa Potrawy', blank=True, max_length=200)
    dish_components = models.CharField("Składniki", blank=True, default="", max_length=1200)
    dish_category = models.CharField("Kategoria", default="Kategoria", choices=cat_dish, max_length=200)
    pizza_price = models.CharField("Rozmiar i cena Pizzy", help_text="np.Mała-10zł", default="", blank=True, max_length=300) 
    price = models.DecimalField("Cena",default="00", max_digits=5, decimal_places=2)

    class Meta:
        verbose_name = 'Menu'
        verbose_name_plural = 'Menu'