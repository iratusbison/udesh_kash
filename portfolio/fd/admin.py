from django.contrib import admin
from .models import FixedDeposit
from .models import Stock
from .models import PortfolioStock
from .models import Portfolio

admin.site.register(FixedDeposit)
admin.site.register(Stock)
admin.site.register(Portfolio)
admin.site.register(PortfolioStock)



# Register your models here.
