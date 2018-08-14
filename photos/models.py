from __future__ import unicode_literals
from django.db import models
from django.urls import reverse_lazy
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

# Create your models here.
User = get_user_model()

class Photo(models.Model):

    image = models.ImageField(upload_to='%Y/%m/%d/orig')
    filtered_image = models.ImageField(upload_to = '%Y/%m/%d/filtered')
    content = models.TextField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete="CASCADE")

    class Meta :
        ordering = ('-created_at', '-pk',)

    def delete(self, *args, **kwargs):
        self.image.delete()
        self.filtered_image.delete()
        # 상속받은 부모클래스 의 딜리트 인스턴스 메서드 호출 -> 모델 객체 지움
        super(Photo,self).delete(*args, **kwargs)

    def get_absolute_url(self):
        url = reverse_lazy('detail', kwargs={'pk':self.pk})
        return url

    def get_user(self):
        return User.objects.get(pk=self.user_id)


