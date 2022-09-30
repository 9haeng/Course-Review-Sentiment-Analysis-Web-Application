# Course Review Sentiment Analysis Web-Application

-----
![thumbnail](https://user-images.githubusercontent.com/70729822/193257454-deacd43c-afb8-4648-a682-8727e6c6575b.png)

[Ratemyprofessor](https://ratemyprofessors.com) 내 수강평을 활용해 강좌 추천 여부를 분석해주는 웹 애플리케이션 제작 프로젝트

[웹 애플리케이션](https://9haeng-course-review-sentiment-analysis-web-app---init---xwszi8.streamlitapp.com/) 을 직접 사용해보길 희망하신다면 링크를 클릭해주세요.

## 프로젝트 배경
----
강좌를 수강한 학생들은 수강평을 통해 자신들의 경험을 타인에게 공유합니다.

수강평에서 일반적으로 사용되는 키워드와 문구는 해당 강좌의 특성을 드러낼 수 있습니다.

이런 개인의 주관이 반영된 수강평은 강의계획서에 기재된 객관적 정보 못지않게 타 학생들의 수강 의사결정에 영향을 미치기도 합니다.

그런 수강평을 활용해 추천도를 분석하는 것은 수강을 고려하는 학생은 물론 해당 교수에게도 중요합니다.

교수는 학생이 남긴 자신의 강좌에 대한 수강평을 분석함으로써 미래에 더 나은 강좌를 구성할 기회를 얻을 수 있습니다.

물론 수강평에 포함된 '태그' 요소와 같은 간단한 지표만을 활용해 강좌를 평가할 수 있습니다. 그렇지만 그런 수치형 자료는 강좌의 어떤 부분이 마음에 들고, 또 어떤 부분이 아쉬운지에 대한 상세한 정보는 포함하지 않기 때문에 그 한계성이 명확합니다.

이 배경을 바탕으로 수강평 감성분석 프로젝트를 진행했습니다.

## 프로젝트 목표
----
`comment` feature를 활용해 강좌 추천 여부를 분류하는 웹 애플리케이션 배포

## 프로젝트 과정
웹 애플리케이션 배포를 제외한 모든 과정은 [지난 프로젝트](https://github.com/9haeng/Course-Review-Sentiment-Analysis) 에서 확인하실 수 있습니다.


## 웹 애플리케이션 구성
----
### 초기화면
![guide](https://user-images.githubusercontent.com/70729822/193257198-db4908d4-0c15-4398-8caa-01b22847329d.gif)

간단한 서비스 가이드 메시지를 기재해 놓았습니다.

### 강좌 수강을 추천으로 분류할 경우
![recommended](https://user-images.githubusercontent.com/70729822/193257267-9a476163-574e-401f-bde4-7f8a79c50683.gif)


### 강좌 수강을 비추천으로 분류할 경우
![not recommended](https://user-images.githubusercontent.com/70729822/193257233-e5b9c76b-3f42-4bb2-8ca8-f365fdfad7ca.gif)

사용자가 입력한 텍스트를 바탕으로 어떤 단어들이 예상 결과에 영향을 미쳤는지 시각화하여 제공합니다.




