import django_filters
from .models import RawWoolData
from django.db.models import Avg

class RawWoolDataFilter(django_filters.FilterSet):
    
    # Exact match filtering for breed (e.g., ?breed=Chokla)
    breed = django_filters.CharFilter(lookup_expr='iexact')  
    
    # Exact match filtering for color (e.g., ?color=White)
    color = django_filters.CharFilter(lookup_expr='iexact')
    
    # Range filtering for price (e.g., ?min_price=60&max_price=80)
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='lte')
    
    # Exact match filtering for micron (e.g., ?micron=32-36)
    micron = django_filters.CharFilter(lookup_expr='iexact')
    
    # Date filtering (e.g., ?date=2022-03-18)
    date = django_filters.DateFilter()
    
    # Substring match filtering for breed (e.g., ?breed_contains=Chok)
    breed_contains = django_filters.CharFilter(field_name='breed', lookup_expr='icontains')
    
    # Multiple choice filtering for color (e.g., ?color_choice=white)
    # Add choices as per your requirement
    COLOR_CHOICES = [
        ('white', 'White'),
        ('black', 'Black'),
        ('brown', 'Brown'),
    ]
    color_choice = django_filters.ChoiceFilter(field_name='color', choices=COLOR_CHOICES)
    
    # Date range filtering (e.g., ?date_range_after=2022-03-18&date_range_before=2022-03-20)
    date_range = django_filters.DateFromToRangeFilter(field_name='date')
    
    # Ordering (e.g., ?ordering=price for ascending, ?ordering=-price for descending)
    ordering = django_filters.OrderingFilter(
        fields=(
            ('price', 'price'),
            ('date', 'date'),
        )
    )

    class Meta:
        model = RawWoolData
        fields = [
            'breed', 'color', 'micron', 'date', 'min_price', 'max_price', 
            'breed_contains', 'color_choice', 'date_range', 'ordering'
        ]
