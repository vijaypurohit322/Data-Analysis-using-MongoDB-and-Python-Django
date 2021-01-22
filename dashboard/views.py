from django.shortcuts import render

# Create your views here.

def ecommerce_report_page(request):
   return render(request, 'retail_report.html', {})


def marketing_report_page(request):
   return render(request, 'marketing_report.html', {})