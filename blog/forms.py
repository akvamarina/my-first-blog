from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	class Meta:
		model = Post    #определение модели для создания формы
		fields = ('title', 'text',)	
		#указание полей, которые будут использоваться для формы 
		#(т.е. добавляться/заполняться в процессе создания формы вручную, а не в коде автоматически)

