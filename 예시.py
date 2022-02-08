class University : #부모클래스
    name = "학교명"
    address = "주소"
    def __init__(self,name,address) : # 
        self.name=name
        self.address=address  

    def show(self): 
        print(self.name+"학교이고" +self.address +" 에 위치해있다")

class Dankook(University) : #University class 상속
    def __init__(self,name,address): 
        super().__init__(name,address)# 부모클래스의 생성자함수 호출

dankook= Dankook("단국대","죽전") #객체 생성
dankook.show()                 #상속받은 메소드 호출 
  

class Animal : 
    def __init__(self,name=""):
        self.name=name; 
    def eat(self) :
        print("동물은 먹는다.")

class Cat(Animal): # 상속
    def __init__(self, name=""):
        super().__init__(name="")
    
    #메소드 오버라이딩: 부모 클래스의 메소드를 재정의하며 
    # 부모클래스의 메소드를 변경하는 것이 필요할 때 사용한다
    #메소드의 이름, 매개변수, 리턴형은 동일
    def eat(self):
        print("고양이는 먹는다.")

rang = Cat() #Cat 클래스안의 eat()호출로, Cat의 eat()이 Animal의 eat()을 오버라이드한다. 
rang.eat()

class Account:
        num_accounts = 0 # 파이썬에서의 클래스 변수
        def __init__(self, name):
                self.name = name #인스턴스 변수 
                Account.num_accounts += 1
        def __del__(self):
                Account.num_accounts -= 1

#사용예
#Lee와 Kim - 각 계좌에 대한 소유자 정보는 인스턴스 변수인 name이 바인딩
Kim = Account("kim")
Lee = Account ("Lee")
#지금까지 은행에서 개설된 계좌:  'kim'과 'lee' 하나씩, 총 두 개 (kim 인스턴스나 lee 인스턴스를 통해 num_accounts라는 이름에 접근)

print("Kim.name: "+Kim.name+", Lee.name:"+Lee.name)
print("Kim.num_accounts: ",Kim.num_accounts,", Lee.num_accounts:",Lee.num_accounts
,"Account.num_accounts:",Account.num_accounts)

from abc import * #추상클래스 생성을 위한 import문 
class Phone(metaclass=ABCMeta) : #추상클래스 생성
    @abstractmethod #추상메소드 선언
    def call(self):
        pass
    
class applePhone(Phone): #추상클래스 상속 
    def call(self): #추상메소드 오버라이딩
        print("따르릉전화왔어요~")

my_iphone = applePhone()
my_iphone.call()