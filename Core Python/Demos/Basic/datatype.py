###Numeric Chategories
# 1:int

x=10
print(type(x))

#2 :float
x=3.14
print(type(x))

#3: complex
x=5+3j
print(type(x))



###Text Chategories

#1 :str
x='This is a first page'
x="This is a second page"

x='''This is first page.
This is a secind page'''


x="""This is a first page.
This is a second page"""
print(type(x))



##Sequencial 

#1 : list
x=[10,20,30,40]
print(type(x))

#2 :tuple
x=(10,20,30,40)
print(type(x))

#3 :range
x=range(1,100)
print(type(x))

###Set Type

#1 :set
x={10,20,30,40}
print(type(x))

#2 :frozenset
x=frozenset({10,20,30,40,50})
print(type(x))


##Mapping
#1 : dict
x={'name':'bhavna','id':101,'address':'pune'}
print(type(x))


###Other
#1 :boolean
x=True
x=False
print(type(x))

#2 :NoneType
x=None
print(type(x))


