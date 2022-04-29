from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Ref
from django.shortcuts import render
from django.shortcuts import redirect
from listings.forms import RefForm

def refs_list(request):
	refs = Ref.objects.all()
	return render(request, 'listings/ref_list.html', {'refs': refs})
	

def modify(request):
	if (request.method == 'POST'):
		form = RefForm(request.POST)
		if form.is_valid():
			gtin2 = form.cleaned_data['gtin']
			date = form.cleaned_data['expiration']
			if Ref.objects.filter(gtin=gtin2).exists():
				instance = Ref.objects.get(gtin=gtin2)
				instance.expiration_date = date
				instance.save()
				return redirect('done')
			p = Ref.objects.create(gtin=gtin2, expiration_date=date)
			return redirect('done');
	else:
		form = RefForm()
	return render(request, 'listings/modify.html', {'form': form})

def done(request):
	return render(request, 'listings/done.html')

def about(request):
	return render(request, 'listings/about.html')

# Create your views here.
