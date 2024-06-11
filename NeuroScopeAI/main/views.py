from django.shortcuts import render,redirect
import numpy as np

# Create your views here.
from .form import ImageForm
from .models import Image

# Create your views here.
def index(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if (form.is_valid()):
            form.save()
            obj=form.instance
            img=Image.objects.all()
            for x in img:
                pred=x.model_prediction()
                x.caption = pred[0]
                glioma = np.round(pred[1][0][0]*100, 4)
                meningioma = np.round(pred[1][0][1]*100, 4)
                notumor = np.round(pred[1][0][2]*100, 4)
                pituitary = np.round(pred[1][0][3]*100, 4)
            return render(request,"index.html",{"img":img,"obj":obj, "glioma":glioma, "meningioma":meningioma, "notumor":notumor, "pituitary": pituitary})
    else:
        out_img=Image.objects.all()
        out_img.delete()
        form=ImageForm()
        img=Image.objects.all()
        for x in img:
            pred=x.model_prediction()
            x.caption = pred[0]
    return render(request,"index.html",{"img":img,"form":form})