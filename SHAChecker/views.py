from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import hashlib
from SHAChecker.models import CountSHA
import sys

def main(request):
    try:
        if request.method == 'POST' and request.FILES['upload']:
            file = request.FILES['upload']
            filesystem = FileSystemStorage()
            filename = filesystem.save(file.name, file)
            file = filesystem.url(filename)

            hashsum = get_hash(file)
            data = CountSHA.objects.all()
            if get_counter(hashsum) != None:
                cashecounter = get_counter(hashsum)
            else:
                query = CountSHA(key=hashsum, value=0)
                query.save()
                cashecounter = 0
            filesystem.delete(file)
            return render(request, 'main.html', {'file': file, 'hash': hashsum, 'cashecounter': cashecounter, 'data': data})
        return render(request, 'main.html')
    except:
        e = sys.exc_info()[0]
        return render(request,'error.html',{'e':e})


def get_counter(hashsum):
    try:
        cashecounter = 0
        obj = CountSHA.objects.filter(key=hashsum)
        for i in obj:
            i.value += 1
            i.save()
            cashecounter = i
        return cashecounter
    except CountSHA.DoesNotExist:
        query = None


def get_hash(file):
    hash = hashlib.sha256()
    with open(file, 'rb') as f:
        hash.update(f.read())
        hashsum = hash.hexdigest()
    return hashsum
