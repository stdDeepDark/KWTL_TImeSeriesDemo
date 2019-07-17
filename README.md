# KWTL_TimeSeriesDemo
 the time series demo of KWTL_Model

前端:KWTL_Model

后端:KWTL_django

[django参考资料](https://www.runoob.com/django/django-tutorial.html)

# 后端运行
KWTL_django目录使用 python manage.py runserver(需要有python和Django的环境)

# 后端添加接口:
 KWTL_django/app1/views.py添加后端处理函数

KWTL_django/KWTL_django/urls.py  内添加接口(可参考views.load_data格式)

```
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('load_data/', views.load_data),
        path('', TemplateView.as_view(template_name='index.html'), name='index'),
        #example
        path('接口/', views.接口),
    ]
```
## 前端http数据请求格式
```
this.$http.get('http://127.0.0.1:8000/接口参数)
        .then(function(response){//处理返回结果     
                alert(response.data)
         })
        .catch((error)=>{//异常处理
            alert(error)
        }
        )
```