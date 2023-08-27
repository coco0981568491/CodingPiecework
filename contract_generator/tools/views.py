from django.shortcuts import render, HttpResponse
from . import tool_funcs

# Create your views here.
# def home(request):

# 	return render(request, 'home.html', {})
	
def generateLeasePage(request):

	if request.method == "POST":

		# get data and name it as file for convenience 
		file = request.FILES["myFile"]

		# process the excel content into word and automatically download from webapp.
		result = tool_funcs.generateLease(file)
		resp = HttpResponse(result.getvalue(), content_type='application/force-download')
		resp['Content-Disposition'] = 'attachment; filename=GlycamToPDB.pdb'

		return resp

	else:
		return render(request, 'LeaseTemplate.html', {})