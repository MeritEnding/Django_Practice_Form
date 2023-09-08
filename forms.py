"""
질문 등록시 사용할 QuestionForm을 생성
[projects\mysite\myapp\forms.py]
"""

from django import forms
from myapp.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model =Question
        fields=['subject','content']

##########
"""
폼(form):페이지 요청시 전달되는 파라미터들을 쉽게 관리하기 위해 사용하는 클래스

장고의 폼: 1) 일반폼(forms.Form), 2) 모델폼(forms.ModelForm)이 있다.
QuestionForm은 모델 폼(forms.ModelForm)을 상속했다.

모델 폼을 사용하면 Model.py와 연결된 모델의 데이터를 저장할수 있는 폼이다. 모델 폼은 이너 클래스인 Meta클래스가 반드시 필요하다.
Meta 클래스 사용법: 사용할 모델과 모델의 속성을 적어야한다.

ex) QuestionForm은 Question 모델과 연결된 폼이고 속성으로 Question모델의 subject와 content를 사용한다고 정의한 것이다.

"""
##########


