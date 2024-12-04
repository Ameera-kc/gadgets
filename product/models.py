import uuid
from django.db import models
from django.utils.translation import gettext_lazy as _




class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_added = models.DateTimeField(db_index=True,auto_now_add=True)    
    date_updated = models.DateTimeField(auto_now_add=True) 

    class Meta:
        abstract = True
        

class Category(BaseModel):
    name = models.CharField(_("Category Name"),max_length=125)
    is_deleted = models.BooleanField(_("Is this category deleted?"),default=False)

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')
        ordering = ['name']

    def __str__(self):
        return str(self.name)    
    

class Product(BaseModel):
    name = models.CharField(_("Product Name"),max_length=255)
    price = models.IntegerField(_("Price"),default=0)
    category = models.ForeignKey("product.Category", on_delete=models.CASCADE, limit_choices_to={'is_deleted': False})
    description = models.TextField(_("Description"))
    image = models.ImageField(_("Image"),upload_to="uploads/products/")
    is_deleted = models.BooleanField(_("Is this product deleted?"),default=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name']

    def __str__(self):
        return str(self.name)